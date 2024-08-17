@echo off
setlocal

:prompt
:: Prompt the user for the file path
set /p filePath="Enter the full path to the file: "

:: Check if the file exists
if not exist "%filePath%" (
    echo File not found: %filePath%
	echo Please enter a valid file path.
	goto :prompt
)

:: Calculate and display the MD5 checksum
echo Calculating MD5 checksum for %filePath%...
certutil -hashfile "%filePath%" MD5

:: Pause to allow user to see the output
pause