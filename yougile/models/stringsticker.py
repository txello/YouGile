from pydantic import BaseModel


class StringStickerController_search(BaseModel):
    """
    Получить список

    Args:
        token (str): Токен

        boardId (str, optional): ID доски
        includeDeleted (bool, optional): По умолчанию, если объект был отмечен как удаленный, то он не будет найден. Поставьте true, чтобы удаленные объекты возвращались
        limit (int): Количество элементов, которые хочется получить. Максимум 1000 (По умолчанию = 50)
        name (str, optional): Имя стикера
        offset (int): Индекс первого элемента страницы (По умолчанию = 0)

    https://ru.yougile.com/api-v2#/operations/StringStickerController_search
    """

    _method: str = "get"
    _url: str = "/api-v2/string-stickers"
    token: str
    _url_params: tuple = ("boardId", "includeDeleted", "limit", "name", "offset")

    boardId: str | None = None
    includeDeleted: bool | None = None
    limit: int = 50
    name: str | None = None
    offset: int = 0


class StringStickerController_create(BaseModel):
    """
    Создать

    Args:
        token (str): Токен

        name (str): Имя стикера
        icon (str, optional): Иконка стикера
        states (list): Состояния стикера

    https://ru.yougile.com/api-v2#/operations/StringStickerController_create
    """

    _method: str = "post"
    _url: str = "/api-v2/string-stickers"
    token: str

    name: str
    icon: str | None = None
    states: list


class StringStickerController_get(BaseModel):
    """
    Получить по ID

    Args:
        token (str): Токен

        id (str): ID стикера текстового

    https://ru.yougile.com/api-v2#/operations/StringStickerController_get
    """

    _method: str = "get"
    _url: str = "/api-v2/string-stickers/{id}"
    token: str
    _url_parse: tuple = ("id",)

    id: str


class StringStickerController_update(BaseModel):
    """
    Изменить

    Args:
        token (str): Токен

        id (str): ID стикера текстового
        deleted (bool, optional): Если true, значит объект удален
        name (str, optional): Имя стикера
        icon (str, optional): Иконка стикера

    https://ru.yougile.com/api-v2#/operations/StringStickerController_update
    """

    _method: str = "put"
    _url: str = "/api-v2/string-stickers/{id}"
    token: str
    _url_parse: tuple = ("id",)

    id: str
    deleted: bool | None = None
    name: str | None = None
    icon: str | None = None
