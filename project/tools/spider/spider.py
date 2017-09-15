import os
from bs4 import BeautifulSoup
from urllib import *
import urllib
from urllib import  request

class Spider:

    def __init__(self, url):
        self.url = url
        self.header = {}
        self.linkList = []
    '''
    url 要下载的地址
    fileName 新建文件名
    '''
    def saveImg(self, url, fileName):

        header = self.header
        #url = "http://s3.51cto.com/wyfs02/M01/30/03/wKioL1OiryfgvGZVAAIosMpN4lo679.jpg"

        try:
            req = urllib.request.Request(url,headers = header)
            html = urllib.request.urlopen(req)
            fileData = html.read()
            file = open(fileName, 'wb')
            file.write(fileData)
            file.close()
        except:
            pass

        # html = urllib.request.urlopen(url)
        # data = html.read()
        # img = open(fileName, "wb")
        # img.write(data)
        # img.close()
    def setHeader(self, header):

        self.header = header
        pass

    def setLinkList(self, linkList):
        self.linkList = linkList

    def getLinkList(self):
        return  self.linkList

    #下载文件列表到指定目录
    #saveDir 目标目录
    #suffix 文件名后缀
    #prefix 文件名前缀
    def downLinkList(self,saveDir, suffix='', prefix=''):



        i = 1;
        for link in self.linkList:
            i += 1
            theSuffix = suffix
            if suffix=='':
                theSuffix = '.' + self.getImageSuffix(link)

            self.saveImg(link, saveDir + "/" + prefix +str(i) + theSuffix)

    def getImageSuffix(self,url):

        suffix = ''
        if len(url)>1 :
            arr = url.split('.')
            index = len(arr) - 1
            suffix = arr[index]

        return suffix




