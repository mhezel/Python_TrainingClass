class Restaurant:
    count = 0
    def init(self, res_name, res_date, res_time, no_of_adults, no_of_children):
        self.res_name = res_name
        self.res_date = res_date
        self.res_time = res_time
        self.no_of_adults = no_of_adults
        self.no_of_children = no_of_children

        self.adult_price = 500
        self.kids_price = 300

        Restaurant.count += 1

    def getcount(self):
        return Restaurant.count

    # superclass's version of display()
    def display(self):
        return "NAME: " + self.res_name + "\t\t\t" + "Date: " + self.res_date + "\t\t\t" + "Time: " + self.res_time + "\t\t\t" + "No of Adults: " + str(self.no_of_adults) + "\t\t\t" + "No of Children: " + str(self.no_of_children) + "\t\t\tSubtotal: " + str(self.getTotalAmt()) + "\n"

    def getTotalAmt(self):
        return ((int(self.no_of_adults) * int(self.adult_price))+(int(self.no_of_children) * int(self.kids_price)))

# definition of the subclass
# inheritance
class Reservation(Restaurant):
    # def switchOn(self):
    # extended method
    def display(self):
        print(super(Reservation, self).display())

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
        view_reservation()
    elif op.upper() == "B":  # Make Reservation

        print('Make Reservation')
        make_reservation()

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

def make_reservation():
    print("============================================")
    try:
        reserve1 = Reservation(
            input('Input Name: '),
            input('Input Date: '),
            input('Input Time: '),
            input('Input No of Adults: '),
            input('Input No of Children: ')
        )
        print(reserve1.display())
        print('Total Reservation: ' + str(reserve1.getcount()))
        # break
    except ValueError:
        print('Invalid Inputs. Please try inputting again...')
        make_reservation()
    #save to textfile
    # saveToTextFile()
    while True:
        try:
            q1 = input("Do you like to add another reservation? [Y/N]")
            break
        except ValueError:
            print("Invalid input. Please try again...")
    if q1.upper() == "Y":  # run add
        make_reservation()
    elif q1.upper() == "N":  # reload to options
        print('back to options...')

    while True:
        try:
            q1 = input("Do you like save these in textfile? [Y/N]")
            break
        except ValueError:
            print("Invalid input. Please try again...")
    if q1.upper() == "Y":  # run add
        # saveToTextFile()
        # reserve1 = Restaurant()
        try:
            fl = open("file.txt", "a")
        except:
            print("File not found")
        else:
            fl.write(
                "NAME: " + reserve1.res_name + "\t\t\t" + "Date: " + reserve1.res_date + "\t\t\t" + "Time: " + reserve1.res_time + "\t\t\t" + "No of Adults: " + str(reserve1.no_of_adults) + "\t\t\t" + "No of Children: " + str(reserve1.no_of_children) + "\t\t\tSubtotal: " + str(reserve1.getTotalAmt()) + "\n")
        finally:
            fl.close()
    elif q1.upper() == "N":  # reload to options
        print('back to options...')

    run_app()


# def saveToTextFile():
#     # reserve1 = Restaurant()
#     try:
#         fl = open("file.txt", "a")
#     except:
#         print("File not found")
#     else:
#         fl.write(
#             "NAME: " + reserve1.res_name + "; " + "Date: " + reserve1.res_date + "; " + "Time: " + reserve1.res_time + "; " + "No of Adults: " + reserve1.no_of_adults + "; " + "No of Children: " + reserve1.no_of_children + "\n")
#     finally:
#         fl.close()

def view_reservation():
    # Read File
    try:
        fl = open("file.txt", "r")
    except:
        print("File not found")
    else:
        line_str = fl.readlines()
        count_record = 0
        for i in line_str:
            count_record +=1
            print(i)
        if count_record >= 1:
            print(str(count_record) + ' Record(s) Found.')
        else:
            print('No Record')
        fl.close()
        # print("File close")
        #ask save to textfile


def generate_report():
    # Read File
    try:
        fl = open("file.txt", "r")
    except:
        print("File not found")
    else:
        line_str = fl.readlines()
        count_record = 0
        print('Date\t\t\tTime\t\t\tName\t\t\tAdults\t\t\tChildren\t\t\tSubtotal\t\t\t')
        for i in line_str:
            count_record +=1
            print(i)
        print('----------------------NOTHING FOLLOWS----------------------')
        if count_record >= 1:
            print(str(count_record) + ' Record(s) Found.')
        else:
            print('No Record')
        fl.close()
        # print("File close")

def delete_reservation():
    # Clear File
    try:
        fl = open("file.txt", "w")
    except:
        print("File not found")
    else:
        str = ""
        fl.write("")
    finally:
        fl.close()
        # print("File close")
    print('Cleared...')
    #save all added
    # print('delete reservation...')

run_app()