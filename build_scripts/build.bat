@echo off
chcp 936 >nul
cd /d "%~dp0"

echo ========================================
echo   Code Stats - Build Script
echo ========================================
echo.

cd ..

echo Cleaning old files...
del "CodeStats.exe" /q 2>nul

echo Creating launch script...
echo @echo off > CodeStats.bat
echo chcp 936 ^>nul >> CodeStats.bat
echo cd /d "%%~dp0" >> CodeStats.bat
echo python codestats_no_pathlib.py %%* >> CodeStats.bat

echo.
echo ========================================
echo   SETUP COMPLETE!
echo ========================================
echo.
echo Generated files:
echo    CodeStats.bat - Launch script
echo.
echo Usage:
echo    Double-click CodeStats.bat to run
echo.
pause