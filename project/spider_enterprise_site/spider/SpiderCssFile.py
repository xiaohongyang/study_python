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
    rootDir = []
    def __init__(self, content, cssRe, relativeDir, rootDir):

        self.content = content
        self.cssRe = cssRe
        self.relativeDir = relativeDir
        self.rootDir = rootDir

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

                oldUrl = url
                try :
                    if os.path.isfile(savePath) == False :
                        spiderTextObj = SpiderText()
                        spiderTextObj.saveText(url, savePath)
                except Exception as e:
                    self.urlList.remove(oldUrl)

        pass

    def replaceContent(self):
        # 3. 替换所有css url
        if len(self.urlList) > 0 :
            for url in self.urlList :
                if isinstance(url, str) :
                    savePath = self.getNewFilePath(url, isAbsolutPath=False)
                    savePath = './' + savePath
                    #替换为本地新的css url
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
                savePath = saveDir + '/' + fileName + '.css'
            except Exception as e:
                savePath = False
                print(str(e))
        else :
            savePath = self.relativeDir + "/" + fileName + '.css'
        return  savePath
        pass



if __name__ == '__main__' :
    pass

