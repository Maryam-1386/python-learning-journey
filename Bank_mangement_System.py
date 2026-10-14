class BankAccount:
    def __init__(self,account_number,owner_name,balance):
        self.account_number = account_number
        self.owner_name = owner_name 

        if balance < 0:
            print("Balance cannot be negative. ")
            self.balance = 0
        else:
            self.balance = balance 

    def __str__(self):
        return f"Account : {self.account_number} | Owner : {self.owner_name} | Balance: {self.balance} "
    
    def deposit(self,amount):

        if amount <= 0:
            print("Amount must be positive.")
            return
        
        self.balance += amount

    def withdraw(self,amount):
        
        if amount <= 0 :
            print("Amount must be positive .")
            return
        
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount

    def show_balance(self):
        print(f"Balance: {self.balance}")
    