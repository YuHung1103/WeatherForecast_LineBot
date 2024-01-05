from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent

# 引入圖文訊息處理
from .FlexMessage import todayMessage, weekMessage

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            # 使用 handle_message 處理文字訊息事件
            handle_message(event)

        return HttpResponse()
    else:
        return HttpResponseBadRequest()

# 定義 Line Bot 的事件處理
def handle_message(event):
    if isinstance(event, MessageEvent):
        if event.message.text == "今日天氣":
            flex_message = todayMessage(event)
            line_bot_api.reply_message(event.reply_token, flex_message)
        elif event.message.text == "一周天氣":
            flex_message = weekMessage(event)
            line_bot_api.reply_message(event.reply_token, flex_message)


