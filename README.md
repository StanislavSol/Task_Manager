[![Actions Status](https://github.com/StanislavSol/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/StanislavSol/python-project-52/actions)
### Code Clamate
<a href="https://codeclimate.com/github/StanislavSol/python-project-52/maintainability"><img src="https://api.codeclimate.com/v1/badges/85f6c9497d22c08f54b9/maintainability" /></a>

[Task manager](https://python-project-52.onrender.com/) - is task management system. It allows you to set tasks, assign performers and change their statuses. To work with the system, registration and authentication are required.

***
## Before installation
To install and run the project, you will need Python version 3.10 and above, the Poetry dependency management tool.

## Install
1. Clone the project repository to your local device:
```
git clone git@github.com:StanislavSol/python-project-52.git

```
2. Go to the project directory and install dependencies using Poetry:
```
cd python-project-52 && make install

```
3. Create a .env file that will contain your sensitive settings:
```
SECRET_KEY=your_key
DEBUG=False
DATABASE_URL=your_value_External_Database_URL_or_use_local_connection

```
4. Run the commands:
```
make migrate

```

***
## Usege
1. To start the server in a production environment using Gunicorn, run the command:
```
make start

```
2. Run the server locally in development mode with the debugger active:
```
make dev 

```
