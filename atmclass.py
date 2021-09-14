class Atm: 
    def __init__(self, number, pin):
        self.number = number
        self.pin = pin
    def balance(self):
        print("Your balance is $70")
    def withdraw(self, amount):
        newbalance = 70-amount
        print("your new balance is ", newbalance)
atm = Atm(12767917, 456)
atm.balance()
atm.withdraw(9)

