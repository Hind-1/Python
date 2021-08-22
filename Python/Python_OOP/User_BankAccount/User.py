from BankAccount import BankAccount
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
        self.account = BankAccount(int_rate=0.02, balance=0)
#  have this method decrease the user's balance by the amount specified.
    def make_withdrawal(self, amount):
        self.account.balance  -= amount
#  have this method increase the user's balance by the amount specified.
    def deposite(self,amount):
        self.account.balance  += amount
# have this method decrease the user's balance by the amount and add that amount to other other_user's balance
    def transfer_money(self,other_user, amount):
        self.account.balance  -= amount
        other_user.deposite(amount)
#  have this method print the user's name and account balance to the terminal
    def display_user_balance(self):
        print(self.name,self.email,self.account.balance)
User1 =User('Hind','Hindwer@gmail.com')
User2 =User('Hend','Hendwer@gmail.com')
User1.display_user_balance()
User2.display_user_balance()