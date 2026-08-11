import os
import json
from datetime import datetime, timezone, timedelta
import requests

# جلب البيانات من البيئة (GitHub Secrets)
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
MESSAGE_ID = os.environ.get("MESSAGE_ID")

# ضبط المنطقة الزمنية (العراق UTC+3)
iraq_tz = timezone(timedelta(hours=3))
today = datetime.now(iraq_tz).date()

# تحديد تاريخ 1 أكتوبر للسنة الحالية أو القادمة
target_year = today.year
if today >= datetime(target_year, 9, 20).date():
    target_year += 1
target_date = datetime(target_year, 9, 20).date()

# حساب الأيام المتبقية
days_left = (target_date - today).days

# نص الرسالة ونص الزر
main_text = "الدوام"

if days_left == 1:
    button_text = "باجر دوام"
else:
    button_text = f" بعد: {days_left} يوم"

# إنشاء هيكل الزر مع ربطه بالرابط الخاص بك
keyboard = {
    "inline_keyboard": [
        [
            {
                "text": button_text, 
                "url": "https://t.me/QXX77/1188"
            }
        ]
    ]
}

# إرسال طلب التعديل إلى تيليجرام
url = f"https://api.telegram.org/bot{BOT_TOKEN}/editMessageText"
payload = {
    "chat_id": CHAT_ID,
    "message_id": MESSAGE_ID,
    "text": main_text,
    "reply_markup": json.dumps(keyboard)
}

response = requests.post(url, json=payload)
print(response.json())
