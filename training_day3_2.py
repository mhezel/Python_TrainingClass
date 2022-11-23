print("***************  RECORD KEEPING APPLICATION  *******************")
def display_dict():
    print(dict)
def add_data(key,value):
    dict1[key] = value
    display_dict()
def del_data(key):
    dict1.pop(key, None)
    display_dict()

dict1 = {}
def main():
    print('''SELECT OPTIONS:\nA - ADD DATA \nB - DELETE DATA \nC - END  ''')
    while True:
        try:#TRY
            select = input("select: ")
            break
        except ValueError: #CATCH
            print("Invalid input.Please select from the options provided...")
            continue

    if select.upper() == "A":#add data
        print('ADD DATA')
        key = input("Enter a Key: ")
        value = input("Enter a Value: ")
        add_data(key,value) #Function call
    elif select.upper() == "B":#delete data
        print('DELETE DATA')
        key_to_delete = input("Enter a Key to delete: ")
        del_data(key_to_delete) #Function call
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