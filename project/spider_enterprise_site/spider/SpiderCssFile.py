import os;
import types
from project.tools.spider.spider_text import *
from  pathlib import Path;
import re
import base64

#1. 抓取所有css url
#2. 抓取所有提取到的css文件并保存到本地
#3. 替换所有css url
class SpiderCssFile :
    urlList = []
    def __init__(self, content, cssRe, saveDir):

        self.content = content
        self.cssRe = cssRe
        self.saveDir = saveDir

    def run(self):
        self.getCssUrlList()
        self.saveCssFiles()
        self.replaceContent()
        pass

    def getCssUrlList(self):
        # 1. 抓取所有css url
        self.urlList = []
        for reItem in self.cssRe:
            list = reItem.findall(self.content)
            if len(list) :
                self.urlList.extend(list)
        pass

    def saveCssFiles(self):
        # 2. 抓取所有提取到的css文件并保存到本地
        if len(self.urlList) > 0 :
            for url in self.urlList :
                savePath = self.getNewFilePath(url)

                if os.path.isfile(savePath) == False :
                    spiderTextObj = SpiderText()
                    spiderTextObj.saveText(url, savePath)

        pass

    def replaceContent(self):
        # 3. 替换所有css url
        if len(self.urlList) > 0 :
            for url in self.urlList :
                if isinstance(url, str) :
                    savePath = self.getNewFilePath(url, isAbsolutPath=False)
                    #替换为本地新的css url
                    self.content = self.content.replace(url, savePath)
        pass


    def getNewFilePath(self, url, isAbsolutPath=True):

        #fileName = base64.b64encode(bytes(url, 'utf-8'))
        # fileName = str(fileName)

        fileName = url.replace('/','__')
        fileName = fileName.replace('\\','___')
        fileName = fileName.replace(':','____')
        fileName = fileName.replace('?','_____')
        fileName = fileName[0:100]
        saveDir = os.getcwd() +  '/' + self.saveDir if isAbsolutPath  else   '/' + self.saveDir
        try :
            if os.path.exists(saveDir) == False:
                os.makedirs(saveDir)
            savePath = saveDir + '/' + fileName + '.css'
        except Exception as e:
            savePath = False
            print(str(e))
        return  savePath
        pass



if __name__ == '__main__' :
    pass

