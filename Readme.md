# tree_menu

## Условие
```text
Задача :
Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:
1) Меню реализовано через template tag
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django
5) Активный пункт меню определяется исходя из URL текущей страницы
6 )Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через 
named url.
8)На отрисовку каждого меню требуется ровно 1 запрос к БД
 Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной 
 странице меню по названию.
 {% draw_menu 'main_menu' %}
 При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.
При решении тестового задания у вас не должно возникнуть вопросов. Если появляются вопросы, вероятнее всего, у вас 
недостаточно знаний.
Задание выложить на гитхаб.
```
## Создание переменной окружения и установка зависимостей
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Запуск миграций, создание пользователя
```bash
python3 manage.py makemigrations                 
python3 manage.py migrate
python3 manage.py createsuperuser
```
## Запуск сервера
```bash
python3 manage.py runserver
```
## Работа с проектом
```bash
open http://127.0.0.1:8000
```
## Добавление новых элементов меню 
```text
Добавление новых элементов меню осущетвляется из админ панели
Поле name название пункта меню
Поле parent выкатывающее поле с пунктами меню для установления связи с выбранного пункта меню и поля name элемента
Поле explicit_url для правильной работоспособности принимает следующий формат /<число>/
```
