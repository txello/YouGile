from contextlib import ExitStack
from io import IOBase
import os
from pathlib import Path
from typing import Any
import requests
from pydantic import BaseModel


YOUGILE_URL = "https://ru.yougile.com"


def query(arg: BaseModel, token: str | None = None) -> requests.Response:
    """
    Универсальный запрос:
    - если модель содержит _file (имена полей-файлов) -> multipart/form-data (files=..., data=...)
    - иначе -> JSON (json=...)
    Поддерживаются варианты значений файлового поля:
      bytes | путь (str/Path) | файловый объект (IOBase) | ('name', bytes[, 'mime/type'])
    """
    arg = arg.model_copy()
    url: str = getattr(arg, "_url")
    method: str = getattr(arg, "_method", "get").lower()

    # --- Заголовки ---
    headers: dict[str, str] = {}

    # Авторизация
    if hasattr(arg, "token"):
        headers["Authorization"] = f"Bearer {token or getattr(arg, 'token')}"
        if token is None:
            delattr(arg, "token")

    # --- Path-параметры ---
    for name in getattr(arg, "_url_parse", ()):
        url = url.format(**{name: getattr(arg, name)})
        delattr(arg, name)

    # --- Query-параметры ---
    params_parts: list[str] = []
    for name in getattr(arg, "_url_params", ()):
        value = getattr(arg, name)
        if value is not None:
            params_parts.append(f"{name}={value}")
        delattr(arg, name)
    if params_parts:
        url = f"{url}?{'&'.join(params_parts)}"

    # --- Тело ---
    body: dict[str, Any] = arg.model_dump(exclude_none=True)

    # --- Файлы / multipart ---
    file_field_names = tuple(getattr(arg, "_file", ()))
    if file_field_names:
        # В multipart Content-Type выставляет requests -> не задаём его в headers
        with ExitStack() as stack:
            files: dict[str, Any] = {}
            for fname in file_field_names:
                v = body.pop(fname, None)
                if v is None:
                    continue

                # ('name.ext', bytes[, 'mime/type'])
                if isinstance(v, tuple) and 2 <= len(v) <= 3 and isinstance(v[0], str):
                    files[fname] = v
                    continue

                # bytes
                if isinstance(v, (bytes, bytearray)):
                    files[fname] = (f"{fname}.bin", bytes(v))
                    continue

                # файловый объект
                if isinstance(v, IOBase):
                    name = getattr(v, "name", f"{fname}.bin")
                    files[fname] = (os.path.basename(str(name)), v)
                    continue

                # путь (str/Path/os.PathLike)
                p = Path(str(v))
                fobj = stack.enter_context(open(p, "rb"))
                files[fname] = (p.name, fobj)

            return getattr(requests, method)(
                url=YOUGILE_URL + url,
                headers=headers,
                data=body or None,
                files=files,
            )

    # --- JSON ---
    headers["Content-Type"] = "application/json"
    return getattr(requests, method)(
        url=YOUGILE_URL + url,
        headers=headers,
        json=body or None,
    )
