@echo off

:: Activate the virtual environment
call env\Scripts\activate

:: Start Django development server in a new command prompt window
start cmd /k "python manage.py runserver"

:: Start Redis server in a new command prompt window
start cmd /k "wsl redis-server"

:: Start Celery worker in a new command prompt window
start cmd /k "celery -A Videoflix_Backend.celery worker --loglevel=info"
