
pip install -r requirements.txt
set APP_SETTINGS=config.DevelopmentConfig
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
