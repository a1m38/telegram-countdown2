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

# تحديد تاريخ هدف (1 أكتوبر للسنة الحالية أو القادمة)
target_year = today.year
if today >= datetime(target_year, 10, 1).date():
    target_year += 1
target_date = datetime(target_year, 10, 1).date()

# حساب الأيام المتبقية
days_left = (target_date - today).days

# نص الرسالة الرئيسية
main_text = "الدوام"

# نص الزر (يحتوي على العد التنازلي)
if days_left == 0:
    button_text = "🎉 اليوم هو 1 أكتوبر!"
else:
    button_text = f"⏳ متبقي: {days_left} يوم"

# إنشاء هيكل الأزرار الشفافة (Inline Keyboard)
# نضع زر واحد فقط، ونربطه ببيانات وهمية (callback_data) لأنه للعرض فقط
keyboard = {
    "inline_keyboard": [
        [
            {"text": button_text, "callback_data": "countdown_display"}
        ]
    ]
}

# إعداد الطلب (تعديل الرسالة بدلاً من إرسال جديدة)
url = f"https://api.telegram.org/bot{BOT_TOKEN}/editMessageText"
payload = {
    "chat_id": CHAT_ID,
    "message_id": MESSAGE_ID,
    "text": main_text,
    "reply_markup": json.dumps(keyboard) # إضافة الأزرار هنا
}

# إرسال الطلب وطباعة النتيجة للتحقق
response = requests.post(url, json=payload)
print(response.json())
