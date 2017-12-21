@echo off
REM The script starts the server with default settings

where python -c "import django" >nul 2>nul
if  NOT %errorlevel%==1 (
    python manage.py runserver 7000
) else (
    @echo Ooops, looks like either python or django is not installed.
)

REM -- END --




