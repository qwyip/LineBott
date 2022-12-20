from linebot import LineBotApi
from linebot.models import TextSendMessage
import time

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('sxZvkJ/GC7RdtY6jmav7xB9TFcmTIqZw9FJ5zF4rQMKUVwuZGl467dBL8bzvN/8Yor8geOWVqc06sa6ufPEVwipidocTrCgYCYRUoMf9RMGL3Z/dCCRwGnQ3e4TdRHpPua15cjRHUiYRz3evDJQXrgdB04t89/1O/w1cDnyilFU=')
# 請填入您的ID
yourID = 'U146570034b8d6111d1e048e2749cd88b'
# 主動推播訊息
line_bot_api.push_message(yourID, 
                          TextSendMessage(text='安安您好！早餐吃了嗎？'))
# 用迴圈推播訊息
for i in [1,2,3,4,5]:
    line_bot_api.push_message(yourID, 
                              TextSendMessage(text='我們來倒數：'+str(i)))
    time.sleep(1)