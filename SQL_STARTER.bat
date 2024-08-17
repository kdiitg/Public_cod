
@echo off
REM Check for admin rights
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Administrator rights required. Run this script as Administrator.
    powershell -Command "Start-Process cmd -ArgumentList '/c %~0 %*' -Verb RunAs"
    exit /b 1
)

:menu
cls
echo =====================
echo MySQL Service Manager
echo =====================
echo.
echo 1. Start MySQL
echo 2. Stop MySQL
echo 3. Restart MySQL
echo 4. Exit
echo.

set /p choice=Enter your choice (1-4): 

if "%choice%"=="1" goto start_mysql
if "%choice%"=="2" goto stop_mysql
if "%choice%"=="3" goto restart_mysql
if "%choice%"=="4" goto end

echo Invalid choice. Please enter a number from 1 to 4.
pause
goto menu

:start_mysql
net start MySQL80
if %errorlevel% neq 0 (
    echo Failed to start MySQL service.
) else (
    echo MySQL service started successfully.
)
pause
goto menu

:stop_mysql
net stop MySQL80
if %errorlevel% neq 0 (
    echo Failed to stop MySQL service.
) else (
    echo MySQL service stopped successfully.
)
pause
goto menu

:restart_mysql
net stop MySQL80
if %errorlevel% neq 0 (
    echo Failed to stop MySQL service.
) else (
    echo MySQL service stopped successfully.
)

net start MySQL80
if %errorlevel% neq 0 (
    echo Failed to start MySQL service.
) else (
    echo MySQL service restarted successfully.
)
pause
goto menu

:end
