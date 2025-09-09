from pydantic import BaseModel


class CompanyController_get(BaseModel):
    """
    Получить детали

    token: str - Токен (Обязательно)

    https://ru.yougile.com/api-v2#/operations/CompanyController_get
    """

    _method: str = "post"
    _url: str = "/api-v2/companies*"
    token: str


class CompanyController_update(BaseModel):
    """
    Изменить

    token: str - Токен (Обязательно)

    title: str - Название компании
    apiData: dict - Вспомогательные данные для разработки


    deleted: bool - Если true, значит объект удален


    https://ru.yougile.com/api-v2#/operations/CompanyController_update
    """

    _method: str = "put"
    _url: str = "/api-v2/companies*"
    token: str

    deleted: bool | None = None
    title: str | None = None
    apiData: dict | None = None
