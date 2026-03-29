from pathlib import Path
from typing import Any

import httpx
import pytest
import requests
from pydantic import BaseModel

import yougile


class AuthenticatedQueryModel(BaseModel):
    token: str | None = None
    chatId: str
    includeArchived: bool | None = None

    _url = "/api-v2/chats/{chatId}"
    _method = "get"
    _url_parse = ("chatId",)
    _url_params = ("includeArchived",)


class PublicQueryModel(BaseModel):
    companyId: str

    _url = "/api-v2/public/{companyId}"
    _method = "get"
    _url_parse = ("companyId",)


class UploadModel(BaseModel):
    token: str | None = None
    file: Any
    description: str | None = None

    _url = "/api-v2/files"
    _method = "post"
    _file = ("file",)


class OptionalUploadModel(BaseModel):
    token: str | None = None
    file: Any | None = None
    description: str | None = None

    _url = "/api-v2/files"
    _method = "post"
    _file = ("file",)


class FileObjectUploadModel(BaseModel):
    token: str | None = None
    file: Any
    description: str | None = None

    _url = "/api-v2/files"
    _method = "post"
    _file = ("file",)

    def model_dump(self, *args: Any, **kwargs: Any) -> dict[str, Any]:
        return {
            "file": self.file,
            "description": self.description,
        }


class ComplexQueryModel(BaseModel):
    token: str | None = None
    companyId: str
    boardId: str
    limit: int | None = None
    archived: bool | None = None

    _url = "/api-v2/companies/{companyId}/boards/{boardId}"
    _method = "get"
    _url_parse = ("companyId", "boardId")
    _url_params = ("limit", "archived")


def test_query_uses_model_token(monkeypatch: pytest.MonkeyPatch) -> None:
    captured: dict[str, Any] = {}

    def fake_get(**kwargs: Any) -> requests.Response:
        captured.update(kwargs)
        return requests.Response()

    monkeypatch.setattr(requests, "get", fake_get)

    model = AuthenticatedQueryModel(
        token="model-token",
        chatId="42",
        includeArchived=True,
    )
    response = yougile.query(model)

    assert isinstance(response, requests.Response)
    assert captured["url"] == "https://ru.yougile.com/api-v2/chats/42?includeArchived=True"
    assert captured["headers"]["Authorization"] == "Bearer model-token"
    assert captured["headers"]["Content-Type"] == "application/json"
    assert captured["json"] is None


def test_client_token_and_timeout_apply_to_request(monkeypatch: pytest.MonkeyPatch) -> None:
    captured: dict[str, Any] = {}

    def fake_get(**kwargs: Any) -> requests.Response:
        captured.update(kwargs)
        return requests.Response()

    monkeypatch.setattr(requests, "get", fake_get)

    client = yougile.Client(
        token="client-token",
        base_url="https://example.yougile.local/",
        timeout=7.5,
    )
    model = AuthenticatedQueryModel(chatId="7")

    client.query(model)

    assert captured["url"] == "https://example.yougile.local/api-v2/chats/7"
    assert captured["headers"]["Authorization"] == "Bearer client-token"
    assert captured["timeout"] == 7.5


def test_query_raises_without_token() -> None:
    model = AuthenticatedQueryModel(chatId="42")

    with pytest.raises(yougile.MissingTokenError):
        yougile.query(model)


def test_public_query_does_not_require_token(monkeypatch: pytest.MonkeyPatch) -> None:
    captured: dict[str, Any] = {}

    def fake_get(**kwargs: Any) -> requests.Response:
        captured.update(kwargs)
        return requests.Response()

    monkeypatch.setattr(requests, "get", fake_get)

    response = yougile.query(PublicQueryModel(companyId="abc"))

    assert isinstance(response, requests.Response)
    assert captured["url"] == "https://ru.yougile.com/api-v2/public/abc"
    assert "Authorization" not in captured["headers"]


def test_query_uploads_files(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    captured: dict[str, Any] = {}
    file_path = tmp_path / "report.txt"
    file_path.write_text("payload", encoding="utf-8")

    def fake_post(**kwargs: Any) -> requests.Response:
        captured.update(kwargs)
        return requests.Response()

    monkeypatch.setattr(requests, "post", fake_post)

    model = UploadModel(
        token="upload-token",
        file=str(file_path),
        description="Quarterly report",
    )
    yougile.query(model)

    assert captured["data"] == {"description": "Quarterly report"}
    assert captured["files"]["file"][0] == "report.txt"
    assert captured["headers"]["Authorization"] == "Bearer upload-token"
    assert "Content-Type" not in captured["headers"]


def test_query_token_argument_has_highest_priority(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured: dict[str, Any] = {}

    def fake_get(**kwargs: Any) -> requests.Response:
        captured.update(kwargs)
        return requests.Response()

    monkeypatch.setattr(requests, "get", fake_get)

    client = yougile.Client(token="client-token")
    model = AuthenticatedQueryModel(token="model-token", chatId="314")

    client.query(model, token="call-token")

    assert captured["headers"]["Authorization"] == "Bearer call-token"


def test_query_normalizes_base_url_and_skips_none_query_params(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured: dict[str, Any] = {}

    def fake_get(**kwargs: Any) -> requests.Response:
        captured.update(kwargs)
        return requests.Response()

    monkeypatch.setattr(requests, "get", fake_get)

    model = ComplexQueryModel(
        token="query-token",
        companyId="c-1",
        boardId="b-2",
        limit=50,
        archived=None,
    )

    response = yougile.query(model, base_url="https://custom.yougile.local/")

    assert isinstance(response, requests.Response)
    assert (
        captured["url"]
        == "https://custom.yougile.local/api-v2/companies/c-1/boards/b-2?limit=50"
    )


def test_query_normalizes_base_url_without_trailing_slash(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured: dict[str, Any] = {}

    def fake_get(**kwargs: Any) -> requests.Response:
        captured.update(kwargs)
        return requests.Response()

    monkeypatch.setattr(requests, "get", fake_get)

    model = AuthenticatedQueryModel(token="query-token", chatId="11")
    yougile.query(model, base_url="https://custom.yougile.local")

    assert captured["url"] == "https://custom.yougile.local/api-v2/chats/11"


def test_query_includes_multiple_query_params(monkeypatch: pytest.MonkeyPatch) -> None:
    captured: dict[str, Any] = {}

    def fake_get(**kwargs: Any) -> requests.Response:
        captured.update(kwargs)
        return requests.Response()

    monkeypatch.setattr(requests, "get", fake_get)

    model = ComplexQueryModel(
        token="query-token",
        companyId="c-1",
        boardId="b-2",
        limit=50,
        archived=False,
    )

    yougile.query(model)

    assert (
        captured["url"]
        == "https://ru.yougile.com/api-v2/companies/c-1/boards/b-2?limit=50&archived=False"
    )


def test_query_does_not_mutate_original_model(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake_get(**kwargs: Any) -> requests.Response:
        return requests.Response()

    monkeypatch.setattr(requests, "get", fake_get)

    model = ComplexQueryModel(
        token="stable-token",
        companyId="original-company",
        boardId="original-board",
        limit=10,
    )

    yougile.query(model)

    assert model.token == "stable-token"
    assert model.companyId == "original-company"
    assert model.boardId == "original-board"
    assert model.limit == 10


def test_query_uploads_bytes_payload(monkeypatch: pytest.MonkeyPatch) -> None:
    captured: dict[str, Any] = {}

    def fake_post(**kwargs: Any) -> requests.Response:
        captured.update(kwargs)
        return requests.Response()

    monkeypatch.setattr(requests, "post", fake_post)

    model = UploadModel(
        token="upload-token",
        file=b"raw-bytes",
        description="Binary payload",
    )
    yougile.query(model)

    assert captured["files"]["file"][0] == "file.bin"
    assert captured["files"]["file"][1] == b"raw-bytes"


def test_query_uploads_file_object(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    captured: dict[str, Any] = {}
    file_path = tmp_path / "file-object.txt"
    file_path.write_text("payload", encoding="utf-8")

    def fake_post(**kwargs: Any) -> requests.Response:
        captured.update(kwargs)
        return requests.Response()

    monkeypatch.setattr(requests, "post", fake_post)

    with file_path.open("rb") as file_object:
        model = FileObjectUploadModel(
            token="upload-token",
            file=file_object,
            description="File object payload",
        )
        yougile.query(model)

    assert captured["files"]["file"][0] == "file-object.txt"


def test_query_passes_tuple_file_payload_through(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured: dict[str, Any] = {}
    file_tuple = ("report.bin", b"tuple-bytes", "application/octet-stream")

    def fake_post(**kwargs: Any) -> requests.Response:
        captured.update(kwargs)
        return requests.Response()

    monkeypatch.setattr(requests, "post", fake_post)

    model = UploadModel(
        token="upload-token",
        file=file_tuple,
        description="Tuple payload",
    )
    yougile.query(model)

    assert captured["files"]["file"] == file_tuple


def test_query_with_empty_file_field_sends_multipart_without_files(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured: dict[str, Any] = {}

    def fake_post(**kwargs: Any) -> requests.Response:
        captured.update(kwargs)
        return requests.Response()

    monkeypatch.setattr(requests, "post", fake_post)

    model = OptionalUploadModel(
        token="upload-token",
        file=None,
        description="No file attached",
    )
    yougile.query(model)

    assert captured["data"] == {"description": "No file attached"}
    assert captured["files"] == {}
    assert "Content-Type" not in captured["headers"]


@pytest.mark.asyncio
async def test_public_async_client_query_does_not_require_token(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured: dict[str, Any] = {}

    class FakeAsyncClient:
        async def __aenter__(self) -> "FakeAsyncClient":
            return self

        async def __aexit__(self, exc_type: Any, exc: Any, tb: Any) -> None:
            return None

        async def request(self, **kwargs: Any) -> httpx.Response:
            captured.update(kwargs)
            return httpx.Response(200)

    monkeypatch.setattr(httpx, "AsyncClient", FakeAsyncClient)

    response = await yougile.AsyncClient().query(PublicQueryModel(companyId="public-id"))

    assert response.status_code == 200
    assert captured["url"] == "https://ru.yougile.com/api-v2/public/public-id"
    assert "Authorization" not in captured["headers"]


@pytest.mark.asyncio
async def test_query_async_uses_client_token_and_timeout(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured: dict[str, Any] = {}

    class FakeAsyncClient:
        async def __aenter__(self) -> "FakeAsyncClient":
            return self

        async def __aexit__(self, exc_type: Any, exc: Any, tb: Any) -> None:
            return None

        async def request(self, **kwargs: Any) -> httpx.Response:
            captured.update(kwargs)
            return httpx.Response(200, json={"ok": True})

    monkeypatch.setattr(httpx, "AsyncClient", FakeAsyncClient)

    client = yougile.AsyncClient(
        token="async-token",
        base_url="https://async.yougile.local/",
        timeout=2.5,
    )
    model = AuthenticatedQueryModel(chatId="99")

    response = await client.query(model)

    assert response.status_code == 200
    assert captured["method"] == "get"
    assert captured["url"] == "https://async.yougile.local/api-v2/chats/99"
    assert captured["headers"]["Authorization"] == "Bearer async-token"
    assert captured["timeout"] == 2.5


@pytest.mark.asyncio
async def test_query_async_raises_without_token() -> None:
    model = AuthenticatedQueryModel(chatId="100")

    with pytest.raises(yougile.MissingTokenError):
        await yougile.query_async(model)


@pytest.mark.asyncio
async def test_query_async_uploads_files(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    captured: dict[str, Any] = {}
    file_path = tmp_path / "async-report.txt"
    file_path.write_text("payload", encoding="utf-8")

    class FakeAsyncClient:
        async def __aenter__(self) -> "FakeAsyncClient":
            return self

        async def __aexit__(self, exc_type: Any, exc: Any, tb: Any) -> None:
            return None

        async def request(self, **kwargs: Any) -> httpx.Response:
            captured.update(kwargs)
            return httpx.Response(201)

    monkeypatch.setattr(httpx, "AsyncClient", FakeAsyncClient)

    model = UploadModel(
        token="async-upload-token",
        file=str(file_path),
        description="Async quarterly report",
    )
    response = await yougile.query_async(model)

    assert response.status_code == 201
    assert captured["method"] == "post"
    assert captured["data"] == {"description": "Async quarterly report"}
    assert captured["files"]["file"][0] == "async-report.txt"
    assert captured["headers"]["Authorization"] == "Bearer async-upload-token"
    assert "Content-Type" not in captured["headers"]


def test_public_symbols_are_exported() -> None:
    assert yougile.Client is not None
    assert yougile.AsyncClient is not None
    assert yougile.MissingTokenError is not None
    assert yougile.query is not None
    assert yougile.query_async is not None
