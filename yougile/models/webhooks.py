from pydantic import BaseModel

class WebhookController_create(BaseModel):
    '''
    Создать подписку
    
    token:str - Токен (Обязательно)
    url:str - URL подписки (Обязательно)
    event:str - Событие подписки. Формат: <тип_объекта>-<событие>. Для объектов project,board,column,task,sticker,department,group_chat,chat_message, возможные события: created,deleted,restored,moved,renamed,updated. Для объектов user, возможные события: added, removed. Может использоваться javascript regexp как значение. Например, task-* - подписка на все события по задачам, или .* - подписка на все события (Обязательно)
    
    https://ru.yougile.com/api-v2#/operations/WebhookController_create
    '''
    _method:str = 'post'
    _url:str = '/api-v2/webhooks'
    token:str
    url:str
    event:str
    
class WebhookController_search(BaseModel):
    '''
    Получить список подписок
    
    token:str - Токен (Обязательно)
    includeDeleted:bool - По умолчанию, если объект был отмечен как удаленный, то он не будет найден. Поставьте true, чтобы удаленные объекты возвращались (Необязательно)
    
    https://ru.yougile.com/api-v2#/operations/WebhookController_search
    '''
    _method:str = 'get'
    _url:str = '/api-v2/webhooks'
    token:str
    _url_params:tuple = ('includeDeleted',)
    includeDeleted:bool|None = None

class WebhookController_put(BaseModel):
    '''
    Изменить подписку
    
    token:str - Токен (Обязательно)
    id:str - ID подписки (Обязательно)
    deleted:bool - Если true, значит объект удален (Необязательно)
    url:str - URL подписки (Необязательно)
    event:str - Событие подписки. Формат: <тип_объекта>-<событие>. Для объектов project,board,column,task,sticker,department,group_chat,chat_message, возможные события: created,deleted,restored,moved,renamed,updated. Для объектов user, возможные события: added, removed. Может использоваться javascript regexp как значение. Например, task-* - подписка на все события по задачам, или .* - подписка на все события (Необязательно)
    disabled:bool - Если true, то вызываться не будет (Необязательно)
    
    https://ru.yougile.com/api-v2#/operations/WebhookController_put
    '''
    _method:str = 'put'
    _url:str = '/api-v2/webhooks/{id}'
    token:str
    _url_parse:tuple = ('id',)
    id:str
    deleted:bool|None = None
    url:str|None = None
    event:str|None = None
    disabled:bool|None = None