# -*- coding: utf-8 -*-

import sys
from slacker import Slacker


args = sys.argv
token = args[1]
pict_path = args[2]
predict = args[3]

predict = predict.split("@")
predict.pop()

message = "侵入者です(｀･ω･´)ゞ\n```" 
pred_dict = {}
for p in predict:
    p_sp = p.split(":")
    pred_dict.update({float(p_sp[0]):p_sp[1]})
for k, v in sorted(pred_dict.items(), reverse=True):
        line = "\n" + v + " (" + str(k) + ")"
        message += line

message += "\n```"

slacker = Slacker(token)
channel_name = "#" + "general"
channel_id = slacker.channels.list().body["channels"][0]["id"]

slacker.chat.post_message(channel_name, message)
result = slacker.files.upload(pict_path, channels=[channel_id])
slacker.pins.add(channel=channel_id, file_=result.body['file']['id'])
