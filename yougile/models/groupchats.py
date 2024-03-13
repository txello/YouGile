from pydantic import BaseModel

class GroupChatController_search(BaseModel):
    '''
    Получить список чатов
    
    token:str - Токен (Обязательно)
    includeDeleted:bool - По умолчанию, если объект был отмечен как удаленный, то он не будет найден. Поставьте true, чтобы удаленные объекты возвращались (Необязательно)
    limit:int - Количество элементов, которые хочется получить. Максимум 1000 (По умолчанию = 50)
    offset:int - Индекс первого элемента страницы (По умолчанию = 0)
    title:str - Имя чата (Необязательно)
    
    https://ru.yougile.com/api-v2#/operations/GroupChatController_search
    '''
    _method:str = 'get'
    _url:str = '/api-v2/group-chats'
    token:str
    _url_params:tuple = ('includeDeleted','limit','offset','title')
    includeDeleted:bool|None = None
    limit:int=50
    offset:int=0
    title:str|None = None
    
class GroupChatController_create(BaseModel):
    '''
    Создать чат
    
    token:str - Токен (Обязательно)
    title:str - Название чата (Обязательно)
    users:dict -Сотрудники в чате (Обязательно)
    
    https://ru.yougile.com/api-v2#/operations/GroupChatController_create
    '''
    _method:str = 'post'
    _url:str = '/api-v2/group-chats'
    token:str
    title:str
    users:dict
    
class GroupChatController_get(BaseModel):
    '''
    Получить по ID
    
    token:str - Токен (Обязательно)
    id:str - ID чата (Обязательно)
    
    https://ru.yougile.com/api-v2#/operations/GroupChatController_get
    '''
    _method:str = 'get'
    _url:str = '/api-v2/group-chats/{id}'
    token:str
    _url_parse:tuple = ('id',)
    id:str
    
class BoardController_update(BaseModel):
    '''
    Изменить
    
    token:str - Токен (Обязательно)
    id:str - ID чата (Обязательно)
    deleted:bool - Если true, значит объект удален (Обязательно)
    title:str - Название чата (Обязательно)
    users:dict - Сотрудники в чате (Обязательно)
    
    https://ru.yougile.com/api-v2#/operations/BoardController_update
    '''
    _method:str = 'put'
    _url:str = '/api-v2/group-chats/{id}'
    token:str
    _url_parse:tuple = ('id',)
    id:str
    deleted:bool
    title:str
    users:dict