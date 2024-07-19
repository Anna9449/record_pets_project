# record_pets_project
### Описание:
Record pets API - проект для ведения учета питомцев (собак и кошек) в котором реализованы:
- Получение списка записей о питомцах
- Внесения данных о питомце
- Добавление фото питомца
- Удаление записей о питомцах списком

### Технологии:

[![name badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![name badge](https://img.shields.io/badge/Django-3776AB?logo=django&logoColor=white)](https://docs.djangoproject.com/en/4.2/releases/3.2/)
[![name badge](https://img.shields.io/badge/Django_REST_framework-3776AB?logo=djangorestramework&logoColor=white)](https://www.django-rest-framework.org/)

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/Anna9449/record_pets_project.git
```
```
cd record_pets_project
```
```
Создать файл .env и заполните его своими данными, пример:

```
POSTGRES_DB=pet # Имя_БД
POSTGRES_USER=pet_user # Имя пользователя БД
POSTGRES_PASSWORD=pet_password # Пароль к БД
DB_HOST=db # Адрес, по которому Django будет соединяться с БД
DB_PORT=5432 # Порт соединения к БД
SECRET_KEY=*** # Секретный ключ Django (без кавычек).
ALLOWED_HOSTS=*** # Список разрешённых хостов (через запятую и без пробелов)
DEBUG=False # Выбрать режим отладки
API_KEY=your_api_key # Ключ аутентификации
```
Установить Docker Compose:

```
sudo apt update
sudo apt install curl
curl -fSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh
sudo apt install docker-compose-plugin 
```

Запустить docker-compose.yml:

```
sudo docker compose -f docker-compose.yml up
```

Создать и выполнить миграции, создать суперпользователя, собрать статические файлы бэкенда и скопировать их:

```
sudo docker compose -f docker-compose.yml exec backend python manage.py makemigrations
sudo docker compose -f docker-compose.yml exec backend python manage.py migrate
sudo docker compose -f docker-compose.yml exec backend python manage.py createsuperuser
sudo docker compose -f docker-compose.yml exec backend python manage.py collectstatic
sudo docker compose -f docker-compose.yml exec backend cp -r /app/static/. /static/static/ 
```
