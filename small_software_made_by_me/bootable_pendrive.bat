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
setlocal enabledelayedexpansion

REM List all disks and ask user to select the USB drive number
echo List of all disks:
(
echo list disk
) > list_disk_script.txt
diskpart /s list_disk_script.txt

REM Prompt user to enter the disk number of the USB drive
set /p disknum=Enter the disk number of your USB drive (0 or 1 or any other): 

REM Create a diskpart script to clean and format the USB drive
(
echo select disk %disknum%
echo clean
echo create partition primary
echo select partition 1
echo active
echo format fs=ntfs quick
echo assign
echo exit
) > diskpart_script.txt

REM Run the diskpart script
diskpart /s diskpart_script.txt

REM Get the assigned drive letter of the USB drive
for /f "tokens=2" %%i in ('diskpart /s get_drive_letter_script.txt') do set usbdrive=%%i

REM Prompt user to choose whether to copy OS files now or later
echo Do you want to copy OS files now or later?
echo 1. Copy now
echo 2. Copy later
set /p choice=Enter your choice (1 or 2): 

if %choice%==1 (
    REM Prompt user to enter the path to the mounted ISO file
    set /p isopath=Enter the path to the mounted ISO file (e.g., E:\): 

    REM Copy all files from the mounted ISO to the USB drive
    xcopy "%isopath%\*" "%usbdrive%\" /E /F /H

    echo Bootable USB drive created successfully!
) else (
    echo You can copy the OS files to the USB drive later.
    echo Bootable USB drive created successfully, but OS files are not copied yet.
)

pause
