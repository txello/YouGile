from pydantic import BaseModel


class CompanyController_get(BaseModel):
    """
    Получить детали

    Args:
        token: str - Токен (Обязательно)

    https://ru.yougile.com/api-v2#/operations/CompanyController_get
    """

    _method: str = "post"
    _url: str = "/api-v2/companies*"
    token: str | None = None


class CompanyController_update(BaseModel):
    """
    Изменить

    Args:
        token: str - Токен (Обязательно)

        deleted: bool - Если true, значит объект удален
        title: str - Название компании
        apiData: dict - Вспомогательные данные для разработки


    https://ru.yougile.com/api-v2#/operations/CompanyController_update
    """

    _method: str = "put"
    _url: str = "/api-v2/companies*"
    token: str | None = None

    deleted: bool | None = None
    title: str | None = None
    apiData: dict | None = None
