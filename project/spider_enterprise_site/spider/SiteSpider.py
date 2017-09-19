import os;
import types
from project.tools.spider.spider_text import *
from  pathlib import Path;
from project.spider_enterprise_site.spider.SpiderCssFile import SpiderCssFile
from project.spider_enterprise_site.spider.SpiderJsFile import SpiderJsFile
from project.spider_enterprise_site.spider.SpiderImageFile import SpiderImageFile
import re


class SiteSpider :

    @staticmethod
    def setLevel(level):
        SiteSpider.level = level

    @staticmethod
    def getLevel():
        return SiteSpider.level
    downingList = []

    level = 0
    cssRe = [
        re.compile(r'link[\s\d\w"\'=]*href="([^"]+)"', re.I|re.M),
        re.compile(r'link[\s\d\w"\'=]*href=\'([^\']+)\'', re.I)
    ]
    cssDir = "static_source/css"

    jsRe = [
        #<script src="http://bk.st.styleweb.com.cn/editor/js/jquery.min.js"></script>
        re.compile(r'script[\s\d\w"\']*src="([^"]+)"', re.I),
        re.compile(r"script[\s\d\w\"']*src='([^']+)'", re.I)
    ]
    jsDir = "static_source/js"

    imageRe = [
        #<script src="http://bk.st.styleweb.com.cn/editor/image/jquery.min.image"></script>
        re.compile(r'<img[\s\d\w"\']*(?<!data-)src="([^"]+)"', re.I),
        re.compile(r"<img[\s\d\w\"']*(?<!data-)src='([^']+)'", re.I)
    ]
    imageDir = "static_source/image"

    htmlRe = [
        #<script src="http://bk.st.styleweb.com.cn/editor/html/jquery.min.html"></script>
        re.compile(r'<a[\s\d\w"\']*href="([^"]+)"', re.I),
        re.compile(r"<a[\s\d\w\"']*href='([^']+)'", re.I)
    ]
    htmlDir = "html"

    htmlContent = ""

    def __init__(self, domain, indexPage="", spiderChildLevel=False):

        self.domain = domain
        self.indexPage = indexPage if indexPage==None else ""
        self.savePath = os.getcwd() + "/" + self.__getDomainName()
        self.spiderChildLevel = spiderChildLevel
        self.__checkAndCreateSaveDir()


    def __checkAndCreateSaveDir(self):
        if os.path.exists(self.savePath) == False :
            os.makedirs(self.savePath)


    def run(self,url=''):

        if url in SiteSpider.downingList :

            return False

        SiteSpider.downingList.append(url)

        self.__spiderSpecialPage(url)

        level = self.getLevel()
        if level > 0 :
            SiteSpider.setLevel(level - 1)

    def __spiderSpecialPage(self, url=''):
        # 抓取首页
        if url=='' :
            indexPage = self.__getPageName()
            self.__spiderPage(indexPage)

        else :
            self.__spiderPage(url)
        pass

    def __spiderPage(self, url):

        # 抓取页面
        # 1.抓取html
        self.__spiderHtml(url)

        # 2.抓取css
        self.__spiderCss(self.htmlContent)

        # 3.抓取js
        self.__spiderJs(self.htmlContent)

        # 4.抓取图片
        self.__spiderImage(self.htmlContent)

        if self.spiderChildLevel :
            self.__spiderJumpHtml(self.htmlContent)

        self.__saveHtml(url)

    def __spiderHtml(self, url):
        # 抓取html

        try:
            spider = SpiderText(url)
            fileName = self.getPageFileName(url)
            filePath = self.savePath + "/" + fileName
            spider.setUrlContent(url)
            self.__updateContent(str(spider.content, 'utf-8'))
        except Exception as e:
            print(str(e))
            pass;

    def __saveHtml(self, url):
        try:
            spider = SpiderText()
            fileName = self.getPageFileName(url)
            filePath = self.savePath + '/' + fileName
            content = bytes(self.htmlContent, 'utf-8')
            spider.setContent(content)
            spider.save(filePath)
        except Exception as e :
            print(str(e))

    def __spiderCss(self, htmlContent):
        # 抓取css
        #1. 抓取所有css url
        #2. 抓取所有提取到的css文件并保存到本地
        #3. 替换所有css url

        spiderCss = SpiderCssFile(htmlContent, self.cssRe, relativeDir=self.cssDir, rootDir=self.savePath)
        spiderCss.run()
        self.__updateContent(spiderCss.content)
        pass

    def __updateContent(self, content):
        self.htmlContent = content

    def __spiderJs(self, htmlContent):
        #抓取js
        spiderJs = SpiderJsFile(htmlContent, self.jsRe, relativeDir=self.jsDir, rootDir=self.savePath, domain = self.domain)
        spiderJs.run()
        self.__updateContent(spiderJs.content)
        pass

    def __spiderImage(self, htmlContent):
        #抓取js
        spiderImage = SpiderImageFile(htmlContent, self.imageRe, relativeDir=self.imageDir, rootDir=self.savePath, domain = self.domain)
        spiderImage.run()
        self.__updateContent(spiderImage.content)
        pass

    def __spiderJumpHtml(self, htmlContent):
        #抓取html跳转页
        spiderHtml = SpiderHtmlFile(htmlContent, self.htmlRe, relativeDir=self.htmlDir, rootDir=self.savePath, domain = self.domain)
        spiderHtml.run()
        self.__updateContent(spiderHtml.content)
        pass

    def __getPageName(self,url='',isAbsolutPath=True):
        if url=='' :
            # 获取首页地址
            indexPageUrl = self.domain +  "/" + self.indexPage
            return  indexPageUrl
        else :

            r = re.compile('^http.*',re.I)
            url = url if r.match(url) != None else  self.domain + url

            fileName = url.replace('/','__')
            fileName = fileName.replace('\\','___')
            fileName = fileName.replace(':','____')
            fileName = fileName.replace('?','_____')
            fileName = fileName.replace('&','_______')
            fileName = fileName.replace('%','________')
            fileName = fileName[0:120]
            relativeDir = self.__getDomainName()
            if isAbsolutPath :
                saveDir = os.getcwd() + '/' + relativeDir
                try :
                    if os.path.exists(saveDir) == False:
                        os.makedirs(saveDir)
                    savePath = saveDir + '/' + fileName + '.html'
                except Exception as e:
                    savePath = False
                    print(str(e))
            else :
                savePath = relativeDir + "/" + fileName + '.html'
            return  savePath
            pass

    def getPageFileName(self, url):

        fileName = ""
        if isinstance(url, str) :
            url = url.replace("http://","")
            url = url.replace("https://","")
            arr = url.split('/')
            index = len(arr) - 1
            name = arr[index]
            fileName = (name + '.html') if  name != "" and name.find('.')== -1 else name

            prex = '_'.join(arr[0:index])
            fileName = prex + '_' + fileName
            domainName = self.__getDomainName()
            if fileName.find(domainName) != -1 :
                fileName = fileName.replace(domainName + "_", "")
            elif fileName[0] == "_" :
                fileName = fileName[1:(len(fileName))]


        if fileName == "" :
            fileName = 'index.html'

        return  fileName

    def __getDomainName(self):
        name = ""
        if isinstance(self.domain, str):
            arr = self.domain.split('/')
            index = len(arr) - 1
            name = arr[index]
        return name
    pass


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
                    != False \
                    or url.find('mailto:') != -1 \
                    or url.find('qq.com') != -1 \
                    or url.find('baidu.com') != -1 \
                    or url.find('javascript:;') != -1 :
                self.urlList.remove(url)
            else :
                tmpList.append(url)
        uniqueList = []
        [uniqueList.append(i) for i in tmpList if not i in uniqueList]
        self.urlList = uniqueList
        pass

    def saveHtmlFiles(self):
        # 2. 抓取所有提取到的html文件并保存到本地
        if len(self.urlList) > 0 :

            level = SiteSpider.getLevel()
            if level < 4 :

                SiteSpider.setLevel(level + 1)
                for url in self.urlList :

                    oldUrl = url
                    #下载页面
                    try :
                        spider = SiteSpider(self.domain, spiderChildLevel=True)
                        if(url.find(self.domain) == -1 and url[0:3] != "http") :
                            url = self.domain + '/' + url  if  url[0] != '/' else self.domain + url
                        result = spider.run(url)
                        if result != False and spider.htmlContent == "" :
                            self.urlList.remove(oldUrl)
                    except Exception as e:
                        (self.urlList).remove(oldUrl)
                        print("faild url:", oldUrl)

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
    domain = "http://chongwumoban.s5.cn.vc"
    SiteSpider.setLevel(SiteSpider.getLevel()+1)
    spider = SiteSpider("http://chongwumoban.s5.cn.vc", spiderChildLevel=True)
    spider.run()
    # spider.run("http://chongwumoban.s5.cn.vc/fuwu")

