from pydantic import BaseModel


class TaskController_search(BaseModel):
    """
    Получить список

    Args:
        token (str): Токен (Обязательно)

        assignedTo (str, optional): ID исполнителей через запятую (Необязательно)
        columnId (str, optional): ID колонки (Необязательно)
        includeDeleted (bool, optional): По умолчанию, если объект был отмечен как удаленный, то он не будет найден. Поставьте true, чтобы удаленные объекты возвращались (Необязательно)
        limit (int, optional): Количество элементов, которые хочется получить. Максимум 1000 (По умолчанию = 50)
        offset (int, optional): Индекс первого элемента страницы (По умолчанию = 0)
        title (str, optional): Заголовок задачи (Необязательно)

    https://ru.yougile.com/api-v2#/operations/TaskController_search
    """

    _method: str = "get"
    _url: str = "/api-v2/tasks"
    token: str
    _url_params: tuple = (
        "assignedTo",
        "columnId",
        "includeDeleted",
        "limit",
        "offset",
        "title",
    )

    assignedTo: str | None = None
    columnId: str | None = None
    includeDeleted: bool | None = None
    limit: int = 50
    offset: int = 0
    title: str | None = None


class TaskController_searchReversed(BaseModel):
    """
    Получить список задач в обратном порядке

    ## Устаревший! Используйте /task-list вместо этого

    Args:
        token (str): Токен (Обязательно)

        assignedTo (str): ID исполнителей через запятую (Необязательно)
        columnId (str): ID колонки (Необязательно)
        includeDeleted (bool): По умолчанию, если объект был отмечен как удаленный, то он не будет найден. Поставьте true, чтобы удаленные объекты возвращались (Необязательно)
        limit (int): Количество элементов, которые хочется получить. Максимум 1000 (По умолчанию = 50)
        offset (int): Индекс первого элемента страницы (По умолчанию = 0)
        title (str): Заголовок задачи (Необязательно)

    https://ru.yougile.com/api-v2#/operations/TaskController_search
    """

    _method: str = "get"
    _url: str = "/api-v2/tasks"
    token: str
    _url_params: tuple = (
        "assignedTo",
        "columnId",
        "includeDeleted",
        "limit",
        "offset",
        "title",
    )

    assignedTo: str | None = None
    columnId: str | None = None
    includeDeleted: bool | None = None
    limit: int = 50
    offset: int = 0
    title: str | None = None


class TaskController_create(BaseModel):
    """
    Создать

    Args:
        token (str): Токен (Обязательно)

        title (str): Название задачи (Обязательно)
        columnId (str, optional): ID колонки родителя (Необязательно)
        description (str, optional): Описание задачи (Необязательно)
        archived (bool, optional): Задача перенесена в архив - True|False (Необязательно)
        completed (bool, optional): Задача выполнена - True|False (Необязательно)
        subtasks (list, optional): Массив ID подзадач (Необязательно)
        assigned (list, optional): Массив ID пользователей, на которых назначена задача (Необязательно)
        deadline (dict, optional): Стикер "Дэдлайн". Указывает на крайний срок выполнения задачи. Имеется возможность кроме даты указать время, а так же дату начала задачи (Необязательно)
        timeTracking (dict, optional): Стикер "Таймтрекинг". Используется для указания ожидаемого и реального времени на выполнение задачи (Необязательно)
        checklists (list, optional): Чеклисты. К задаче всегда будет присвоен переданный объект. Если необходимо внести изменения, нужно сначала получить чеклисты, затем произвести корректировку, а затем записать в задачу заново (Необязательно)
        stickers (dict, optional): Пользовательские стикеры. Передаются в виде объекта ключ-значение. Где ключ - это ID стикера, значение - ID состояния. Для открепления стикера от задачи, используйте "-" как значение состояния (Необязательно)
        color (str, optional): Цвет карточки задач на доске, доступны цвета: task-primary, task-gray, task-red, task-pink, task-yellow, task-green, task-turquoise, task-blue, task-violet (Необязательно)
        idTaskCommon (str, optional): ID задачи, сквозной через всю компанию (Необязательно)
        idTaskProject (str, optional): ID задачи, внутри проекта (Необязательно)
        stopwatch (dict, optional): Стикер "Секундомер". Позволяет запустить секундомер, а так же ставить его на паузу и запускать заново (Необязательно)
        timer (dict, optional): Стикер "Таймер". Позволяет установить таймер на заданное время, а также возможность ставить его на паузу и запускать заново (Необязательно)

    https://ru.yougile.com/api-v2#/operations/TaskController_create
    """

    _method: str = "post"
    _url: str = "/api-v2/tasks"
    token: str

    title: str
    columnId: str | None = None
    description: str | None = None
    archived: bool | None = None
    completed: bool | None = None
    subtasks: list | None = None
    assigned: list | None = None
    deadline: dict | None = None
    timeTracking: dict | None = None
    checklists: list | None = None
    stickers: dict | None = None
    color: str | None = None
    idTaskCommon: str | None = None
    idTaskProject: str | None = None
    stopwatch: dict | None = None
    timer: dict | None = None


class TaskController_get(BaseModel):
    """
    Получить по ID

    Args:
        token (str): Токен (Обязательно)

        id (str): ID задачи (Обязательно)

    https://ru.yougile.com/api-v2#/operations/TaskController_get
    """

    _method: str = "get"
    _url: str = "/api-v2/tasks/{id}"
    token: str
    _url_parse: tuple = ("id",)

    id: str


class TaskController_update(BaseModel):
    """
    Изменить

    Args:
        token (str): Токен (Обязательно)

        id (str): ID задачи (Обязательно)
        deleted (bool, optional): Если true, значит объект удален (Необязательно)
        title (str, optional): Название задачи (Необязательно)
        columnId (str, optional): ID колонки родителя (Необязательно)
        description (str, optional): Описание задачи (Необязательно)
        archived (bool, optional): Задача перенесена в архив - True|False (Необязательно)
        completed (bool, optional): Задача выполнена - True|False (Необязательно)
        subtasks (list, optional): Массив ID подзадач (Необязательно)
        assigned (list, optional): Массив ID пользователей, на которых назначена задача (Необязательно)
        deadline (dict, optional): Стикер "Дэдлайн". Указывает на крайний срок выполнения задачи. Имеется возможность кроме даты указать время, а так же дату начала задачи (Необязательно)
        timeTracking (dict, optional): Стикер "Таймтрекинг". Используется для указания ожидаемого и реального времени на выполнение задачи (Необязательно)
        checklists (list, optional): Чеклисты. К задаче всегда будет присвоен переданный объект. Если необходимо внести изменения, нужно сначала получить чеклисты, затем произвести корректировку, а затем записать в задачу заново (Необязательно)
        stickers (dict, optional): Пользовательские стикеры. Передаются в виде объекта ключ-значение. Где ключ - это ID стикера, значение - ID состояния. Для открепления стикера от задачи, используйте "-" как значение состояния (Необязательно)
        color (str, optional): Цвет карточки задач на доске, доступны цвета: task-primary, task-gray, task-red, task-pink, task-yellow, task-green, task-turquoise, task-blue, task-violet (Необязательно)
        idTaskCommon (str, optional): ID задачи, сквозной через всю компанию (Необязательно)
        idTaskProject (str, optional): ID задачи, внутри проекта (Необязательно)
        stopwatch (dict, optional): Стикер "Секундомер". Позволяет запустить секундомер, а так же ставить его на паузу и запускать заново (Необязательно)
        timer (dict, optional): Стикер "Таймер". Позволяет установить таймер на заданное время, а также возможность ставить его на паузу и запускать заново (Необязательно)

    https://ru.yougile.com/api-v2#/operations/TaskController_update
    """

    _method: str = "put"
    _url: str = "/api-v2/tasks/{id}"
    token: str
    _url_parse: tuple = ("id",)

    id: str
    deleted: bool | None = None
    title: str | None = None
    columnId: str | None = None
    description: str | None = None
    archived: bool | None = None
    completed: bool | None = None
    subtasks: list | None = None
    assigned: list | None = None
    deadline: dict | None = None
    timeTracking: dict | None = None
    checklists: list | None = None
    stickers: dict | None = None
    color: str | None = None
    idTaskCommon: str | None = None
    idTaskProject: str | None = None
    stopwatch: dict | None = None
    timer: dict | None = None


class TaskController_getChatSubscribers(BaseModel):
    """
    Получить список участников чата задачи

    Args:
        token (str): Токен (Обязательно)

        id (str): ID задачи (Обязательно)

    https://ru.yougile.com/api-v2#/operations/TaskController_getChatSubscribers
    """

    _method: str = "get"
    _url: str = "/api-v2/tasks/{id}/chat-subscribers"
    token: str
    _url_parse: tuple = ("id",)

    id: str


class TaskController_updateChatSubscribers(BaseModel):
    """
    Изменить список участников чата задачи

    Args:
        token (str): Токен (Обязательно)

        id (str): ID задачи (Обязательно)

        content (list): Подписчики чата задачи (Обязательно)

    https://ru.yougile.com/api-v2#/operations/TaskController_updateChatSubscribers
    """

    _method: str = "put"
    _url: str = "/api-v2/tasks/{id}/chat-subscribers"
    token: str
    _url_parse: tuple = ("id",)

    id: str
    content: list

