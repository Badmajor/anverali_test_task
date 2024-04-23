#  Тестовое задание компании Anverali Group
Необходимо создать сайт с админ панелью и 2-мя кабинетами на Flask или Django. Сайт может быть не оформлен красиво. Структура на выбор. Можно взять за основу сайт kwork.ru. На сайте помимо админки должны быть два кабинета заказчика и исполнителя. Минимальный набор полей в профилях (имя, контактные данные, опыт). БД PostgreSQL

## Описание

### Модели

- CustomUser 

Модель CustomUser расширяет базовую модель пользователя Django AbstractUser и добавляет дополнительные поля для хранения контактной информации и опыта.
Поля:

    username: Имя пользователя (уникальное поле).
    email: Адрес электронной почты (уникальное поле).
    first_name: Имя пользователя.
    last_name: Фамилия пользователя.
    contact: Контактная информация пользователя.
    experience: Описание опыта пользователя.

- Order

Модель Order представляет собой заказ, который может быть создан пользователем (owner) и выполнен исполнителем (contractor).
Поля:

    title: Название заказа.
    owner: Пользователь, создавший заказ (ссылка на CustomUser).
    contractor: Пользователь, назначенный на выполнение заказа (ссылка на CustomUser).

### Маршруты

- /admin/ - Путь к админ-панели
- / - Главная 
- /accounts/login/ - Страница входа
- /accounts/logout/ - Страница для выхода
- /accounts/register/ - Страница регистрации
- /accounts/profile/ - Страница пользователя
- /accounts/profile/`<slug:role>` - Личный кабинет пользователя в зависимости от выбранной роли (seller, buyer)

## Запуск проекта

Для запуска проекта выполните следующие шаги:

```bash
# Создайте виртуальное окружение
python -m venv venv

# Активируйте виртуальное окружение
 # - linux
source /venv/bin/activate 
 # - windows
source /venv/Script/activate

# Установите зависимости
pip install -r requirements.txt

# Создайте файл с переменными окружения
echo "#DJANGO
SECRET_KEY_DJANGO=django-insecure
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,

#DATABASE
POSTGRES_DB=anverali
POSTGRES_USER=anverali
POSTGRES_PASSWORD=supersecretpass" > .env


# Запустить контейнер с БД PostgreSQL
sudo docker run --name postgress_for_anverali 
-e POSTGRES_PASSWORD=supersecretpass 
-e POSTGRES_USER=anverali 
-e POSTGRES_DB=anverali 
-p 5432:5432 
-d postgres

# Перейдите в папку с проектом
cd anveral_test_task/

# Выполните миграции
python manage.py migrate

# Запустите сервер
python manage.py runserver
```



Заказчик: https://hh.ru/employer/5037806

Вакансия: https://hh.ru/vacancy/97466453