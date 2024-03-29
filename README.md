# Cooky Backend


## Setup

This project is using python version `3.11.4`
```
> python --version
Python 3.11.4
```
First start the virtual environment
```
> python -m venv .venv
```
Then install required packages
```
> pip install -r requirements.txt
```
Create a `.env` file to configure the database credentials

```
# .env file

ENGINE=<your database engine>
HOST=<your host name>
NAME=<your database name>
USER=<your user name>
PASSWORD=<your password>
PORT=<your port number>
```

and finally, start the server

```
> python manage.py runserver
```




# TODO

### As an admin
<input type="checkbox" disabled checked  /> I want to be able to view the admin dashboard <br>
<input type="checkbox" disabled  /> I want to be able to view the list of all recipes <br>
<input type="checkbox" disabled  /> I want to be able to add a recipe <br>
<input type="checkbox" disabled  /> I want to be able edit any of the recipes <br>
<input type="checkbox" disabled  /> I want to be able delete any of the recipes <br>
<input type="checkbox" disabled  /> I want to be able to view and use the recipe dashboard like a basic user <br>

#### Optional:

<input type="checkbox" disabled  /> I want to be able to add, update, and delete both admin and basic users <br>