from pydantic import BaseModel


class CrmContactPersonsController_create(BaseModel):
    """
    Создать контактное лицо

    Args:
        projectId (str): ID CRM проекта, где создаётся контакт
        title (str): Имя/название контактного лица
        fields (dict): Поля контактного лица

    https://ru.yougile.com/api-v2#/operations/CrmContactPersonsController_create
    """

    _method: str = "post"
    token: str | None = None
    _url: str = "/api-v2/crm/contact-persons"
    projectId: str
    title: str
    fields: dict
