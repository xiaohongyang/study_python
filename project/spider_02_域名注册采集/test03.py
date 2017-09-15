import traceback
import urllib
import urllib
import urllib.request
import urllib.parse

import threading

inFile = open('proxy.txt', 'r')
outFile = open('available.txt', 'w')
url = 'http://www.lindenpat.com/search/detail/index?d=CN03819011@CN1675532A@20050928'
url = 'http://panda.www.net.cn/cgi-bin/check.cgi?area_domain=aa.com'
lock = threading.Lock()


def test():
    lock.acquire()
    line = inFile.readline().strip()
    lock.release()
    # if len(line) == 0: break
    protocol,proxy = line.split('=')
    cookie = "PHPSESSID=5f7mbqghvk1kt5n9illa0nr175; kmsign=56023b6880039; KMUID=ezsEg1YCOzxg97EwAwUXAg=="
    try:
        proxy_support = urllib.request.ProxyHandler({protocol.lower():'://'.join(line.split('='))})
        opener = urllib.request.build_opener(proxy_support, urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        request = urllib.request.Request(url)
        request.add_header("cookie",cookie)
        content = urllib.request.urlopen(request,timeout=4).read()
        if len(content) >= 30:
            lock.acquire()
            print('add proxy', proxy)
            outFile.write('\"%s\",\n' %proxy)
            lock.release()
        else:
            print('出现验证码或IP被封杀')
    except Exception as err:
        print(traceback.format_exc())
all_thread = []
for i in range(500):
    t = threading.Thread(target=test)
    all_thread.append(t)
    t.start()

for t in all_thread:
    t.join()

inFile.close()
outFile.close()