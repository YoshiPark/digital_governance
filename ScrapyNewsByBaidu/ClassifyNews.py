import jpype
import linecache
import jieba
import shutil
import os
from boilerpipe.extract import Extractor


def getline(the_file_path, line_number):
  if line_number < 1:
    return ''
  for cur_line_number, line in enumerate(open(the_file_path, 'rU')):
    if cur_line_number == line_number-1:
      return line
  return ''

ReadFileDir = '/home/yoshipark/PycharmProjects/digital_governance/NewsAddress'
file = open(ReadFileDir, 'r')
sel = 0
currentdir = '/home/yoshipark/PycharmProjects/digital_governance/newsFilter/'
towarddir = '/home/yoshipark/PycharmProjects/digital_governance/newsClassify/'
curline = 1
linenum = len(file.readlines())
while curline < linenum:
    publisher = getline(ReadFileDir, curline).replace('\n', '')

    if os.path.exists(currentdir + publisher):
        print("Find publisher is ok")
    else:
        print("Failed to find publisher")


    Address = getline(ReadFileDir, curline + 1).replace('\n', '')
    success = False
    NewDir = ""
    try:
        for w in jieba.cut(Address):
            if (str(w).find("市") > -1):
                NewDir = w
                success = True
                break
    except:
        NewDir = "无名地址"
        print("It's failed to cut the address")

    if os.path.exists(towarddir + NewDir):
        print("The Dir is exist")
    else:
        print("Dir: %s" % NewDir)
        os.makedirs(towarddir + NewDir)

    if os.path.exists(towarddir + NewDir + '/' + publisher):
        print("The publisher is exist")
    else:
        if os.path.exists(currentdir + publisher):
            shutil.copytree(currentdir + publisher, towarddir + NewDir + '/' + publisher)
    curline += 2



