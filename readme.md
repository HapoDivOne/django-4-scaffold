## Django 5 Scaffold

Quickly set up the skeleton for your Django 5.x app. 
With Django-Scaffold you can quickly create CRUD generic class-based views for your models so you will have a basic CRUD API with Django Rest Framework.

## Specs

- Django 5.0
- Python 3.11

## Features

- Pre-install: django, mysqlclient, PyMySQL, djangorestframework
- Model, migrate hotels API example

## How to install

1. Create a new virtual environment using Python `venv` by running the following command:
   ```
   python3.11 -m venv env
   ```
   This will create a new directory called `env` that contains the virtual environment.
2. Activate the virtual environment by running the following command:
   ```
   source env/bin/activate
   ```
4. Install libs:
   ```
   pip install --upgrade pip
   pip install -r requirements.txt
   ```  
6. Create `.env`:  
   ```shell
   cp .env.example .env
   ```
   Set your database connection in `.env` file.
7. Run migration:
   ```
   python manage.py makemigrations hotels

   python manage.py makemigrations users

   python manage.py migrate
   ```
9. Serve local development server
   
   ```
   python manage.py runserver
   ```
   Now you can access local webserver at: http://127.0.0.1:8000
10. Test api using Django REST framework at http://127.0.0.1:8000/api/hotels/
11. Open swagger page api at http://127.0.0.1:8000/swagger

12. Run compile lang localte
   ```
   django-admim compilemessages
   ```

13. Run unittest
   ```
   python manage.py test users
   ```

14. Export Demo Api
   ```
   http://127.0.0.1:8000/api/user/export-csv
   http://127.0.0.1:8000/api/user/export-pdf
   http://127.0.0.1:8000/api/user/export-xslx
   ```
