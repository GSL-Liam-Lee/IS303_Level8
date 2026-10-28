import random


class BankAccount:
    """Represents a simple bank account with a name, balance, and account number."""

    # Initialize the account with a customer name.
    # The starting balance is always zero when a new account is created.
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.account_number = random.randint(10000, 99999)

    # Add money to the account only when the deposit amount is positive.
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    # Remove money from the account only if the amount is valid and available.
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print(f"You balance is {self.balance}, please withdraw a valid amount!")

    # Display the account owner name, account number, and current balance.
    def account_statement(self):
        print(f"Name: {self.name}")
        print(f"Account number: {self.account_number}")
        print(f"Balance: ${self.balance:.2f}")
