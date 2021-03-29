# Invoice CSV Uploading 


## Tech

- Angular 11 
- Python Flask
- Postgres SQL


## Installation Frontend

Install the dependencies and start the frontend.

```sh
cd fronend
npm i
ng serve
```
Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## Installation backend
Install the dependencies and devDependencies and start the backend.

```sh
cd backend/src
pip install -r requirements.txt
```
### Migration Postgres
change your postgres SQLALCHEMY_DATABASE_URI from backend/src/config.py

```sh
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```
Navigate to `http://localhost:5000/` to check backend is running.
Set your SERVER_URL in frontend/environments/environment.ts

### Run backend

```sh
set APP_SETTINGS=config.DevelopmentConfig
python manage.py runserver
```
