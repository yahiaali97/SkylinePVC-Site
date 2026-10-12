@echo off
cd /d "%~dp0"
echo Skyline site: http://localhost:8080
start "" http://localhost:8080
where python >nul 2>nul && (python tools\serve.py 8080 & goto :eof)
where py >nul 2>nul && (py tools\serve.py 8080 & goto :eof)
where npx >nul 2>nul && (npx --yes serve -l 8080 & goto :eof)
echo Python or Node.js is required. Install one, then run this file again.
pause
