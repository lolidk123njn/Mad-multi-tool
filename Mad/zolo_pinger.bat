@echo off
chcp 65001
mode 60,20
color 4

title multi tool pinger

:greeting
cls
echo ┌─┐┌─┐┬  ┌─┐  ┬┌─┐  ┌─┐┬┌┐┌┌─┐┌─┐┬─┐
echo ┌─┘│ ││  │ │  │├─┘  ├─┘│││││ ┬├┤ ├┬┘
echo └─┘└─┘┴─┘└─┘  ┴┴    ┴  ┴┘└┘└─┘└─┘┴└─                                       
set /p IP=Enter IP::
:top
PING -n 1 %IP% | FIND "TTL="
IF ERRORLEVEL 1 (SET in=0b & echo lmao thanks.) 
color %in%
ping -t 2 0 10 127.0.0.1 >nul
GoTo top