from pydantic import BaseModel


class ProjectRolesController_search(BaseModel):
    """
    Получить список

    Args:
        token (str): Токен

        projectId (str): ID проекта
        limit (int): Количество элементов, которые хочется получить. Максимум 1000 (По умолчанию = 50)
        name (str, optional): Имя роли
        offset (int): Индекс первого элемента страницы  (По умолчанию = 0)

    https://ru.yougile.com/api-v2#/operations/ProjectRolesController_search
    """

    _method: str = "get"
    _url: str = "/api-v2/projects/{projectId}/roles"
    token: str
    _url_parse: tuple = ("projectId",)
    _url_params: tuple = ("limit", "name", "offset")

    projectId: str
    limit: int = 50
    name: str | None = None
    offset: int = 0


class ProjectRolesController_create(BaseModel):
    """
    Создать

    Args:
        token (str): Токен

        projectId (str): ID проекта
        name (str): Название роли
        description (str, optional): Описание роли
        permissions (dict): Права в проекте

    https://ru.yougile.com/api-v2#/operations/ProjectRolesController_create
    """

    _method: str = "post"
    _url: str = "/api-v2/projects/{projectId}/roles"
    token: str
    _url_parse: tuple = ("projectId",)

    projectId: str
    name: str
    description: str | None = None
    permissions: dict


class ProjectRolesController_get(BaseModel):
    """
    Получить по ID

    Args:
        token (str): Токен

        id (str): ID роли проекта
        projectId (str): ID проекта

    https://ru.yougile.com/api-v2#/operations/ProjectRolesController_get
    """

    _method: str = "get"
    _url: str = "/api-v2/projects/{projectId}/roles/{id}"
    token: str
    _url_parse: tuple = ("projectId", "id")

    id: str
    projectId: str


class ProjectRolesController_update(BaseModel):
    """
    Изменить

    Args:
        token (str): Токен

        id (str): ID проекта
        projectId (str): ID проекта
        name (str, optional): Название роли
        description (str, optional): Описание роли
        permissions (dict): Права в проекте

    https://ru.yougile.com/api-v2#/operations/ProjectRolesController_update
    """

    _method: str = "put"
    _url: str = "/api-v2/projects/{projectId}/roles/{id}"
    token: str
    _url_parse: tuple = ("projectId", "id")

    id: str
    projectId: str
    name: str | None = None
    description: str | None = None
    permissions: dict


class ProjectRolesController_delete(BaseModel):
    """
    Удалить

    Args:
        token (str): Токен

        id (str): ID роли проекта
        projectId (str): ID проекта

    https://ru.yougile.com/api-v2#/operations/ProjectRolesController_delete
    """

    _method: str = "delete"
    _url: str = "/api-v2/projects/{projectId}/roles/{id}"
    token: str
    _url_parse: tuple = ("projectId", "id")

    id: str
    projectId: str
