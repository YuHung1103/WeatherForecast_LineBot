# 引入圖文訊息
from linebot.models import FlexSendMessage

# 引入爬蟲程式
from .WeatherCrawler import today, week

def todayMessage(event):
    data = today()
    return FlexSendMessage(
        alt_text='今天天氣狀況',
        contents={
            "type": "bubble",
            "size": "mega",
            "hero": {
                "type": "image",
                "url": "https://attach.setn.com/newsimages/2022/12/02/3945459-PH.jpg",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover",
                "action": {
                    "type": "message",
                    "label": "action",
                    "text": "今日天氣"
                },
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
    )
    
def weekMessage(event):
    data = week()
    return FlexSendMessage(
        alt_text='今天天氣狀況',
        contents={
            "type": "carousel",
            "contents": [
                {
                "type": "bubble",
                "size": "micro",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": data[0][0],
                        "weight": "bold",
                        "size": "md",
                        "wrap": True
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "氣溫",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[0][1]+"°C",
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
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
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[0][2],
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "體感溫度",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[0][3]+"°C",
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "紫外線",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[0][4],
                            "size": "xs",
                            "color": "#666666",
                            "flex": 5
                        }
                        ]
                    },
                    {
                        "type": "text",
                        "text": "------------------"
                    },
                    {
                        "type": "text",
                        "text": data[1][0],
                        "weight": "bold",
                        "size": "md",
                        "wrap": True
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "氣溫",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[1][1]+"°C",
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
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
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[1][2],
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "體感溫度",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[1][3]+"°C",
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "紫外線",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[1][4],
                            "size": "xs",
                            "color": "#666666",
                            "flex": 5
                        }
                        ]
                    }
                    ],
                    "spacing": "sm",
                    "paddingAll": "13px"
                }
                },
                {
                "type": "bubble",
                "size": "micro",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": data[2][0],
                        "weight": "bold",
                        "size": "md",
                        "wrap": True
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "氣溫",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[2][1]+"°C",
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
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
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[2][2],
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "體感溫度",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[2][3]+"°C",
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "紫外線",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[2][4],
                            "size": "xs",
                            "color": "#666666",
                            "flex": 5
                        }
                        ]
                    },
                    {
                        "type": "text",
                        "text": "------------------"
                    },
                    {
                        "type": "text",
                        "text": data[3][0],
                        "weight": "bold",
                        "size": "md",
                        "wrap": True
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "氣溫",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[3][1]+"°C",
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
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
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[3][2],
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "體感溫度",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[3][3]+"°C",
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "紫外線",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[3][4],
                            "size": "xs",
                            "color": "#666666",
                            "flex": 5
                        }
                        ]
                    }
                    ],
                    "spacing": "sm",
                    "paddingAll": "13px"
                }
                },
                {
                "type": "bubble",
                "size": "micro",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": data[4][0],
                        "weight": "bold",
                        "size": "md",
                        "wrap": True
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "氣溫",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[4][1]+"°C",
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
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
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[4][2],
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "體感溫度",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[4][3]+"°C",
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "紫外線",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[4][4],
                            "size": "xs",
                            "color": "#666666",
                            "flex": 5
                        }
                        ]
                    },
                    {
                        "type": "text",
                        "text": "------------------"
                    },
                    {
                        "type": "text",
                        "text": data[5][0],
                        "weight": "bold",
                        "size": "md",
                        "wrap": True
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "氣溫",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[5][1]+"°C",
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
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
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[5][2],
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "體感溫度",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[5][3]+"°C",
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "紫外線",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[5][4],
                            "size": "xs",
                            "color": "#666666",
                            "flex": 5
                        }
                        ]
                    }
                    ],
                    "spacing": "sm",
                    "paddingAll": "13px"
                }
                },
                {
                "type": "bubble",
                "size": "micro",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": data[6][0],
                        "weight": "bold",
                        "size": "md",
                        "wrap": True
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "氣溫",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[6][1]+"°C",
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
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
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[6][2],
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "體感溫度",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[6][3]+"°C",
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "紫外線",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[6][4],
                            "size": "xs",
                            "color": "#666666",
                            "flex": 5
                        }
                        ]
                    },
                    {
                        "type": "text",
                        "text": "------------------"
                    },
                    {
                        "type": "text",
                        "text": data[7][0],
                        "weight": "bold",
                        "size": "md",
                        "wrap": True
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "氣溫",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[7][1]+"°C",
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
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
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[7][2],
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "體感溫度",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[7][3]+"°C",
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "紫外線",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[7][4],
                            "size": "xs",
                            "color": "#666666",
                            "flex": 5
                        }
                        ]
                    }
                    ],
                    "spacing": "sm",
                    "paddingAll": "13px"
                }
                },
                {
                "type": "bubble",
                "size": "micro",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": data[8][0],
                        "weight": "bold",
                        "size": "md",
                        "wrap": True
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "氣溫",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[8][1]+"°C",
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
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
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[8][2],
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "體感溫度",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[8][3]+"°C",
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "紫外線",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[8][4],
                            "size": "xs",
                            "color": "#666666",
                            "flex": 5
                        }
                        ]
                    },
                    {
                        "type": "text",
                        "text": "------------------"
                    },
                    {
                        "type": "text",
                        "text": data[9][0],
                        "weight": "bold",
                        "size": "md",
                        "wrap": True
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "氣溫",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[9][1]+"°C",
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
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
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[9][2],
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "體感溫度",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[9][3]+"°C",
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "紫外線",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[9][4],
                            "size": "xs",
                            "color": "#666666",
                            "flex": 5
                        }
                        ]
                    }
                    ],
                    "spacing": "sm",
                    "paddingAll": "13px"
                }
                },
                {
                "type": "bubble",
                "size": "micro",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": data[10][0],
                        "weight": "bold",
                        "size": "md",
                        "wrap": True
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "氣溫",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[10][1]+"°C",
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
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
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[10][2],
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "體感溫度",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[10][3]+"°C",
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "紫外線",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[10][4],
                            "size": "xs",
                            "color": "#666666",
                            "flex": 5
                        }
                        ]
                    },
                    {
                        "type": "text",
                        "text": "------------------"
                    },
                    {
                        "type": "text",
                        "text": data[11][0],
                        "weight": "bold",
                        "size": "md",
                        "wrap": True
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "氣溫",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[11][1]+"°C",
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
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
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[11][2],
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "體感溫度",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[11][3]+"°C",
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "紫外線",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[11][4],
                            "size": "xs",
                            "color": "#666666",
                            "flex": 5
                        }
                        ]
                    }
                    ],
                    "spacing": "sm",
                    "paddingAll": "13px"
                }
                },
                {
                "type": "bubble",
                "size": "micro",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": data[12][0],
                        "weight": "bold",
                        "size": "md",
                        "wrap": True
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "氣溫",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[12][1]+"°C",
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
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
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[12][2],
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "體感溫度",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[12][3]+"°C",
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "紫外線",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[12][4],
                            "size": "xs",
                            "color": "#666666",
                            "flex": 5
                        }
                        ]
                    },
                    {
                        "type": "text",
                        "text": "------------------"
                    },
                    {
                        "type": "text",
                        "text": data[13][0],
                        "weight": "bold",
                        "size": "md",
                        "wrap": True
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "氣溫",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[13][1]+"°C",
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
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
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[13][2],
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "體感溫度",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[13][3]+"°C",
                            "flex": 5,
                            "size": "xs",
                            "color": "#666666"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "紫外線",
                            "size": "xs",
                            "margin": "none",
                            "flex": 4,
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "text",
                            "text": data[13][4],
                            "size": "xs",
                            "color": "#666666",
                            "flex": 5
                        }
                        ]
                    }
                    ],
                    "spacing": "sm",
                    "paddingAll": "13px"
                }
                }
            ]
        }
    )