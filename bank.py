from bank_account import BankAccount

# Stretch Goal 4
class Bank:
    def __init__(self) -> None:
        self.accounts = list()

    def create_account(self, full_name, account_number, balance, account_type):
        if(balance == ''):
            balance = 0
        if(account_type == ''):
            account_type = 'savings'    
        if(account_number == ''):
            account = BankAccount(full_name, account_type, balance=balance)
        else:
            account = BankAccount(full_name, account_type, account_number, balance)

        self.accounts.append(account)
        print(f"Your new account number is: {account.account_number}")
        print('Bank accounts:', self.accounts)
        return self.accounts
    
    def find_account(self, account_number):
        for account in self.accounts:
            if(account_number == account.account_number):
                return account
        print(f"Account number {account_number} not found.")  
        return None

    def deposit(self, amount, account_number):
        account_to_deposit = self.find_account(account_number)
        if(account_to_deposit):
            account_to_deposit.balance += amount
            print(f"Amount deposited: ${amount} new balance ${account_to_deposit.balance}")
        else:
            print("Account not found.")

    def withdraw(self, amount, account_number):
        account_to_withdraw = self.find_account(account_number)
        if(account_to_withdraw):
            if(account_to_withdraw.balance < amount):
                account_to_withdraw.balance -= 10
                print(f"Insufficient funds. $10 overdraft fee applied, new balance ${account_to_withdraw.balance}")
                return True
            account_to_withdraw.balance -= amount
            print(f"Amount withdrawn: ${amount} new balance ${account_to_withdraw.balance}")
        else:
            print("Account not found.") 

    def transfer(self, amount, account_number_withdrawal, account_number_deposit):
        account_to_withdraw = self.find_account(account_number_withdrawal)
        account_to_deposit = self.find_account(account_number_deposit)
        
        if(account_to_withdraw and account_to_deposit): 
            is_overdrawn = self.withdraw(amount, account_number_withdrawal)
            if(not is_overdrawn):
                self.deposit(amount, account_number_deposit)
            else:
                print('Transaction cannot be completed') 
        else:
            if not account_to_withdraw:
                print(f"Account {account_number_withdrawal} not found.")
            if not account_to_deposit:
                print(f"Account {account_number_deposit} not found.")

    def statement(self, account_number):
        account = self.find_account(account_number)
        if(account):
            output = f"{account.full_name}\nAccount No.: {account.account_number}\nBalance: ${account.balance}"
            print(output)
        else:
            print("Account not found.") 

bank = Bank()
bank.create_account('xica', '1', 100, 'checking')
bank.create_account('blerep', '2', 100, 'checking')
bank.statement('1')
bank.statement('2')
bank.transfer(10, '1', '2')
