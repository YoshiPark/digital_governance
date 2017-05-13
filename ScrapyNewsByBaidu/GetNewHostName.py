import jpype
import linecache
import os
from boilerpipe.extract import Extractor
import urllib.parse
import GetLinkICP
import GetCompanyAddress
import socket

class ComAdd:
    def __init__(self, company, address):
        self.company = company
        self.address = address
    def getcompany(self):
        return self.company

    def getaddress(self):
        return self.address

def getline(the_file_path, line_number):
  if line_number < 1:
    return ''
  for cur_line_number, line in enumerate(open(the_file_path, 'rU')):
    if cur_line_number == line_number-1:
      return line
  return ''

publisher = []
company = []
ReadFileDir = '/home/yoshipark/PycharmProjects/digital_governance/NewsLink'
file = open(ReadFileDir, 'r')
sel = 0
wrriteFile = '/home/yoshipark/PycharmProjects/digital_governance/NewsAddress'
writefile = open(wrriteFile, 'a')
curline = 1
linenum = len(file.readlines())
while curline < linenum:
    Publisher = getline(ReadFileDir, curline).replace('\n', '')
    if Publisher not in publisher:
        print(Publisher)
        publisher.append((Publisher))
        Link = urllib.parse.urlparse(getline(ReadFileDir, curline + 2).replace('\n', '')).hostname
        exist = False
        Company = GetLinkICP.getcompanyname(Link)
        Address = ""
        if not Company == "":
            for item in company:
                if Company == item.getcompany():
                    Address = item.getaddress()
                    exist = True
                    break

            if exist == False:
                Address = GetCompanyAddress.getaddress(Company)
                if Address == "":
                    Address = "无名地址"
                company.append(ComAdd(Company, Address))
        else:
            Address = "无名地址"

        writefile.write(Publisher + "\n" + Address + "\n")

    curline += 3

writefile.close()


