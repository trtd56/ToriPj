#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from slacker import Slacker
import pygame.mixer
import time

SOUNDFILE="/home/pi/ToriPj/sound.mp3"
SOUNDTIME=3.5

# 引数から各要素を受け取る
args = sys.argv
token = args[1]
pict_path = args[2]
predict = args[3]

# 予測結果は改行が@になっている
predict = predict.split("@")
predict.pop()

# 表示メッセージ作成
message = "侵入者です(｀･ω･´)ゞ\n```" 
pred_dict = {}
for p in predict:
    p_sp = p.split(":")
    pred_dict.update({float(p_sp[0]):p_sp[1]})
# 認識確率順でソート
for k, v in sorted(pred_dict.items(), reverse=True):
        line = "\n" + v + " (" + str(k) + ")"
        message += line
message += "\n```"

# 投稿するChannel設定
slacker = Slacker(token)
channel_name = "#" + "general"
channel_id = slacker.channels.list().body["channels"][0]["id"]

# Slackに投稿
slacker.chat.post_message(channel_name, message)
result = slacker.files.upload(pict_path, channels=[channel_id])
slacker.pins.add(channel=channel_id, file_=result.body['file']['id'])

# 音を鳴らす
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(SOUNDFILE)
pygame.mixer.music.play(-1)
time.sleep(SOUNDTIME)
pygame.mixer.music.stop()
