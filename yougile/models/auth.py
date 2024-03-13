from pydantic import BaseModel
class AuthKeyController_companiesList(BaseModel):
    '''
    Получить список компаний
    
    login:str - Логин пользователя (Обязательно)
    password:str - Пароль пользователя (Обязательно)
    name:str - Название компании (Необязательно)
    
    limit:int - Количество элементов, которые хочется получить. Максимум 1000 (По умолчанию = 50)
    offset:int - Индекс первого элемента страницы (По умолчанию = 0)
    
    https://ru.yougile.com/api-v2#/operations/AuthKeyController_companiesList
    '''
    _method:str = 'post'
    _url:str = '/api-v2/auth/companies'
    _url_params:tuple = ('limit','offset')
    login:str
    password:str
    name:str|None = None
    
    limit:int=50
    offset:int=0
    
    
class AuthKeyController_search(BaseModel):
    '''
    Получить список ключей
    
    login:str - Логин пользователя (Необязательно)
    password:str - Пароль пользователя (Необязательно)
    companyId:str - ID компании (Необязательно)
    
    https://ru.yougile.com/api-v2#/operations/AuthKeyController_search
    '''
    _method:str = 'post'
    _url:str = '/api-v2/auth/keys/get'
    login:str
    password:str
    companyId:str
    
class AuthKeyController_create(BaseModel):
    '''
    Создать ключ
    
    login:str - Логин пользователя (Обязательно)
    password:str - Пароль пользователя (Обязательно)
    companyId:str - ID компании (Обязательно)
    
    https://ru.yougile.com/api-v2#/operations/AuthKeyController_create
    '''
    _method:str = 'post'
    _url:str = '/api-v2/auth/keys'
    login:str
    password:str
    companyId:str
    
class AuthKeyController_delete(BaseModel):
    '''
    Удалить ключ
    
    key:str - Ключ (Обязательно)
    
    https://ru.yougile.com/api-v2#/operations/AuthKeyController_delete
    '''
    _method:str = 'delete'
    _url:str = '/api-v2/auth/keys/{key}'
    _url_parse:tuple = ('key',)
    key:str