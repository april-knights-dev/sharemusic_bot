# coding: utf-8

from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ
import os
import requests
import urllib.request as req
import sys
import json
from bs4 import BeautifulSoup

import json
import pprint

import random

# @respond_to('string')     bot宛のメッセージ
#                           stringは正規表現が可能 「r'string'」
# @listen_to('string')      チャンネル内のbot宛以外の投稿
#                           @botname: では反応しないことに注意
#                           他の人へのメンションでは反応する
#                           正規表現可能
# @default_reply()          DEFAULT_REPLY と同じ働き
#                           正規表現を指定すると、他のデコーダにヒットせず、
#                           正規表現にマッチするときに反応
#                           ・・・なのだが、正規表現を指定するとエラーになる？

# message.reply('string')   @発言者名: string でメッセージを送信
# message.send('string')    string を送信
# message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する
#                               文字列中に':'はいらない


# .*でどんなメッセージでも受け付ける状態
# respond_toで指定してもいいし、中でif message=xxx と分岐してもいい

# @respond_to(('.*'))
@respond_to('音楽')
def music_func(message): # argsはメッセージの内容を取ってる messageはメンション者の取得

    # 1. 型を確認する → type(変数)
    # 2. 型に応じて分解する

    result = fetch_text('CC9NTUBEY') # 過去の投稿データ
    # print(result)
    msg = result['messages']
    target_user = msg[0]['user']
    # print(len(msg))
    # music_link = msg[0]['attachments'][0]['title_link']

    # result["text"] = result.get("text") →　中身が出てくる
    music_list = [] 
    for n in msg:
        if n.get('attachments') is not None:
            if n['attachments'][0].get('title_link') is not None:
                 music_list.append(n['attachments'][0]['title_link'])

    # music_list.append({n['user'] , n['attachments'][0]['title_link']})
    # [{user: XXX, url: YYY},{user: XXX, url: YYY},{user: XXX, url: YYY}]

    # @share_music_bot: 音楽
    # [URL1, URL2, URL3, URL4, URL5, URL6, .....] → ここからランダム
    # print(target_user)

    randnum = random.randrange(0,len(music_list) - 1) #len(music_list)で今ある投稿分の乱数を指定
    music_list[randnum] # こんにちわ

    # msg = result['messages'] # リスト型
    # # print(msg,type(msg))
    # # print(msg[0]) # >> 'author_link': 'https://www.youtube.com/user/blacklipton'
    # msg_0 = msg[0] # 辞書型
    # at = msg_0['attachments']
    # # print(at)
    # # for k,v in msg_0.items():
    # #     print(k,v)
    # at_0 = at[0]
    # # print(at_0)
    # link = at_0['title_link']
    # print(music_link) 


    # @share_music_bot: UGES7CGJU
    # {"UGES7CGJU": [URL1, URL2, URL3], "QWEZZRT2": [URL1], ....}


    message.reply(f'この曲おすすめだから聞いてみてぽよ〜\n{music_list[randnum]}') 
    #message.reply(message.body['text']) # メンション
    # message.reply(result['text'])
    
@respond_to('うまめし') 
def umameshi_func(message):

    result2 = fetch_text('CC8JN3PC6')
    # print(result2)
    msg2 = result2['messages']
    
    umameshi_list = []
    for n in msg2:
        if n.get('attachments') is not None:
            if n['attachments'][0].get('title_link') is not None:
                 umameshi_list.append(n['attachments'][0]['title_link'])
    # print(umameshi_list)
    # print(len(umameshi_list))

    randnum2 = random.randrange(0,len(umameshi_list) - 1) 
    umameshi_list[randnum2] 

    message.reply(f'ここ美味しいからおすすめぽよ〜\n{umameshi_list[randnum2]}') 

# @listen_to('リッスン')
# def listen_func(message):
#     message.send('誰かがリッスンと投稿したようだ')      # ただの投稿
#     message.reply('君だね？')

# SLACK_CHANNEL_ID = "CC9NTUBEY"
SLACK_URL = "https://slack.com/api/conversations.history"
TOKEN = os.environ["TOKEN"]
# チャンネルの投稿を全て取得
def fetch_text(channel_id):
    """ share_musicチャンネルの投稿を取得してjsonに変換
    Returns:
        str: チャンネル投稿のデータjson
    """
    payload = {
        "channel": channel_id,
        "token": TOKEN,
        "limit": 1000,
    }
    response = requests.get(SLACK_URL, params=payload)
    json_data = response.json()
    return json_data

