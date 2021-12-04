#!/bin/sh
cd /app
pip install -r requirements.txt
sleep 10
python /app/bot.py

apt-get update
apt-get install -y cron
cp /app/crontabbot /etc/cron.d/crontabbot
chmod 0644 /etc/cron.d/crontabbot
crontab /etc/cron.d/crontabbot
cron -f
