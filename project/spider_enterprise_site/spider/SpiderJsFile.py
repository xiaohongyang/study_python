import os;
import types
from project.tools.spider.spider_text import *
from  pathlib import Path;
import re
import base64
import urllib
#1. 抓取所有js url
#2. 抓取所有提取到的js文件并保存到本地
#3. 替换所有js url
class SpiderJsFile :
    urlList = []
    rootDir = []
    def __init__(self, content, jsRe, relativeDir, rootDir, domain):

        self.content = content
        self.jsRe = jsRe
        self.relativeDir = relativeDir
        self.rootDir = rootDir
        self.domain = domain

    def run(self):
        self.getJsUrlList()
        self.saveJsFiles()
        self.replaceContent()
        pass

    def getJsUrlList(self):
        # 1. 抓取所有js url
        self.urlList = []
        for reItem in self.jsRe:
            list = reItem.findall(self.content)
            if len(list) :
                self.urlList.extend(list)

        pass

    def saveJsFiles(self):
        # 2. 抓取所有提取到的js文件并保存到本地
        if len(self.urlList) > 0 :
            for url in self.urlList :

                savePath = self.getNewFilePath(url)

                if os.path.isfile(savePath) == False :
                    spiderTextObj = SpiderText()

                    downUrl = url
                    r = re.compile('^http.*',re.I)
                    downUrl = downUrl if r.match(downUrl) != None else  self.domain + downUrl
                    spiderTextObj.saveText(downUrl, savePath)

        pass

    def replaceContent(self):
        # 3. 替换所有js url
        if len(self.urlList) > 0 :
            for url in self.urlList :
                if isinstance(url, str) :

                    savePath = self.getNewFilePath(url, isAbsolutPath=False)
                    savePath = './' + savePath
                    #替换为本地新的js url

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
                savePath = saveDir + '/' + fileName + '.js'
            except Exception as e:
                savePath = False
                print(str(e))
        else :
            savePath = self.relativeDir + "/" + fileName + '.js'
        return  savePath
        pass



if __name__ == '__main__' :
    pass

