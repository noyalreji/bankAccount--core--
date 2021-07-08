class BankAccount:
  def __init__(self,name, int_rate = 0.01, balance = 0):
    self.name = name
    self.int_rate = int_rate
    self.balance = balance

  def deposit(self, amount):
      self.balance += amount
      return self
  
  def withdraw(self, amount):
      if (self.balance < amount):
        print("Insufficient funds: Charging a $5 fee")
        self.balance -= 5
      else:
        self.balance -= amount
      return self

  def display_account_info(self):
      print((f"Bank: {self.name}, Balance: $ {self.balance}"))

  def yield_interest(self):
    yield_interest = self.balance * 0.01
    if (self.balance >= 0):
        self.balance += yield_interest
    return self
  
  # combining the string value to the object in memory 
  def __str__(self) -> str:
      return (f"Bank: {self.name}, Balance: {self.balance}")
  
  #get info from all accounts
  def bank_account_info(accounts):
      for account in accounts:
        print(account)
  
# Create 2 accounts
accounts = [BankAccount(name="Dojo Bank"), BankAccount(name="American Bank")]



# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
accounts[0].deposit(5000).deposit(4000).deposit(5000).withdraw(10000).yield_interest()
BankAccount.bank_account_info(accounts)

# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
accounts[1].deposit(5000).deposit(4000).withdraw(10000).withdraw(1000).withdraw(1000).withdraw(1000).yield_interest()
BankAccount.bank_account_info(accounts)