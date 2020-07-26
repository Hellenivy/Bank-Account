from datetime import datetime

    def __init__(self, first_name, last_name,phone_no,bank): 
        self.self.first_name = first_name
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
          try: 
          amount + 1
          except:TypeError
          print("Please enter amount in figures")
          return

        if amount <=0:
        print("You can\'t deposit zero or negative")
        
        else:
         self.balance += amount:
         self.deposits.append(amount)
            formated_time = time.strftime("%A, %drd %B %Y, %H:%M %p")
        print("You have deposited {} to {}".format(amount, self.account_name(),formated_time))
        return

    def withdraw(self, amount):
        try:
            amoount + 1
        except TypeError:
            print("You must enter the amount in figures")
            return
 
        if amount <= 0:
          print("You can\'t withdraw zero or negative")

        elif amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            self.withdrawals.append(amount)
            print("You have withdrawn {} from {}".format(amount, self.account_name()))
      
    def get_balance(self):
     return "The balance for {} is {}".format(self.account_name(), self.balance)
  
    def show_deposit_statements(self):
        for deposit in self.deposits:
            formated_time = time.strftime("%A, %drd %B %Y, %H:%M %p")
            print("{} deposited on {}".format(deposit, formated_time))
 
    def show_withdrawals_statement(self):
        for withdraw in  self.withdrawals:
            print(withdraw)

    def request_loan(self, amount):
        try:
            amount + 1
        except TypeError:
            print("Please enter the amount in figures")
            return

        if amount <= 0:
            print("You can\'t request for an amount low than zero")
        else:
             self.loan = amount
             print("You have been given a loan of {}".format(amount))

    def repay_loan(self, amount):
        try:
            amount + 1
        except TypeError:
            print("Please enter the amount in figures")
            return

        if amount <= 0:
            print("Too low to repay your amount")
        elif self.loan == 0:
            print("You don't have a loan at the moment")
        elif amount > self.loan:
            print("Your loan is {} please enter an amount that is less or equal".format(self.loan))
        else:
            self.loan -= amount
            print("You have repaid you loan with {} your balance is {}".format(amount, self.loan))

acc1 = BankAccount("Noisemaker" ,"Owili",+2567093886720,"Tropical")
acc1.first_name
acc1.deposit(100000)
print(acc1.first_name)
acc1.deposit(200100)
print(acc1.balance)
acc1.request_loan(8000)
acc1.repay_loan(3000)
acc1.repay_loan(45688)
acc1.repay_loan(4000)
print(acc1.loan)
print(acc1.balance)
acc1.request_loan(7840)
acc1.deposit(769)
acc1.deposit("eighty")
acc1.deposit(3456)
acc1.deposit(1234)
acc1.show_deposit_statements()
acc1.request_loan("ninety")
