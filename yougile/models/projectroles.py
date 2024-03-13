from pydantic import BaseModel

class ProjectRolesController_search(BaseModel):
    '''
    Получить список
    
    token:str - Токен (Обязательно)
    projectId:str - ID проекта (Обязательно)
    limit:int - Количество элементов, которые хочется получить. Максимум 1000 (По умолчанию = 50)
    name:str - Имя роли (Необязательно)
    offset:int - Индекс первого элемента страницы  (По умолчанию = 0)
    
    https://ru.yougile.com/api-v2#/operations/ProjectRolesController_search
    '''
    _method:str = 'get'
    _url:str = '/api-v2/projects/{projectId}/roles'
    token:str
    _url_parse:tuple = ('projectId',)
    _url_params:tuple = ('limit','name','offset')
    projectId:str
    limit:int=50
    name:str|None = None
    offset:int=0
    
class ProjectRolesController_create(BaseModel):
    '''
    Создать
    
    token:str - Токен (Обязательно)
    projectId:str - ID проекта (Обязательно)
    name:str - Название роли (Обязательно)
    description:str - Описание роли (Необязательно)
    permissions:dict - Права в проекте (Обязательно)
    
    https://ru.yougile.com/api-v2#/operations/ProjectRolesController_create
    '''
    _method:str = 'post'
    _url:str = '/api-v2/projects/{projectId}/roles'
    token:str
    _url_parse:tuple = ('projectId',)
    projectId:str
    name:str
    description:str|None = None
    permissions:dict
    
class ProjectRolesController_get(BaseModel):
    '''
    Получить по ID

    token:str - Токен (Обязательно)
    id:str - ID роли проекта (Обязательно)
    projectId:str - ID проекта (Обязательно)
    
    https://ru.yougile.com/api-v2#/operations/ProjectRolesController_get
    '''
    _method:str = 'get'
    _url:str = '/api-v2/projects/{projectId}/roles/{id}'
    token:str
    _url_parse:tuple = ('projectId','id')
    id:str
    projectId:str
    
class ProjectRolesController_update(BaseModel):
    '''
    Изменить
    
    token:str - Токен (Обязательно)
    id:str - ID проекта (Обязательно)
    projectId:str - ID проекта (Обязательно)
    name:str - Название роли (Необязательно)
    description:str - Описание роли (Необязательно)
    permissions:dict - Права в проекте (Обязательно)
    
    https://ru.yougile.com/api-v2#/operations/ProjectRolesController_update
    '''
    _method:str = 'put'
    _url:str = '/api-v2/projects/{projectId}/roles/{id}'
    token:str
    _url_parse:tuple = ('projectId','id')
    id:str
    projectId:str
    name:str|None = None
    description:str|None = None
    permissions:dict

class ProjectRolesController_delete(BaseModel):
    '''
    Удалить
    
    token:str - Токен (Обязательно)
    id:str - ID роли проекта (Обязательно)
    projectId:str - ID проекта (Обязательно)
    
    https://ru.yougile.com/api-v2#/operations/ProjectRolesController_delete
    '''
    _method:str = 'delete'
    _url:str = '/api-v2/projects/{projectId}/roles/{id}'
    token:str
    _url_parse:tuple = ('projectId','id')
    id:str
    projectId:str