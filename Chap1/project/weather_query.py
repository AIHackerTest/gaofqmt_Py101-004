# -*- coding: utf-8 -*-
# import the weather information from a txt file
# store it to a dictionary
# read the file, and strip the line seperator:

from sys import exit

weather_d = []
history = {}

with open('../resource/weather_info.txt', 'r') as file:
    for x in [x.rstrip('\n') for x in file.readlines()]:
        weather_d.append(tuple(x.split(',')))

weather_d = dict(weather_d)

while True:

    city = input("请输入指令或要查询的城市名称> ").strip()

    if city == 'help':
        print ("""
        输入城市名，查询天气状况;
        输入help，获取帮助;
        输入history，获取查询历史;
        输入quit，退出天气查询系统。
        """)
    elif city == "history":
        for x, y in history.items():
            print (x, y)
    elif city == 'quit':
        file.close()
        exit(1)
    elif not(city in weather_d.keys()):
        print("您输入的城市暂未收录，请重新输入！")
        continue
    else:
        print(weather_d[city])
        history[city] = weather_d[city]
