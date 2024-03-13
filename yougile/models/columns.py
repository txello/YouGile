from pydantic import BaseModel

class ColumnController_search(BaseModel):
    '''
    Получить список
    
    token:str - Токен (Обязательно)
    boardId:str - ID доски (Небязательно)
    includeDeleted:bool - По умолчанию, если объект был отмечен как удаленный, то он не будет найден. Поставьте true, чтобы удаленные объекты возвращались (Небязательно)
    limit:int - Количество элементов, которые хочется получить. Максимум 1000 (По умолчанию = 50)
    offset:int - Индекс первого элемента страницы (По умолчанию = 0)
    title:str - Имя колонки (Небязательно)
    
    https://ru.yougile.com/api-v2#/operations/ColumnController_search
    '''
    _method:str = 'get'
    _url:str = '/api-v2/columns'
    token:str
    _url_params:tuple = ('boardId','includeDeleted','limit','offset','title')
    boardId:str|None = None
    includeDeleted:bool|None = None
    limit:int=50
    offset:int=0
    title:str|None = None
    
class ColumnController_create(BaseModel):
    '''
    Создать
    
    token:str - Токен (Обязательно)
    title:str - Название колонки (Обязательно)
    color:int - Цвет колонки. Указывается в виде числа. Примеры цветов представлены ниже (Небязательно)
    boardId:str - Id доски, в которой находится колонка (Обязательно)
    
    https://ru.yougile.com/api-v2#/operations/ColumnController_create
    '''
    _method:str = 'post'
    _url:str = '/api-v2/columns'
    token:str
    title:str|None = None
    color:int|None = None
    boardId:str|None = None
    
class ColumnController_get(BaseModel):
    '''
    Получить по ID
    
    token:str - Токен (Обязательно)
    id:str - ID колонки (Обязательно)

    https://ru.yougile.com/api-v2#/operations/ColumnController_get
    '''
    _method:str = 'get'
    _url:str = '/api-v2/columns/{id}'
    token:str
    _url_parse:tuple = ('id',)
    id:str
    
class ColumnController_update(BaseModel):
    '''
    Изменить
    
    token:str - Токен (Обязательно)
    id:str - ID колонки (Обязательно)
    deleted:bool - Если true, значит объект удален (Небязательно)
    title:str - Название колонки (Небязательно)
    color:int - Цвет колонки. Указывается в виде числа. Примеры цветов представлены ниже (Небязательно)
    boardId:str - Id доски, в которой находится колонка (Небязательно)

    https://ru.yougile.com/api-v2#/operations/ColumnController_update
    '''
    _method:str = 'put'
    _url:str = '/api-v2/columns/{id}'
    token:str
    _url_parse:tuple = ('id',)
    id:str
    deleted:bool|None = None
    title:str|None = None
    color:int|None = None
    boardId:str|None = None