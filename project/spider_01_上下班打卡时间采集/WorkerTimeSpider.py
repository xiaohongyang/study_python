'''
艾德工作上下班打卡记录 数据抓取
'''
import urllib
import urllib.request
import urllib.parse
import project.tools.spider.spider
from bs4 import BeautifulSoup
from datetime import date

class WorkerTimeSpider():

    def __init__(self, url, sessionid='27dfc1ccbee9671055915c8a031f96bb'):
        self.url = url
        self.isSessionOk = True;
        self.sessionid= sessionid

    #设计抓包header信息
    def getHeaders(self):

        header = {
            # 'Host': 'kaoqin.adsage.com',
            # 'Connection': 'keep-alive',
            # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            # 'Upgrade-Insecure-Requests': '1',
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
            # 'Accept-Encoding': 'gzip, deflate, sdch',
            # 'Accept-Language': 'zh-CN,zh;q=0.8',
            # 'Cookie': 'yunsuo_session_verify=e5b63df7710e24028ae04211bd489764; sessionid='+self.sessionid
            #
            'Host': 'kaoqin.adsage.com',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
            'Referer': 'http://kaoqin.adsage.com/iclock/accounts/login/?next=/iclock/staff/',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            #'Cookie': 'yunsuo_session_verify=a730a7892052999e590ababb6ac27e99; sessionid=bed716cf36da098292d1175a4ac188a1'
            #'Cookie': 'yunsuo_session_verify=a730a7892052999e590ababb6ac27e99; sessionid=6f363be21bb4d8961ca457a4c50ca16c'
            # 'Cookie': '_ws_uid=2cb1690bP1022220009U2032B21S10A16.90348; yunsuo_session_verify=a730a7892052999e590ababb6ac27e99; sessionid=35d779891d73bafc1314f1fb663644a3'
            'Cookie': '_ws_uid=2cb1690bP1022220009U2032B21S10A16.90348; yunsuo_session_verify=a730a7892052999e590ababb6ac27e99; sessionid=f7c6b555f49a48902b3a9f347db74aaa'


        }

        return  header

    #获取数据并写入文件
    def getTimes(self,p=1,saveFileName="./data/worker_times.txt",errorFile="./data/err.txt"):

        headers = {}
        try:
            headers = self.getHeaders()
        except:
            pass

        values = {'p': p}
        data = urllib.parse.urlencode(values)
        self.url = self.url +"&"+ data
        req = urllib.request.Request(self.url, headers=headers, method='post')

        try:
            # req.set_proxy('127.0.0.1:8087', 'http')
            html = urllib.request.urlopen(req)
            content = html.read()
            return self.write2File(content, saveFileName)
        except Exception as e:

            f = open(errorFile,'a',encoding='utf-8')
            if e.code == 302 :

                self.isSessionOk = False;
                f.write( "error:302" + self.url );
                f.close()
                return e;
            else:

                f.write( "第"+str(p)+"页读取失败\n" )
                f.close()

    #写入文件
    def write2File(self,html,fileName):
        bs = BeautifulSoup(html, 'html.parser')
        trs = bs.find_all("tr", height="25px")
        if len(trs) > 0:
            lines = []
            for tr in trs:
                lines.append(tr.contents[1].text + "\n")
            f = open(fileName, 'a')
            f.writelines(lines)
            f.close()
        else:
            return  -1



#获取员工账户信息
#http://kaoqin.adsage.com/iclock/staff/employee/?UserID__id__exact=1576&fromTime=&toTime=


def getData():

    sessionid = 'b581b3915ef5af169f2f98e83565af38'
    user_id = 1577
    url = 'http://kaoqin.adsage.com/iclock/staff/transaction/?t=staff_transaction.html&UserID__id__exact='\
          +str(user_id)+'&fromTime=2015-01-01&toTime=2020-08-25'

    for i in range(1,500):
        spider = WorkerTimeSpider(url, sessionid)
        rs = spider.getTimes(i,saveFileName='./data/worker_times_'+date.today().__str__()+'.txt')
        if spider.isSessionOk == False:
            break



# bs = BeautifulSoup(html, 'html.parser')
#bs.find_all("tr",height="25px")
# for tr in trs:
#     print(tr.contents[1].text , tr.contents[2].text)

if __name__ == '__main__':
    getData()




