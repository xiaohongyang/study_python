import urllib
import urllib
import urllib.request
import urllib.parse
import project.tools.spider.spider
from bs4 import BeautifulSoup
 
# get the proxy
of = open('proxy.txt', 'w')
for page in range(1,50):
    url = 'http://www.xicidaili.com/nn/%s' %page
    user_agent = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
    request = urllib.request.Request(url)
    request.add_header("User-Agent", user_agent)
    content = urllib.request.urlopen(request)
    soup = BeautifulSoup(content, 'html.parser')
    trs = soup.find('table', {"id":"ip_list"}).findAll('tr')
    for tr in trs[1:]:
        tds = tr.findAll('td')
        ip = tds[2].text.strip()
        port = tds[3].text.strip()
        protocol = tds[6].text.strip()
        if protocol == 'HTTP' or protocol == 'HTTPS':
            of.write('%s=%s:%s\n' % (protocol, ip, port))
            print('%s://%s:%s' % (protocol, ip, port))