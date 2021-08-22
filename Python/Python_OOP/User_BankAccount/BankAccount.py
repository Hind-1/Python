class BankAccount:
    def __init__(self,int_rate,balance = 20):
        self.int_rate= int_rate
        self.balance=balance
    def deposite (self,amount):
        self.balance+=amount
        return self
    def withdraw(self,amount):
        if(self.balance<amount):
            print("Insufficient funds: Charging a $5 fee")
        else:
            self.balance-=amount
        return self

    def display_account_info (self):
        print(self.balance)
        return self

    def yield_interest(self):
        self.balance *=1 + self.int_rate
        return self