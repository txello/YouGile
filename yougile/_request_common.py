import os
from contextlib import ExitStack
from dataclasses import dataclass
from io import IOBase
from pathlib import Path
from typing import Any, cast

from pydantic import BaseModel

from .errors import MissingTokenError

YOUGILE_URL = "https://ru.yougile.com"


@dataclass(slots=True)
class PreparedRequest:
    method: str
    url: str
    headers: dict[str, str]
    json_body: dict[str, Any] | None
    form_body: dict[str, Any] | None
    file_field_names: tuple[str, ...]


def normalize_base_url(base_url: str) -> str:
    return base_url.rstrip("/")


def prepare_request(
    arg: BaseModel,
    *,
    fallback_token: str | None,
) -> PreparedRequest:
    model = arg.model_copy()
    url = str(getattr(model, "_url"))
    method = str(getattr(model, "_method", "get")).lower()
    headers: dict[str, str] = {}

    request_token = fallback_token
    if hasattr(model, "token"):
        model_token = cast(str | None, getattr(model, "token"))
        if request_token is None:
            request_token = model_token
        delattr(model, "token")

        if request_token is None:
            raise MissingTokenError(
                "This request requires a token. Pass it in the model, query(...), "
                "or Client(...)."
            )

    if request_token is not None:
        headers["Authorization"] = f"Bearer {request_token}"

    url_parse_names = cast(tuple[str, ...], tuple(getattr(model, "_url_parse", ())))
    if url_parse_names:
        url = url.format(**{name: getattr(model, name) for name in url_parse_names})

    for name in url_parse_names:
        delattr(model, name)

    params_parts: list[str] = []
    for name in cast(tuple[str, ...], tuple(getattr(model, "_url_params", ()))):
        value = getattr(model, name)
        if value is not None:
            params_parts.append(f"{name}={value}")
        delattr(model, name)
    if params_parts:
        url = f"{url}?{'&'.join(params_parts)}"

    body = cast(dict[str, Any], model.model_dump(exclude_none=True))
    file_field_names = cast(tuple[str, ...], tuple(getattr(model, "_file", ())))

    if file_field_names:
        return PreparedRequest(
            method=method,
            url=url,
            headers=headers,
            json_body=None,
            form_body=body,
            file_field_names=file_field_names,
        )

    headers["Content-Type"] = "application/json"
    return PreparedRequest(
        method=method,
        url=url,
        headers=headers,
        json_body=body or None,
        form_body=None,
        file_field_names=file_field_names,
    )


def build_multipart_files(
    body: dict[str, Any],
    file_field_names: tuple[str, ...],
    stack: ExitStack,
) -> dict[str, Any]:
    files: dict[str, Any] = {}
    for field_name in file_field_names:
        value = body.pop(field_name, None)
        if value is None:
            continue

        if (
            isinstance(value, tuple)
            and 2 <= len(value) <= 3
            and isinstance(value[0], str)
        ):
            files[field_name] = value
            continue

        if isinstance(value, (bytes, bytearray)):
            files[field_name] = (f"{field_name}.bin", bytes(value))
            continue

        if isinstance(value, IOBase):
            name = getattr(value, "name", f"{field_name}.bin")
            files[field_name] = (os.path.basename(str(name)), value)
            continue

        path = Path(str(value))
        file_object = stack.enter_context(open(path, "rb"))
        files[field_name] = (path.name, file_object)

    return files
