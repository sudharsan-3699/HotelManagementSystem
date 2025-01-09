from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from register import Register
from hotel import HotelManagementSystem

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1600x900+0+0")

        self.bg = ImageTk.PhotoImage(file=r"D:\Mumbai_Aug_2018.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=1, y=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=100, y=170, width=340, height=450)

        img1 = Image.open(r"D:\Academics\2year\4 semester\DBMS\project\login-icon.png")
        img1 = img1.resize((100, 100), Image.BILINEAR)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=220, y=175, width=100, height=100)

        get_str = Label(frame, text="WELCOME", font=("ubuntu", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        username = Label(frame, text="Username", font=("ubuntu", 15, "bold"), fg="white", bg="black")
        username.place(x=70, y=155)

        self.txtuser = ttk.Entry(frame, font=("ubuntu", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password = Label(frame, text="Password", font=("ubuntu", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame, font=("ubuntu", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=250, width=270)

        loginbtn = Button(frame, command=self.login, text="Login", font=("ubuntu", 15, "bold"), bd=3, relief=RIDGE,
                          fg="white", bg="blue", activebackground="blue", activeforeground="white")
        loginbtn.place(x=110, y=300, width=120, height=35)

        registerbtn = Button(frame, text="New User",command=self.register_window,font=("ubuntu", 15, "bold"), borderwidth=0, fg="white", bg="black",
                             activebackground="blue", activeforeground="white")
        registerbtn.place(x=20, y=350, width=160, height=35)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required!")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Manipal@26", database="mydata")
            my_cursor = conn.cursor()
            query = "SELECT * FROM register WHERE email=%s AND pass=%s"
            value = (self.txtuser.get(), self.txtpass.get())
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row is not None:
                self.new_window = Toplevel(self.root)
                self.app = HotelManagementSystem(self.new_window)
            else:
                messagebox.showerror("Error", "Invalid username or password")

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()
