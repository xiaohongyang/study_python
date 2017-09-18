import os;
import types
from project.tools.spider.spider_text import *
from  pathlib import Path;
from project.spider_enterprise_site.spider.SpiderCssFile import SpiderCssFile
from project.spider_enterprise_site.spider.SpiderJsFile import SpiderJsFile
from project.spider_enterprise_site.spider.SpiderImageFile import SpiderImageFile
from project.spider_enterprise_site.spider.SpiderHtmlFile import SpiderHtmlFile
import re


class SiteSpider :

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

    def __init__(self, domain, indexPage=""):

        self.domain = domain
        self.indexPage = indexPage if indexPage==None else ""
        self.savePath = os.getcwd() + "/" + self.__getDomainName()
        self.__checkAndCreateSaveDir()


    def __checkAndCreateSaveDir(self):
        if os.path.exists(self.savePath) == False :
            os.makedirs(self.savePath)


    def run(self,url=''):

        self.__spiderSpecialPage(url)


    def __spiderSpecialPage(self, url=''):
        # 抓取首页
        if url=='' :
            indexPage = self.__getPageName()
            self.__spiderPage(indexPage)
            #抓取首页下面的所有一级页面
            self.level += 1
            # self.__spiderJumpHtml(self.htmlContent)
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

        self.__saveHtml(url)

    def __spiderHtml(self, url):
        # 抓取html

        try:
            spider = SpiderText(url)
            fileName = self.getPageFileName(url)
            filePath = self.savePath + "/" + fileName
            spider.setUrlContent(url)
            self.__updateContent(str(spider.content, 'utf-8'))
        except Exception:
            print(Exception.__str__())
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
            if fileName.index(domainName) != None :
                fileName = fileName.replace(domainName + "_", "")


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


if __name__ == '__main__' :
    domain = "http://chongwumoban.s5.cn.vc"
    spider = SiteSpider("http://chongwumoban.s5.cn.vc")
    spider.run()
    # spider.run("http://chongwumoban.s5.cn.vc/fuwu")

