import ExtractEverySheet
import SaveEverySheet
import GetStockInfo
import FileOperator
import re
import datetime

LogFailInfo = []

def HandlePerStock(stock, date):
    stockid = re.findall(r'[^()]+', stock)[1]
    if FileOperator.IsExistFile(date, stock) == False:
        try:
            workbook = SaveEverySheet.CreateWorkBook()
            for sheet in ExtractEverySheet.SheetURLName:
                FinancialAnalysisURLs = ExtractEverySheet.GetAllYearUrl(sheet, stockid, ExtractEverySheet.Year)
                DataList = ExtractEverySheet.GetAllFinancialAnalysisSheetData(FinancialAnalysisURLs)
                worksheet = workbook.add_sheet(sheet)
                SaveEverySheet.SaveSheetData(worksheet, DataList, 0)
            StockShareDividendsURL = ExtractEverySheet.StockShareDividendsUrl(stockid).GetCompleteStr()
            BonusResultList, RationedSharesResultList = ExtractEverySheet.GetStockShareDividendsSheetData(
                StockShareDividendsURL)
            SaveEverySheet.SaveStockShareDividendsSheetData(workbook, ExtractEverySheet.StockShareDividends,
                                                            BonusResultList,
                                                            RationedSharesResultList)
            SaveEverySheet.SaveWorkBook(workbook, FileOperator.FilePos(date, stock))
            print(str(date + ": " + stock + " 爬取成功"))

        except:
            print(str(date + ": " + stock + " 爬取失败"))
            ErrorInfo = str(date + ": " + stock + " 爬取失败")
            LogFailInfo.append(ErrorInfo)



if __name__ == '__main__':
    Date = datetime.datetime.now().strftime('%Y-%m-%d')
    FileOperator.CreateFile(Date)
    stockidList = GetStockInfo.GetStockData()
    for stock in stockidList:
        HandlePerStock(stock, Date)

    
