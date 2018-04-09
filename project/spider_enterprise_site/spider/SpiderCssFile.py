import os;
import types
from project.tools.spider.spider_text import *
from  pathlib import Path;
import re
import base64
from project.spider_enterprise_site.spider.BaseSpider import BaseSpider

#1. 抓取所有css url
#2. 抓取所有提取到的css文件并保存到本地
#3. 替换所有css url
class SpiderCssFile (BaseSpider):
    urlList = []
    rootDir = []
    def __init__(self, content, cssRe, relativeDir, rootDir, domain, directory):

        self.content = content
        self.cssRe = cssRe
        self.relativeDir = relativeDir
        self.rootDir = rootDir
        self.domain = domain
        self.directory = directory

    def run(self):
        #抓取所有css url
        self.getCssUrlList()
        #抓取所有提取到的css文件并保存到本地
        self.saveCssFiles()
        #替换所有css url
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
                        webUrl = self.getWebUrl(url, self.domain, self.directory)
                        spiderTextObj = SpiderText()
                        spiderTextObj.saveText(webUrl, savePath)
                except Exception as e:
                    #下载异常则从下载队列中移除
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
        if r.match(url) == None and url[0:1] != '/':
            url = self.domain + self.directory + url
        elif r.match(url) == None :
            url = self.domain + url

        url = url.split(".css")[0]

        fileName = url.replace('/','_')
        fileName = fileName.replace('\\','_')
        fileName = fileName.replace(':','_')
        fileName = fileName.replace('?','_')
        fileName = fileName.replace('&','_')
        fileName = fileName.replace('%','_')
        fileName = fileName.replace(',','_')
        fileName = fileName.replace('-','_')
        fileName = fileName[0:120]
        _tmpRelativeDir = self.relativeDir
        if isAbsolutPath :
            # 保存文件内容的时候使用绝对路径
            _tmpRelativeDir = self.rootDir + '/' + _tmpRelativeDir + self.directory
            try :
                if os.path.exists(_tmpRelativeDir) == False:
                    os.makedirs(_tmpRelativeDir)
                savePath = _tmpRelativeDir + '/' + fileName + '.css'
            except Exception as e:
                savePath = False
                print(str(e))
        else :
            # 获取文件地址时使用相对路径，(将来更新html中的路径字符串)
            savePath = _tmpRelativeDir + "/" + self.directory + fileName + '.css'
        return  savePath
        pass



if __name__ == '__main__' :
    pass

