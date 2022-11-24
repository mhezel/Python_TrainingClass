import pymysql
def conn():
    con=pymysql.connect(host="localhost",user="root",password="root",db="py_db")
    return con
def insert(lname,fname,address,con_):
    sql="INSERT INTO tbl_profile(lname,fname,address) VALUES('%s','%s','%s')" % (lname,fname,address)
    #print(sql)
    cursors = con_.cursor()
    cursors.execute(sql)
    con_.commit()
def query(sql,con_):
    cursors=con_.cursor()
    cursors.execute(sql)
    data=cursors.fetchall()
    return data
def add_profile():
    lname_ = input("Please enter Lastname:")
    fname_ = input("Please enter Firstname:")
    address_ = input("Please enter Address:")
    insert(lname_, fname_, address_, db)
    print("Record Added!")
def delete_profile(id,con_):
    sql="delete from tbl_profile where id='%i'" % int(id)
    cursors = con_.cursor()
    cursors.execute(sql)
    con_.commit()
    print("Record Deleted!")
def update_profile(id,lname,fname,address,con_):
    sql = "update tbl_profile set lname='%s',fname='%s',address='%s' where id='%i'" % (lname,fname,address,int(id))
    cursors = con_.cursor()
    cursors.execute(sql)
    con_.commit()
    print("Record Updated!")
def show_profile(con_):
    sql_msg = "SELECT * FROM tbl_profile"
    rslt = query(sql_msg, con_)
    for row in rslt:
        print(row)
        #for i in row:
         #print(i)

db=conn()
next_transaction="Y"
while next_transaction.upper()=="Y":
    next_transaction=input("***CRUD-APP***  {press Y/y to continue}  ")
    if next_transaction.upper()=="Y":
        selection=input("Select Options: "
                     "[a] AddProfile "
                     "[d] Delete Record "
                     "[s] Show Record "
                     "[u] Update Profile ")

    if selection.upper()=="A":
        add_profile()
    elif selection.upper()=="D":
        id=input("Please enter ID No.:")
        delete_profile(id,db)
    elif selection.upper()=="S":
        show_profile(db)
    elif selection.upper() == "U":

        id=input("Please enter ID No.: ")
        lname_ = input("Please enter Lastname: ")
        fname_ = input("Please enter Firstname: ")
        address_ = input("Please enter Address: ")
        update_profile(id,lname_,fname_,address_,db)

    elif annext_transactions.upper()=="N":
        print("Thanks!...")
    else:
        next_transaction="Y"