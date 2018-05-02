#2018/02/24 MaXiaohui
import csv
import downloadCSV
import glConstant
import bugTable

#写入部门，状态，devFix日期，verifyClose日期
queryLink="OrangeFPandPatch"
#csvFile=downloadCSV.downloadCSV(glConstant.bugURL,queryLink)
#csvFile=r"C:\Users\maxh\Desktop\Buglist\源文件\OrangeFPandPatch201802011021.csv"

#在列表List1后面添加多个元素List2
def arrayAdd(list1,list2):
    for i in range(len(list2)):
        list1.append(list2[i])

def analysisCSV(csvFile):
    #读出csv文件到一个list列表中，待处理
    lines=csv.reader(open(csvFile,encoding="utf-8"))
    data=[]
    for line in lines:
        data.append(line)

    #处理文件，添加上以下三列，并挨个处理填写相关数据
    headers=["BugFix日期","BugReopen日期","状态分类","负责人部门"]
    arrayAdd(data[0],headers)
    #print(data[0])
    for i in range(1,len(data)):
        data[i][6]=data[i][6][:-9]
        data[i][9] = data[i][9][:-9]
        if data[i][3] in glConstant.closeStatus:
            #tableDatelist = bugTable.resolveopenDate(data[i][0])
            #tableDatelist.append("Closed")
            tableDatelist=[data[i][6],"","Closed"]
            arrayAdd(data[i],tableDatelist)
        else:
            arrayAdd(data[i], ["",""])
        if data[i][3] in glConstant.openStatus:
            tag="无相关部门"
            arrayAdd(data[i], ["Open"])
            for k, glConstant.v in glConstant.team.items():
                if data[i][7] in glConstant.v:
                    arrayAdd(data[i], [k])
                    tag="有相关部门"
            if tag=="无相关部门":
                print(data[i][7]+"为新员工，未加入部门中，请更新配置文件中的组成员列表")
        if data[i][3]=="已解决 (RESOLVED)":
            arrayAdd(data[i], ["Resolved"])

    #将处理好的data数据在重新写入到csv文件中
    writer = csv.writer(open(csvFile,'w'))
    writer.writerows(data)

if __name__=="__main__":
    analysisCSV(csvFile)
