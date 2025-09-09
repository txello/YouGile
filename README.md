# Yougile API для Python

## Информация о библиотеке

Библиотека является разработкой стороннего разработчика для удобства обращения к Yougile API.

## Установка

Если вы устанавливаете вручную, перед использованием библиотеки, необходимо установить следующее:

```console
> pip install pydantic
> pip install requests
```

Если вы устанавливаете из PyPI, то эти библиотеки устанавливаются автоматически:

```console
> pip install yougile-api
```

## Wiki

У моделей есть правила:

1. Название моделей полностью копируют URL этой модели на официальном API.
2. У всех моделей есть описания параметров, краткого описания из официального API и ссылка на запрос.
3. Названия параметров модели и их типизация идентичны параметрам из официального API (За исключением параметра ```token```)

## Возможности

Вы можете использовать токен не только к отдельным моделям, но и к самой функции запроса:

```python
import yougile
import yougile.models as models

def yougile_get(model:yougile.BaseModel) -> yougile.Response:
    return yougile.query(model,token="TOKEN")
model = models.ChatMessageController_search(chatId="12324")
response = yougile_get(model)
for msg in response.json()['content']:
    print(msg['text'])
```

## Примеры

### 1. Получаем список доступных компаний

```python
import yougile # Импортируем библиотеку
import yougile.models as models # Импортируем модели

model = models.AuthKeyController_companiesList(login="USERNAME",password="PASSWORD") # Указываем модель запроса листа компаний через авторизацию
response = yougile.query(model) # Делаем запрос на сервер
print(response.text) # Получаем ответ
```

### 2. Создаем токен

```python
import yougile
import yougile.models as models

model = models.AuthKeyController_create(login="USERNAME",password="PASSWORD",companyId="12345")
response = yougile.query(model)
print(response.json()['key'])
```

### 3. Получаем историю сообщений

```python
import yougile
import yougile.models as models

model = models.ChatMessageController_search(token="TOKEN",chatId="12324")
response = yougile.query(model)
for msg in response.json()['content']:
    print(msg['text'])
```

## Версии

### v1.0.0

* Созданы первые модели
* Создано подключение к серверу API

### v1.0.1

* Исправлены модели
* Исправлены комментарии

### v1.1.0

* Добавлены новые модели: `CompanyController_get`, `CompanyController_update`, `FileController_uploadFile`,
`TaskController_getChatSubscribers`, `TaskController_updateChatSubscribers`
* Добавлена возможность загрузки файла через `FileController_uploadFile`
* Добавлено CI/CD
* Исправлены модели `TaskController_get` и `TaskController_update` (Спасибо [XTerris](https://github.com/XTerris))
* Исправлены модели в документации
* Улучшена документация: Заменена на Google Docstring
* Выполнен рефакторинг кода
