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
