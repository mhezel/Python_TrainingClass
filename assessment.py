num_list = []
class Customer:
    def __init__(self):
        self.__name = "<name>"
        self.__date = "<date>"
        self.__time = "<time>"
        self.__adult_number = "<adult_number>"
        self.__children_number = "<children_number>"

    def setData(self, name, date, time,adult_number,children_number ):
        self.__name = name
        self.__date = date
        self.__time = time
        self.__adult_number = adult_number
        self.__children_number = children_number

        num_list.append(date)
        num_list.append(time)
        num_list.append(name)
        num_list.append(adult_number)
        num_list.append(children_number)

    def showData(self):
        print("******  Customer  ******")
        print("Date | Time | Name | Adults | Children")
        for row in num_list:
            for elem in row:
                print(elem, end=' ')
        s = "\nTotal number of Adults: {}"
        s2 = s.format(num_list[3])
        print(s2)
        ss= "\nTotal number of Children: {}"
        ss2 = s.format(num_list[4])
        print(ss2)

class Restaurant(Customer): #Inheritance

    def setRestuarantData(self, name, date, time, adult_number,children_number ):
        self.setData(name, date, time,adult_number,children_number)

    def viewReservation(self):
        self.showData()

    #def makeReservation(self,x):
        #make

    #def deleteReservation(self,x):
        #delete

    #def generateReport(self,x):
        #generate

    def saveReservetoText(self, num_list):
        try:
            fl = open("reservation.txt", "a")
        except:
            print("File not found")
        else:
            file = num_list
            fl.write(file)
        finally:
            fl.close()

def menu():
    print("################### RESTAURANT RESERVATION PROGRAM #######################")
    print("################### A.View all Reservations ##############################")
    print("################### B. Make Reservations #################################")
    print("################### C. Delete Reservations ###############################")
    print("################### D. Generate Report ###################################")
    print("################### E. Exit ##############################################")

    while True:
        try:
            x = input("What do you wish to do . . . . :  ")
            break
        except ValueError:
            print("Invalid input. Please try again...")

    if x.upper() == 'A':
        e = Restaurant()
        e.viewReservation()

    elif x.upper() == 'B':
        print("******** NEW CUSTOMER ********")
        e = Restaurant()
        e.setRestuarantData(input("Name: "), input("Date: "), input("Time: "), input("Number of Children: "),input("Number of Adults: "))

    #elif x.upper() == 'C':

    elif x.upper() == 'D':
        e=Restaurant()
        e.saveReservetoText()

    elif x.upper() == 'E':
        print("Thank you!! ")
        quit()

    else:
        print("Invalid Input. Please try again...")
        print("============================================\n")

    while True:
        next_transac = input('''
            Would you like to try again?
            Please type Y/N: ''')
        if next_transac.upper() == 'Y':
            menu()
            break
        elif next_transac.upper() == 'N':
            print("Thank you, Goodbye...")
        else:
            print("Invalid Input. Please try again...")
menu()


