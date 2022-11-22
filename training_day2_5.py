#------------------FILE HANDLING----------------------#
#file = input('Enter Filename: ')
#fhand = open(file)
next_transaction = 'Y'
while True:
    print('############### Record Keeping App #######################')
    print("1.Add Record")
    print("2.View Record")
    print("3.Clear All Record")
    print("4.Exit")
    x = int(input("Enter the choice which you want to perform: "))
    try:
        if (x == 1):#Add file
            try:
                fl = open("fl.txt", "a")
            except:
                print("File not found")
            else:
                file = input('Please write some text file. . .')
                fl.write(file)
            finally:
                fl.close()
# print("File close")
        elif (x == 2):  # Read file
            try:
                fl = open("fl.txt", "r")
            except:
                print("File not found")
            else:
                str = fl.readlines()
                for i in str:
                    print(i)
            finally:
                fl.close()
        # print("File close")
        elif (x == 3):  # Clear File
            try:
                fl = open("fl.txt", "w")
            except:
                print("File not found")
            else:
                str = ""
                fl.write("")
            finally:
                 fl.close()
                 print("No More Records Found")
        # print("File close")
        elif (x == 4):
             print("Thank you")
        else:
             print("not valid input. Please enter 1, 2 ,3 ,4 or 5." % choice)

    # check if user wants another transaction
    # break the while loop if answer is no

        next_transaction = input("Let's do next transaction? (Y/N): ")
        if (next_transaction.upper() == "N"):
            exit()
    except ValueError:
        print("Invalid input.  Please enter 1, 2, 3, or 4.")



