#统计原价和折后总价
# 一家商场在降价促销。 如果购买金额低于或等于 10 元，会给 10% 的折扣，
# 如果购买金额大于 10元，会给 20% 的折扣。编写一个程序，询问购买价格，
# 再显示折扣( 10% 或 20%) 和最终价格。
import easygui

pointLevel01 = 0.1
pointLevel02 = 0.2

moneyLevel01 = 10
moneyLevel02 = 20

goods = ['苹果','香蕉','桃子']
prices = [5,15,30]
totalPrice = saleTotalPrice = 0

selectedArr = []

for item in goods:
    selected = easygui.choicebox("请选择您要买的水果","请选择", choices=goods)
    if None != selected:
        selectedArr.append(selected)

string = "";
for item in selectedArr:
    itemPrice = prices[goods.index(item)]


    if itemPrice >= moneyLevel02:
        saleMoney = itemPrice * (1-pointLevel02)
    elif itemPrice >= moneyLevel01:
        saleMoney = itemPrice * (1-pointLevel01)
    else:
        saleMoney = itemPrice

    saleTotalPrice += saleMoney
    totalPrice += itemPrice

    string += (item + ":" + str(itemPrice) + "("+ str(saleMoney) +") \r\n")


message = "原价总需要:" + str(totalPrice)+";折后价只需要:" + str(saleTotalPrice) + "\r\n" + string
easygui.msgbox(message)

