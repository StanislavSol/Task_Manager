install:
	poetry install

start:
	poetry run python manage.py runserver 0.0.0.0:8000

.PHONY: makemessages 
makemessages:
	poetry run django-admin makemessages -l ru

.PHONY: compilemessages
compilemessages:
	poetry run django-admin compilemessages

shell:
	poetry run python manage.py shell

makemigration:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

collectstatic:
	poetry run python manage.py collectstatic
