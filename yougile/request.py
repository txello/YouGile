from contextlib import ExitStack

import requests
from pydantic import BaseModel

from ._request_common import (
    YOUGILE_URL,
    build_multipart_files,
    normalize_base_url,
    prepare_request,
)


class Client:
    """Клиент YouGile API с настройками подключения."""

    def __init__(
        self,
        token: str | None = None,
        base_url: str = YOUGILE_URL,
        timeout: float | None = None,
    ) -> None:
        self.token = token
        self.base_url = normalize_base_url(base_url)
        self.timeout = timeout

    def query(
        self,
        arg: BaseModel,
        token: str | None = None,
    ) -> requests.Response:
        prepared = prepare_request(
            arg,
            fallback_token=token or self.token,
        )

        if prepared.file_field_names:
            with ExitStack() as stack:
                form_body = dict(prepared.form_body or {})
                files = build_multipart_files(form_body, prepared.file_field_names, stack)
                return getattr(requests, prepared.method)(
                    url=self.base_url + prepared.url,
                    headers=prepared.headers,
                    data=form_body or None,
                    files=files,
                    timeout=self.timeout,
                )

        return getattr(requests, prepared.method)(
            url=self.base_url + prepared.url,
            headers=prepared.headers,
            json=prepared.json_body,
            timeout=self.timeout,
        )


def query(
    arg: BaseModel,
    token: str | None = None,
    base_url: str = YOUGILE_URL,
) -> requests.Response:
    """Выполнить синхронный запрос к YouGile API."""
    return Client(token=token, base_url=base_url).query(arg)
