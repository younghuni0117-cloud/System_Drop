@echo off
setlocal
if not exist "%~dp0system_drop_offline.zip.part001" goto missing
if not exist "%~dp0system_drop_offline.zip.part002" goto missing
if not exist "%~dp0system_drop_offline.zip.part003" goto missing
if not exist "%~dp0system_drop_offline.zip.part004" goto missing
if not exist "%~dp0system_drop_offline.zip.part005" goto missing
copy /b "%~dp0system_drop_offline.zip.part001"+"%~dp0system_drop_offline.zip.part002"+"%~dp0system_drop_offline.zip.part003"+"%~dp0system_drop_offline.zip.part004"+"%~dp0system_drop_offline.zip.part005" "%~dp0system_drop_v0.11.0_windows_offline.zip"
if errorlevel 1 goto failed
echo.
echo Done. Extract system_drop_v0.11.0_windows_offline.zip and run start_windows.bat.
pause
exit /b 0
:missing
echo A part is missing. Save all five parts and this BAT in the same folder.
pause
exit /b 1
:failed
echo Could not join files. Check available disk space and folder permissions.
pause
exit /b 1
