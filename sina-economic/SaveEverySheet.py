import xlwt
def SaveSheetData(worksheet, dataList, rowindex):
    for rowdata in dataList:
        colindex = 0
        for celldata in rowdata:
            worksheet.write(rowindex, colindex, celldata)
            colindex += 1
        rowindex += 1

def WriteBonusTitle(worksheet):
    worksheet.write_merge(0, 0, 0, 8, "分红")
    worksheet.write_merge(1, 1, 1, 2, "分红方案(每10股)")
    worksheet.write(2, 0, "公告日期")
    worksheet.write(2, 1, "送股(股)")
    worksheet.write(2, 2, "转增(股)")
    worksheet.write(2, 3, "派息(税前)(元)")
    worksheet.write(2, 4, "进度")
    worksheet.write(2, 5, "除权除息日")
    worksheet.write(2, 6, "股权登记日")
    worksheet.write(2, 7, "红股上市日")
    worksheet.write(2, 8, "查看详细")

def SaveBonusSheetData(worksheet, dataList):
    rowindex = 3
    for rowdata in dataList:
        colindex = 0
        for celldata in rowdata:
            worksheet.write(rowindex, colindex, celldata)
            colindex += 1
        rowindex += 1

def WriteRationedSharesTitle(worksheet, rowindex):
    worksheet.write_merge(rowindex, rowindex, 0, 10, "配股")
    worksheet.write(rowindex + 1, 0, "公告日期")
    worksheet.write(rowindex + 1, 1, "配股方案(每10股配股股数)")
    worksheet.write(rowindex + 1, 2, "配股价格(元)")
    worksheet.write(rowindex + 1, 3, "基准股本(万股)")
    worksheet.write(rowindex + 1, 4, "除权日")
    worksheet.write(rowindex + 1, 5, "股权登记日")
    worksheet.write(rowindex + 1, 6, "缴款起始日")
    worksheet.write(rowindex + 1, 7, "缴款终止日")
    worksheet.write(rowindex + 1, 8, "配股上市日")
    worksheet.write(rowindex + 1, 9, "募集资金合计(元)")
    worksheet.write(rowindex + 1, 10, "查看详细")


def SaveStockShareDividendsSheetData(workbook, sheet_name, BonusResultList, RationedSharesResultList):
    worksheet = workbook.add_sheet(sheet_name)
    WriteBonusTitle(worksheet)
    SaveSheetData(worksheet, BonusResultList, 3)
    WriteRationedSharesTitle(worksheet, len(BonusResultList) + 3)
    SaveSheetData(worksheet, RationedSharesResultList, len(BonusResultList) + 5)



def CreateWorkBook():
    return xlwt.Workbook()

def SaveWorkBook(workbook,filepath):
    workbook.save(str(filepath))