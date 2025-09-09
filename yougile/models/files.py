from pydantic import BaseModel


class FileController_uploadFile(BaseModel):
    """
    Загрузить

    Загружает файл на сервер и возвращает его URL.
    Если вы хотите использовать curl из командной строки, не указывайте явно boundary в Content-Type — curl сам выставит нужный заголовок.

    Args:
        token (str): Токен

    file: bytes - Файл (Обязательно)

    https://ru.yougile.com/api-v2#/operations/FileController_uploadFile
    """

    _method: str = "post"
    _url: str = "/api-v2/upload-file"
    token: str
    _file: tuple = ("file",)

    file: str
