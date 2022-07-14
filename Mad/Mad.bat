@echo off
chcp 65001 >nul
:again
cls
title login
color d
echo.
echo ╔╦╗╔═╗╔╦╗  ╔╦╗╦ ╦╦ ╔╦╗╦  ╔╦╗╔═╗╔═╗╦  
echo ║║║╠═╣ ║║  ║║║║ ║║  ║ ║   ║ ║ ║║ ║║  
echo ╩ ╩╩ ╩═╩╝  ╩ ╩╚═╝╩═╝╩ ╩   ╩ ╚═╝╚═╝╩═╝
echo.
set /p user=Enter username:
if %user% == mad goto password
:password
set /p pass=Enter password:
if %pass% == mad goto main
echo Wrong login, Try Again
timeout 3 >NUL
goto again
:main
cls
color b
echo                                  ╔╦╗╔═╗╔╦╗  ╔╦╗╦ ╦╦ ╔╦╗╦  ╔╦╗╔═╗╔═╗╦  
echo                                  ║║║╠═╣ ║║  ║║║║ ║║  ║ ║   ║ ║ ║║ ║║  
echo                                  ╩ ╩╩ ╩═╩╝  ╩ ╩╚═╝╩═╝╩ ╩   ╩ ╚═╝╚═╝╩═╝
echo.
echo.
echo    discord tools          ip things          token login             generators           about
echo ╔════════════════════╦═════════════════╦════════════════════╦═══════════════════════╦════════════════╗
echo.║[1] Webhook Spammer ║[8] Ip Pinger    ║ [10] Token Login   ║[11] Nitro Generator   ║[13] Exit       ║
echo ║[2] Token Finder    ║[9] Ip Lookup    ║                    ║[12] Token Generator   ║                ║
echo ║[3] Vanity Tool     ║                 ║                    ║                       ║                ║
echo ║[4] Mass Reporter   ║                 ║                    ║                       ║                ║
echo ║[5] Self Bot        ║                 ║                    ║                       ║                ║
echo ║[6] Discord Nuker   ║                 ║                    ║                       ║                ║
echo ║[7] Server Cloner   ║                 ║                    ║                       ║                ║
echo ╚════════════════════╩═════════════════╩════════════════════╩═══════════════════════╩════════════════╝
:mainlogo
echo.
set /p main=Choose ur number:
if %main% == 1 zolo_spammer.py
if %main% == 3 zolo_fake_vanity_tool.py
if %main% == 2 zolo_token_finder.py
if %main% == 4 zolo_mass_report.py
if %main% == 5 selfbot.py
if %main% == 6 Zolo_Nuker.py
if %main% == 7 main.py
if %main% == 8 zolo_pinger.bat
if %main% == 9 ip_lookup.bat
if %main% == 10 token_login.py
if %main% == 11 nitro_gen.py
if %main% == 12 token_gen.py
if %main% == 13 
goto mainlogo
:pinger 
start pinger.bat
goto mainlogo
