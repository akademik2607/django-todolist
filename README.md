Project: DjangoTodolist
Description: Todo list
Stack: python3.9, Django, Postgres

pip install -r requirements.txt

#.env
SECRET_KEY = exemple-key
DB_NAME = exemple-dbname
DB_HOST = exemple-dbhost
DB_USER = exemple-dbuser
DB_PASSWORD = exemple-dbpassword
DB_PORT = exemple-dbport

python manage.py makemigrations
python migrate