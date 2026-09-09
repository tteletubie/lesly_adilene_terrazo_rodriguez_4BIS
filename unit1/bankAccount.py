class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance

    def deposit(self, money):
        self.__balance += money
        print(f"Deposited ${money} to {self.holder}'s account!")

    def withdraw(self, money):
        if money <= 0:
            print(f"It's impossible to withdraw ${money}")

        if money > self.__balance:
            print("You don't have the money to that request")
        else:
            self.__balance -= money
            print(f"Withdrew ${money} from {self.holder}'s account!")

    def checkStatus(self):
        print("\n-------------")
        print(f"The current balance is ${self.__balance}")
        print("-------------\n")


print("\033c")
leslyBank = BankAccount("Lesly", 0)
print(f"{leslyBank.holder} has ${leslyBank._BankAccount__balance}\n")
leslyBank.deposit(100)
leslyBank.checkStatus()
leslyBank.withdraw(50)
leslyBank.checkStatus()
