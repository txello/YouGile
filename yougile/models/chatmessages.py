from pydantic import BaseModel


class ChatMessageController_search(BaseModel):
    """
    Получить историю сообщений

    Args:
        token (str): Токен

        chatId (str): ID чата
        fromUserId (str, optional): ID сотрудника от кого сообщение
        includeDeleted (bool, optional): По умолчанию, если объект был отмечен как удаленный, то он не будет найден. Поставьте true, чтобы удаленные объекты возвращались
        includeSystem (bool, optional): Включать ли системные сообщения. По умолчанию они не включаются
        label (str, optional): Поиск по быстрой ссылке сообщения
        limit (int, optional): Количество элементов, которые хочется получить. Максимум 1000
        offset (int, optional): Индекс первого элемента страницы
        since (int, optional): Искать среди сообщений, время создания которых позже указанного времени (timestamp)
        text (str, optional): Строка, которую сообщение должно содержать

    https://ru.yougile.com/api-v2#/operations/ChatMessageController_search
    """

    _method: str = "get"
    _url: str = "/api-v2/chats/{chatId}/messages"
    token: str | None = None
    _url_parse: tuple = ("chatId",)
    _url_params: tuple = (
        "fromUserId",
        "includeDeleted",
        "includeSystem",
        "label",
        "limit",
        "offset",
        "since",
        "text",
    )

    chatId: str
    fromUserId: str | None = None
    includeDeleted: bool | None = None
    includeSystem: bool | None = None
    label: str | None = None
    limit: int = 50
    offset: int = 0
    since: int | None = None
    text: str | None = None


class ChatMessageController_sendMessage(BaseModel):
    """
    Написать в чат

    Args:
        token (str): Токен

        chatId (str): ID чата
        text (str): Текст сообщения
        textHtml (int): Текст сообщения в формате HTML
        label (str): Быстрая ссылка

    https://ru.yougile.com/api-v2#/operations/ChatMessageController_sendMessage
    """

    _method: str = "post"
    _url: str = "/api-v2/chats/{chatId}/messages"
    token: str | None = None
    _url_parse: tuple = ("chatId",)

    chatId: str
    text: str
    textHtml: int
    label: str


class ChatMessageController_get(BaseModel):
    """
    Получить сообщение по ID

    Args:
        token (str): Токен

        chatId (str): ID чата
    id:str ID сообщения (Обязательно)

    https://ru.yougile.com/api-v2#/operations/ChatMessageController_get
    """

    _method: str = "get"
    _url: str = "/api-v2/chats/{chatId}/messages/{id}"
    token: str | None = None
    _url_parse: tuple = ("chatId", "id")
    chatId: str
    id: str


class ChatMessageController_update(BaseModel):
    """
    Изменить сообщение

    Args:
        token (str): Токен

        chatId (str): ID чата
        id (str): ID сообщения
        deleted (bool, optional): Если true, значит объект удален
        label (str, optional): Быстрая ссылка
        react (str): Список реакций админа. Допустимые значения: 👍 👎 👏 🙂 😀 😕 🎉 ❤ 🚀 ✔ (По умолчанию = 👍)

    https://ru.yougile.com/api-v2#/operations/ChatMessageController_update
    """

    _method: str = "put"
    _url: str = "/api-v2/chats/{chatId}/messages/{id}"
    token: str | None = None
    _url_parse: tuple = ("chatId", "id")

    chatId: str
    id: str
    deleted: bool | None = None
    label: str | None = None
    react: str = "👍"
