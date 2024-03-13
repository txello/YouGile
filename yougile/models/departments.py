from pydantic import BaseModel

class DepartmentController_search(BaseModel):
    '''
    Получить список
    
    token:str - Токен (Обязательно)
    includeDeleted:bool - По умолчанию, если объект был отмечен как удаленный, то он не будет найден. Поставьте true, чтобы удаленные объекты возвращались (Небязательно)
    limit:int - Количество элементов, которые хочется получить. Максимум 1000 (По умолчанию = 50)
    offset:int - Индекс первого элемента страницы (По умолчанию = 0)
    parentId:str - ID родительского отдела (Небязательно)
    title:str - Имя отдела (Небязательно)
    
    https://ru.yougile.com/api-v2#/operations/DepartmentController_search
    '''
    _method:str = 'get'
    _url:str = '/api-v2/departments'
    token:str
    _url_params:tuple = ('includeDeleted','limit','name','offset','title')
    includeDeleted:bool|None = None
    limit:int=50
    offset:int=0
    parentId:str|None = None
    title:str|None = None
    
class DepartmentController_create(BaseModel):
    '''
    Создать
    
    token:str - Токен (Обязательно)
    title:str - Название отдела (Небязательно)
    parentId:str - Id родительского отдела. Оставить пустым или "-", если это отдел верхнего уровня (Небязательно)
    users:dict - Сотрудники на отделе и их роль. Возможные значения: 1) manager или member 2) "-" или "" для удаления существующего пользователя из отдела (Небязательно)
    
    https://ru.yougile.com/api-v2#/operations/DepartmentController_create
    '''
    _method:str = 'post'
    _url:str = '/api-v2/departments'
    token:str
    title:str|None = None
    parentId:str|None = None
    users:dict|None = None
    
class DepartmentController_get(BaseModel):
    '''
    Получить по ID
    
    token:str - Токен (Обязательно)
    id:str - ID отдела (Обязательно)
    
    https://ru.yougile.com/api-v2#/operations/DepartmentController_get
    '''
    _method:str = 'get'
    _url:str = '/api-v2/departments/{id}'
    token:str
    _url_parse:tuple = ('id',)
    id:str
    
class DepartmentController_update(BaseModel):
    '''
    Изменить
    
    token:str - Токен (Обязательно)
    id:str - ID отдела (Обязательно)
    deleted:bool - Если true, значит объект удален (Небязательно)
    title:str - Название отдела (Небязательно)
    parentId:str - Id родительского отдела. Оставить пустым или "-", если это отдел верхнего уровня (Небязательно)
    users:dict - Сотрудники на отделе и их роль. Возможные значения: 1) manager или member 2) "-" или "" для удаления существующего пользователя из отдела (Небязательно)
    
    https://ru.yougile.com/api-v2#/operations/DepartmentController_update
    '''
    _method:str = 'put'
    _url:str = '/api-v2/departments/{id}'
    token:str
    _url_parse:tuple = ('id',)
    id:str
    deleted:bool|None = None
    title:str|None = None
    parentId:str|None = None
    users:dict|None = None