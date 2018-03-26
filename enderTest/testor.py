#!/usr/bin/python
# -*- coding: UTF-8 -*-

def printme( str ):

    "打印任何传入的字符串"

    print (str);

    return;



# 调用函数

printme("我要调用用户自定义函数!");

printme("再次调用同一函数");


wordList=["abc", "test"]
text="test"
#text="123test456"

#checking List.contaions(xxx);
if any(word in text for word in wordList):
    print("Match.");
else:
    print("NotMatch.");

if (wordList.__contains__(text)):
    print("Match.");
else:
    print("NotMatch.");

for word in wordList:
    if (word in text):
        print("Match.");
    else:
        print("NotMatch.");