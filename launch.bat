@echo off
:: Ensure we are working in the script's current folder
cd /d "%~dp0"

echo ---------------------------------------------------
echo  STARTING OHPYNE...
echo ---------------------------------------------------

:: 1. Open the browser to the local address
:: We do this first so it's ready when the server starts.
start "" "http://localhost:8000/ohpyne.html"

:: 2. Start the simple Python server
:: This command blocks the window, keeping the server alive.
echo  Local server running on Port 8000.
echo  Do NOT close this window while using the app.
echo.
python -m http.server 8000