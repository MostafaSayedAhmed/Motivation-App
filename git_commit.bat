:: @echo off: Turns off command echoing so that the commands themselves don't show up in the console while the script is running.
@echo off

:: The following line is a comment, explaining what this script does. It doesn't get executed.
:: This script automates the process of committing and pushing changes to a Git repository without using a desktop application.

set var=main
:: Change to certain branch
git checkout %var%

:: The command below adds all modified or new files to the staging area in Git, preparing them for a commit.
git add .

:: This section checks if the user has provided a commit message as an argument. 
:: If no message is provided, it shows an error message and stops the script.
IF "%~1"=="" (
    echo Please provide a commit message as the first argument.
    exit /b
)

:: If a commit message is provided, this line creates a commit with that message.
git commit -m "%~1"

:: This line pushes the committed changes to the 'main' branch of the remote repository named 'origin'.
git push origin %var%

:: Once the process is completed, this line displays a success message.
echo Commit and push completed successfully!

:: 'pause' keeps the command prompt window open so you can see the success message.
pause

exit