import time, bank_account
#from bank_account import InterestAccount
from bank_account import *

class Game_object:
    def __init__(self, name):
        self.name = name
    def pickup(self):
        pass
        # put code here to add this object to the player's collection

class Coin(Game_object):
    def __init__(self,name, value):
        Game_object.__init__(self, name)
        self.value = value
    def spend(self, buyer, seller):
        pass
        # put code here to remove the coin from the buyer's money and add it to the buyer's money



coin = Coin("1元",5)
print(coin.name,":",coin.value)

jackAccount = InterestAccount("肖红阳", time.time())
jackAccount.recharge(588)
jackAccount.cash(8)
jackAccount.showAccountMoney()

jackAccount.addInterest()
jackAccount.showAccountMoney()