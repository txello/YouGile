from pydantic import BaseModel

class SprintStickerStateController_get(BaseModel):
    '''
    Получить по ID
    
    token:str - Токен (Обязательно)
    stickerId:str - ID стикера (Обязательно)
    stickerStateId:str - ID состояния стикера (Обязательно)
    includeDeleted:bool - По умолчанию, если объект был отмечен как удаленный, то он не будет найден. Поставьте true, чтобы удаленные объекты возвращались (Необязательно)
    
    https://ru.yougile.com/api-v2#/operations/SprintStickerStateController_get
    '''
    _method:str = 'get'
    _url:str = '/api-v2/sprint-stickers/{stickerId}/states/{stickerStateId}'
    _url_parse:tuple = ('stickerId','stickerStateId')
    token:str
    _url_params:tuple = ('includeDeleted',)
    stickerId:str
    stickerStateId:str
    includeDeleted:bool|None = None
    
class SprintStickerStateController_update(BaseModel):
    '''
    Изменить
    
    token:str - Токен (Обязательно)
    stickerId:str - ID стикера (Обязательно)
    stickerStateId:str - ID состояния стикера (Обязательно)
    deleted:bool - Если true, значит объект удален (Необязательно)
    name:str - Имя состояния стикера (Необязательно)
    begin:int - Дата начала спринта в секундах от 01.01.1970 (Необязательно)
    end:int - Дата окончания спринта в секундах от 01.01.1970 (Необязательно)
    
    https://ru.yougile.com/api-v2#/operations/SprintStickerStateController_update
    '''
    _method:str = 'put'
    _url:str = '/api-v2/sprint-stickers/{stickerId}/states/{stickerStateId}'
    _url_parse:tuple = ('stickerId','stickerStateId')
    token:str
    stickerId:str
    stickerStateId:str
    deleted:bool|None = None
    name:str|None = None
    begin:int|None = None
    end:int|None = None
    
class SprintStickerStateController_create(BaseModel):
    '''
    Создать
    
    token:str - Токен (Обязательно)
    stickerId:str - ID стикера (Обязательно)
    name:str - Имя состояния стикера (Обязательно)
    begin:int - Дата начала спринта в секундах от 01.01.1970 (Необязательно)
    end:int - Дата окончания спринта в секундах от 01.01.1970 (Необязательно)
    
    https://ru.yougile.com/api-v2#/operations/SprintStickerStateController_create
    '''
    _method:str = 'post'
    _url:str = '/api-v2/sprint-stickers/{stickerId}/states'
    token:str
    _url_parse:tuple = ('stickerId',)
    stickerId:str
    name:str
    begin:int|None = None
    end:int|None = None