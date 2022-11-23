print("WORD BANK PROGRAM")
array_list=[]
def functionRun():
    print("============================================")
    while True:
        try:
            x = input("Enter a word/context pls:  ")
            break
        except ValueError:
            print("Invalid input. Please try again...")
    #input in list
    array_list.append(x)

    while True:
        next_transac = input('''Would you like to try again? Please type Y for YES or N for No.''')
        if next_transac.upper() == 'Y':
            functionRun()
            break
        elif next_transac.upper() == 'N':
            #total number of words
            counter = 0
            for i in array_list:
                counter += 1
                print(i)
            if counter >= 1 and array_list[0] != '':
                print(str(counter) + ' Word(s) Found.')
            elif counter == 1 and array_list[0] == '':
                print('Empty / Blank no content found')
            else:
                print('No Word found')
            print(array_list)
            print("Thank you, Goodbye...")
        else:
            print("Invalid Input. Please try again...")
            print("============================================\n")
functionRun()