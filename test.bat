@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if not errorlevel 1 (
    py -3 run.py test %*
) else (
    where python >nul 2>nul
    if errorlevel 1 (
        echo Python 3.10 or newer is required. Install it from https://www.python.org/downloads/
        pause
        exit /b 1
    )
    python run.py test %*
)
set "result=%errorlevel%"
echo.
if not "%result%"=="0" echo Tests or setup failed. See the message above, then run test.bat again.
pause
exit /b %result%
