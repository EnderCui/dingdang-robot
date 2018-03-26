# -*- coding: utf-8-*-
import sys
import json

DEVICES = {"tv": 'switch.tv',
           "left": 'switch.tvleft'}



service = DEVICES["left"].split('.')[0]
print("service:" + service)

data = json.dumps({'entity_id': DEVICES["left"]})
print("data:" + data)


text = u"打开"
if text == u"打开":
    cmd = "turn_on"
else:
    cmd = "turn_off"

print("cmd:" + cmd)