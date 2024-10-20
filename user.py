from bank import Bank

class User:
    def __init__(self, account_num, name, email, address, account_type) -> None:
        self.account_num = account_num
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.loan = 0
        self.transaction = []

        def check_balance(self):
            print(f"Available Balance: {self.balance}")

        def deposit(self,amount):
            if amount > 0:
                self.balance += amount
                self.transaction.append(f"Deposited: {amount}")
                print(f"Deposited {amount} Successfully!!! & New Balance is {self.balance}")
            else:
                print(f"Can't Found")

        def withdraw(self,amount):
            if amount > self.balance:
                print(f"Withdrawal amount exceeded")
            elif amount <= 0:
                print(f"Invalid Amount")
            else:
                self.balance -= amount
                self.transaction.append(f"Withdrawed: {amount}")
                print(f"Withdrwed {amount} Successfully!!! & New Balance is {self.balance}")

        def take_loan(self,amount):


        