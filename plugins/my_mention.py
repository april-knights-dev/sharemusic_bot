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
@respond_to(('.*'))
def mention_func(message): # argsはメッセージの内容を取ってる messageはメンション者の取得
    result = fetch_text()
    print(result)
    message.reply(message.body['text']) # メンション



# @listen_to('リッスン')
# def listen_func(message):
#     message.send('誰かがリッスンと投稿したようだ')      # ただの投稿
#     message.reply('君だね？')

SLACK_CHANNEL_ID = "CC9NTUBEY"
SLACK_URL = "https://slack.com/api/conversations.history"
TOKEN = os.environ["TOKEN"]
# チャンネルの投稿を全て取得
def fetch_text():
    """ share_musicチャンネルの投稿を取得してjsonに変換
    Returns:
        str: チャンネル投稿のデータjson
    """
    payload = {
        "channel": SLACK_CHANNEL_ID,
        "token": TOKEN
    }
    response = requests.get(SLACK_URL, params=payload)
    json_data = response.json()
    return json_data