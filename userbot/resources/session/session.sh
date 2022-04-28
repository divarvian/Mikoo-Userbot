#!/usr/bin/env bash
# Ultroid - UserBot
# Copyright (C) 2022 Mikoo-Userbot
#
# This file is a part of < https://github.com/divarvian/Mikoo-Userbot/ >
# PLease read the GNU Affero General Public License in <https://www.github.com/divarvian/Mikoo-Userbot/blob/main/LICENSE/>

clear
sec=3
spinner=(⣻ ⢿ ⡿ ⣟ ⣯ ⣷)
while [ $sec -gt 0 ]; do
    echo -ne "\e[33m ${spinner[sec]} Starting dependency installation in $sec seconds...\r"
    sleep 1
    sec=$(($sec - 1))
done
echo -e "\e[1;32mInstalling Dependencies ---------------------------\e[0m\n"
apt-get update
apt-get upgrade -y
pkg upgrade -y
pkg install python wget -y
wget https://raw.githubusercontent.com/divarvian/Mikoo-Userbot/Mikoo-Userbot/userbot/resources/session/string_session.py
pip install telethon
clear
python3 string_session.py
