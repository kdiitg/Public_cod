@echo off
setlocal

:: Define the XML file path
set XML_FILE_PATH=/sdcard/ui_dump.xml

:: Function to run adb command
:run_adb_command
adb %* >nul 2>&1
exit /b %errorlevel%

:: List connected devices
echo Listing connected devices...
run_adb_command devices
if errorlevel 1 (
    echo Error listing devices.
    goto end
)

:: Check if any devices are connected
for /f "skip=1 tokens=1" %%i in ('adb devices') do (
    if not "%%i"=="" (
        set DEVICE_ID=%%i
        goto device_found
    )
)

:: No devices found, prompt for IP address
echo No devices found. Please enter the IP address of the device (e.g., 192.168.1.3:5555):
set /p IP_ADDRESS=

:: Connect to the device via IP
echo Connecting to %IP_ADDRESS%...
run_adb_command connect %IP_ADDRESS%
if errorlevel 1 (
    echo Error connecting to device.
    goto end
)

:: List devices again after connecting
run_adb_command devices
if errorlevel 1 (
    echo Error listing devices.
    goto end
)

for /f "skip=1 tokens=1" %%i in ('adb devices') do (
    if not "%%i"=="" (
        set DEVICE_ID=%%i
        goto device_found
    )
)

echo Failed to connect to any device.
goto end

:device_found
echo Using device: %DEVICE_ID%

:: Dump the UI hierarchy
echo Dumping UI hierarchy to %XML_FILE_PATH%...
run_adb_command -s %DEVICE_ID% shell uiautomator dump %XML_FILE_PATH%
if errorlevel 1 (
    echo Error dumping UI hierarchy.
    goto end
)

:: Ask for the save location
echo Enter the destination path to save the XML file (e.g., C:\path\to\file.xml):
set /p DEST_PATH=

:: Pull the XML file from the device
echo Pulling XML file to %DEST_PATH%...
run_adb_command -s %DEVICE_ID% pull %XML_FILE_PATH% "%DEST_PATH%"
if errorlevel 1 (
    echo Error pulling file.
    goto end
)

echo File pulled successfully.

:end
endlocal
pause

