from pydantic import BaseModel

class ProjectController_search(BaseModel):
    '''
    Получить список
    
    token:str - Токен (Обязательно)
    includeDeleted:bool - По умолчанию, если объект был отмечен как удаленный, то он не будет найден. Поставьте true, чтобы удаленные объекты возвращались (Необязательно)
    limit:int - Количество элементов, которые хочется получить. Максимум 1000 (По умолчанию = 50)
    offset:int - Индекс первого элемента страницы (По умолчанию = 0)
    title:str - Имя проекта (Необязательно)
    
    https://ru.yougile.com/api-v2#/operations/ProjectController_search
    '''
    _method:str = 'get'
    _url:str = '/api-v2/projects'
    token:str
    _url_params:tuple = ('includeDeleted','limit','offset','title')
    includeDeleted:bool|None = None
    limit:int=50
    offset:int=0
    title:str|None = None
    
class ProjectController_create(BaseModel):
    '''
    Создать
    
    token:str - Токен (Обязательно)
    title:str - Название проекта (Обязательно)
    users:dict - Сотрудники на проекте и их роль. Возможные значения: 1) системные роли: worker, admin, observe 2) ID пользовательской роли 3) "-" для удаления существующего пользователя из проекта (Необязательно)
    
    https://ru.yougile.com/api-v2#/operations/ProjectController_create
    '''
    _method:str = 'post'
    _url:str = '/api-v2/projects'
    token:str
    title:str
    users:dict|None = None
    
class ProjectController_get(BaseModel):
    '''
    Получить по ID
    
    token:str - Токен (Обязательно)
    id:str - ID проекта (Обязательно)
    
    https://ru.yougile.com/api-v2#/operations/ProjectController_get
    '''
    _method:str = 'get'
    _url:str = '/api-v2/projects/{id}'
    token:str
    _url_parse:tuple = ('id',)
    id:str
    
class ProjectController_update(BaseModel):
    '''
    Изменить
    
    token:str - Токен (Обязательно)
    id:str - ID проекта (Обязательно)
    deleted:bool - Если true, значит объект удален (Необязательно)
    title:str - Название проекта (Обязательно)
    users:dict - Сотрудники на проекте и их роль. Возможные значения: 1) системные роли: worker, admin, observe 2) ID пользовательской роли 3) "-" для удаления существующего пользователя из проекта (Необязательно)
    
    https://ru.yougile.com/api-v2#/operations/ProjectController_update
    '''
    _method:str = 'put'
    _url:str = '/api-v2/projects/{id}'
    token:str
    _url_parse:tuple = ('id',)
    id:str
    deleted:bool|None = None
    title:str
    users:dict|None = None