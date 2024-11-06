@echo off
setlocal enabledelayedexpansion

:: Set up the environment path
set CONDA_PATH=D:\miniforge3\envs

:: Function to check directory and activate environment
:check_directory
set "curr_dir=%cd%"
echo DEBUG: Checking directory %curr_dir%

echo %curr_dir% | findstr /i "D:\workspace" >nul
if %errorlevel% equ 0 (
    for %%I in ("%curr_dir%") do set "dirname=%%~nxI"
    if exist "%CONDA_PATH%\!dirname!" (
        if not "!dirname!"=="%CONDA_DEFAULT_ENV%" (
            call conda activate !dirname!
            echo Activated environment: !dirname!
        )
    ) else (
        if defined CONDA_DEFAULT_ENV (
            call conda deactivate
            echo Deactivated environment
        )
    )
) else (
    if defined CONDA_DEFAULT_ENV (
        call conda deactivate
        echo Not in workspace, deactivated environment
    )
)
goto :eof

:: Set up prompt hook to run our check
prompt $E[1;32m$P$E[0m$_$G$S
doskey cd=cd $* $T prompt
set PROMPT=$E[1;32m$P$E[0m$_$G$Scall %~f0$S

:: Initial check
call :check_directory

@REM "commandline": "%SystemRoot%\\System32\\cmd.exe ",