from django.core.management.base import BaseCommand
from linebot import LineBotApi
from linebot.models import TextSendMessage

class Command(BaseCommand):
    help = 'Send reminder message'

    def handle(self, *args, **options):
        # 在這裡放置你想要執行的程式碼
        line_bot_api = LineBotApi('oICs/1ggwjQxfrRo/ri3gqe5eRz0tRlATiOmREJH5yoyA4xTPbTGZ12ssstwRSMmBg8+8LHePQ2j+KQMv6iQBppMvsRI8LWlbIPmMz4K5AVr1kfR90oXq3puISpHhw7f77H/IZzr6r3v8Hxy3golsgdB04t89/1O/w1cDnyilFU=')
        line_bot_api.push_message("Ufdefbb24d3a9605853ad90e47676216f", TextSendMessage(text='你的提醒訊息'))
        self.stdout.write(self.style.SUCCESS('Successfully sent reminder message'))
