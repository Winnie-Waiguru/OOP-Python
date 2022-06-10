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
        transaction=100
        if (amount+transaction)>self.balance:
            return f"Your balance is {self.balance}, you cannot withdraw the {amount}"
        elif (amount+transaction)<=0:
            return f"Amount must be greater than zero"
        else:    
            self.balance-=(amount +transaction)
            self.withdrawals.append(amount)
            return f"You withdrew {amount} and the transaction cost was {transaction}.Your new balane is {self.balance}"
        
    def deposits_statement(self):
        for depo in self.deposits:
            print(depo)
        
    def withdrawals_statement(self):
        for withdraws in self.withdrawals:
            print(withdraws) 
            
    def current_balance(self):
        balance=self.balance
        print("Your current balance is {balance}")        
           
         
               