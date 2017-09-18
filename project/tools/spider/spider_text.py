import os
from bs4 import BeautifulSoup
from urllib import *
import urllib
from urllib import  request

class SpiderText:

    content = ""

    def __init__(self, url=''):
        self.url = url
        self.header = {}
        self.linkList = []

    def saveText(self, url, fileName):
        '''
        url 要下载的地址
        fileName 新建文件名
        '''
        self.setUrlContent(url)

        try:
            file = open(fileName, 'wb')
            file.write(self.content)
            file.close()
        except Exception as e:
            print(str(e))
        # html = urllib.request.urlopen(url)
        # data = html.read()
        # img = open(fileName, "wb")
        # img.write(data)
        # img.close()

    def setUrlContent(self, url):
        header = self.header
        req = urllib.request.Request(url,headers = header)
        html = urllib.request.urlopen(req)
        fileData = html.read()

        self.content = fileData

    def setContent(self, content):
        self.content = content

    def save(self, fileName):
        try:
            file = open(fileName, 'wb')
            file.write(self.content)
            file.close()
        except Exception as e:
            print(str(e))

    def setFieName(self, fileName):
        self.fileName = fileName

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
    def downLinkList(self,saveDir, suffix, prefix=''):

        i = 1;
        for link in self.linkList:
            i += 1
            self.saveText(link, saveDir + "/" + prefix +str(i)+suffix)



