#2018/02/24 MaXiaohui
import csv
import downloadCSV
import pandas as pd
import numpy as np
import datetime
import glConstant

#写入部门，状态，devFix日期，verifyClose日期
queryLink="OrangeFPandPatch"
#csvFile=downloadCSV.downloadCSV(glConstant.bugURL,queryLink)
csvFile=r"C:\Users\maxh\Desktop\Buglist\源文件\OrangeFPandPatch201802011825.csv"


def summary(csvFile):
    df_all=pd.read_csv(csvFile,encoding = 'gb18030')
    #筛选Open bug的负责人以及负责部门
    df_open_bug = df_all[["Bug 编号", "项目", "状态", "摘要", "严重程度", "负责人真实姓名", "负责人部门", "状态分类"]][(df_all["状态分类"] == "Open")]
    df_open_summary = pd.pivot_table(df_open_bug, index=["项目","负责人部门", "负责人真实姓名"], values=["状态分类"], aggfunc=[len], margins=True)
    table_open_summary = df_open_summary.to_html()
    #print(table_open_summary)

    #筛选所有bug的总体状态
    df2=df_all[["项目","状态分类"]]
    df_total_summary = pd.pivot_table(df2, index=["项目"],columns="状态分类",values=["状态分类"],aggfunc=[len])
    table_total_summary = df_total_summary.to_html()
    #print(table_total_summary)

    #筛选criticlbug
    alist = ["critical","Show Stopper"]
    df_critical = df_all[["Bug 编号", "项目","模块", "状态", "摘要", "严重程度", "负责人真实姓名", "负责人部门", "开启日"]][(df_all["状态分类"] == "Open") & (df_all["严重程度"].isin(alist))]
    table_critical = df_critical.to_html()

    # 筛选today new bug
    df_today = df_all[["Bug 编号", "项目","模块","状态","摘要","严重程度","负责人真实姓名","负责人部门","开启日","反馈者真实姓名"]][(df_all["开启日"]==glConstant.todaytag2)]
    table_today = df_today.to_html()


    return table_open_summary,table_critical,table_today

if __name__=="__main__":
    summary(csvFile)