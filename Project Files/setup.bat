@echo off
setlocal

rem -- Set the PORT if not already set
if "%PORT%"=="" set PORT=8501

rem -- Create the directory if it doesn't exist
if not exist "%USERPROFILE%\.streamlit\" mkdir "%USERPROFILE%\.streamlit\"

rem -- Create or overwrite the Streamlit configuration file
(
echo [server]
echo port = %PORT%
echo enableCORS = false
echo headless = true
) > "%USERPROFILE%\.streamlit\config.toml"

echo Configuration complete.
pause
