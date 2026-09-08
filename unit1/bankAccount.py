class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance

    def deposit(self, money):
        self.__balance += money

    def withdraw(self, money):
        if money > self.__balance:
            print("You don't have the money to that request")
        else:
            self.__balance -= money

    def checkStatus(self):
        print("-------------")
        print(f"The current balance is ${self.__balance}")


galileoBank = BankAccount("Galileo", 0)
galileoBank.deposit(100)
galileoBank.checkStatus()
galileoBank.withdraw(20)
galileoBank.checkStatus()
