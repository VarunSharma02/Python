#Implement inheritance and polymorphism concepts by extending the bank 
#
class BankAccount:
    def __init__(self,account_no,name,balance=0):
        self.name = name
        self.account_no = account_no
        self.balance = balance
    def deposit(self,amount):
        if amount >= 0:
            self.balance += amount
            return f'You successfully deposited {amount} in account {self.account_no}'
        else:
            return "Not valid amount"
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance -= amount
            return f'{self.name} successfully withdraw {amount} from account {self.account_no} \nThe updated balance is {self.balance}'
        else:
            return "Insufficient funds"
    def check_balance(self):
        return self.balance
    def account_info(self):
        return f'''Account Number:{self.account_no}
Holder Name:{self.name}
Account Balance:{self.balance}'''
    
class SavingAccount(BankAccount):
    def __init__(self,account_num,account_name,balance=0,interest_rate=1.78):
        self.interest_rate = interest_rate
        super().__init__(account_num,account_name,balance)
    def add_interest(self):
        self.balance+= self.balance * self.interest_rate

class CheckingAccount(BankAccount):
    def __init__(self,account_num,account_name,balance=0,overdraft_limit=100):
        self.overdraft_limit=overdraft_limit
        super().__init__(account_num,account_name,balance)
    def withdraw(self,amount):
        if amount<=self.balance+self.overdraft_limit:
            self.balance-=amount
            
            return f'{self.name} successfully withdraw {amount} from account {self.account_no} \nThe updated balance is {self.balance}'
        else:
            return "Insufficient funds"
saving_account1=SavingAccount(1,"Varun ",10000)
checlking_account1=CheckingAccount(2,"Aman",12000)

saving_account1.deposit(2000)
print(saving_account1.account_info())
    
    

            
            
