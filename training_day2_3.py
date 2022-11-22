#-------------------------MODULE 3 FUNCTIONS AND METHODS

#def print_lyrics():
    #print('Sample Only')
    #print('Done')
#print_lyrics()

#def greet(lan):
    #if lan == 'en':
       #return ('hello')
    #elif lan == 'spa':
        #return ('hola')
    #elif lan == 'tag':
        #return ('kamusta')

#greet1=greet('tag')
#print(greet1)

#def addTwo(a,b):
    #sum = a + b
    #return sum

#sum = addTwo(5,5)
#print(sum)

#for i in range(1, 10, 2):
    #print(i)

#--------------------MODULE 4 LOOPS AND ITERATION

#for i in [5,4,3,2,1]:
    #print(i)

#arr_1 = ['mhez', 'mm', 'mz']
#print(len(arr_1))

#for x in arr_1:
    #print(x)

next_calculation = 'Y'
while True:
    x = input("Please input first number: ")  # string
    y = input("Please input second number: ")  # string
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Quit Calculator")
    choice = int(input("Enter the choice which you want to perform: "))

    ##-----------FUNCTIONS----------------------##
    def add(a, b):  # Function for Addition
        c = a + b
        return c


    def sub(a, b):  # Function for Subtraction
        c = a - b
        return c


    def multi(a, b):  # Function for Multiplication
        c = a * b
        return c


    def divi(a, b):  # Function for Division
        c = a / b
        return c

    ##-----------FUNCTIONS----------------------##

    try:
        x = int(x) #int
        y = int(y) #int

    except :
        print ('#0xxxx error; Please input a numerical value')
        continue
        print("Please choose the operations which you want to perform")
    try:
        if (choice == 1):
            result = add(x, y)
            print("The result is:", result)
        elif (choice == 2):
            result = sub(x, y)
            print("The result is:", result)
        elif (choice == 3):
            result = multi(x, y)
            print("The result is:", result)
        elif (choice == 4):
            if (y == 0):
                print("Cannot divide it by zero")
            else:
                result = divi(x, y)
                print("The result is:", result)
        elif (choice == 5):
            quit()
        else:
            print("%d is not valid input. Please enter 1, 2 ,3 ,4 or 5." % choice)

        # check if user wants another calculation
        # break the while loop if answer is no

        next_calculation = input("Let's do next calculation? (Y/N): ")
        if(next_calculation.upper() == "N"):
         exit()
        else:
            continue

    except ValueError:
        print("%r is not valid input.  Please enter 1, 2, 3, 4 or 5.")
        print("Thank you for using this calculator!")



