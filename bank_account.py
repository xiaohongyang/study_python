class BankAccount:
    def __init__(self,name,account,accountMoney=0):
        self.name = name
        self.account = account
        self.accountMoney = accountMoney

    def showAccountMoney(self):
        print("当前余额为:",self.accountMoney)

    def recharge(self, amount):
        # 充值
        if amount>0:
            self.accountMoney += amount
    def cash(self, amount):
        # 取款
        if amount <= self.accountMoney:
            self.accountMoney -= amount

class InterestAccount(BankAccount):
    def __init__(self,name, account):
        BankAccount.__init__(self,name, account)

    def addInterest(self):
        self.accountMoney = self.accountMoney + self.accountMoney*0.1