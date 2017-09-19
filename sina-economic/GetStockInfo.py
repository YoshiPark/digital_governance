import requests
from bs4 import BeautifulSoup
import bs4.element
import re
headers = {
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3213.3 Mobile Safari/537.36"
}

def ExtractStockMarket(city, stockmarket):
    resultList = []
    for stock in stockmarket.children:
        if isinstance(stock, bs4.element.Tag):
            if city == "上海":
                if re.findall(r'[^()]+', stock.text)[1][0] == '6':
                    resultList.append(stock.text)
            else:
                resultList.append(stock.text)
    return resultList

def GetStockData():
    Url = "http://quote.eastmoney.com/stocklist.html"
    Response = requests.get(url=Url, headers=headers)
    Response.encoding = "gb2312"
    soup = BeautifulSoup(Response.text, "lxml")
    stockmarkets = soup.select("#quotesearch > ul")
    ShanghaiList = ExtractStockMarket("上海", stockmarkets[0])
    ShenzhenList = ExtractStockMarket("深圳", stockmarkets[1])
    Stocklist = ShanghaiList + ShenzhenList
    return Stocklist