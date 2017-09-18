import os;
import types
from project.tools.spider.spider_text import *
from  pathlib import Path;
import re
import base64
import urllib
#1. 抓取所有image url
#2. 抓取所有提取到的image文件并保存到本地
#3. 替换所有image url
class SpiderImageFile :
    urlList = []
    rootDir = []
    def __init__(self, content, imageRe, relativeDir, rootDir, domain):

        self.content = content
        self.imageRe = imageRe
        self.relativeDir = relativeDir
        self.rootDir = rootDir
        self.domain = domain

    def run(self):
        self.getImageUrlList()
        self.saveImageFiles()
        self.replaceContent()
        pass

    def getImageUrlList(self):
        # 1. 抓取所有image url
        self.urlList = []
        for reItem in self.imageRe:
            list = reItem.findall(self.content)
            if len(list) :
                self.urlList.extend(list)

        pass

    def saveImageFiles(self):
        # 2. 抓取所有提取到的image文件并保存到本地
        if len(self.urlList) > 0 :
            for url in self.urlList :

                savePath = self.getNewFilePath(url)

                oldUrl = url
                try:
                    if os.path.isfile(savePath) == False :
                        spiderTextObj = SpiderText()

                        downUrl = url
                        r = re.compile('^http.*',re.I)
                        downUrl = downUrl if r.match(downUrl) != None else  self.domain + downUrl
                        spiderTextObj.saveText(downUrl, savePath)
                except Exception as e :
                    self.urlList.remove(oldUrl)

        pass

    def replaceContent(self):
        # 3. 替换所有image url
        if len(self.urlList) > 0 :
            for url in self.urlList :
                if isinstance(url, str) :

                    savePath = self.getNewFilePath(url, isAbsolutPath=False)
                    savePath = './' + savePath
                    #替换为本地新的image url

                    self.content = self.content.replace(url, savePath)
        pass


    def getNewFilePath(self, url, isAbsolutPath=True):

        #fileName = base64.b64encode(bytes(url, 'utf-8'))
        # fileName = str(fileName)

        r = re.compile('^http.*',re.I)
        url = url if r.match(url) != None else  self.domain + url

        fileName = url.replace("http://","")
        fileName = fileName.replace("https://","")
        fileName = fileName.replace("?","_")
        fileName = fileName.replace("&","__")
        fileNameList = fileName.split('/')
        fileName = fileNameList[(len(fileNameList)-1)]


        relativePath = '/'.join(fileNameList[0:(len(fileNameList)-1)])
        relativePath = self.relativeDir + '/' + relativePath

        saveDir = relativePath
        if isAbsolutPath :
            saveDir = self.rootDir + '/' + saveDir
            try :
                if os.path.exists(saveDir) == False:
                    os.makedirs(saveDir)
                savePath = saveDir + '/' + fileName
            except Exception as e:
                savePath = False
                print(str(e))
        else :
            savePath = relativePath + "/" + fileName
        return  savePath
        pass


if __name__ == '__main__' :
    pass
