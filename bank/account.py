
    def __init__(self, first_name, last_name):
        self.bank, self.fself.first_name = first_name
        self.last_name = last_name
        self.phone_no = phone_no
        self.bank = bank
        self.balance = 0
        self.withdraw_summary = []
        self.deposit_summary = []
        self.loan_balance = 0

    def account_name(self):
        name = "{} account for {} {}".format(
            self.bank, self.first_name, self.last_name, self.phone_no, self.bank)
        return name
     
   
    def deposit(self, amount):
        if amount <=0:
        print("You can\'t deposit zero or negative")

       
    def else:
            self.balance += amount
            print("You have deposited {} to {}".format(amount, self.account_name()))
            return

    def withdraw(self, amount):
         
        if amount <= 0:
          print("You can\'t withdraw zero or negative")
          
       
        elif amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print("You have withdrawn {} from {}".format(amount, self.account_name()))
       
                    
    def _get_balance(self):
        return "The balance for {} is {}".format(self.account_name(), self.balance)


    def lend_loan(self, loan):
      if loan <= 0:
        print("Invalid request")
        
      else: 
        self.loan_balance += loan
        print("{} you have borrowed {}".format(self.account_name(), loan))
      
    def pay_loan(self, loan):
      if loan <= 0:
        print("Invalid amount to reduce your loan")
      else:
        self.loan_balance -= loan
        print(" You have repaid {}".format(loan))
      
    def deposit_statement(self, amount):
      self.deposit(self, amount)

      return self.deposit_summary.append(amount)   
    
    
    
    def deposit_statement(self, amount):
      self.deposit(self, amount)
      
      return self.deposit_summary.append(amount)
         
     
acc1 = BankAccount("Noisemaker" ,"Owili",+2567093886720,"Tropical")
print(acc1.phone_no)
acc1.deposit(100000)
acc1.withdraw(5000)
acc1.withdraw(75)
acc1.deposit(200100)
acc1.deposit(900)
acc1.lend_loan(80000)
acc1.lend_loan(45000)
acc1.pay_loan(90800)
print(acc1.getloan_balance())
print(acc1.deposit_summary())

      
 
