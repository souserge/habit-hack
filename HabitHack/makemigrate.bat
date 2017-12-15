@echo off
REM The script updates the database

where python -c "import django" >nul 2>nul
if  NOT %errorlevel%==1 (
	python manage.py makemigrations
	python manage.py migrate
) else (
    @echo Ooops, looks like either python or django is not installed.
)

REM -- END --




