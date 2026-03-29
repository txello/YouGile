from pydantic import BaseModel


class GroupChatController_search(BaseModel):
    """
    Получить список чатов

    Args:
        token (str): Токен

        includeDeleted (bool, optional): По умолчанию, если объект был отмечен как удаленный, то он не будет найден. Поставьте true, чтобы удаленные объекты возвращались
        limit (int): Количество элементов, которые хочется получить. Максимум 1000 (По умолчанию = 50)
        offset (int): Индекс первого элемента страницы (По умолчанию = 0)
        title (str, optional): Имя чата

    https://ru.yougile.com/api-v2#/operations/GroupChatController_search
    """

    _method: str = "get"
    _url: str = "/api-v2/group-chats"
    token: str | None = None
    _url_params: tuple = ("includeDeleted", "limit", "offset", "title")

    includeDeleted: bool | None = None
    limit: int = 50
    offset: int = 0
    title: str | None = None


class GroupChatController_create(BaseModel):
    """
    Создать чат

    Args:
        token (str): Токен

        title (str): Название чата
        users (dict): Сотрудники в чате
        userRoleMap (dict): Роли сотрудников в чате
        roleConfigMap (dict): Настройки ролей

    https://ru.yougile.com/api-v2#/operations/GroupChatController_create
    """

    _method: str = "post"
    _url: str = "/api-v2/group-chats"
    token: str | None = None

    title: str
    users: dict
    userRoleMap: dict
    roleConfigMap: dict


class GroupChatController_get(BaseModel):
    """
    Получить по ID

    Args:
        token (str): Токен

        id (str): ID чата

    https://ru.yougile.com/api-v2#/operations/GroupChatController_get
    """

    _method: str = "get"
    _url: str = "/api-v2/group-chats/{id}"
    token: str | None = None
    _url_parse: tuple = ("id",)

    id: str


class GroupChatController_update(BaseModel):
    """
    Изменить чат

    Args:
        token (str): Токен

        id (str): ID чата
        deleted (bool, optional): Если true, значит объект удален
        title (str, optional): Название чата
        users (dict, optional): Сотрудники в чате
        userRoleMap (dict, optional): Роли сотрудников в чате
        roleConfigMap (dict, optional): Настройки ролей

    https://ru.yougile.com/api-v2#/operations/GroupChatController_update
    """

    _method: str = "put"
    _url: str = "/api-v2/group-chats/{id}"
    token: str | None = None
    _url_parse: tuple = ("id",)

    id: str
    deleted: bool | None = None
    title: str | None = None
    users: dict | None = None
    userRoleMap: dict | None = None
    roleConfigMap: dict | None = None
