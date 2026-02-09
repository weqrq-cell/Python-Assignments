class BankAccount:
    def __init__(self, acc_no, balance=0):
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("Current Balance:", self.balance)


# Main Program
account = BankAccount(101, 5000)

account.deposit(2000)
account.withdraw(1500)
account.check_balance()