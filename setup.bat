@echo off
echo ========================================================
echo DarkDecode System Setup Script
echo ========================================================

echo.
echo [1/4] Checking Python installation...
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed or not in PATH. Please install Python 3.11+.
    pause
    exit /b
)

echo.
echo [2/4] Setting up Python Virtual Environment...
IF NOT EXIST "venv" (
    python -m venv venv
    echo Virtual environment created successfully.
) ELSE (
    echo Virtual environment already exists.
)

echo.
echo [3/4] Activating Virtual Environment and Installing Dependencies...
call venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt

echo.
echo [4/4] Applying Database Migrations...
python manage.py makemigrations
python manage.py migrate

echo.
echo ========================================================
echo Setup Complete!
echo ========================================================
echo To start the server, you can run the following commands:
echo.
echo 1. venv\Scripts\activate
echo 2. python manage.py runserver
echo.

set /p create_admin="Do you want to create an admin superuser account now? (y/n): "
if /i "%create_admin%"=="y" (
    python manage.py createsuperuser
)

echo.
echo Setup finished.
pause
