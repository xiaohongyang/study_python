

class MyExeption(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


try:
    raise MyExeption("出错了sss")
except MyExeption:
    print(MyExeption.value)



print(321)

def add(a,b):
    return  a+b

print(add(3,2))

def add(c,d):
    return  c+d+12;

print(add(3,2))

exit()
import re;
import sys;
import urllib
import urllib.request
import easygui

#列表分片 [x:y]
a = ['a','b','c','d','e']

#列表分片

a.append("333");
a.extend(["444" ])
#插入元素
a.insert(0,88)
#判断元素是否存在
if(88 in a):
    print(88,'存在')
print(a.index(88))
#删除元素
a.remove(88)
print(a)
#list排序
list_b = a[:]
list_b.sort()
#list倒序排列
list_b.sort(reverse=True)
print(list_b)
#sorted()方法
newer = sorted(list_b)
print(newer)
print(list_b)

#不可改变列表 用()定义
a = ("空","了","无")
for item in a:
    print(item)

print(a[1])
#双重列表

b= [1,2,3]
for i in range(3):
    b[i]=[1,2]
    for j in range(2):
        b[i][j] = str(i) + str(j)
print(b)

if '11' in b[1]:
    print(b[1])

age = 1
def printMyAddress(someName, houseNum):
    global age;
    age = 3;
    print(someName)
    print("江苏省")
    print("苏州市")
    print("相城区")
    print(houseNum)
    print("age:",age)

printMyAddress(houseNum=388,someName="肖红阳")
print(age)

def printName(name):

    x = 11
    y = 6

    frame = '''
   *    *    *
     *  *  *
        *
   *  *  *  * *
   *          *
   *  *  *  * *
   *  *  *  * *
   *        * *
   *          *
    '''
    print(frame)

def printPersonInfo(info):

    if len(info) < 2:
        return False

    print(info[1])


printName("A")
printPersonInfo(['a','v'])

class Ball:

    def __init__(self):
        self.direction = "down"
    def bounce(self):
        if self.direction == "down":
            self.direction = "up"
    def __str__(self):
        return  "3333"

ball = Ball()
print(ball.direction)
Ball.bounce(ball)
#ball.bounce()
print(ball.direction)
a = print(ball)
print(a)
exit();
# f = open('text.txt','r');
# for eachLine in f:
#    print(re.split(r'\s\s+',eachLine))
# f.close()


# f = open('text.txt', 'r', -1, 'utf-8');
#
# for eachLine in f:
#    print(re.split(r'\s+',eachLine));
# f.close();

a = b = 3
print(a,b)
b = 9
print (a, b)
print("a"+"3"+"a")
a = """
hi
Hello
你好
"""

print(a)


# filevv = urllib.request.urlretrieve("http://onedesk.adsage.com",'index.html')
# page = urllib.request.urlopen("http://zhidao.baidu.com/link?url=hdu03NVxOKcRGNRl6iWLlNLx6bYkZAkwN_-1mbYTd5uJDzfzuXOPf8915b9t4VimhtciZo-yskkTKtqmKwDvsYgmrk8F0oFRpLIA9kkRfle")
# html = page.read()
# print( html )
#
# urllib.request.urlretrieve("http://zhidao.baidu.com/link?url=hdu03NVxOKcRGNRl6iWLlNLx6bYkZAkwN_-1mbYTd5uJDzfzuXOPf8915b9t4VimhtciZo-yskkTKtqmKwDvsYgmrk8F0oFRpLIA9kkRfle","index.txt")

response = easygui.msgbox("你好,Xiao!","Hello!", "确定");
print(response)

flavor = easygui.buttonbox("您喜欢哪种菜?","选择菜品",choices=["牛肉",'猪肉','鸡蛋'],default_choice='猪肉')
easygui.msgbox("您选择的是"+flavor)

flavor = easygui.choicebox("您喜欢哪种菜?", "选择菜品", choices=["牛肉","猪肉","鸡蛋"]);
easygui.msgbox("您选择的是"+flavor)