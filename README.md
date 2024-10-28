# Bank Account Assignment

## Description
This assignment highlights the use of object oriented programming in Python. It features two classes: `BankAccount`, which creates an individual bank account, and `Bank`, which holds multiple accounts as a list. Through `Bank`, a user can create an individual `BankAccount` and then perform different actions such as deposit, print statements, and transfer. In `Bank` a user needs to supply a account number to interact with the accounts. The assignment also makes use of user generated input in the `application.py` file. 

## How to Run this Program

### 1. `bank_account.py`
**Instantiate a `BankAccount` class:**
```
account = BankAccount(full_name, account_type, account_number, balance)
```
**Arguments**
- full_name: str 
- account_type: str = 'checking' | 'savings' (default)
- account_number: str = Random Eight Digit Number (default)
- balance: int = 0 (default)

**Run the file:**
```
python3 bank_account.py
```
### 2.  `application.py`

**Run the file:**
```
python3 application.py
```
### 3. `bank.py`
**Instantiate a `Bank` class:** 
```
bank = Bank()

# Example Usage
bank.create_account(full_name, account_number, balance, account_type)
bank.statement(account_number)
bank.transfer(amount, account_to_withdraw, account_to_deposit)
bank.deposit(amount, account_number)
bank.withdraw(amount, account_number)
```
**Arguments**
- full_name: str 
- account_type: str = 'checking' | 'savings' (default)
- account_number: str = Random Eight Digit Number (default)
- amount: int
- balance: int = 0 (default)
- account_to_withdraw: str
- account_to_deposit: str

**Run the file:**
```
python3 bank.py
```