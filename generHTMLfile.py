import glConstant
project="OrangeFPandPatch"

def generateHtml(table1,table2,table3,table4):
    #定义生成的报告样式，html形式
    GEN_HTML=project+"_bugstatus"+glConstant.todaytag+'.html'  #命名生成的html
    str_0 = "Hi all"
    str_1 = "以下是"+project+"Bug状态"
    str_2 = "以下是各部门Open bug数目"
    str_3 = "Critical buglist"
    str_4 = '今天新报的bug'

    f= open(GEN_HTML,'w')
    message = """
    <html>
    <head></head>
    <body>
    <p>%s</p>
    <p>%s</p>
    <p>%s</p>
    <p>%s</p>
    <p>%s</p>
    <p>%s</p>
    <p>%s</p>
    <p>%s</p>
    <p>%s</p>
    </body>
    </html>"""%(str_0,str_1,table1,str_2,table2,str_3,table3,str_4,table4)
    f.write(message)
    f.close()
    return GEN_HTML

if __name__=="__main__":
    generateHtml("haha", "bbb","ccc","ddd")