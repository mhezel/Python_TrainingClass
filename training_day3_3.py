#---------------------------OOP PYTHON---------------------------------#
#STATE - PROPERTIES
#BEHAVIOR - METHODS

class Car:
    counter=0
    def __init__(self, color, model, manufacturer):
        self.color = color
        self.model = model
        self.manufacturer = manufacturer
    def display_car(self):
         print(self.color, self.model, self.manufacturer)
    def car_count(self):
        print(Car.counter)

car = Car("blue", "civic", "honda")
car.display_car()

car2 = Car("red", "elantra", "nissan")
car2.display_car()

car3 = Car("black", "montero", "mitsubishi")
car3.display_car()

class Dog:
    def __greet(): #private
        print('hello')
    def _greet2(): #protected
        print('hello2')
    def greet3():  # public
            print('hello3')

puppy = Dog
puppy.greet3()#-->public
puppy._greet2() #-->protected
puppy._greet()#-->unable to call outside the class-->private

