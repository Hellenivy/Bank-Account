
class BankAccount:
    bank = "KCB"
   
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0
   
    def account_name(self):
        name = "{} account for {} {}".format(
        self.bank, self.first_name, self.last_name)
        return name
   
    def deposit(self, amount):
        self.balance += amount
        print("You have deposited {} to your account".format(amount))
       
    def get_balance(self):
        return "The balance for {} is {}".format(self.account_name(), self.balance)
   
    def withdraw(self, amount):
        if amount>0:
         self.balance >= amount
         self.balance-=amount
        print("You have withdrawn {} from your account".format(amount))
       else:
          print("Insufficient funds")
acc1 = BankAccount("Nylan" , "Dylan")
acc2 = BankAccount("Noisemaker" , "Owili")
print(acc1.account_name())
print(acc2.account_name())

acc1.deposit(100)
acc2.deposit(55)
acc1.deposit(75)
acc2.deposit(-100)

print(acc2.get_balance())
print(acc1.get_balance())
