import os

def ExtractDate(date):
    year = date.split("-")[0]
    month = date.split("-")[1]
    day = date.split("-")[2]
    return year, month, day

def CreateFile(date):
    year, month, day = ExtractDate(date)
    YearDirectory = os.path.join(os.getcwd(), year)
    if os.path.exists(YearDirectory) == False:
        os.mkdir(YearDirectory)
    MonthDirectory = os.path.join(YearDirectory, month)
    if os.path.exists(MonthDirectory) == False:
        os.mkdir(MonthDirectory)
    DayDirectory = os.path.join(MonthDirectory, day)
    if os.path.exists(DayDirectory) == False:
        os.mkdir(DayDirectory)

def IsExistFile(date, title):
    return os.path.exists(FilePos(date, title))


def FilePos(date, title):
    year, month, day = ExtractDate(date)
    path = os.getcwd() + "/" + year + "/" + month + "/" + day + "/" + title + ".xls"
    return path


def CreateLogFile(date, LogsInfo):
    year, month, day = ExtractDate(date)
    F = open(os.getcwd() + "/" + year + "/" + month + "/" + day + "/" + "LogInfo,txt", 'w')
    for Log in LogsInfo:
        F.write(Log + "\n")
    F.close()