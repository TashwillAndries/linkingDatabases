from tkinter import *
from tkinter import messagebox
import mysql.connector


login = Tk()
login.title("Login Page")
login.geometry("500x350")


def register():
    if username_entry.get() == "" or password_entry.get() == "":
        messagebox.showerror("Error", "All fields required")
    else:
        try:
            my_db = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                            database='Hospital', auth_plugin='mysql_native_password')
            my_cursor = my_db.cursor()
            data = "INSERT INTO login (user, password) VALUES (%s, %s)"
            val = (username_entry.get(), password_entry.get())
            my_cursor.execute(data, val)
            my_db.commit()
        except ValueError:
            messagebox.showerror("ERROR", "User name must be letters only")


def user_login():
    my_db = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                    database='Hospital', auth_plugin='mysql_native_password')
    my_cursor = my_db.cursor()
    xy = my_cursor.execute("SELECT * FROM login")

    for i in my_cursor:
        if username_entry.get() == i[0] and password_entry.get() == i[1]:
            messagebox.showinfo("Congratulations", "Successful login")
            break
    if username_entry.get() != i[0] and password_entry.get() != i[1]:
        messagebox.showerror("Error", "User or password does not exist")
        username_entry.delete(0, END)
        password_entry.delete(0, END)


username_label = Label(login, text="Please enter username")
username_label.place(x=50, y=51)
username_entry = Entry(login)
username_entry.place(x=280, y=51)
password_label = Label(login, text="Please enter password")
password_label.place(x=50, y=150)
password_entry = Entry(login)
password_entry.place(x=280, y=150)
login_btn = Button(login, text="Login", bg="pink", padx=50, command=user_login)
login_btn.place(x=100, y=250)
register_btn = Button(login, text="Register New User", bg="pink", command=register)
register_btn.place(x=280, y=250)
login.mainloop()
