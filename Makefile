install:
	poetry install

start:
	poetry run python manage.py runserver

build:
	./build.sh