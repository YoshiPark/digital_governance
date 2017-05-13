from pyquery import PyQuery as pq
from urllib.parse import urlparse
import requests
import time

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

    def getheaders(self):
        return self.headers


def getcompanyname(domain):
    sleepsecond = 1
    time.sleep(sleepsecond)
    url = "http://m.tool.chinaz.com/beian?s=" + domain + "&guid=547e8248-6dfb-4f4f-b52d-8a287e89b844&code="
    response = Response(url=url, headers=headers)
    print(response.url)
    company = ""
    try:
        for items in response.doc(".headcontbeian").items():
            print((items.text().split())[1])
            company = (items.text().split())[1]
            break

    except:
        print("can't get the icp of company")
    return company

# test
# getcompanyname("http://www.southmoney.com")

