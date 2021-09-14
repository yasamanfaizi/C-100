class Car:
    def __init__(self, model, colour, speed, company):
        self.model = model
        self.colour = colour
        self.speed = speed
        self.company = company
    def start(self):
        print("car has started")
    def accelerate(self, value):
        print("car accleration is ", value)

car1 = Car("a1", "black", 80, "tesla")
print(car1.model)
car1.start()
car1.accelerate(7)