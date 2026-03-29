from pydantic import BaseModel


class CrmExternalIdController_findContactByExternalId(BaseModel):
    """
    Найти контакт по внешнему ID

    Найти контакт CRM по идентификатору внешнего мессенджера

    Args:
        chatId (str): ID чата во внешнем мессенджере
        provider (str): Провайдер внешней интеграции

    https://ru.yougile.com/api-v2#/operations/CrmExternalIdController_findContactByExternalId
    """

    _method: str = "get"
    token: str | None = None
    _url: str = "/api-v2/crm/contacts/by-external-id"
    chatId: str
    provider: str
