from pydantic import BaseModel


class SprintStickerController_search(BaseModel):
    """
    Получить список

    Args:
        token (str): Токен

        boardId (str, optional): ID доски
        includeDeleted (bool, optional): По умолчанию, если объект был отмечен как удаленный, то он не будет найден. Поставьте true, чтобы удаленные объекты возвращались
        limit (int): Количество элементов, которые хочется получить. Максимум 1000 (По умолчанию = 50)
        name (str, optional): Имя стикера
        offset (int): Индекс первого элемента страницы (По умолчанию = 0)

    https://ru.yougile.com/api-v2#/operations/SprintStickerController_search
    """

    _method: str = "get"
    _url: str = "/api-v2/sprint-stickers"
    token: str
    _url_params: tuple = ("boardId", "includeDeleted", "limit", "name", "offset")

    boardId: str | None = None
    includeDeleted: bool | None = None
    limit: int = 50
    name: str | None = None
    offset: int = 0


class SprintStickerController_create(BaseModel):
    """
    Создать

    Args:
        token (str): Токен

        name (str): Имя стикера
    states:list (Обязательно)

    https://ru.yougile.com/api-v2#/operations/SprintStickerController_create
    """

    _method: str = "post"
    _url: str = "/api-v2/sprint-stickers"
    token: str

    name: str
    states: list


class SprintStickerController_getSticker(BaseModel):
    """
    Получить по ID

    Args:
        token (str): Токен

        id (str): ID стикера спринта

    https://ru.yougile.com/api-v2#/operations/SprintStickerController_getSticker
    """

    _method: str = "get"
    _url: str = "/api-v2/sprint-stickers/{id}"
    token: str
    _url_parse: tuple = ("id",)

    id: str


class SprintStickerController_update(BaseModel):
    """
    Изменить

    Args:
        token (str): Токен

        id (str): ID стикера спринта
        deleted (bool, optional): Если true, значит объект удален
    name:str (Необязательно)

    https://ru.yougile.com/api-v2#/operations/SprintStickerController_update
    """

    _method: str = "put"
    _url: str = "/api-v2/sprint-stickers/{id}"
    token: str
    _url_parse: tuple = ("id",)

    id: str
    deleted: bool | None = None
    name: str | None = None
