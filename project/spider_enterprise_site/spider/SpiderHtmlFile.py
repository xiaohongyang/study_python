import os;
import types
from project.tools.spider.spider_text import *
from  pathlib import Path;
import re
import base64
import urllib
import project.spider_enterprise_site.spider.SpiderCssFile as SiteSpider
import sys

#1. 抓取所有html url
#2. 抓取所有提取到的html文件并保存到本地
#3. 替换所有html url
class SpiderHtmlFile :
    urlList = []
    rootDir = []
    def __init__(self, content, htmlRe, relativeDir, rootDir, domain):

        self.content = content
        self.htmlRe = htmlRe
        self.relativeDir = relativeDir
        self.rootDir = rootDir
        self.domain = domain

    def run(self):
        self.getHtmlUrlList()
        self.saveHtmlFiles()
        self.replaceContent()
        pass

    def getHtmlUrlList(self):
        # 1. 抓取所有html url
        self.urlList = []
        for reItem in self.htmlRe:
            list = reItem.findall(self.content)
            if len(list) :
                self.urlList.extend(list)
        tmpList = []
        for k,url in enumerate(self.urlList):
            url = url.replace(' ','')
            if url in ['','/',
                       '/index.html',
                       '/index.php','/index','index','index.html','index.php'] \
                    == False :
                self.urlList.remove(url)
            else :
                tmpList.append(url)
        self.urlList = tmpList
        pass

    def saveHtmlFiles(self):
        # 2. 抓取所有提取到的html文件并保存到本地
        if len(self.urlList) > 0 :
            for url in self.urlList :

                #下载页面
                spider = SiteSpider(self.domain)
                spider.run(url)
                return

        pass

    def replaceContent(self):
        # 3. 替换所有html url
        if len(self.urlList) > 0 :

            spider = SiteSpider(self.domain)
            for url in self.urlList :
                if isinstance(url, str) :

                    savePath = spider.getPageFileName(url)
                    #替换为本地新的html url
                    self.content = self.content.replace(url, savePath)
        pass


    def getNewFilePath(self, url, isAbsolutPath=True):

        #fileName = base64.b64encode(bytes(url, 'utf-8'))
        # fileName = str(fileName)

        r = re.compile('^http.*',re.I)
        url = url if r.match(url) != None else  self.domain + url

        fileName = url.replace('/','__')
        fileName = fileName.replace('\\','___')
        fileName = fileName.replace(':','____')
        fileName = fileName.replace('?','_____')
        fileName = fileName.replace('&','_______')
        fileName = fileName.replace('%','________')
        fileName = fileName[0:120]
        saveDir = self.relativeDir
        if isAbsolutPath :
            saveDir = self.rootDir + '/' + saveDir
            try :
                if os.path.exists(saveDir) == False:
                    os.makedirs(saveDir)
                savePath = saveDir + '/' + fileName + '.html'
            except Exception as e:
                savePath = False
                print(str(e))
        else :
            savePath = self.relativeDir + "/" + fileName + '.html'
        return  savePath
        pass



if __name__ == '__main__' :
    pass

