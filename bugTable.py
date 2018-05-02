#2018/02/29 MaXiaohui
from selenium import webdriver
import glConstant
import time

profile = webdriver.FirefoxProfile('C:/Users/maxh/AppData/Roaming/Mozilla/Firefox/Profiles/un78gn4r.default')

def lineSplit(listArr, findStr):
    date1 = "空值"
    for j in listArr:
        if findStr in j:
            date1 = j
    return date1


# 获的bug的resolveDate和reopenDate
def resolveopenDate(bugID):
    linkURL = glConstant.bugHistorTable + str(int(bugID))
    browser1 = webdriver.Firefox(profile)
    reopenDate = ""
    resolveDate = ""
    browser1.get(linkURL)
    table = browser1.find_elements_by_xpath('/html/body/div[2]/table/tbody')
    for i in table:
        list = (i.text).split('\n')
        for j in list:
            if "已解决 (RESOLVED)" in j and ("已通过 (VERIFIED)" or 'REOPEN') not in j:
                rowList = j.split()
                resolveDate = lineSplit(rowList, '-')    #获取到bug设置成resolve的时间
            if "已通过 (VERIFIED)" in j:
                rowList2 = j.split()
        for l in list:
            if "REOPEN" in l:
                rowList1 = l.split()
                reopenDate = lineSplit(rowList1, '-')    #获取到bug设置成reopen的时间
                break
    time.sleep(2)
    browser1.close()
    print(bugID, resolveDate, reopenDate)
    return [resolveDate,reopenDate]

if __name__=="__main__":
    resolveopenDate(30552)