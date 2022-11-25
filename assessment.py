list1=[]
class Customer:
    def init(self):
        self.__name = "<name>"
        self.__date = "<date>"
        self.__time = "<time>"
        self.__adult_number = "<adult_number>"
        self.__children_number = "<children_number>"
    def setData(self, name, date, time, adult_number, children_number):
        self.__name = name
        self.__date = date
        self.__time = time
        self.__adult_number = adult_number
        self.__children_number = children_number

class Restaurant(Customer): #Inheritance

    def setRestuarantData(self, name, date, time, adult_number, children_number):
        self.setData(name, date, time, adult_number, children_number)
        list1.append([name,date,time,adult_number,children_number])

    def showData(self):
        print("******  Customer  ******")
        print("Date | Time | Name | Adults | Children")
        for i in list1:
            print(i, end=' ')
            print("\n")


def run_app():
    operator_list = ('''
    RESTAURANT RESERVATION SYSTEM
    System Menu:
    A. View all Reservations 
    B. Make Reservation 
    C. Delete Reservation
    D. Generate Report 
    E. Exit  
    ''')
    print(operator_list)
    print("============================================")
    while True:
        try:
            op = input("Select Options (A,B,C,D,E): ")
            break
        except ValueError:
            print("Invalid input. Please try again...")
    if op.upper() == "A":  # View all Reservations
        print('View all Reservations ')
        e= Restaurant()
        e.showData()
    elif op.upper() == "B":  # Make Reservation
        print("Make Reservation")
        e = Restaurant()
        e.setRestuarantData(input("Name: "), input("Date: "),
                            input("Time: "), input("Number of Children: "),
                            input("Number of Adults: "))
        while True:
            try:
                q1 = input("Do you like to add another reservation? [Y/N]")
                break
            except ValueError:
                print("Invalid input. Please try again...")
        if q1.upper() == "Y":  # run add
            e = Restaurant()
            e.setRestuarantData(input("Name: "), input("Date: "),
                                input("Time: "), input("Number of Children: "),
                                input("Number of Adults: "))
        elif q1.upper() == "N":  # reload to options
            print('back to options...')

    elif op.upper() == "C":  # Delete Reservation
        print('Delete Reservation')
        delete_reservation()
    elif op.upper() == "D":  # Generate Report
        print('Generate Report')
        generate_report()
    elif op.upper() == "E":  # Exit
        print('EXIT')
        exit_record()
    else:
        print("Invalid Input. Please try again")
        print("============================================")

    while True:
        try_again = input('''
            Would you like to try again?
            Please type Y for YES or N for No.
            ''')
        print("============================================")

        if try_again.upper() == 'Y':
            run_app()
            break
        elif try_again.upper() == 'N':
            print("Thank you, Goodbye...")
            import sys
            sys.exit()
        else:
            print("Invalid Input. Please try again...")
            print("============================================\n")
run_app()




