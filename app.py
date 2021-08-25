from os import X_OK
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

from urllib.parse import parse_qsl

import math

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('eIXivx5ncsmJ+rfxJa4SCSHoSVIBF/PNkqWr86IrMk8YWTyX8HD1AhbzP64QL1xnrRWG4ZsFxemXPjx5mMbX7GHj838rrljJpcYEEomA4TM/7TrxUCLTt89QUSZUn4sMKALcMITi7WJBqx/eG5I7swdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('b89ec2b4ec3d7ad080595b22ac05cb61')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# flow

def start(event):
    message = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        title='主題',
        text='請選擇想要的主題',
        actions=[
            PostbackTemplateAction(
                label='活動資訊',
                text='活動資訊',
                data='action=step0&type=活動資訊'
            ),
            PostbackTemplateAction(
                label='線上知識',
                text='線上知識',
                data='action=step0&type=線上知識'
            )
        ]
    )
)
    line_bot_api.reply_message(event.reply_token, message)


def hd(event):
    message = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        title='活動類型',
        text='請選擇一個有興趣的類型',
        actions=[
            PostbackTemplateAction(
                label='生理',
                text='生理',
                data='action=step1&type=生理'
            ),
            PostbackTemplateAction(
                label='心理',
                text='心理',
                data='action=step1&type=心理'
            ),
            # PostbackTemplateAction(
            #     label='飲食營養與健康',
            #     text='飲食營養與健康',
            #     data='action=step1&type=飲食營養與健康'
            # ),
            PostbackTemplateAction(
                label='運動活動',
                text='運動活動',
                data='action=step1&type=運動活動'
            )
        ]
    )
)
    line_bot_api.reply_message(event.reply_token, message)

def vw(event):
    message = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        title='線上知識',
        text='請選擇一個有興趣的知識',
        actions=[
            PostbackTemplateAction(
                label='生理',
                text='生理',
                data='action=step2&type=生理'
            ),
            PostbackTemplateAction(
                label='心理',
                text='心理',
                data='action=step2&type=心理'
            ),
            PostbackTemplateAction(
                label='飲食營養與健康',
                text='飲食營養與健康',
                data='action=step2&type=飲食營養與健康'
            )
        ]
    )
)
    line_bot_api.reply_message(event.reply_token, message)

def hd1(event):

    Image_Carousel = TemplateSendMessage(
        alt_text='目錄 template',
        template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url='https://i.imgur.com/edbSpt7.png',
                action=URIAction(
                    label='請點擊圖片進入活動',
                    uri='https://event.moc.gov.tw/sp.asp?xdurl=ccEvent2016/eventSearchList.asp&ev_start=&ev_end=&dateLimit=&ev_city=&ev_char1=all&ev_char2=&ev_char3=&stitle=&ev_series_id=&ev_place=&ev_location=&ev_format=all&ev_shower=&dept_name=&ev_xx=&pageSize=10&groupingField=&groupingValue=&ctNode=676&mp=1&currentPage=1'
                )
            )
        ]
    )
    )
    line_bot_api.reply_message(event.reply_token,Image_Carousel)

def hd2(event):
    Image_Carousel = TemplateSendMessage(
        alt_text='目錄 template',
        template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url='https://i.imgur.com/Jqa1eeJ.png',
                action=URIAction(
                    label='請點擊圖片進入活動',
                    uri='https://mental-health.gov.taipei/ActiveList.aspx?n=6CCBECECB36BFE4E&sms=F62510C10F2670B1'
                )
            )
        ]
    )
    )
    line_bot_api.reply_message(event.reply_token,Image_Carousel)

def hd3(event):
    Image_Carousel = TemplateSendMessage(
        alt_text='目錄 template',
        template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url='https://i.imgur.com/ENm0x9S.png',
                action=URIAction(
                    label='請點擊圖片進入活動',
                    uri='https://www.fongxu.com/%E8%BF%91%E6%9C%9F%E6%B4%BB%E5%8B%95%E5%A0%B1%E5%90%8D/2021%E5%8A%A9%E4%BA%BA%E5%A4%A5%E4%BC%B4%E5%90%91%E5%89%8D%E8%B5%B0%E7%B3%BB%E5%88%97%E8%AA%B2%E7%A8%8B'
                )
            )
        ]
    )
    )
    line_bot_api.reply_message(event.reply_token,Image_Carousel)

def hd4(event):
    Image_Carousel = TemplateSendMessage(
        alt_text='目錄 template',
        template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url='https://i.imgur.com/H6mTmCP.png',
                action=URIAction(
                    label='請點擊圖片進入活動',
                    uri='https://www.beclass.com/default.php?name=ShowList&op=catRank&range=F&fbclid=IwAR2eqQ7Mwci6N1Ww6rv7QO3qDvoA2WHNItsOHu4PQKhVImxanxA7-pm5qmo'
                )
            )
        ]
    )
    )
    line_bot_api.reply_message(event.reply_token,Image_Carousel)

def py1(event):
    Image_Carousel = TemplateSendMessage(
        alt_text='目錄 template',
        template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url='https://i.imgur.com/edbSpt7.png',
                action=URIAction(
                    label='請點擊圖片進入影片',
                    uri='https://www.mohw.gov.tw/lp-44-1.html'
                )
            )
        ]
    )
    )
    line_bot_api.reply_message(event.reply_token,Image_Carousel)

def py2(event):
    Image_Carousel = TemplateSendMessage(
        alt_text='目錄 template',
        template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url='https://i.imgur.com/Jqa1eeJ.png',
                action=URIAction(
                    label='請點擊圖片進入影片',
                    uri='https://mental-health.gov.taipei/News_Photo.aspx?n=17823B9C2328F92B&sms=D5799DC48EFC6840'
                )
            )
        ]
    )
    )
    line_bot_api.reply_message(event.reply_token,Image_Carousel)

def py3(event):
    Image_Carousel = TemplateSendMessage(
        alt_text='目錄 template',
        template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url='https://i.imgur.com/ENm0x9S.png',
                action=URIAction(
                    label='請點擊圖片進入影片',
                    uri='https://www.hpa.gov.tw/Video/RecommendVideo.aspx?nodeid=848'
                )
            )
        ]
    )
    )
    line_bot_api.reply_message(event.reply_token,Image_Carousel)

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # message = TextSendMessage(text=event.message.text)
    # line_bot_api.reply_message(event.reply_token, message)
    message_text = str(event.message.text).lower()
    pass_key = ['生理','心理','飲食營養與健康','線上知識','活動資訊','運動活動']
    if message_text =='開始':
        start(event)
    elif message_text =='填寫表單':
        Image_Carousel = TemplateSendMessage(
            alt_text='目錄 template',
            template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/gJ830Dn.pngg',
                    action=URIAction(
                        label='請點擊圖片填寫表單',
                        uri='https://docs.google.com/forms/d/e/1FAIpQLSctgAtphqn0YdStEscas2Q4bE46xZvkVQ34WsuGDtlpKiBD4w/viewform'
                    )
                )
            ]
        )
        )
        line_bot_api.reply_message(event.reply_token,Image_Carousel)
    elif message_text =='查看結果':
        # message = TextSendMessage(text='目前測驗尚在產出中，請稍後，謝謝您。')
        # line_bot_api.reply_message(event.reply_token, message)

        image_message = ImageSendMessage(original_content_url='https://i.imgur.com/FNt5jWH.png',preview_image_url='https://i.imgur.com/FNt5jWH.png')
        line_bot_api.reply_message(event.reply_token,image_message)
    elif message_text=='1234567890':
        image_message = ImageSendMessage(original_content_url='https://images2.imgbox.com/7a/fc/3ALLS4B7_o.jpg',preview_image_url='https://images2.imgbox.com/7a/fc/3ALLS4B7_o.jpg')
        line_bot_api.reply_message(event.reply_token,image_message)
    elif message_text=='123':
        image_message = ImageSendMessage(original_content_url='https://lh3.googleusercontent.com/csxITfrJXz45rGNVuB2ImkyxLa-G1G8G5HPPBhhF8T6MUGq6S19L3M4xk3WIill9mvCHNyx8WjAQDEWtXQqI=w1920-h902-rw',preview_image_url='https://lh3.googleusercontent.com/csxITfrJXz45rGNVuB2ImkyxLa-G1G8G5HPPBhhF8T6MUGq6S19L3M4xk3WIill9mvCHNyx8WjAQDEWtXQqI=w1920-h902-rw')
        line_bot_api.reply_message(event.reply_token,image_message)
    elif message_text in pass_key:
        pass
    else :
        message = TextSendMessage(text='結果正在產生中，請稍後在試。')
        line_bot_api.reply_message(event.reply_token, message)

@handler.add(PostbackEvent)
def handler_postback(event):
    # 我們需要把拿到的data字串轉換成字典，那我們會使用urllib裡的prase_qsl
    # prase_qsl可以解析一個query字串把它轉換成一個list
    # 那list如果要轉換成字典，在前面加上dict即可
    # 有了字典就可以針對action和server去取得資料（action和server是自定義宣告的，可以做更換）

    data = dict(parse_qsl(event.postback.data))
    action_data = data.get('action')
    type_data = data.get('type')
    # 接著就是做判斷，判斷我們的action等於什麼，然後做什麼事
    # 那我們這邊判斷如果等於step2，我們就做預約的動作

    if action_data =='step0':
        if type_data == '線上知識':
            vw(event)
        elif type_data =='活動資訊':
            hd(event)
    elif action_data == 'step1':
        if type_data == '生理':
            hd1(event) 
        elif type_data == '心理':
            hd2(event) 
        elif type_data == '飲食營養與健康':
            hd3(event) 
        elif type_data == '運動活動':
            hd4(event) 
    elif action_data =='step2':
        if type_data == '生理':
            py1(event) 
        elif type_data == '心理':
            py2(event)
        elif type_data == '飲食營養與健康':
            py3(event) 

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
