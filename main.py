#import our class from funtion file
from BankAccount import BankAccount

print("Welcome to the Bank of Zehao!")
#we need. a name for our instance
customer_name = input("Please enter your name:\n")
account = BankAccount(customer_name)

#These are some new functions in our main file which will take value we input and process through the function we wrote in function file
def make_deposit(account):
    deposit_amount = float(input("How much would you like to deposit?\n"))
    account.deposit(deposit_amount)

def make_withdrawal(account):
    withdraw_amount = float(input("How much would you like to withdraw?\n"))
    account.withdraw(withdraw_amount)

def view_account_information(account):
    account.account_statement()

option = "5"#this is used to start our loop, it could be any umber out 

while option != "4":
    print("Please choose an option: ")
    print("1. Make a deposit\n2. Make a withdrawal\n3. View account information\n4. Quit")
    option = input("")
    #The code below is used to remind our customer input correct answer from 1-4, only they input correct opton that we can continue our function
    while option not in ['1','2','3','4']:
        option = input("Invalid choice. Please try again.\n")
    #here we just have to call function we wrote above, whihc can help our code look more clean
    if option == '1':
        make_deposit(account)
    elif option == '2':
        make_withdrawal(account)
    elif option == '3':
        view_account_information(account)
                
    

