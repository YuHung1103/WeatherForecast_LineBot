# 引入爬蟲程式
from .WeatherCrawler import today

def pushTodayMessage():
    data = today()
    flex_message = {
        "type": "bubble",
        "size": "mega",
        "hero": {
            "type": "image",
            "url": data[0],
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover",
            "margin": "none"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "台北市今日氣溫 "+data[1]+"°C",
                "weight": "bold",
                "size": "xl"
            },
            {
                "type": "box",
                "layout": "vertical",
                "margin": "lg",
                "spacing": "sm",
                "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "降雨機率",
                        "color": "#aaaaaa",
                        "size": "md",
                        "wrap": True,
                        "flex": 2
                    },
                    {
                        "type": "text",
                        "text": data[2],
                        "wrap": True,
                        "color": "#666666",
                        "size": "md",
                        "flex": 4
                    }
                    ]
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                    {
                        "type": "text",
                        "text": "天氣狀況",
                        "flex": 2,
                        "color": "#aaaaaa",
                        "size": "md"
                    },
                    {
                        "type": "text",
                        "text": data[3],
                        "flex": 4,
                        "wrap": True,
                        "size": "md",
                        "color": "#666666"
                    }
                    ],
                    "spacing": "sm"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                    {
                        "type": "text",
                        "text": "氣溫狀況",
                        "flex": 2,
                        "color": "#aaaaaa",
                        "size": "md"
                    },
                    {
                        "type": "text",
                        "text": data[4],
                        "flex": 4,
                        "wrap": True,
                        "size": "md",
                        "color": "#666666"
                    }
                    ],
                    "spacing": "sm"
                }
                ]
            }
            ]
        }
    }

    return flex_message
    