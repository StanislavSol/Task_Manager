PORT ?= 8000
WEB_CONCURRENCY ?= 4

install:
	poetry install

start:
	poetry run gunicorn -w $(WEB_CONCURRENCY) -b 0.0.0.0:$(PORT) task_manager.wsgi:application

dev:
	poetry run python manage.py runserver

compile:
	cd task_manager && poetry run django-admin makemessages -l ru && poetry run django-admin compilemessages --ignore=venv

shell:
	poetry run python manage.py shell

migrate:
	poetry run python manage.py makemigrations && poetry run python manage.py migrate

collectstatic:
	poetry run python manage.py collectstatic
	
start:
	gunicorn task_manager.wsgi:application

test:
	poetry run ./manage.py test


lint:
	poetry run flake8
