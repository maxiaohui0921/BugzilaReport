#2018/02/24 MaXiaohui
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glConstant
import time
import downloadCSV
import numpy as np

#写入部门，状态，devFix日期，verifyClose日期
queryLink="OrangeFPandPatch"
#csvFile=downloadCSV.downloadCSV(glConstant.bugURL,queryLink)
#print(csvFile)
csvFile=r"C:\Users\maxh\Desktop\Buglist\源文件\OrangeFPandPatch201802021102.csv"
df_all = pd.read_csv(csvFile, encoding='gb18030')

def filterdf(df,column,filterstr):
    #按照某一列的某个值进行筛选,得到的是个dataFrame
    df_filter=df[df[column]==filterstr]
    return  df_filter

def pvTable(df,index1,column1,value1):
    dfpvTable = pd.pivot_table(df, index=[index1],columns=column1,values=[value1], fill_value=0, aggfunc=[len])
    return dfpvTable

def series(df,column):   #计算总数，根据一列
    df_sub = df[column].value_counts().sort_index()
    return df_sub

def joinSeires(s1,s2):   #把两个序列连在一起，以index为链接，把不存在的值都填写成0
    df_join = pd.concat([s1, s2], axis=1).fillna(0)
    return df_join

def linePicture(df):
    df.plot(kind="line", rot=30)
    plt.savefig(r"C:\Users\maxh\Desktop\python\sendEmail\chart.png", bbox_inches='tight', transparent=True)  # 保存图
    chartPic = r"C:\Users\maxh\Desktop\python\sendEmail\chart.png"
    return chartPic

def seriesSuple(df):
    series_status = series(df, "状态分类")
    series_submit = series(df, "开启日")
    try:
        series_status["New/Today"] = series_submit[glConstant.todaytag2]
    except(KeyError, Exception):
        series_status["New/Today"] = 0

    series_close = series(df, "BugFix日期")
    try:
        series_status["Close/Today"] = series_close[glConstant.todaytag2]
    except(KeyError, Exception):
        series_status["Close/Today"] = 0

    df_resolve = filterdf(df,"状态分类","Resolved")
    series_resolved = series(df_resolve, "修改日期")
    try:
        series_status["resolvedToday"] = series_resolved[glConstant.todaytag2]
    except(KeyError, Exception):
        series_status["resolvedToday"] = 0

    return series_status

def totalTable(csvFile,pro1,pro2):
    df = pd.read_csv(csvFile, encoding='gb18030')
    df_patch = filterdf(df, "项目", pro1)
    df_fp = filterdf(df, "项目", pro2)
    se_pa = seriesSuple(df_patch)
    se_fp = seriesSuple(df_fp)
    total = pd.DataFrame([se_pa, se_fp])
    total.index = [pro1, pro2]
    table=total.to_html()
    return table

if __name__=="__main__":
    '''
    df_patch = filterdf(df_all,"项目","Orange1_Patch_SW")
    df_fp = filterdf(df_all,"项目","Orange1.5_SW")
    se_pa=seriesSuple(df_patch)
    se_fp=seriesSuple(df_patch)
    total=pd.DataFrame([se_pa, se_fp])
    total.index = ["Orange1_Patch_SW","Orange1.5_SW"]
    '''
    total=totalTable(csvFile,"Orange1_Patch_SW","Orange1.5_SW")
    print(total)
