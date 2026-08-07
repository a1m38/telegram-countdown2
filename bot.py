import os
from datetime import datetime, timezone, timedelta
import requests

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
MESSAGE_ID = os.environ.get("MESSAGE_ID")

iraq_tz = timezone(timedelta(hours=3))
today = datetime.now(iraq_tz).date()

target_year = today.year
if today >= datetime(target_year, 10, 1).date():
    target_year += 1
target_date = datetime(target_year, 10, 1).date()

days_left = (target_date - today).days

if days_left == 0:
    text = "🎉 اليوم هو 1 أكتوبر!"
else:
    text = f"⏳ متبقي على 1 أكتوبر: {days_left} يوم."

url = f"https://api.telegram.org/bot{BOT_TOKEN}/editMessageText"
payload = {
    "chat_id": CHAT_ID,
    "message_id": MESSAGE_ID,
    "text": text
}

response = requests.post(url, json=payload)
print(response.json())
