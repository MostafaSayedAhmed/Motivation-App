
@echo off
:: Script to automate pulling process without using desktop application

:: Adding folder to git
git add .

:: Check if a commit message was provided.
IF "%~1"=="" (
    echo Please provide a commit message as the first argument.
    exit /b
)

:: Commit changes and write custom message
git commit -m "%~1"

:: Push changes to repository
git push origin main

:: Confirm completion.
echo Commit and push completed successfully!

pause
