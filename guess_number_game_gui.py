#一个GUI猜数字的小游戏

import sys
import easygui
from random import randint

rightNumber = randint(0,100)
guessTime = chanceTime = 10


easygui.msgbox("游戏开始:请输入您猜到的数字!(提示：范围在0-100之间),点击确定按钮开始!"+"您有"+str(chanceTime)+"次机会!"
               ,title="猜数游戏,开发语言:Python"
               ,ok_button="确定");

while(guessTime > 0):
    number = easygui.integerbox("输入数字:","ff")
    number = int(number)
    if number > rightNumber :
        easygui.msgbox("这个数字太大咯!")
    elif number < rightNumber:
        easygui.msgbox("这个数字太小咯")
    else:
        easygui.msgbox("恭喜您,您只用了"+str(chanceTime-guessTime)+"次就猜对咯！大神啊!")
        exit()
    guessTime -= 1


easygui.msgbox(str(chanceTime)+"次机会用完,失败了……")


