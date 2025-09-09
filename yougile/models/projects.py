from pydantic import BaseModel


class ProjectController_search(BaseModel):
    """
    Получить список

    Args:
        token (str): Токен

        includeDeleted (bool, optional): По умолчанию, если объект был отмечен как удаленный, то он не будет найден. Поставьте true, чтобы удаленные объекты возвращались
        limit (int): Количество элементов, которые хочется получить. Максимум 1000 (По умолчанию = 50)
        offset (int): Индекс первого элемента страницы (По умолчанию = 0)
        title (str, optional): Имя проекта

    https://ru.yougile.com/api-v2#/operations/ProjectController_search
    """

    _method: str = "get"
    _url: str = "/api-v2/projects"
    token: str
    _url_params: tuple = ("includeDeleted", "limit", "offset", "title")

    includeDeleted: bool | None = None
    limit: int = 50
    offset: int = 0
    title: str | None = None


class ProjectController_create(BaseModel):
    """
    Создать

    Args:
        token (str): Токен

        title (str): Название проекта
        users (dict, optional): Сотрудники на проекте и их роль. Возможные значения: 1) системные роли: worker, admin, observe 2) ID пользовательской роли 3) "-" для удаления существующего пользователя из проекта

    https://ru.yougile.com/api-v2#/operations/ProjectController_create
    """

    _method: str = "post"
    _url: str = "/api-v2/projects"
    token: str

    title: str
    users: dict | None = None


class ProjectController_get(BaseModel):
    """
    Получить по ID

    Args:
        token (str): Токен

        id (str): ID проекта

    https://ru.yougile.com/api-v2#/operations/ProjectController_get
    """

    _method: str = "get"
    _url: str = "/api-v2/projects/{id}"
    token: str
    _url_parse: tuple = ("id",)

    id: str


class ProjectController_update(BaseModel):
    """
    Изменить

    Args:
        token (str): Токен

        id (str): ID проекта
        deleted (bool, optional): Если true, значит объект удален
        title (str): Название проекта
        users (dict, optional): Сотрудники на проекте и их роль. Возможные значения: 1) системные роли: worker, admin, observe 2) ID пользовательской роли 3) "-" для удаления существующего пользователя из проекта

    https://ru.yougile.com/api-v2#/operations/ProjectController_update
    """

    _method: str = "put"
    _url: str = "/api-v2/projects/{id}"
    token: str
    _url_parse: tuple = ("id",)

    id: str
    deleted: bool | None = None
    title: str
    users: dict | None = None
