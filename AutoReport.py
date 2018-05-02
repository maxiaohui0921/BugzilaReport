import downloadCSV
import analysisCSV
import summaryCSV
import generHTMLfile
import win32com.client as win32
import glConstant
import sendEmail
import linePicture

queryLink = "OrangeFPandPatch"      #如果想跟踪其他项目，只需要变更这个字段，这是一个bugzilla中建立的搜索link
csvFile=downloadCSV.downloadCSV(glConstant.bugURL, queryLink)
print("文件下载完成，路径在："+csvFile)
analysisCSV.analysisCSV(csvFile)
print("文件分析完成，补充了相应字段")
table2,table3,table4 = summaryCSV.summary(csvFile)
table1 = linePicture.totalTable(csvFile, "Orange1_Patch_SW", "Orange1.5_SW")
print("状态汇总完成，生成了相应表格")
filename=generHTMLfile.generateHtml(table1,table2,table3,table4)
print("状态汇总完成，生成html内容")
sendEmail.sendEmail(filename,queryLink)
print("请在邮箱里查收邮件")