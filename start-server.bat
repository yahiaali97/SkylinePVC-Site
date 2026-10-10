@echo off
cd /d "%~dp0"
echo Skyline site: http://localhost:8080
start "" http://localhost:8080
where python >nul 2>nul && (python -m http.server 8080 & goto :eof)
where py >nul 2>nul && (py -m http.server 8080 & goto :eof)
where npx >nul 2>nul && (npx --yes http-server -p 8080 -c-1 & goto :eof)
echo Python or Node.js is required. Install one, then run this file again.
pause
