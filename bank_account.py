import random
random_account = str(random.randrange(10000000, 99999999,1))

class BankAccount:
    def __init__(self, full_name:str , account_type: str, account_number = random_account, balance: int = 0) -> None:
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited: ${amount} new balance ${self.balance}")

    def withdraw(self, amount):
        if(self.balance < amount):
            print("Insufficient funds.")
            self.balance = self.balance - 10
        else:
            self.balance -= amount
            print(f"Amount withdrawn: ${amount} new balance: ${self.balance}")

    def get_balance(self):
        print(f"Hello {self.full_name} your current balance is: ${self.balance}")
        return self.balance
    
    def add_interest(self):
        if(self.account_type == 'savings'):
            self.balance*=1.1
        else:
            self.balance *=1.00083

    def print_statement(self):
        output = f"{self.full_name}\nAccount No.: {self.account_number}\nBalance: ${self.balance}"
        print(output)


account_one = BankAccount('Mitchell', 'checking','03141582')
account_one.deposit(400000)
account_one.print_statement()
account_one.add_interest()
account_one.withdraw(150)
account_one.print_statement()