import re
class BaseSpider:

    def __init__(self):
        pass

    # 获取外网访问url地址
    @staticmethod
    def getWebUrl(url, domain, directory):

        if(len(url) > 3 and url[:2] == "//"):
            url = url.replace(url[:2], "http://")
        r = re.compile('^http.*',re.I)
        if r.match(url) == None and url[0:1] != '/':
            url = domain + directory + url
        elif r.match(url) == None :
            url = domain + url
        return  url
    pass