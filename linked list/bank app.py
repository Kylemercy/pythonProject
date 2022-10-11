class bank_account:

    def set_details(self, name, balance=0):
        self.name = name
        self.balance = balance

    def display_method(self):
        print(f'your banks details are name:{self.name} and balance is {self.balance}')

    def deposit(self):
        amount = float(input('Enter amount you want to deposit: '))
        self.balance += amount
        print(f'your money has been deposited successfully.your balance is {self.balance}')

    def withdraw(self):
        total = float(input('Enter amount you want to withdraw: '))
        if total > self.balance:
            print('insufficient funds.')
        else:
            self.balance = self.balance - total
            print('your account balance is:', self.balance)


bank = bank_account()
bank.set_details('jane', 7000)
bank.display_method()
bank.deposit()
bank.withdraw()
