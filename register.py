from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk   
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # ===================variables===================
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_security= StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        self.bg = ImageTk.PhotoImage(file=r"D:\Mumbai_Aug_2018.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=1, y=1, relwidth=1, relheight=1)
        
        # ==================frame=========================
        frame = Frame(self.root, bg="white")
        frame.place(x=350, y=120, width=800, height=550)

        register_lbl = Label(frame, text="Register Here", font=("ubuntu",25,"bold"), fg="green", bg="white")
        register_lbl.place(x=20, y=20)

        # ==================label and entry================
        # ==================row1===========================
        fname = Label(frame, text="First Name", font=("ubuntu",15,"bold"), fg="black", bg="white")
        fname.place(x=50, y=100)

        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("ubuntu",15,"bold"))
        fname_entry.place(x=50, y=130, width=250)


        l_name = Label(frame, text="Last Name", font=("ubuntu,",15,"bold"), bg="white", fg="black")
        l_name.place(x=370, y=100)

        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=("ubuntu",15))
        self.txt_lname.place(x=370, y=130, width=250)

        # ===========row2====================================

        contact = Label(frame, text="Contact Number", font=("ubuntu",15,"bold"), bg="white", fg="black")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("ubuntu",15))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=("ubuntu",15,"bold"), bg="white", fg="black")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("ubuntu",15))
        self.txt_email.place(x=370, y=200, width=250)

        # ===========row3======================================

        security_Q = Label(frame, text="Select Security Question", font=("ubuntu",15,"bold"), bg="white", fg="black")
        security_Q.place(x=50, y=270)

        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("ubuntu",15,"bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Nick Name", "Your Pet Name")
        self.combo_security_Q.place(x=50, y=300, width=250)
        self.combo_security_Q.current(0)

        security = Label(frame, text="Security Answer", textvariable=self.var_security, font=("ubuntu",15,"bold"), bg="white", fg="black")
        security.place(x=370, y=270)

        self.txt_security= ttk.Entry(frame, font=("ubuntu",15))
        self.txt_security.place(x=370, y=300, width=250)

        # ============row4=====================================
        pswd = Label(frame, text="Password", font=("ubuntu",15,"bold"), bg="white", fg="black")
        pswd.place(x=50, y=340)

        self.txt_pswd = ttk.Entry(frame, textvariable=self.var_pass, font=("ubuntu",15))
        self.txt_pswd.place(x=50, y=370, width=250) 

        confirm_pswd = Label(frame, text="Confirm password", font=("ubuntu",15,"bold"), bg="white", fg="black")
        confirm_pswd.place(x=370, y=340)

        self.txt_confirm_pswd = ttk.Entry(frame, textvariable=self.var_confpass, font=("ubuntu",15))
        self.txt_confirm_pswd.place(x=370, y=370, width=250) 

        # ==================checkbutton========================
        self.var_check = IntVar()
        self.checkbtn = Checkbutton(frame, variable=self.var_check, text="I agree to the Terms and Conditions", font=("ubuntu",12,"bold"), bg="white", fg="black", onvalue=1, offvalue=0)    
        self.checkbtn.place(x=50, y=420)

        # ==================buttons=============================
        img = Image.open(r"D:\Academics\2year\4 semester\DBMS\project\register-now.png")
        img = img.resize((200,50), Image.BILINEAR)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, image=self.photoimage, command=self.register_data, borderwidth=0, cursor="hand2", font=("ubuntu",15,"bold"), bg="white", fg="black")
        b1.place(x=10, y=470, width=300)

        img1 = Image.open(r"F:\login_button.png")
        img1 = img1.resize((200,50), Image.BILINEAR)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1, borderwidth=0, cursor="hand2", font=("ubuntu",15,"bold"), bg="white", fg="black")
        b1.place(x=330, y=470, width=300)

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All Fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password does not match")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree our terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Manipal@26",database="mydata")
            my_cursor=conn.cursor()
            query=("Select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User alreasy exist, please try another E-mail")
            else:
                my_cursor.execute("Insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                self.var_fname.get(),
                self.var_lname.get(),
                self.var_contact.get(),
                self.var_email.get(),
                self.var_securityQ.get(),
                self.var_security.get(),
                self.var_pass.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registration Successful")
            
if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
