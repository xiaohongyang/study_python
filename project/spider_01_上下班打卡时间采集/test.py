#下载百度表情文件
import os
import sys
import json
import urllib
import urllib.request

from bs4 import BeautifulSoup

from project.tools.spider.spider import Spider

class FacePicSpider():
    def __init__(self, initUrl, headers, saveDir, imgSuffix, prefix=''):
        #初始化 定义列表页地址 如:http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E6%9A%B4%E8%B5%B0%E6%BC%AB%E7%94%BB%E8%A1%A8%E6%83%85&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E6%9A%B4%E8%B5%B0%E6%BC%AB%E7%94%BB%E8%A1%A8%E6%83%85&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=90&rn=30&gsm=5a&1469414418332=
        self.spider = Spider("")
        self.iniUrl = initUrl
        self.headers = headers
        self.saveDir = saveDir
        self.imgSuffix = imgSuffix
        self.prefix = prefix
        self.picUrlArray = []

    def setPicUrlArray(self):

        req = urllib.request.Request(url=self.iniUrl, headers=self.headers)
        listHtml = urllib.request.urlopen(req)
        listPageContent = listHtml.read()

        jsonStrings = listPageContent.decode("UTF-8")
        jsonStrings = jsonStrings.replace("\\\'s", "")
        jsonObj = json.loads(jsonStrings)

        linksJson = jsonObj["data"]
        if self.picUrlArray != []:
            self.picUrlArray = []
        print(len(linksJson))
        if len(linksJson) > 0:
            for link in linksJson:
                if link.__contains__('thumbURL'):
                    self.picUrlArray.append(link['thumbURL'])

    def getPicUrlArray(self):
        return self.picUrlArray

    def downAllPic(self):

        self.setPicUrlArray()
        if len(self.picUrlArray) > 0 :
            self.spider.setLinkList(self.picUrlArray)
            if (not os.path.exists(self.saveDir)):
                os.mkdir(self.saveDir);
            self.spider.downLinkList(self.saveDir, self.imgSuffix, self.prefix)


#spider.saveImg(url,"./down/vvtestzzzz21135.png")

#listPageUrl = "http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E6%9A%B4%E8%B5%B0%E6%BC%AB%E7%94%BB%E8%A1%A8%E6%83%85&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E6%9A%B4%E8%B5%B0%E6%BC%AB%E7%94%BB%E8%A1%A8%E6%83%85&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=90&rn=30&gsm=5a&1469414418332="
listPageUrl = "http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E6%9A%B4%E8%B5%B0%E6%BC%AB%E7%94%BB%E8%A1%A8%E6%83%85&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E6%9A%B4%E8%B5%B0%E6%BC%AB%E7%94%BB%E8%A1%A8%E6%83%85&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=120&rn=30&gsm=5a&1469414418332="
# listPageUrl = "http://jike.com/api/zeroprize/prizeTimes"

# listPageHtml = urllib.request.urlopen(listPageUrl);
# listContent = listPageHtml.read()
# listContent = listContent.decode('utf-8');
# listContent = listContent.replace("\\\'s", "")
# myJson =json.loads(listContent)
#
#
# for item in myJson['data']:
#     if item.__contains__('thumbURL'):
#         # print(item['thumbURL'])
#         pass

facePicSpider = FacePicSpider(listPageUrl,{},'./down/facepic','.png', prefix='a_')
facePicSpider.downAllPic()

exit()


url = "http://img2.imgtn.bdimg.com/it/u=4046962068,3343118610&fm=206&gp=0.jpg"
spider = Spider("")

spider.setHeader(
    {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
        'Referer': 'http://img2.imgtn.bdimg.com/it/u=4046962068,3343118610&fm=206&gp=0.jpg',
        'Connection': 'keep-alive',
        'Host': 'img2.imgtn.bdimg.com'
    }
)

spider.setLinkList([url,url,url])
spider.downLinkList("./down",'.png')


