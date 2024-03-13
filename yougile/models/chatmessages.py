from pydantic import BaseModel

class ChatMessageController_search(BaseModel):
    '''
    Получить историю сообщений
    
    token:str - Токен (Обязательно)
    chatId:str - ID чата (Обязательно)
    fromUserId:str - ID сотрудника от кого сообщение (Необязательно)
    includeDeleted:bool - По умолчанию, если объект был отмечен как удаленный, то он не будет найден. Поставьте true, чтобы удаленные объекты возвращались (Необязательно)
    includeSystem:bool - Включать ли системные сообщения. По умолчанию они не включаются (Необязательно)
    label:str - Поиск по быстрой ссылке сообщения (Необязательно)
    limit:int - Количество элементов, которые хочется получить. Максимум 1000 (Необязательно)
    offset:int - Индекс первого элемента страницы (Необязательно)
    since:int - Искать среди сообщений, время создания которых позже указанного времени (timestamp) (Необязательно)
    text:str - Строка, которую сообщение должно содержать (Необязательно)
    
    https://ru.yougile.com/api-v2#/operations/ChatMessageController_search
    '''
    _method:str = 'get'
    _url:str = '/api-v2/chats/{chatId}/messages'
    token:str
    _url_parse:tuple = ('chatId',)
    _url_params:tuple = ('fromUserId','includeDeleted','includeSystem','label','limit','offset','since','text')
    chatId:str
    fromUserId:str|None = None
    includeDeleted:bool|None = None
    includeSystem:bool|None = None
    label:str|None = None
    limit:int=50
    offset:int=0
    since:int|None = None
    text:str|None = None
    
class ChatMessageController_sendMessage(BaseModel):
    '''
    Написать в чат
    
    token:str - Токен (Обязательно)
    chatId:str - ID чата (Обязательно)
    text:str - Текст сообщения (Обязательно)
    textHtml:int - Текст сообщения в формате HTML (Обязательно)
    label:str - Быстрая ссылка (Обязательно)
    
    https://ru.yougile.com/api-v2#/operations/ChatMessageController_sendMessage
    '''
    _method:str = 'post'
    _url:str = '/api-v2/chats/{chatId}/messages'
    token:str
    _url_parse:tuple = ('chatId',)
    chatId:str
    text:str
    textHtml:int
    label:str
    
class ChatMessageController_get(BaseModel):
    '''
    Получить сообщение по ID
    
    token:str - Токен (Обязательно)
    chatId:str - ID чата (Обязательно)
    id:str ID сообщения (Обязательно)
    
    https://ru.yougile.com/api-v2#/operations/ChatMessageController_get
    '''
    _method:str = 'get'
    _url:str = '/api-v2/chats/{chatId}/messages/{id}'
    token:str
    _url_parse:tuple = ('chatId','id')
    chatId:str
    id:str
    
class ChatMessageController_update(BaseModel):
    '''
    Изменить сообщение
    
    token:str - Токен (Обязательно)
    chatId:str - ID чата (Обязательно)
    id:str - ID сообщения (Обязательно)
    deleted:bool - Если true, значит объект удален (Необязательно)
    label:str - Быстрая ссылка (Необязательно)
    react:str - Список реакций админа. Допустимые значения: 👍 👎 👏 🙂 😀 😕 🎉 ❤ 🚀 ✔ (По умолчанию = 👍)

    https://ru.yougile.com/api-v2#/operations/ChatMessageController_update
    '''
    _method:str = 'put'
    _url:str = '/api-v2/chats/{chatId}/messages/{id}'
    token:str
    _url_parse:tuple = ('chatId','id')
    chatId:str
    id:str
    deleted:bool|None = None
    label:str|None = None
    react:str = '👍'