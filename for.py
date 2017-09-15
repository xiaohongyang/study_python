#fn: 决策树
"""
for循环
"""
#*******
#多行注释
#*******

choices = ["鸡蛋", "苹果", "香蕉", "白菜"]

k=0
options = [0, 1]

for i in options:   #是否选择鸡蛋
    for j in options:
        for i2 in options:
            for i3 in options:
                for i4 in options:
                    print( i, j, i2, i3, i4)

dict(((i,i) for i in range(10)))
exit();
for looper in range(10,-10,-1):
    print( str(10) +"*"+ str(looper) +"="+ str(10*looper))

