from bank_account import BankAccount

is_running = True
return_to_menu = True
account = ''
bank = list()
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
    else:
        account = BankAccount(full_name, account_type, account_number, balance)

    bank.append(account)
    print(f"You new account number is: {account.account_number}")
    return bank

def find_account(bank):
    is_valid = False
    while not is_valid:
        print('What is the account number?')
        user_input = input('-> ')
        for account in bank:
            if account.account_number == user_input:
                is_valid = True
                return account
        print("Account not found. Please try again.")

print('Welcome to the bank')
while(is_running):
    print(menu)
    user_action = input('->')
    match user_action:
        case '1':
            print('What is the full name associated with the account?')
            full_name = input('-> ')

            print('Please provide an eight digit account number, or one will be provided')
            account_number = input('-> ')

            print('''
                  How much money will you fund the account with? 
                  Leave blank for an empty account''')
            balance = input('->')

            print('Is this a (1)checkings or (2)savings account? (Defaults to Savings)')
            account_type = input('-> ')

            instatiate_account(full_name=full_name, account_number=account_number, balance=balance, account_type=account_type)
        case '2':
            if(len(bank) > 0):
                account = find_account(bank)
                if(account != ''):
                    account.print_statement()

                    print('Would you like to conduct another transaction? Y/N')
                    is_running = True if input('-> ').lower() == 'y' else False
                else:
                    print('No account found, please try again')

            else:
                print('Whoops! You don\'t have an account.\n Please make an account before attempting this action')    
        case '3':
            if(len(bank) > 0):
                account = find_account(bank)
                if(account != ''):
                    account.print_statement()
                    print('How much would you like to deposit?')
                    deposit = int(input('-> '))
                    
                    account.deposit(deposit)

                    print('Would you like to conduct another transaction? Y/N')
                    is_running = True if input('-> ').lower() == 'y' else False
                else:
                    print('No account found, please try again')
            else:
                print('Whoops! You don\'t have an account.\n Please make an account before attempting this action')
        case '4':
                if(len(bank) > 0):
                    account = find_account(bank)
                    if(account != ''):
                        print('How much would you like to withdraw?')
                        withdrawl = int(input('-> '))

                        account.withdraw(withdrawl)

                        print('Would you like to conduct another transaction? Y/N')
                        is_running = True if input('-> ').lower() == 'y' else False
                    else:
                        print('No account found, please try again')
                else:
                    print('Whoops! You don\'t have an account.\n Please make an account before attempting this action')
        case _:
            print('Please select a valid option')

