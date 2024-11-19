@echo off

cd "C:\Users\Mostafa Sayed\AppData\Local\Programs\Python\Scripts"

pyinstaller --onefile --windowed --icon "G:\Works\Application\Motivation-App\Source Code\Images\Icon.ico" --distpath "G:\Works\Application\Motivation-App\Output\dist" --workpath "G:\Works\Application\Motivation-App\Output\build" --specpath "G:\Works\Application\Motivation-App\Output\spec" --add-data "G:\Works\Application\Motivation-App\Source Code\backend;backend" --add-data "G:\Works\Application\Motivation-App\Source Code\Images;Images" --add-data "G:\Works\Application\Motivation-App\Source Code\GUI;GUI" "G:\Works\Application\Motivation-App\Source Code\main.py"

cd "G:\Works\Application\Motivation-App\Output\dist"

xcopy "G:\Works\Application\Motivation-App\Source Code\Images" "G:\Works\Application\Motivation-App\Output\dist\Images" /E /I /H /Y 

xcopy "G:\Works\Application\Motivation-App\Source Code\backend" "G:\Works\Application\Motivation-App\Output\dist\backend" /E /I /H /Y 

xcopy "G:\Works\Application\Motivation-App\Source Code\GUI" "G:\Works\Application\Motivation-App\Output\dist\GUI" /E /I /H /Y 

echo Conversion Completed The exe file is at dist enjoy

pause