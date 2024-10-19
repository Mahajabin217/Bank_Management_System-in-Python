from user import User

class Bank:
    def __init__(self):
        self.account = {}
        self.total_balance = 0
        self.total_loan = 0

    def create_account(self, name, email, address, account_type):
        print(f"{account_num} is Created Successfully!!!")

    def delete_account(self, account_num):
        print(f"{account_num} is Deleted Successfully!!!")

    def show_all_user_accounts(self,account):
        print(f"Account: {account.account_num}, Name: {account.name}")

    def total_available_balance(self):
        print(f"Total Available Balance is: {self.total_balance}")

    def total_loan_amount(self):
        print(f"Total Loan Amount: {self.total_loan}")

    def loan_feature(self):
        print(f"Loan Feature")
        
