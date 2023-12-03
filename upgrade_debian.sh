#!/bin/sh
apt update
apt dist-upgrade -y
python3 update_info.py
apt update
apt dist-upgrade -y
apt autoremove -y