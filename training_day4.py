import pymysql
def Database():
    global conn, cursor
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='root',
                           db='test')
    cursor = conn.cursor()

def insertData():
    Database()
    cursor.execute(
        "INSERT INTO `member` (firstname, "
        "lastname, "
        "gender, "
        "address, "
        "username, password, employee_type) VALUES(%s, %s, %s, %s, %s, %s, %s)",
        (str(input('Input First Name: ')),
         str(input('Input Lastname: ')),
         str(input('Input Gender: ')),
         str(input('Input Address: ')),
         str(input('Input Username: ')),
         str(input('Input Password: ')),
         str(input('Input Employee Type: '))
         ))

    cursor.execute("SELECT * FROM `member`")
    fetch = cursor.fetchall()
    for data in fetch:
        print(data)
    conn.commit()

    cursor.close()
    conn.close()
    print('Record Created!')

def deleteData():
    Database()
    cursor.execute("DELETE FROM `member` WHERE `mem_id` = %s" % str(input('Input ID of record you want to delete: ')))

    cursor.execute("SELECT * FROM `member`")
    fetch = cursor.fetchall()
    for data in fetch:
        print(data)
    conn.commit()
    cursor.close()
    conn.close()
    print('Record Deleted!')


def viewData():
    Database()
    cursor.execute("SELECT * FROM `member`")
    fetch = cursor.fetchall()
    countRecord = 0
    for data in fetch:
        countRecord +=1
        print(data)
    conn.commit()
    cursor.close()
    conn.close()
    print(str(countRecord) + ' Record(s) Found!')

print("PYTHON AND MYSQL")
def run_app():
    print("============================================")
    while True:
        try:
            #ask user for command A-View Record, B-Insert, C-Delete
            op = input('OPTIONS: \nA - VIEW RECORDS \nB - INSERT RECORD \nC - DELETE RECORD \n'
                       'Input (A/B/C): ')
            print("============================================")
            if op.upper() == 'A':
                print("VIEW RECORDS")
                viewData()
            elif op.upper() == 'B':
                print("INSERT RECORD")
                insertData()
            elif op.upper() == 'C':
                print("DELETE RECORD")
                deleteData()
            else:
                print("Invalid Inputted Option. Please try again...")
                print("============================================\n")

            break
        except ValueError:
            print("Invalid input. Please try again...")

    #input in list
    # word_list.append(word)
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