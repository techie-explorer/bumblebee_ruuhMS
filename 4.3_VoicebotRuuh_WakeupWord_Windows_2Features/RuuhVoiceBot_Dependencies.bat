@echo off
color 02
echo Welcome to Ruuh Voice Bot
ping -n 2 127.0.0.1>nul

echo Please make sure your computer is connected to the internet. If not, connect it and then launch this file. If connected already, please ignore !

ping -n 2 127.0.0.1>nul

echo Relax while we install the dependencies (Required only for the 1st time)

ping -n 2 127.0.0.1>nul
echo 5
ping -n 2 127.0.0.1>nul
echo 4
ping -n 2 127.0.0.1>nul
echo 3
ping -n 2 127.0.0.1>nul
echo 2
ping -n 2 127.0.0.1>nul
echo 1
ping -n 2 127.0.0.1>nul

cls
echo Let's begin !
pip install gtts;
pip install speechrecognition;
pip install fbchat;
pip install googletrans;
pip install google-cloud-translate;
pip install playsound
pip install google-cloud-speech;
cls
echo You are all set to experience the new face of Microsoft Ruuh !
PAUSE