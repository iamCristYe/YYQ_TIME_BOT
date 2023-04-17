import os
import flask
import telebot
from datetime import datetime
from pytz import timezone
if 1:
    LA = timezone("America/Los_Angeles")
    Copenhagen = timezone("Europe/Copenhagen")
    SH = timezone("Asia/Shanghai")
    Tokyo = timezone("Asia/Tokyo")
    fmt = "%H:%M"

    msg = f"""🇺🇸 {datetime.now(LA).strftime(fmt)}
🇩🇰 {datetime.now(Copenhagen).strftime(fmt)}
🇭🇰 {datetime.now(SH).strftime(fmt)}
🇯🇵 {datetime.now(Tokyo).strftime(fmt)}"""
    print(msg)