# decompose_links

Принимает ссылки по API и логирует их в виде словаря.\
Допустимые методы запросов - GET, POST.\

В ответ на запросы вашего приложения сервис возвращает сообщения в формате JSON.\

Post-запросы направляются на адрес:
https://<URL системы>/api/v1/links/

Например:
http://127.0.0.1:8000/api/v1/links/


### Параметры запроса
В теле запроса в формате JSON должна передаваться ссылка в виде словаря ключ-значение.\
Ключ - 'links'.
В запросе необходимо использовать заголовок Content-Type: application/json.\

Например: 
{"link": "https://github.com/Kasaress/decompose_links.git"}


В случае успешного запроса сервис вернет ответ с кодом 200 и словарем в теле сообщения.\
Например:
"Ссылка в логе: {'scheme': 'https', 'netloc': 'github.com', 'path': '/Kasaress/decompose_links.git', 'is_git': True, 'git_name': 'decompose_links'}"

### Возможные ключи в словаре:
'scheme': протокол
'netloc': доменное имя
'path': путь
'params': параметры последнего элемента пути
'query': компоненты запроса
'fragment': идентификатор фрагмента
'is_git': признак того, что ссылка ведет на git
'git_name': название репозитория на git

### Настройка и запуск сервера: 
**Клонировать репозиторий**
```bash
  git clone https://github.com/Kasaress/decompose_links.git
```
**Создать и активировать виртуальную среду:**
```bash
  python -m venv venv
```
``` bash
  source venv/bin/activate 
```

**Установить зависимости из файла requirements.txt:**
```bash
pip install -r requirements.txt
```

**Перейдите в основную папку:**
```bash
cd decompose_links
```

**Запустите проект:**
```bash
python manage.py runserver
```

### Зависимости
requests==2.26.0
django==2.2.16
djangorestframework==3.12.4
python-dotenv==0.20.0

### Технологии:
_Python 3.7
Django 2.2.16
Djangorestframework 3.12.4
Redoc_



