from pydantic import BaseModel

class StringStickerController_search(BaseModel):
    '''
    Получить список
    
    token:str - Токен (Обязательно)
    boardId:str - ID доски (Необязательно)
    includeDeleted:bool - По умолчанию, если объект был отмечен как удаленный, то он не будет найден. Поставьте true, чтобы удаленные объекты возвращались (Необязательно)
    limit:int - Количество элементов, которые хочется получить. Максимум 1000 (По умолчанию = 50)
    name:str - Имя стикера (Необязательно)
    offset:int - Индекс первого элемента страницы (По умолчанию = 0)
    
    
    
    https://ru.yougile.com/api-v2#/operations/StringStickerController_search
    '''
    _method:str = 'get'
    _url:str = '/api-v2/string-stickers'
    token:str
    _url_params:tuple = ('boardId','includeDeleted','limit','name','offset')
    boardId:str|None = None
    includeDeleted:bool|None = None
    limit:int=50
    name:str|None = None
    offset:int=0
    
class StringStickerController_create(BaseModel):
    '''
    Создать
    
    token:str - Токен (Обязательно)
    name:str - Имя стикера (Обязательно)
    icon:str - Иконка стикера (Необязательно)
    states:list Состояния стикера (Обязательно)
    
    https://ru.yougile.com/api-v2#/operations/StringStickerController_create
    '''
    _method:str = 'post'
    _url:str = '/api-v2/string-stickers'
    token:str
    name:str
    icon:str|None = None
    states:list

class StringStickerController_get(BaseModel):
    '''
    Получить по ID
    
    token:str - Токен (Обязательно)
    id:str - ID стикера текстового (Обязательно)
    
    https://ru.yougile.com/api-v2#/operations/StringStickerController_get
    '''
    _method:str = 'get'
    _url:str = '/api-v2/string-stickers/{id}'
    token:str
    _url_parse:tuple = ('id',)
    id:str
    
class StringStickerController_update(BaseModel):
    '''
    Изменить
    
    token:str - Токен (Обязательно)
    id:str - ID стикера текстового (Обязательно)
    deleted:bool - Если true, значит объект удален (Необязательно)
    name:str - Имя стикера (Необязательно)
    icon:str - Иконка стикера (Необязательно)
    
    https://ru.yougile.com/api-v2#/operations/StringStickerController_update
    '''
    _method:str = 'put'
    _url:str = '/api-v2/string-stickers/{id}'
    token:str
    _url_parse:tuple = ('id',)
    id:str
    deleted:bool|None = None
    name:str|None = None
    icon:str|None = None