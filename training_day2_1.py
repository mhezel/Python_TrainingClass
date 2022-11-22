#MODULE 2 CONTROL STUCTURES ASND OPERATORS


#for i in range(5):
    #print(i)
    #if i > 2:
        #print('bigger than 2')
    #print('done with ', i)

#x = 99
#if x > 1:
    #print('More than one')
    #if x < 100:
        #print('less than 100')
#print('all done')

x = input("Please enter your office designation('IT / ACCT / HR'): ")
y = input("Please enter number of years in service: ")

stringConver = x.upper()

if(stringConver == 'IT'):
    if(int(y) >= 10):
        print(10000)
    else:
        print(5000)
elif(stringConver == 'ACCT'):
    if (int(y) >= 10):
        print(12000)
    else:
        print(6000)
elif(stringConver == 'HR'):
    if (int(y) >= 10):
        print(15000)
    else:
        print(7500)
else:
    print("designation not found!")






