# from bank import Bank

class User:
    def __init__(self, account_num, name, email, address, account_type):
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

        def withdraw(self,amount,bank):
            if amount > self.balance:
                if bank.total_balance < amount:
                    print(f"The Bank is Bankrupt")
                else:
                    print(f"Withdrawal amount exceeded")
            elif amount <= 0:
                print(f"Invalid Amount")
            else:
                self.balance -= amount
                self.transaction.append(f"Withdrawed: {amount}")
                print(f"Withdrwed {amount} Successfully!!! & New Balance is {self.balance}")

        def take_loan(self,amount,bank):
            if bank.loan_on:
                if self.loan < 2:
                    self.balance += amount
                    bank.total_loan += amount
                    self.loan += 1
                    self.transaction.append(f"Loan Taken {amount} Successfully!!!")
                else:
                    print(f"You Can't Take Loan Anymore")
            else:
                print(f"Loan Feature is OFF")

        def transfer_money(self,amount,onno_account,bank):
            if amount > self.balance:
                print(f"Sorry, You Don't Have Enough Money")

            elif onno_account not in bank.account:
                print(f"Acoount Doesn't Exist")

            else:
                self.balance -= amount
                bank.account[onno_account].balance += amount
                self.transaction.append(f"Transfered {amount} Successfully To {onno_account}")
                
        def transaction_history(self):
            if self.transaction:
                for transactions in self.transaction:
                    print(f"Transactioned History: ")
            else:
                print(f"No Transaction Found")





        