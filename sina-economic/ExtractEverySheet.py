import requests
from bs4 import BeautifulSoup
import bs4.element
import time
headers = {
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3213.3 Mobile Safari/537.36"
}
SheetURLName = ["vFD_BalanceSheet", "vFD_ProfitStatement", "vFD_CashFlow"]
StockShareDividends = "vISSUE_ShareBonus"
Year = ["2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008", "2007"]

class FinancialAnalysisUrl:
    def __init__(self, SheetName, StockId, Year):
        FinancialAnalysisUrl.prefix = "http://money.finance.sina.com.cn/corp/go.php/"
        FinancialAnalysisUrl.sheetname = SheetName
        FinancialAnalysisUrl.infix = "/stockid/"
        FinancialAnalysisUrl.stockid = StockId
        FinancialAnalysisUrl.postfix = "/ctrl/"
        FinancialAnalysisUrl.year = Year
        FinancialAnalysisUrl.lastfix = "/displaytype/4.phtml"

    def GetCompleteStr(self):
        return str(FinancialAnalysisUrl.prefix + FinancialAnalysisUrl.sheetname + FinancialAnalysisUrl.infix + FinancialAnalysisUrl.stockid + FinancialAnalysisUrl.postfix + FinancialAnalysisUrl.year + FinancialAnalysisUrl.lastfix)


class StockShareDividendsUrl:
    def __init__(self, StockId):
        StockShareDividendsUrl.prefix = "http://vip.stock.finance.sina.com.cn/corp/go.php/vISSUE_ShareBonus/stockid/"
        StockShareDividendsUrl.stockid = StockId
        StockShareDividendsUrl.postfix = ".phtml"

    def GetCompleteStr(self):
        return str(StockShareDividendsUrl.prefix + str(StockShareDividendsUrl.stockid) + StockShareDividendsUrl.postfix)



def GetAllYearUrl(SheetName, StockID, Years):
    ResultList = []
    for Year in Years:
        YearUrl = FinancialAnalysisUrl(SheetName, StockID, Year)
        ResultList.append(YearUrl.GetCompleteStr())
    return ResultList

def ExtractSheetData(sheet):
    ResultList = []
    for tr in sheet.children:
        if isinstance(tr, bs4.element.Tag):
            result = []
            for child in tr.children:
                if isinstance(child, bs4.element.Tag):
                    info = str(child.text)
                    if info == "--":
                        result.append("0")
                    else:
                        result.append(info)
            if len(result) != 0:
                ResultList.append(result)
    return ResultList

def GetPerFinancialAnalysisSheetData(URL):
    Response = requests.get(url=URL, headers=headers)
    time.sleep(0.5)
    Response.encoding = "gb2312"
    soup = BeautifulSoup(Response.text, "lxml")
    tablesheet = soup.find("tbody")
    if isinstance(tablesheet, bs4.element.Tag):
        ResultList = ExtractSheetData(tablesheet)
    else:
        ResultList = []
    return ResultList

def GetAllFinancialAnalysisSheetData(URLs):
    ResultList = []
    for URL in URLs:
        PerDataList = GetPerFinancialAnalysisSheetData(URL)
        if len(ResultList) == 0 and len(PerDataList) != 0:
            ResultList.append(PerDataList)
        else:
            try:
                for i in range(0, len(PerDataList)):
                    if len(PerDataList) != 1:
                        for j in range(1, len(PerDataList[i])):
                            ResultList[0][i].append(PerDataList[i][j])
            except ValueError:
                print("Merge error!")
    return ResultList[0]

def GetStockShareDividendsSheetData(URL):
    Response = requests.get(url=URL, headers=headers)
    time.sleep(0.5)
    Response.encoding = "gb2312"
    soup = BeautifulSoup(Response.text, "lxml")

    Bonussheet = soup.select("#sharebonus_1 > tbody")[0]
    BonusResultList = ExtractSheetData(Bonussheet)
    RationedShares = soup.select("#sharebonus_2 > tbody")[0]
    RationedSharesResultList = ExtractSheetData(RationedShares)
    return BonusResultList, RationedSharesResultList