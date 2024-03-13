from pydantic import BaseModel

class TaskController_search(BaseModel):
    '''
    Получить список
    
    token:str - Токен (Обязательно)
    columnId:str - ID колонки (Необязательно)
    includeDeleted:bool - По умолчанию, если объект был отмечен как удаленный, то он не будет найден. Поставьте true, чтобы удаленные объекты возвращались (Необязательно)
    limit:int - Количество элементов, которые хочется получить. Максимум 1000 (По умолчанию = 50)
    offset:int - Индекс первого элемента страницы (По умолчанию = 0)
    title:str - Заголовок задачи (Необязательно)
    
    https://ru.yougile.com/api-v2#/operations/TaskController_search
    '''
    _method:str = 'get'
    _url:str = '/api-v2/tasks'
    token:str
    _url_params:tuple = ('columnId','includeDeleted','limit','offset','title')
    columnId:str|None = None
    includeDeleted:bool|None = None
    limit:int=50
    offset:int=0
    title:str|None = None
    
class TaskController_create(BaseModel):
    '''
    Создать
    
    token:str - Токен (Обязательно)
    title:str - Название задачи (Обязательно)
    columnId:str - ID колонки родителя (Необязательно)
    description:str - Описание задачи (Необязательно)
    archived:bool - Задача перенесена в архив - True|False (Необязательно)
    completed:bool - Задача выполнена - True|False (Необязательно)
    subtasks:list - Массив ID подзадач (Необязательно)
    assigned:list - Массив ID пользователей, на которых назначена задача (Необязательно)
    deadline:dict - Стикер "Дэдлайн". Указывает на крайний срок выполнения задачи. Имеется возможность кроме даты указать время, а так же дату начала задачи (Необязательно)
    timeTracking:dict - Стикер "Таймтрекинг". Используется для указания ожидаемого и реального времени на выполнение задачи (Необязательно)
    checklists:list - Чеклисты. К задаче всегда будет присвоен переданный объект. Если необходимо внести изменения, нужно сначала получить чеклисты, затем произвести корректировку, а затем записать в задачу заново (Необязательно)
    stickers:dict - Пользовательские стикеры. Передаются в виде объекта ключ-значение. Где ключ - это ID стикера, значение - ID состояния. Для открепления стикера от задачи, используйте "-" как значение состояния (Необязательно)
    stopwatch:dict - Стикер "Секундомер". Позволяет запустить секундомер, а так же ставить его на паузу и запускать заново (Необязательно)
    timer:dict - Стикер "Таймер". Позволяет установить таймер на заданное время, а также возможность ставить его на паузу и запускать заново (Необязательно)
    
    https://ru.yougile.com/api-v2#/operations/TaskController_create
    '''
    _method:str = 'post'
    _url:str = '/api-v2/tasks'
    token:str
    title:str
    columnId:str|None = None
    description:str|None = None
    archived:bool|None = None
    completed:bool|None = None
    subtasks:list|None = None
    assigned:list|None = None
    deadline:dict|None = None
    timeTracking:dict|None = None
    checklists:list|None = None
    stickers:dict|None = None
    stopwatch:dict|None = None
    timer:dict|None = None

class TaskController_get(BaseModel):
    '''
    Получить по ID
    
    token:str - Токен (Обязательно)
    id:str - ID задачи (Обязательно)
    
    https://ru.yougile.com/api-v2#/operations/BoardController_get
    '''
    _method:str = 'get'
    _url:str = '/api-v2/tasks/{id}'
    _url_parse:tuple = ('id',)
    id:str
    
class TaskController_update(BaseModel):
    '''
    Изменить
    
    token:str - Токен (Обязательно)
    id:str - ID задачи (Обязательно)
    deleted:bool - Если true, значит объект удален (Необязательно)
    title:str - Название задачи (Необязательно)
    columnId:str - ID колонки родителя (Необязательно)
    description:str - Описание задачи (Необязательно)
    archived:bool - Задача перенесена в архив - True|False (Необязательно)
    completed:bool - Задача выполнена - True|False (Необязательно)
    subtasks:list - Массив ID подзадач (Необязательно)
    assigned:list - Массив ID пользователей, на которых назначена задача (Необязательно)
    deadline:dict - Стикер "Дэдлайн". Указывает на крайний срок выполнения задачи. Имеется возможность кроме даты указать время, а так же дату начала задачи (Необязательно)
    timeTracking:dict - Стикер "Таймтрекинг". Используется для указания ожидаемого и реального времени на выполнение задачи (Необязательно)
    checklists:list - Чеклисты. К задаче всегда будет присвоен переданный объект. Если необходимо внести изменения, нужно сначала получить чеклисты, затем произвести корректировку, а затем записать в задачу заново (Необязательно)
    stickers:dict - Пользовательские стикеры. Передаются в виде объекта ключ-значение. Где ключ - это ID стикера, значение - ID состояния. Для открепления стикера от задачи, используйте "-" как значение состояния (Необязательно)
    stopwatch:dict - Стикер "Секундомер". Позволяет запустить секундомер, а так же ставить его на паузу и запускать заново (Необязательно)
    timer:dict - Стикер "Таймер". Позволяет установить таймер на заданное время, а также возможность ставить его на паузу и запускать заново (Необязательно)
    
    https://ru.yougile.com/api-v2#/operations/BoardController_update
    '''
    _method:str = 'put'
    _url:str = '/api-v2/tasks/{id}'
    _url_parse:tuple = ('id',)
    id:str
    deleted:bool|None = None
    title:str|None = None
    columnId:str|None = None
    description:str|None = None
    archived:bool|None = None
    completed:bool|None = None
    subtasks:list|None = None
    assigned:list|None = None
    deadline:dict|None = None
    timeTracking:dict|None = None
    checklists:list|None = None
    stickers:dict|None = None
    stopwatch:dict|None = None
    timer:dict|None = None