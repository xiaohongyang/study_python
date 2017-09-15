'''
艾德工作上下班打卡记录 数据抓取
'''
import urllib
import urllib.request
import urllib.parse
import project.tools.spider.spider
from bs4 import BeautifulSoup
from datetime import date
from time import sleep
import time
import threading
import re

inFile = open('proxy.txt', 'r')
errorFile = open("data/err.txt", 'r', encoding='utf-8')
errLines = errorFile.readlines()
print(errLines)



class WorkerTimeSpider():
    def __init__(self, url, sessionid='b581b3915ef5af169f2f98e83565af38', domain='xiaohongyang.cc'):
        self.url = url
        self.sessionid= sessionid
        self.domain=domain
        self.errFailFile="./data/errfail.txt"

    def getHeaders(self):
        header = {
            'Host': 'panda.www.net.cn',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cookie': 'login_aliyunid="25808****@qq.com"; login_aliyunid_ticket=hZ9ympASAe4xmF4oGQW*Xd_opVYrKw4Kcd22h4B_Mypof_BNTwUhTOoNC1ZBeeMfKJzxdnb95hYssNIZor6q7SCxRtgmGCbifG2Cd4ZWazmBdHI6sgXZqg4XFWQfyKpeu*0vCmV8s*MT5tJl3_1$$wfO0; login_aliyunid_csrf=_csrf_tk_1412370893233629; login_aliyunid_pk=1636357660206465; hichina_nickname=25808229; hssid=11tRzaMc9eYZj4fNb1KaLjg1; hsite=6; aliyun_country=CN; aliyun_site=CN; JSESSIONID=QM566DC1-WMRC68KFR7MRSMTAHC4W1-EY5ZVPRI-9MH52; tmp0=eNpdj1uPmkAYhm%2B3abr1JzSbvTIrGYZhAK%2BqeGIpWAFP9IKOM4MQhEHRKtv0h%2By%2FLdHdNOndkyfv%2Bx0mrYpXVSqK6FTxQ5Tx2gQ6FblEdml9KqQkpUlaEImJnKSFRBNOszPfSAXnbCe2jfJv%2FXlTf727tezyDSx2fwM3pVlBcn7%2F7oNG8OPH6wif7LjFPl95cN3jNtEPb4dZ7Jby0iqbk9Y%2FzgOR8eJnS8YKVlQNYwABRlhtQVUHOoSG%2FHW%2Fl5pf7t4FeE1Co87Lnt%2Fj6JKPkBjPlu0Vi0S5WB%2FsM7IpgzBB%2FcipSxFHfTc4z5NgKlxTDvucO7H9%2FHJhxcZQk3VVuVYoDniv%2BebFO27zsblJ4zE0GQqX5CXvs4mFq%2B0q3G%2FRarScxbVd8lMb%2FDLzhV61nUA9Pu%2BUSH58PMdT4Lrgi4E4ZBoAFMYQURnrhs70mCCgENzcpbruJ3%2Fo%2B9bUjZzpYPgN%2FPidsu7DzFExHphyZ%2Bl4Jtbtkac5nu8EvYmJlnJnuFbDxXfP6hjORIUPT%2FTYlZEGdENBimFo6InQ%2F0R%2B6YI%2F4V82k632'
        }

        return  header

    def do(self, postfix=1, saveFileName="./data/domain_avaliable.txt", faleFile="./data/err.txt", errorFile="./data/err.txt" ):

        headers = {}
        self.faleFile = faleFile
        self.errorFile=errorFile

        try:
            headers = self.getHeaders()
        except:
            pass

        # proxLine = 'http=183.131.151.208:80'
        proxLine = self.getProxLine()  #inFile.readline().strip()
        # if len(line) == 0: break
        protocol,proxy = proxLine.split('=')
        cookie = "PHPSESSID=5f7mbqghvk1kt5n9illa0nr175; kmsign=56023b6880039; KMUID=ezsEg1YCOzxg97EwAwUXAg=="

        self.url = self.url
        req = urllib.request.Request(self.url,headers=headers, method='get')

        try:
            proxy_support = urllib.request.ProxyHandler({protocol.lower():'://'.join(proxLine.split('='))})
            opener = urllib.request.build_opener(proxy_support, urllib.request.HTTPHandler)
            urllib.request.install_opener(opener)

            req = urllib.request.Request(self.url)
            req.set_proxy('127.0.0.1:8087', 'http')

            # html = urllib.request.urlopen(url=self.url)
            html = urllib.request.urlopen(req)
            content = html.read()
            return self.write2File(content, saveFileName)
        except BaseException:
            self.errLog(self.errorFile,proxLine)
            pass

    def errLog(self,logFile,proxLine,encoding='utf-8'):

        #保存错误日志
        f = open(logFile, 'a', encoding=encoding)
        f.write( '出现验证码或IP被封杀:'+ proxLine + "\n")
        f.close()

        #操作没有进行的域名
        fFail = open(self.errFailFile, 'a', encoding=encoding)
        fFail.write(self.domain+"\n")
        fFail.close()

    def getProxLine(self):
        proxLine = inFile.readline().strip()
        errorProxLines = self.getErrorPfoxLines()
        if proxLine in errorProxLines:
            return self.getProxLine()
        return proxLine

    def getErrorPfoxLines(self):

        for i in range(len(errLines)):
            errLines[i] = errLines[i].strip("出现验证码或IP被封杀:")
            errLines[i] = errLines[i].strip()
        return errLines

    def write2File(self,html,fileName):

        content = html.decode("utf-8")
        content = content.lower()
        check = content.find("not available")==-1 and content.find("In Use".lower())==-1

        if check :
            lines = []
            lines.append(self.domain + "\n")
            f = open(fileName, 'a')
            f.writelines(lines)
            f.close()
        else:
            lines = []
            lines.append(self.domain + "\n")
            f = open(self.faleFile, 'a')
            f.writelines(lines)
            f.close()




def getData(domain_name='xiaohongyang.cc'):

    print(domain_name)
    url = 'http://panda.www.net.cn/cgi-bin/check.cgi?area_domain='+domain_name
    sessionid = 'b581b3915ef5af169f2f98e83565af38'
    spider = WorkerTimeSpider(url, sessionid, domain=domain_name)
    rs = spider.do(1, saveFileName='./data/avaliable_' + date.today().__str__() + '.txt',
                   faleFile="./data/notavaliable_" + date.today().__str__() + '.txt')

def do():
    letterArr = range(ord('a'), ord('z'))
    numberArr = range(0, 10)

    for number_01 in numberArr:
        for number_02 in numberArr:
            for letter_01 in letterArr:
                for letter_02 in letterArr:
                    domainName = str(number_01) + str(number_02) + chr(letter_01)+ chr(letter_02) +'.cc'
                    check = re.match(r'^([\d])\1([\w])\2', domainName)
                    if check is not None :
                        try:
                            # threading._start_new_thread(getData,(domainName,))
                            # break;
                            getData(domainName)
                        except:
                            print("error")
                        # sleep(0.1)

def p(threadName):
    print("%s %s" % (threadName, time.time()))
    sleep(1)
    pass



if __name__ == '__main__':
    do()

    pass





