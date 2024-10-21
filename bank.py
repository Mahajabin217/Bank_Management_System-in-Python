from user import User
import random 

class Bank:
    def __init__(self):
        self.account = {}
        self.total_balance = 0
        self.total_loan = 0
        self.loan_on = True

    def create_account(self, name, email, address, account_type):
        account_num = random.randint(10000,99999)
        if account_type not in ['Savings','Current']:
            return "Invalid Account Type"
        
        user = User(account_num,name,email,address,account_type)
        self.account[account_num] = user

        print(f"{account_num} is Created Successfully!!!")
        return user

    def delete_account(self, account_num):
        if account_num in self.account:
            del self.account[account_num]
            print(f"{account_num} is Deleted Successfully!!!")
        else:
            print("Invalid Account")

    def show_all_user_accounts(self):
        if self.account:
            for user in self.account.values(): 
                print(f"Account: {user.account_num}, Name: {user.name}")
        else:
            print("Not Found")

    def total_available_balance(self):
        print(f"Total Available Balance is: {self.total_balance}")

    def total_loan_amount(self):
        print(f"Total Loan Amount: {self.total_loan}")

    def loan_feature(self):
        self.loan_on = not self.loan_on
        status = "ON" if self.loan_on else "OFF"
        print(f"Loan Feature is: {status}")
        
