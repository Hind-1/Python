class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 10
#  have this method decrease the user's balance by the amount specified.
    def make_withdrawal(self, amount):
        self.account_balance -= amount
#  have this method increase the user's balance by the amount specified.
    def deposite(self,amount):
        self.account_balance += amount
# have this method decrease the user's balance by the amount and add that amount to other other_user's balance
    def transfer_money(self,other_user, amount):
        self.account_balance -= amount
        other_user.deposite(amount)
#  have this method print the user's name and account balance to the terminal
    def display_user_balance(self):
        print(self.name,self.email,self.account_balance)
User1 =User('Hind','Hindwer@gmail.com')
User2 =User('Hend','Hendwer@gmail.com')
User2.transfer_money(User1,10)
User1.display_user_balance()
User2.display_user_balance()