class Account:
    def __init__(self,account_name, account_number,balance,account_type):
        self.account_name=account_name
        self.account_number=account_number
        self.balance=balance
        self.account_type=account_type
        
    def deposit(self,deposit):
        self.deposit=deposit
        self.balance += self.deposit
        return f"Your balance is {self.balance}"
    
    def withdraw(self, withdraw):
        self.withdraw=withdraw
        self.balance-=self.withdraw
        return f"Your balane is {self.balance}"