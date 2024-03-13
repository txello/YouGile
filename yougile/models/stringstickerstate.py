from pydantic import BaseModel

class StringStickerStateController_get(BaseModel):
    '''
    Получить по ID
    
    token:str - Токен (Обязательно)
    stickerId:str - ID текстового стикера (Обязательно)
    stickerStateId:str - ID состояния текстового стикера (Обязательно)
    includeDeleted:bool - По умолчанию, если объект был отмечен как удаленный, то он не будет найден. Поставьте true, чтобы удаленные объекты возвращались (Необязательно)
    
    https://ru.yougile.com/api-v2#/operations/StringStickerStateController_get
    '''
    _method:str = 'get'
    _url:str = '/api-v2/string-stickers/{stickerId}/states/{stickerStateId}'
    _url_parse:tuple = ('stickerId','stickerStateId')
    token:str
    _url_params:tuple = ('includeDeleted',)
    stickerId:str
    stickerStateId:str
    includeDeleted:bool|None = None
    
class StringStickerStateController_update(BaseModel):
    '''
    Изменить
    
    token:str - Токен (Обязательно)
    stickerId:str - ID текстового стикера (Обязательно)
    stickerStateId:str - ID состояния текстового стикера (Обязательно)
    deleted:bool - Если true, значит объект удален (Необязательно)
    name:str - Имя состояния стикера (Необязательно)
    color:str - Цвет состояния стикера (Необязательно)
    
    https://ru.yougile.com/api-v2#/operations/StringStickerStateController_update
    '''
    _method:str = 'put'
    _url:str = '/api-v2/string-stickers/{stickerId}/states/{stickerStateId}'
    _url_parse:tuple = ('stickerId','stickerStateId')
    token:str
    stickerId:str
    stickerStateId:str
    deleted:bool|None = None
    name:str|None = None
    color:str|None = None
    
class StringStickerStateController_create(BaseModel):
    '''
    Создать
    
    token:str - Токен (Обязательно)
    stickerId:str - ID текстового стикера (Обязательно)
    name:str - Имя состояния стикера (Обязательно)
    color:str - Цвет состояния стикера (Необязательно)
    
    https://ru.yougile.com/api-v2#/operations/StringStickerStateController_create
    '''
    _method:str = 'post'
    _url:str = '/api-v2/string-stickers/{stickerId}/states'
    token:str
    _url_parse:tuple = ('stickerId',)
    stickerId:str
    name:str
    color:str|None = None