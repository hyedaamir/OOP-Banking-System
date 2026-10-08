# OOP Banking System
# Day 13-16 - Classes, Objects and Encapsulation
class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.__balance = balance

    def deposit(self, amount ):
        if amount > 0:
            self.__balance += amount
            print(f"Rs. {amount} deposited successfully.")
        else:
            print("Please enter a valid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Please enter a valid amount.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Rs. {amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Current Balance: Rs. {self.__balance}")

    def show_account(self):
        print("\nAccount Details: ")
        print(f"Account Holder : {self.account_holder}")
        print(f"Account Number : {self.account_number}")
        print(f"Balance       : Rs. {self.__balance}")
account = BankAccount("Hyeda", "1001", 5000)
print("Banking System ")

account.show_account()

print("\n Deposit: ")
account.deposit(2000)

print("\nWithdraw: ")
account.withdraw(1000)

print("\nBalance ")
account.check_balance()

print("\n Final Account Details: ")
account.show_account()