from pydantic import BaseModel


class StringStickerStateController_get(BaseModel):
    """
    Получить по ID

    Args:
        token (str): Токен

        stickerId (str): ID текстового стикера
        stickerStateId (str): ID состояния текстового стикера
        includeDeleted (bool, optional): По умолчанию, если объект был отмечен как удаленный, то он не будет найден. Поставьте true, чтобы удаленные объекты возвращались

    https://ru.yougile.com/api-v2#/operations/StringStickerStateController_get
    """

    _method: str = "get"
    _url: str = "/api-v2/string-stickers/{stickerId}/states/{stickerStateId}"
    _url_parse: tuple = ("stickerId", "stickerStateId")
    token: str
    _url_params: tuple = ("includeDeleted",)

    stickerId: str
    stickerStateId: str
    includeDeleted: bool | None = None


class StringStickerStateController_update(BaseModel):
    """
    Изменить

    Args:
        token (str): Токен

        stickerId (str): ID текстового стикера
        stickerStateId (str): ID состояния текстового стикера
        deleted (bool, optional): Если true, значит объект удален
        name (str, optional): Имя состояния стикера
        color (str, optional): Цвет состояния стикера

    https://ru.yougile.com/api-v2#/operations/StringStickerStateController_update
    """

    _method: str = "put"
    _url: str = "/api-v2/string-stickers/{stickerId}/states/{stickerStateId}"
    _url_parse: tuple = ("stickerId", "stickerStateId")
    token: str

    stickerId: str
    stickerStateId: str
    deleted: bool | None = None
    name: str | None = None
    color: str | None = None


class StringStickerStateController_create(BaseModel):
    """
    Создать

    Args:
        token (str): Токен

        stickerId (str): ID текстового стикера
        name (str): Имя состояния стикера
        color (str, optional): Цвет состояния стикера

    https://ru.yougile.com/api-v2#/operations/StringStickerStateController_create
    """

    _method: str = "post"
    _url: str = "/api-v2/string-stickers/{stickerId}/states"
    token: str
    _url_parse: tuple = ("stickerId",)

    stickerId: str
    name: str
    color: str | None = None
