# Cooky Backend

## Setup

This project is using python version `3.11.4`.

start a virtual environment and activate it

```
python -m venv .venv
.venv/Scripts/activate
```

install the required packages

```
pip install -r requirements.txt
```

create a `.env` file to configure the database credentials

```
# .env file

ENGINE=<your database engine>
HOST=<your host name>
NAME=<your database name>
USER=<your user name>
PASSWORD=<your password>
PORT=<your port number>
```

start the server

```
> python manage.py runserver
```
