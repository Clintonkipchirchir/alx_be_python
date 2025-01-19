class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount
    
    def withdraw(self, amount):
        sufficient_funds = self.account_balance - amount
        if sufficient_funds > 0 or sufficient_funds == 0:
            self.account_balance -= amount
            return True
        else:
            return False
    
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")

