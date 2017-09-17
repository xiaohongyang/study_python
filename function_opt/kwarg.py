import re

def say(name,*args):
    print("我是%s" %  (name))
    for arg in args:
        print(arg)

def say02(name, **kwargs):
    print("我是%s" % (name))
    for key in kwargs:
        print("key:%s" % (key))

def say03(name,name2='hihi', *args, **kwargs):
    print("我是%s" % (name))
    for arg in args:
        print(arg)

    for key in kwargs:
        print("key:%s" % (key))

    print( args[1])
    print(kwargs.get('c'))

say("肖红阳","1","2","3",{'a':333,'b':'44'})

import sys

cssList = []
htmlString = '''
<link href="http://bk.st.styleweb.com.cn/editor/??do-basic.css,do-layout.css,do-form.css,do-element.css,element/do-tabText.css,js/wow/animate.css?201791601326" rel="stylesheet" type="text/css"/><link href="http://bk.st.styleweb.com.cn/editor/??do-basic.css,do-layout.css,do-form.css,do-element.css,element/do-tabText.css,js/wow/animate.css?2017916013263" rel="stylesheet" type="text/css"/>
'''


cssRe = re.compile('http')
matchGroup = cssRe.match( htmlString)

print('matchGroup:')
print(matchGroup)

print(cssList)

line = "Cats are smarter than dogs"

matchObj = re.search(r'(.*?) .*?', line, re.M | re.I)

if matchObj:
    print(
    "matchObj.group() : ", matchObj.group())
    print(
    "matchObj.group(1) : ", matchObj.group(1))
    print(
    "matchObj.group(2) : ", matchObj.group(2))
else:
    print(
    "No match!!")


exit()
say02("jack", age='10', theClass='二级')

say03("xiao",3,4,5, a=3,b=4,c=5)