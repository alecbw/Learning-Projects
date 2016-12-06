""" This code does the following things
Top level: creates and manipulates a personal bank account
* accepts deposits
* allows withdrawals 
* displays the balance
* displays the details of the account """

class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name
    
  def __repr__(self):
  	return "This account belongs to %s and it has a balance of $%.2f" % (self.name, self.balance) 
  
  def show_balance(self):
    print "The balance is $%.2f" % self.balance
    
  def deposit(self, amount):
    if amount <= 0:
      print "You can't deposit a negative amount"
      return
    else:
      print "So you're depositing $%.2f" % amount
      self.balance += amount
      self.show_balance()
      
  def withdraw(self, amount):
    if amount >= self.balance:
      print "You can't withdraw more than you have"
      return
    else:
      print "So you're withdrawing $%.2f" % amount
      self.balance -= amount
      self.show_balance()

my_account = BankAccount("alec")
my_account.__repr__()
print my_account
my_account.show_balance()

my_account.deposit(2000)
my_account.withdraw(1000)
print my_account
