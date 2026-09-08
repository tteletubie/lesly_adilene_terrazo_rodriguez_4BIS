class Monster:
    def __init__(self, flavor: str, design, price, quantity):
        self.flavor = flavor
        self.design = design
        self.price = price
        self.quantity = quantity

    def drink(self):
        self.quantity = 0
        print("Drunk")

    def open(self):
        print(f"Can of {self.flavor} is open")

    def close(self):
        print(f"Can of {self.flavor} is closed")


# Create multiple intsances using the class

monsterClassic = Monster("Classic", "black", 2, 100)
print("Liquid (ML): ", monsterClassic.quantity)
monsterClassic.open()

print("\n=============\n")

monsterPeach = Monster("Peach", "Pink", 2.99, 100)
print("Price: ", monsterPeach.price)
monsterPeach.close()
