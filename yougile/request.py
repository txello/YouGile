from contextlib import ExitStack
from io import IOBase
import os
from pathlib import Path
from typing import Any

import requests
from pydantic import BaseModel


YOUGILE_URL = "https://ru.yougile.com"


def _normalize_base_url(base_url: str) -> str:
    return base_url.rstrip("/")


class Client:
    """Клиент YouGile API с настройками подключения."""

    def __init__(self, token: str | None = None, base_url: str = YOUGILE_URL) -> None:
        self.token = token
        self.base_url = _normalize_base_url(base_url)

    def query(self, arg: BaseModel, token: str | None = None) -> requests.Response:
        """
        Универсальный запрос:
        - если модель содержит _file (имена полей-файлов) -> multipart/form-data
        - иначе -> JSON
        Поддерживаются варианты значений файлового поля:
          bytes | путь (str/Path) | файловый объект (IOBase) | ('name', bytes[, 'mime/type'])
        """
        arg = arg.model_copy()
        url: str = getattr(arg, "_url")
        method: str = getattr(arg, "_method", "get").lower()

        headers: dict[str, str] = {}
        request_token = token or self.token

        if hasattr(arg, "token"):
            model_token = getattr(arg, "token")
            if request_token is None:
                request_token = model_token
            if request_token is not None:
                headers["Authorization"] = f"Bearer {request_token}"
            delattr(arg, "token")

        for name in getattr(arg, "_url_parse", ()):
            url = url.format(**{name: getattr(arg, name)})
            delattr(arg, name)

        params_parts: list[str] = []
        for name in getattr(arg, "_url_params", ()):
            value = getattr(arg, name)
            if value is not None:
                params_parts.append(f"{name}={value}")
            delattr(arg, name)
        if params_parts:
            url = f"{url}?{'&'.join(params_parts)}"

        body: dict[str, Any] = arg.model_dump(exclude_none=True)
        file_field_names = tuple(getattr(arg, "_file", ()))

        if file_field_names:
            with ExitStack() as stack:
                files: dict[str, Any] = {}
                for fname in file_field_names:
                    value = body.pop(fname, None)
                    if value is None:
                        continue

                    if (
                        isinstance(value, tuple)
                        and 2 <= len(value) <= 3
                        and isinstance(value[0], str)
                    ):
                        files[fname] = value
                        continue

                    if isinstance(value, (bytes, bytearray)):
                        files[fname] = (f"{fname}.bin", bytes(value))
                        continue

                    if isinstance(value, IOBase):
                        name = getattr(value, "name", f"{fname}.bin")
                        files[fname] = (os.path.basename(str(name)), value)
                        continue

                    path = Path(str(value))
                    file_object = stack.enter_context(open(path, "rb"))
                    files[fname] = (path.name, file_object)

                return getattr(requests, method)(
                    url=self.base_url + url,
                    headers=headers,
                    data=body or None,
                    files=files,
                )

        headers["Content-Type"] = "application/json"
        return getattr(requests, method)(
            url=self.base_url + url,
            headers=headers,
            json=body or None,
        )


def query(
    arg: BaseModel,
    token: str | None = None,
    base_url: str = YOUGILE_URL,
) -> requests.Response:
    """Выполнить синхронный запрос к YouGile API."""
    return Client(token=token, base_url=base_url).query(arg)
