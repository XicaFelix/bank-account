from bank_account import BankAccount

is_running = True
menu = '''
Please Choose an option:
1. Create Account
2. View Statements
3. Deposit
4. Withdraw
'''

def instatiate_account(full_name, account_number, balance, account_type):
    if(balance == ''):
        balance = 0
    if(account_type == ''):
        account_type = 'savings'    
    if(account_number == ''):
        account = BankAccount(full_name, account_type, balance=balance)
        return account
    else:
        account = BankAccount(full_name, account_type, account_number, balance)
        return account

    

while(is_running):
    account = ''
    print('Welcome to the bank')
    print(menu)
    user_action = input('->')
    match user_action:
        case '1':
            print('What is the full name associated with the account?')
            full_name = input('-> ')
            print('Please provide an eight digit account number, or one will be provided')
            account_number = input('-> ')
            print('''How much money will you fund the account with? 
                  Leave blank for an empty account''')
            balance = input('->')
            print('Is this a (1)checkings or (2)savings account? (Defaults to Savings)')
            account_type = input('-> ')
            account = instatiate_account(full_name=full_name, account_number=account_number, balance=balance, account_type=account_type)
        case '2':
        case '3':
        case '4':
        case _:
            
