
class BankAccount1:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        elif self.balance > 100:
            self.balance += self.int_rate
        return self
    def display_account_info(self):
        print("\n", "-"*10)
        print(f"\nAccount balance is: {self.balance}")
        return self

class BankAccount2:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < amount:
            print("\nInsufficient funds: Charging a $10 fee")
            self.balance -= 10
        elif self.balance > 100:
            self.balance += self.int_rate
        return self
    def display_account_info(self):
        print(f"\nAccount balance is: {self.balance}")
        return self

class User:
    def __init__(self, first_name, last_name, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email_address
        self.account1 = BankAccount1(int_rate=0.02, balance=0)
        self.account2 = BankAccount2(int_rate=0.01, balance=0)

Joel = User("Joel", "Okoh", "eazjay@gmail.com")
Joel.account1.deposit(150).display_account_info()
Joel.account2.withdraw(105).display_account_info()
Joel.account2.deposit(100).display_account_info()
Joel.account1.withdraw(20).display_account_info()