# -*- coding: utf-8 -*-
import time
import os
import jpype
from boilerpipe.extract import Extractor
from pyquery import PyQuery as pq
from urllib.parse import urlparse
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}


class Response:
    def __init__(self, url, method='GET', headers=headers, **kwargs):
        self.host = urlparse(url).scheme + '://' + urlparse(url).netloc
        self.rep = requests.request(url=url, method=method, headers=headers, verify=False, **kwargs)
        self.method = method
        self.headers = self.rep.request.headers
        self.ok = self.rep.ok
        self.url = self.rep.url
        self.text = self.rep.text
        self.doc = pq(self.rep.content)
        try:
            self.json = self.rep.json()
        except:
            self.json = {}
        self.cookies = self.rep.cookies


new_count = 0
newstext = []
newshref = []
newsauthor = []
print("please input the key word you want to search:")
keyword = input()
while new_count < 730:
    sleepsecond = 1;
    time.sleep(sleepsecond)
    url = 'http://news.baidu.com/ns?word=%s&pn=%d&cl=2&ct=1&tn=news&rn=20&ie=utf-8&bt=0&et=0' % (keyword, new_count)

    print(url)
    response = Response(url=url, headers=headers)

    for each in response.doc('.c-title a').items():
        newstext.append(each.text())
        newshref.append(each.attr.href)
    for each in response.doc('.c-author').items():
        newstr = each.text().split()
        print(newstr[0])
        newsauthor.append(newstr[0])

    new_count += 10

WriteFileDir = '/home/yoshipark/PycharmProjects/digital_governance/NewsLink'
file = open(WriteFileDir, 'w')
if len(newstext) != len(newsauthor):
    print(len(newstext))
    print(len(newsauthor))
    print("wrong")
else:
    for i in range(len(newstext)):
        print("%s\n%s\n%s\n" % (newsauthor[i], newstext[i], newshref[i]))
        file.write("%s\n%s\n%s\n" % (newsauthor[i], newstext[i], newshref[i]))
file.close()
