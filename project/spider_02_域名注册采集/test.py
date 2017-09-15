import requests
import re

of = open('proxy.txt', 'w')
url = 'http://www.youdaili.net/Daili/guonei/3661'
for i in range(1,4):
    if i == 1:
        Url = url+'.html'
    else:
        Url = url+'_%s.html' %i
    html = requests.get(Url).text
    res = re.findall(r'\d+\.\d+\.\d+\.\d+\:\d+', html)
    for pro in res:
        of.write('http=%s\n' %pro)
        print(pro)
of.closed