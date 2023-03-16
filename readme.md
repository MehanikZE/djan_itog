Менеджер задач

Для работы программы необходимо иметь установленную СУБД Postgresql 
По умолчанию настроено на следующие данные: DB_USER = "postgres" DB_NAME = "djn_itog" DB_PASSWORD = "Vrt342zf" DB_HOST = "127.0.0.1" 
При использовании других учетных данных к БД, необходимо скорректировать в разделе "settings.py" 
Также необходимо наличие модулей из requirements.txt Программа запускается с помощью команды py  manage.py runserver  режиме сервера разработчика. 
После запуска необходимо перейти на http://127.0.0.1:8000/ где доступен список  маршрутов, 
основные 
admin/
data/
data_crt/
data_upd/<int:pk>
delete/<int:pk>

admin/ - админ панель
api/drf-auth/ - страница авторизации DRF
data/ - список задач в системе
data_crt/ - добавление задачи
data_upd/<int:pk> - изменение задачи
data_del/<int:pk> - удаление задачи
project_crt/ - создание проекта
project_data/ - список проектов в системе
project_upd/<int:pk> - обновление проекта
project_del/<int:pk> - удаление проекта
accounts/ - вход в аккуунт
api/
    
Например http://127.0.0.1:8000/admin/ вход в админ панель ресурса откуда можно управлять данными, для доступа необходимо создать пользователя командой   py  manage.py createsuperuser
Так же управление доступно с вышеперечисленных алиасов, стоит отметить что ссылки типа data_upd/int:pk, data_del/int:pk предполагают указание номера задачи int:pk для выполнения изменения или удаления конкретной задачи с определенным id.
Управление задачами доступно только авторизованным пользователям. Авторизация осуществляется через логин пароль.

Тесты
Использованы тесты для отладки pytest.

Логирование
Производится запись логов действий в ситсеме уровня отладки (DEBUG) в файл logg.log

Управление через API
- реализовано API с помощью djangorestframework - дает управление посредством API
  - GET /api/tasks - получть список всех задач
  - GET /api/tasks/{id} - получть одну конкретную задачу
  - POST /api/tasks - создать задачу
  - PUT (или PATCH) /api/tasks/{id} - отредактировать существующую задачу
  - DELETE /api/tasks/{id} - удалить одну задачу
- реализовано с пощью страничной пагинации  page отображение в 7 задач на странице
- реализовано использование фильтрации по задачам ?zadachi=... , ?ordering=..., активгости задачи active_switch=True/False
Пример url DRF http://127.0.0.1:8000/api/tasks/5, где последнее число номер задачи и применимы вышеописанные методы, корректность ввода эндпоитов смотреть выше
Фильтрация http://127.0.0.1:8000/api/tasks?.... , где после ? указывается способ фильтрации из описанных выше
Аналлогичным образом происходит работа с группой projects.
Ведется история записи изменений задач
Исходный код отформатирован посредством инструмента Black.


