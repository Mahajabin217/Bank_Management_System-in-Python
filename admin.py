from bank import Bank
"""
class Admin(Bank):
    def create_account(self, name, email, address, account_type):
        super().create_account(name, email, address, account_type)

    def delete_account(self, account_num):
        super().bank.delete_account(account_num)

    def show_all_user_accounts(self):
        super().bank.show_all_user_accounts()

    def total_available_balance(self):
        super().bank.total_available_balance()

    def total_loan_amount(self):
        super().bank.total_loan_amount()

    def loan_feature(self):
        super().bank.loan_feature() """

class Admin:
    def __init__(self,bank):
        self.bank = bank

    def create_account(self, name, email, address, account_type):
        return self.bank.create_account(name, email, address, account_type)

    def delete_account(self, account_num):
        self.bank.delete_account(account_num)

    def show_all_user_accounts(self):
        self.bank.show_all_user_accounts()

    def total_available_balance(self):
        self.bank.total_available_balance()

    def total_loan_amount(self):
        self.bank.total_loan_amount()

    def loan_feature(self):
        self.bank.loan_feature()