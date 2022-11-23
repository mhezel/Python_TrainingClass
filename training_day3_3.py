#---------------------------OOP PYTHON---------------------------------#
#STATE - PROPERTIES
#BEHAVIOR - METHODS

class Car:
    def __init__(self, color, model, manufacturer):
        self.color = color
        self.model = model
        self.manufacturer = manufacturer
    def display_car(self):
         print(self.color, self.model, self.manufacturer)

car = Car("blue", "civic", "honda")
car.display_car()

car2 = Car("red", "elantra", "nissan")
car2.display_car()

car3 = Car("black", "montero", "mitsubishi")
car3.display_car()

