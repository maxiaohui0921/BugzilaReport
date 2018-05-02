#2018/02/24 MaXiaohui
import datetime
import re
import time

#默认下载文件保存路径
default_path='C:/Users/maxh/Desktop/Buglist/源文件/'
bugURL="http://192.168.40.151:8000"
openStatus=["处理中 (IN_PROGRESS)","New","ASSIGNED","REOPEN","MONITOR","已确认 (CONFIRMED)","未确认 (UNCONFIRMED)","BLOCKED","处理中 (IN_PROGRESS)"]
closeStatus = ["已通过 (VERIFIED)","CLOSED","POSTPONED"]
bugHistorTable="http://192.168.40.151:8000/show_activity.cgi?id="
todaytag = datetime.date.today().strftime('%Y%m%d')
todaytag2 =  datetime.date.today().strftime('%Y-%m-%d')


orange_dev_session=["刘欢","杨洋","杨扬","杨文永","任凯","毛训雷","元军峰","商颖","王迪远","司哲铭","wangyu","李珂珍","马涛","孙天宝","黄朝阳","韩佳佳","杜超","曾波凯","卢子明","张鑫","何银飞","时东方","李佳","李萌"]
test_session=["韩琦","王燕","史秀岭","孙东升","刘菲","皮立伟","魏欠欠","汪浩","王勇","王冠群","邓艳丽","张骏弛","胡浩均","边莉莎","尹春萍","薛会爽","贾燕子","高柏","赵颖","邹铭","杨小燕","赵惠娟","谷满娜","杨蔚","邢月红","马晓慧","王喆","王挺","郭媛媛","王存平","杜新伟","翟昆明"]
product_session=["石英睿","周正","秦丹","范伟","巴图","胡金玉","张荣娜","陈君","郭培栋","赵序","李畅","徐嘉俊","丁汉福","刘昊","范强","迟雨薇","林志鹏","孙孟哲","王岩","吕佳琳","杨震","张勇1","李建东"]
cloud_session=["曲翰林","邢广明","严巍","黄小明","薛姣","吉燕丽","张鹏","yangjin","陈柳平","杜龙辉","田建林","吴志杰"]
xi_an_session=["尚江峰","王筱博","王磊","冯超","杨茹","陈红","马朝阳","屈志刚","yangyonggang","冯亚琼","陈平","施香香","李斌杰","muyanfei","张勇","潘亚峰","zhangzhe","杨永刚","王越红","卢彦斐","文景顺","郑俊飞"]
chengmai_session=["韩伟","潘涛","姜海","王俊","周腾腾","代春伟","郭本义","王卫全","张振强","马群","孙良","丁薇","朱兆祥","池风云","宋友发","丁森杰","尉军军","程亚楠","周春华","周星星"]
android_dev=["孟策","沈向峰","陈换博","李吉喆","毛明青","王凤芝","陈帅宇","刘江龙","李彬杰","王子建"]
ios_dev=["朱坤","张澄","潘阳军","侯江辉","李继伟","单佩星","胡永","郑松月","耿笑威","朱磊"]
team={'Orange软件':orange_dev_session,'测试':test_session,'产品':product_session,'云端':cloud_session,'西安':xi_an_session,'Android开发':android_dev,'IOS开发':ios_dev,'其他':'其他'}

receiver=['maxh@oradt.com']
receiverTo2=["likezhen@oradt.com","yangwy@oradt.com","yangyang2@oradt.com","yangyang@oradt.com","maoxl@oradt.com","renkai@oradt.com","shangying@oradt.com","suntb@oradt.com","sunmz@oradt.com","yuanjunfeng@oradt.com","huangchaoyang@oradt.com","sizheming@oradt.com","liuhuan@oradt.com","hanjj@oradt.com","zengbokai@oradt.com","wangdiyuan@oradt.com","lijia@oradt.com","limeng@oradt.com","luziming@oradt.com","matao@oradt.com","zhangxin@oradt.com","shidongfang@oradt.com","heyinfei@oradt.com","wangyu@oradt.com","xuehuishuang@oradt.com","wangxiaobo@oradt.com"]
receiverCC=["wangcp@oradt.com","wangyan1@oradt.com","duxw@oradt.com","caihuiyao@oradt.com","shiyingrui@oradt.com","annychen@oradt.com","liufei@oradt.com","lihaibo@oradt.com","hanqi@oradt.com"]

receiverTo1=["wangcp@oradt","zouming@oradt.com","gaobai@oradt.com"]
receiverCC1=["xuehuishuang@oradt","lijia@oradt"]