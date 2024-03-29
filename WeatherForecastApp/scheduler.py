from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.conf import settings
from linebot import LineBotApi
from linebot.models import FlexSendMessage
import pytz

from .pushMessage import pushTodayMessage

def send_reminder():
    line_bot_api = LineBotApi('oICs/1ggwjQxfrRo/ri3gqe5eRz0tRlATiOmREJH5yoyA4xTPbTGZ12ssstwRSMmBg8+8LHePQ2j+KQMv6iQBppMvsRI8LWlbIPmMz4K5AVr1kfR90oXq3puISpHhw7f77H/IZzr6r3v8Hxy3golsgdB04t89/1O/w1cDnyilFU=')
    line_bot_api.push_message('Ufdefbb24d3a9605853ad90e47676216f', FlexSendMessage(alt_text="今日天氣預報", contents=pushTodayMessage()))

# 取得台灣時區
taipei_tz = pytz.timezone('Asia/Taipei')
# 初始化 scheduler
scheduler = BlockingScheduler(timezone=taipei_tz)
# 非同步的後台調度器
scheduler = BackgroundScheduler()
scheduler.add_job(send_reminder, trigger=CronTrigger(hour=7, minute=0), id='send_reminder_job')
scheduler.start()