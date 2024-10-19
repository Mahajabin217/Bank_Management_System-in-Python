class User:
    def __init__(self, account_num, name, email, address, account_type) -> None:
        self.account_num = account_num
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0

        