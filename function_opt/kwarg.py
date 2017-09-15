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

say02("jack", age='10', theClass='二级')

say03("xiao",3,4,5, a=3,b=4,c=5)