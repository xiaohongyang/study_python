class Person():

    def __init__(self):
        self.name = "蜡台 "
        print("init ...")

    @property
    def name(self):
        return  self._name

    @name.setter
    def name(self,value):
        self._name = value

    @name.getter
    def name(self):
        return  self._name

    @staticmethod
    def sayHello(message):
        print(message)


    @classmethod
    def introduce(cls,message):
        cls.sayHello(message)


    def say(self,message):
        self.sayHello(message)



p = Person()
Person.sayHello("Hi 您好")
Person.introduce("HOHO")
p.say(message="什么")
p.say(message=p.name)


def testFlask(startMsg, endMsg):
    def ret(f):
        def wrapper():
            print(startMsg)
            f()
            print(endMsg)
        return wrapper
    return ret

@testFlask("start ok", "end ok")
def hello():
    print('Hello')

hello()

class Flask():
    def __init__(self):
        self.routers = {}
    def route(self, path):
        def decorator(f):
            self.routers[path] = f
            return  f
        return decorator

    def server(self,path):
        viewFunction = self.routers.get(path)
        if viewFunction:
            return viewFunction()
        else :
            raise ValueError('Route "{}"" has not been registered', format(path))


app = Flask()

@app.route("/")
def Hello():
    print("Hello")






