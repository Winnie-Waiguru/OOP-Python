class Account:
    def __init__(self,account_name, account_number):
        self.balance=0
        self.account_name=account_name
        self.account_number=account_number
        self.deposits=[]
        self.withdrawals=[]

        
    def deposit(self,amount):
        if amount <=0:
            return f"Deposit amount should be more than zero"
        else:
            self.balance += amount
            self.deposits.append(amount)
            return f"You deposited {amount}.Your new balance is {self.balance}"
             
    
    def withdraw(self, amount):
        if amount>self.balance:
            return f"Your balance is {self.balance}, you cannot withdraw the {amount}"
        elif amount<=0:
            return f"Amount must be greater than zero"
        else:    
            self.balance-=amount
            self.withdrawals.append(amount)
            return f"You withdrew {amount}.Your new balane is {self.balance}"
        
    def deposits_statement(self):
        print(*self.deposits, sep="\n")
        
    def withdrawals_statement(self):
        print(*self.withdrawals, sep="\n")    