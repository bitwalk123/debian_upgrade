#!/bin/sh
apt update
apt dist-upgrade -y
python update_info.py
apt update
apt dist-upgrade -y
