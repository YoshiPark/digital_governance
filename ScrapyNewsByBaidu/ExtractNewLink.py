import jpype
import linecache
import os
from boilerpipe.extract import Extractor


def getline(the_file_path, line_number):
  if line_number < 1:
    return ''
  for cur_line_number, line in enumerate(open(the_file_path, 'rU')):
    if cur_line_number == line_number-1:
      return line
  return ''

ReadFileDir = '/home/yoshipark/PycharmProjects/digital_governance/NewsLink'
file = open(ReadFileDir, 'r')
sel = 0
currentdir = '/home/yoshipark/PycharmProjects/digital_governance/news/'
curline = 1
linenum = len(file.readlines())
while curline < linenum:
    Dir = getline(ReadFileDir, curline).replace('\n', '')

    if os.path.exists(currentdir + Dir):
        print("The Dir is exist")
    else:

        print("Dir: %s" % Dir)
        os.makedirs(currentdir + Dir)

    Filename = getline(ReadFileDir, curline + 1).replace('\n', '')
    path = currentdir + Dir + '/' + Filename
    File = open(path, 'w')

    Url = getline(ReadFileDir, curline + 2).replace('\n', '')
    try:
        extractor = Extractor(extractor='ArticleExtractor', url=Url)
        extracted_text = extractor.getText()
        print(extracted_text)
        File.write(extracted_text)
        File.close()
    except:
        print("wrong")

    curline += 3



