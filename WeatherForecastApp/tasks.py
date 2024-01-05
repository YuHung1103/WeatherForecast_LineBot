import schedule
import time
from FlexMessage import todayMessage
from linebot import LineBotApi
from linebot.models import FlexSendMessage
from django.conf import settings

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def send_daily_weather_message():
    print("Executing send_daily_weather_message function")
    user_id = "Ufdefbb24d3a9605853ad90e47676216f"  # 替換為實際的使用者ID
    flex_message = todayMessage(user_id)
    line_bot_api.push_message(user_id, messages=FlexSendMessage(alt_text="Today's Weather", contents=flex_message))

# 設定每天早上七點執行一次
schedule.every().day.at("16:14").do(send_daily_weather_message)

while True:
    schedule.run_pending()
    time.sleep(1)