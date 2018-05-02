#2018/02/24 MaXiaohui

from selenium import webdriver
import glConstant
import time
import datetime
import os

#常用变量定义
today = datetime.date.today().strftime('%Y-%m-%d')
defalt_name="bugs-"+today
todaytag = datetime.date.today().strftime('%Y%m%d')
timetag = time.strftime('%H%M')

#打开目标网址,点击指定网址下载CSV文件
def downloadCSV(url,text):
    profile = webdriver.FirefoxProfile('C:/Users/maxh/AppData/Roaming/Mozilla/Firefox/Profiles/un78gn4r.default')
    browser = webdriver.Firefox(profile)
    browser.get(url)
    time.sleep(3)
    browser.find_element_by_link_text(text).click()
    time.sleep(10)
    browser.find_element_by_link_text("导出CSV报表").click()
    time.sleep(10)
    csvFile = glConstant.default_path + text + todaytag + timetag + ".csv"
    os.rename(glConstant.default_path + defalt_name + ".csv",csvFile)
    browser.close()
    return csvFile

if __name__=="__main__":
    print("This is downloadCSV.py running")
    queryLink="OrangeFPandPatch"
    downloadCSV(glConstant.bugURL,queryLink)