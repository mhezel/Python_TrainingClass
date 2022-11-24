class House:
    def __init__(self):
        self.__floor_size="<size>"
        self.__floor_number="<floor number>"
        self.__door_number="<door number>"
    def setData(self,floor_size,floor_number,door_number):
        self.__floor_size=floor_size
        self.__floor_number=floor_number
        self.__door_number=door_number
    def showData(self):
        print("******  HOUSE PROPERTIES  ******")
        print("Floor Size: ",self.__floor_size)
        print("Floor: ", self.__floor_number)
        print("Door: ", self.__door_number)

    def lightOpen(self):
        print("LIGHTS OPEN!")
    def ovenOpen(self):
        print("OVEN OPEN!")

    def switchOn(self):
        self.showData()
        self.lightOpen() # Calls lightOpen function
        self.ovenOpen() # Calls ovenOpen function
        print("*****************************")

class Townhouse(House): #Inheritance

    def setTownhouseData(self,floor_size,floor_number,door_number):
        self.setData(floor_size,floor_number,door_number)

    def showHouse(self):
        self.showData()
        print("         House Lights and Oven is Turned Off       ")
        print("***************************************************")
    def onEverything(self, indicator):
        if(indicator == 'Y'):
            self.switchOn()
        else:
            self.showHouse()

next_transaction = 'Y'
while True:

    print("********NEW HOUSE********")
    e = Townhouse()
    e.setTownhouseData(input("FloorSize: "),input("Floor Number: "),input("Door Number: "))
    e.onEverything(input("Do you want to switch on the house?: Y/N: "))

    next_transaction = input("Let's do next transaction? (Y/N): ")
    if (next_transaction.upper() == "N"):
        exit()
    else:
        next_transaction = 'Y'


