from tkinter import *
from tkinter import messagebox
import pymysql
import mysql_connector as model

usrn = ""
pwd = ""
login=Tk()
login.eval('tk::PlaceWindow . center')
login.resizable(1, 1)
login.title("User Authentication")
login.geometry("400x200")
login.iconbitmap('/icons/40_ico_1.ico')

def login_user():
    usrn= txt1.get()
    pwd = txt2.get()
#messagebox.showinfo("Messenger",usrn)
con=model.db_connection()
sql_query="select * from tbl_user where username=%s and password=MD5(%s)"
#print(sql_query)
tuple1=(usrn,pwd)
results_query=model.query_param(sql_query,con,tuple1)
rslt_data=model.query_list(results_query)
print(rslt_data)

if rslt_data=="0":
    messagebox.showerror("Messenger","Authentication Failed ")
else:
    messagebox.showinfo("Messenger", "Successfully Login. ")
    login.destroy()


def logout_user():
    messagebox.showinfo("User Logout", "Sample")
    logout_user.quit()
    #def load_login():


labl1 = Label(login, text="UserName").place(x=10, y=50)
txt1 = Entry(login, width=50)
txt1.place(x=70, y=50)
labl1 = Label(login, text="Password").place(x=10, y=80)
txt2 = Entry(login, width=50, show="*")
txt2.place(x=70, y=80)

btn = Button(login, text="Ok", command=login_user, width=10)
btn.place(x=120, y=120)
btn2 = Button(login, text="Cancel", command=login.destroy, width=10)
btn2.place(x=200, y=120)

usrn=(txt1.get())
pwd=(txt2.get())

login.mainloop()