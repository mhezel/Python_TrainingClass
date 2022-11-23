print("***************  RECORD KEEPING APPLICATION  *******************")
dict1 = {}
def main():
    print('''SELECT OPTIONS:\nA - ADD DATA \nB - DELETE DATA \nC - END ''')

    while True:
        try:
            select = input("select: ")
            break
        except ValueError:
            print("Invalid input. Please select from the options provided...")
    if select.upper() == "A":#add data
        print('ADD DATA')
        key = input("Enter a Key: ")
        value = input("Enter a Value: ")
        dict1[key] = value
        print(dict1)
    elif select.upper() == "B":#delete data
        print('DELETE DATA')
        key_to_delete = input("Enter a Key to delete: ")
        dict1.pop(key_to_delete, None)
        print(dict1)
    elif select.upper() == "C":#end
        print('End')
        print("Thank you...")
    else:
        print("Invalid Input. Please try again")
    while True:
        next_transac = input('''
        Would you like to try again?
        Please type Y for YES or N for No.
        ''')
        if next_transac.upper() == 'Y':
            main()
            break
        elif next_transac.upper() == 'N':
            print("Thank you, Goodbye...")
        else:
            print("Invalid Input. Please try again...")
main()