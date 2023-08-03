
"""

Bank Account Assignment
The class should also have the following methods:

deposit(self, amount) - increases the account balance by the given amount
withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
display_account_info(self) - print to the console: eg. "Balance: $100"
yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
This means we need a class that looks something like this:

class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        # your code here
    def withdraw(self, amount):
        # your code here
    def display_account_info(self):
        # your code here
    def yield_interest(self):
        # your code here
"""

class Bank_Account:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print("Insufficient funds: Charging a $5 fee will deduct $5")
            self.balance = self.balance - 5
        return self

    def displayAccountInfo(self):
        print(f"Balance: ${self.balance}")

    def yieldInterest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        else:
            print("You have a negative account balance.")
        return self

User1 = Bank_Account()
User2 = Bank_Account()

User1.displayAccountInfo()

User1.deposit(10).deposit(10).deposit(100).withdraw(50).yieldInterest().displayAccountInfo()
User2.deposit(30).deposit(30).withdraw(20).withdraw(20).withdraw(100).withdraw(50).yieldInterest().displayAccountInfo()





