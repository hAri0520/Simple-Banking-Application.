import random

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.acc_no = str(random.randint(100000, 999999))

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited to your account. \nNew balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return
        self.balance -= amount
        print(f"{amount} withdrawn from your account. \nNew balance: {self.balance}")

def show_menu():
    print("\n1. New Account Opening")
    print("2. Deposit money to account")
    print("3. Withdraw money from account")
    print("4. Show balance")
    print("5. Quit")

if __name__ == "__main__":
    accounts = {}
    while True:
        show_menu()
        choice = int(input('\nEnter the operation to be performed : '))
        
        if choice == 1:
            name = input('\nEnter the name for the new account: ')
            account = BankAccount(name)
            accounts[account.acc_no] = account
            print(f"\nNew account created for {name} with account number {account.acc_no}")
            
        elif choice == 2:
            acc_no = input('\nEnter the account number for depositing money: ')
            if acc_no in accounts:
                amount = int(input('Enter amount to be deposited: '))
                accounts[acc_no].deposit(amount)
            else:
                print("\nThere is no account with the given account number. Please enter the correct account number")
            
        elif choice == 3:
            acc_no = input('\nEnter the account number for withdrawing money: ')
            if acc_no in accounts:
                amount = int(input('Enter amount to be withdrawn: '))
                accounts[acc_no].withdraw(amount)
            else:
                print("\nThere is no account with the given account number. Please enter the correct account number")
            
        elif choice == 4:
            acc_no = input('\nEnter the account number for showing balance: ')
            if acc_no in accounts:
                print(f"\nThe balance for the account with account number {acc_no} is {accounts[acc_no].balance}")
            else:
                print("\nThere is no account with the given account number. Please enter the correct account number")
            
        elif choice == 5:
            print("\nThanks for banking with us")
            break
