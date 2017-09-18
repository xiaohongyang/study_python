import os;
import types
from project.tools.spider.spider_text import *
from  pathlib import Path;
from project.spider_enterprise_site.spider.SpiderCssFile import SpiderCssFile
import re


class SiteSpider :

    cssRe = [
        re.compile(r'link[^"]+href="([^"]+)"', re.I),
        re.compile(r'link[^\']+href=\'([^\']+)\'', re.I)
    ]
    cssDir = "static_source/css"
    htmlContent = ""

    def __init__(self, domain, indexPage=""):

        self.domain = domain
        self.indexPage = indexPage if indexPage==None else ""
        self.savePath = os.getcwd() + "/" + self.__getDomainName()
        self.__checkAndCreateSaveDir()


    def __checkAndCreateSaveDir(self):
        if os.path.exists(self.savePath) == False :
            os.makedirs(self.savePath)


    def run(self):

        self.__spiderIndex()


    def __spiderIndex(self):
        # 抓取首页
        indexPage = self.__getIndexPage()
        self.__spiderPage(indexPage)
        pass

    def __spiderPage(self, url):

        # 抓取页面
        # 1.抓取html
        self.__spiderHtml(url)

        # 2.抓取css
        self.__spiderCss(self.htmlContent)

        # 3.抓取js
        self.__spiderJs(url)

        self.__saveHtml(url)

    def __spiderHtml(self, url):
        # 抓取html

        try:
            spider = SpiderText(url)
            fileName = self.__getPageFileName(url)
            filePath = self.savePath + "/" + fileName
            spider.setUrlContent(url)
            self.__updateContent(str(spider.content, 'utf-8'))
        except Exception:
            print(Exception.__str__())
            pass;

    def __saveHtml(self, url):
        try:
            spider = SpiderText()
            fileName = self.__getPageFileName(url)
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
        cssDir = self.savePath +  '/' +'static_source/css'
        spiderText = SpiderText()
        spiderCss = SpiderCssFile(htmlContent, self.cssRe, self.cssDir)
        spiderCss.run()
        self.__updateContent(spiderCss.content)
        pass

    def __updateContent(self, content):
        self.htmlContent = content

    def __spiderJs(self, url):
        #抓取js
        pass

    def __getIndexPage(self):
        # 获取首页地址
        indexPageUrl = self.domain +  "/" + self.indexPage
        return  indexPageUrl

    def __getPageFileName(self,url):

        fileName = ""
        if isinstance(url, str) :
            arr = url.split('/')
            index = len(arr) - 1
            name = arr[index]
            fileName = (name + '.html') if  name != "" and name.find('.')== -1 else name

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

