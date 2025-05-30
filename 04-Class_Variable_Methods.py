# Assignment 6, Question 4
# Class Variable and Class Methods

class Bank:
    
    bank_name = "Habib Bank Limited"
    
    def __init__(self, account_holder):
        self.account_holder = account_holder
    
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
    
    def show_details(self):
        print(f"\n- The Bank Name: {Bank.bank_name} | Account Holder: {self.account_holder}")
        
acc1 = Bank("Muhammad Shariq")
acc1.show_details()

Bank.change_bank_name("Allied Bank Limited")
acc1.show_details()