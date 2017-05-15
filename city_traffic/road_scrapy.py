# -*- coding: utf-8 -*-  
import urllib.request
from bs4 import BeautifulSoup
import time
import json
import requests
import os
from datetime import datetime
import sched
from threading import Timer

schedule = sched.scheduler(time.time, time.sleep)

def scrapy():
    try:
        file = open('efficient_road.txt','r')
        write = open('traffic.txt', 'a')
        write.write("DateTime : " + format(datetime.now()) + '\n')
        for line in file.readlines():
            #print('http://restapi.amap.com/v3/traffic/status/road?key=99454a31574b48f86cee79c14a9386fc' + '&name=' + line.strip() + '&adcode=440100')
            url = 'http://restapi.amap.com/v3/traffic/status/road?key=99454a31574b48f86cee79c14a9386fc' + '&name=' + line.strip() + '&adcode=440100'
            html = requests.get(url)
            node = json.loads(html.text)
            print(node)
            if node['infocode'] == '10000':
                #efficient_road.write(line.strip() + '\n')
                write.write(str(node) + '\n')
            time.sleep(0.1)
    finally:
        if file:
            file.close()
            write.close()

def run_Task():
    x = datetime.today()
    for i in range(8, 21, 4):
        y = x.replace(day = x.day, hour = i, minute = 0, second = 0, microsecond = 0)
        if y >= x:
            delta_t = y - x
            secs = delta_t.seconds + 1
            print("scrapy will start after " + str(secs) + " seconds")
            print(datetime.now())
            t = Timer(secs, scrapy)
            t.start()
    tomorrow = x.replace(day = x.day + 1, hour = 0, minute = 0, second=0, microsecond=0)
    delta_day_seconds = tomorrow - x

    day_seconds = delta_day_seconds.seconds + 1
    t = Timer(day_seconds, run_Task)
    t.start()

if __name__ == '__main__':
    run_Task()
