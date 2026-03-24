from abc import ABC, abstractmethod


class Bank(ABC):
    def __init__(self, bank_name, branch_name, ifsc_code, location):
        self.bank_name = bank_name
        self.branch_name = branch_name
        self.ifsc_code = ifsc_code
        self.location = location

    @abstractmethod
    def display_account_details(self):
        pass


class account_holder(Bank):
    def __init__(self, account_holder_name, account_number, account_type, balance):
        super().__init__("SBI", "karur Branch", "SBIN0001234", "karur")
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

    def display_account_details(self):
        print("Account Holder Name:", self.account_holder_name)
        print("Account Number:", self.account_number)
        print("Account Type:", self.account_type)
        print("Balance:", self.balance)


a1 = account_holder("Rathi", 1234567890, "Savings", 5000)
a1.display_account_details()
print(a1.bank_name)
print(a1.branch_name)
print(a1.ifsc_code)
print(a1.location)
