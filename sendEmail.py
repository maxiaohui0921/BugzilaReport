import downloadCSV
import analysisCSV
import summaryCSV
import generHTMLfile
import win32com.client as win32
import glConstant
import time
import linePicture

project="OrangeFPandPatch"

#自动发送邮件
def sendEmail(htmlfile,project):
    hfile= open(htmlfile,'r')
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    receivers = glConstant.receiver
	#receiversCC = glConstant.receiverCC1
    mail.To = receivers[0]
	#mail.CC = receiversCC[0]
    mail.Subject =project+'_Bug状态报告_'+glConstant.todaytag
    mail_body =hfile.read()
    #上面的是html脚本语言
    mail.HTMLBody = mail_body
    #mail.Attachments.Add(f)
    mail.Send()
    hfile.close()

if __name__=="__main__":
    queryLink = "OrangeFPandPatch"
    csvFile=downloadCSV.downloadCSV(glConstant.bugURL, queryLink)
    print("文件下载完成，路径在："+csvFile)
    analysisCSV.analysisCSV(csvFile)
    print("文件分析完成，补充了相应字段")
    table2,table3,table4 = summaryCSV.summary(csvFile)
    print("状态汇总完成，生成了相应表格")
    table1 = linePicture.totalTable(csvFile, "Orange1_Patch_SW", "Orange1.5_SW")
    filename=generHTMLfile.generateHtml(table1,table2,table3,table4)
    print("状态汇总完成，生成html内容")
    sendEmail(filename,project)
    print("请在邮箱里查收邮件")