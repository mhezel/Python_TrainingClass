
while True:
    x = input("Please enter your office designation('IT / ACCT / HR'): ")  # string
    y = input("Please enter number of years in service: ")  # string
    try:
        y = int(y)
    except :
        print ('Non numeric data found.')
        continue
    stringConver = x.upper()
    if(stringConver == 'IT'):
        if(y >= 10):
            print(10000)
        else:
            print(5000)
    elif(stringConver == 'ACCT'):
        if(y >= 10):
            print(12000)
        else:
            print(6000)
    elif(stringConver == 'HR'):
        if(y >= 10):
            print(15000)
        else:
            print(7500)
    else:
        print("designation not found!")
    quit()
