from bank import Bank
from user import User
from admin import Admin

def user_op(user,bank):

    while True:
        print("\n___________ USER OPTION __________")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Take Loan")
        print("5. Transfer Money")
        print("6. Transaction History")
        print("7. Exit")

        op = int(input("Choose an Option: "))
        
        if op == 1:
            user.check_balance()

        elif op == 2:
            amount = int(input("Enter Deposit Amount: "))
            user.deposit(amount)

        elif op == 3:
            amount = int(input("Enter Withdraw Amount: "))
            user.withdraw(amount)

        elif op == 4:
            amount = int(input("Enter Loan Amount: "))
            user.take_loan(amount,bank)

        elif op == 5:
            onno_account = int(input("Enter a account number: "))
            amount = int(input("Enter Transfer Amount: "))
            user.transfer(onno_account,amount,bank)

        elif op == 6:
            user.transaction_history()

        elif op == 7:
            break

        else:
            print("INVALID OPTION")


def admin_op(admin):

    while True:
        print("\n___________ ADMIN OPTION __________")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. Show All Accounts")
        print("4. Check Total Balance")
        print("5. Check Total Loan Amount")
        print("6. Loan Feature")
        print("7. Exit")

        op = int(input("Enter an Option: "))

        if op == 1:
            name = input("Enter Your Name: ")
            email = input("Enter Your Email: ")
            address = input("Enter Your Address: ")
            account_type = input("Enter Your Account Type(Savings/Current): ")
            admin.create_account(name,email,address,account_type)

        elif op == 2:
            account_num = int(input("Enter Your Account NUmber: "))
            admin.delete_account(account_num)

        elif op == 3:
            admin.show_all_user_accounts()
        
        elif op == 4:
            admin.total_available_balance()

        elif op == 5:
            admin.total_loan_amount()
        
        elif op == 6:
            admin.loan_feature()
        
        elif op == 7:
            break

        else:
            print("INVALID OPTION")


def main(bank):
    # bank = Bank()
    admin = Admin(bank)

    while True:
        print("\n__________ WELCOME TO THE SONALI BANK _________")
        print("1. Admin")
        print("2. User")
        print("3. Exit")

        pos = input("Enter Your Position: ")

        if pos == "1":
            admin_password = input("Enter Admin Password: ")
            if admin_password == "@admin123":
                admin_op(admin)
            else:
                print("Incorrect Password")
        
        elif pos == "2":
            account_num = int(input("Enter Your Account Number: "))
            if account_num in bank.account:
                user = bank.account[account_num]
                user_op(user,bank)
            else:
                print("404 Not Found")

        elif pos == "3":
            break

        else:
            print("Try Again")

bank = Bank()
main(bank)           





                
