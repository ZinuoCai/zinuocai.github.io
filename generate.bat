@echo off
REM Generate HTML from jemdoc sources in src\
REM Usage: generate.bat
REM Prerequisite: conda activate jemdoc
cd /d %~dp0

echo ==^> Generating HTML from src\*.jemdoc ...
for %%f in (src\*.jemdoc) do (
    echo   Processing %%~nxf ...
    python jemdoc "%%f"
    if errorlevel 1 goto :error
)

echo ==^> Moving HTML to root ...
move /Y src\*.html . >nul

echo ==^> Done. Generated pages:
dir /b *.html
goto :eof

:error
echo Generation failed.
exit /b 1
