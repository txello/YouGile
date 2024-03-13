from pydantic import BaseModel

class UserController_search(BaseModel):
    '''
    Получить список
    
    token:str - Токен (Обязательно)
    email:str - Почта сотрудника (Небязательно)
    limit:int - Количество элементов, которые хочется получить. Максимум 1000 (По умолчанию = 50)
    offset:int - Индекс первого элемента страницы  (По умолчанию = 0)
    projectId:str - ID проекта (Небязательно)
    
    https://ru.yougile.com/api-v2#/operations/UserController_search
    '''
    _method:str = 'get'
    _url:str = '/api-v2/auth/companies'
    token:str
    _url_params:tuple = ('email','limit','offset','projectId')
    email:str|None = None
    limit:int=50
    offset:int=0
    projectId:str|None = None
    
class UserController_create(BaseModel):
    '''
    Пригласить в компанию
    
    token:str - Токен (Обязательно)
    email:str - Почтовый ящик сотрудника (Обязательно)
    isAdmin:bool - Имеет ли пользователь права администратора (Небязательно)
    
    https://ru.yougile.com/api-v2#/operations/UserController_create
    '''
    _method:str = 'post'
    _url:str = '/api-v2/users'
    token:str
    email:str
    isAdmin:bool|None = None
    
class UserController_get(BaseModel):
    '''
    Получить по ID
    
    token:str - Токен (Обязательно)
    id:str - ID сотрудника (Обязательно)
    
    https://ru.yougile.com/api-v2#/operations/UserController_get
    '''
    _method:str = 'get'
    _url:str = '/api-v2/users/{id}'
    token:str
    _url_parse:tuple = ('id',)
    id:str

class UserController_update(BaseModel):
    '''
    Изменить
    
    token:str - Токен (Обязательно)
    id:str - ID сотрудника (Обязательно)
    isAdmin:bool - Имеет ли пользователь права администратора  (Небязательно)
    
    https://ru.yougile.com/api-v2#/operations/UserController_update
    '''
    _method:str = 'put'
    _url:str = '/api-v2/users/{id}'
    token:str
    _url_parse:tuple = ('id',)
    id:str
    isAdmin:bool|None = None
    
class UserController_delete(BaseModel):
    '''
    Удалить из компании
    
    token:str - Токен (Обязательно)
    id:str - ID сотрудника (Обязательно)
    
    https://ru.yougile.com/api-v2#/operations/UserController_delete
    '''
    _method:str = 'delete'
    _url:str = '/api-v2/users/{id}'
    token:str
    _url_parse:tuple = ('id',)
    id:str