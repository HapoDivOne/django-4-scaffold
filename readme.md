## Django 4 scaffold

1. Create a new virtual environment using Python venv by running the following command:
   ```
   python3.11 -m venv env
   ```
   This will create a new directory called `env` that contains the virtual environment.
2. Activate the virtual environment by running the following command:
   ```
   source env/bin/activate
   ```
3. Install libs:
   ```
   pip install --upgrade pip
   pip install -r requirement.txt
   ```
4. Create `.env`:
   
   ```shell
   cp .env.example .env
   ```
   Set your database connection in .env file.

5. Run migration:
   ```
   python manage.py migrate
   ```

6. Serve local development server
   
   ```
   python manage.py runserver
   ```
   Now you can access local webserver at: http://127.0.0.1:8000

7. Test api using Django REST framework

   http://127.0.0.1:8000/api/hotels/