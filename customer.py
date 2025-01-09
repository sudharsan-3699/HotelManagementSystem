from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk   
from tkinter import messagebox
import random
import mysql.connector

class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        # vaiable
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_first_name=StringVar()
        self.var_last_name=StringVar()
        self.var_gender=StringVar()
        self.var_pincode=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_no=StringVar()
        self.var_address=StringVar()

        #=========title===========================
        lbl_title=Label(self.root,text="Add Customer Details",font=("ubuntu",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #==========logo======================================= 
        img2=Image.open(r"D:\Academics\2year\4 semester\DBMS\project\taj_logo.jpg")
        img2=img2.resize((230,50),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=50)

        #========labelFrame========================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("ubuntu",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #label&entry
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("ubuntu",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("ubuntu",13,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)

        #cust_first_name
        lbl_fname=Label(labelframeleft,text="First Name",font=("ubuntu",12,"bold"),padx=2,pady=6)
        lbl_fname.grid(row=1,column=0,sticky=W)

        textfname=ttk.Entry(labelframeleft,textvariable=self.var_first_name,width=29,font=("ubuntu",13,"bold"))
        textfname.grid(row=1,column=1)

        #cust_last_name
        lbl_lname=Label(labelframeleft,text="Last Name",font=("ubuntu",12,"bold"),padx=2,pady=6)
        lbl_lname.grid(row=2,column=0,sticky=W)

        textlname=ttk.Entry(labelframeleft,textvariable=self.var_last_name,width=29,font=("ubuntu",13,"bold"))
        textlname.grid(row=2,column=1)

        #gender
        label_gender=Label(labelframeleft,text="Gender",font=("ubuntu",12,"bold"),padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("ubuntu",13,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        #pincode
        lblpin=Label(labelframeleft,text="Pincode",font=("ubuntu",12,"bold"),padx=2,pady=6)
        lblpin.grid(row=4,column=0,sticky=W)

        txtpin=ttk.Entry(labelframeleft,textvariable=self.var_pincode,width=29,font=("ubuntu",13,"bold"))
        txtpin.grid(row=4,column=1)

        #mobilenumber
        lblmobile=Label(labelframeleft,text="Mobile Number",font=("ubuntu",12,"bold"),padx=2,pady=6)
        lblmobile.grid(row=5,column=0,sticky=W)

        txtmobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=29,font=("ubuntu",13,"bold"))
        txtmobile.grid(row=5,column=1)

        #email
        lblemail=Label(labelframeleft,text="E-Mail ID",font=("ubuntu",12,"bold"),padx=2,pady=6)
        lblemail.grid(row=6,column=0,sticky=W)

        txtemail=ttk.Entry(labelframeleft,textvariable=self.var_email,width=29,font=("ubuntu",13,"bold"))
        txtemail.grid(row=6,column=1)

        #idproof
        lblidproof=Label(labelframeleft,text="ID Proof Type",font=("ubuntu",12,"bold"),padx=2,pady=6)
        lblidproof.grid(row=7,column=0,sticky=W)

        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("ubuntu",13,"bold"),width=27,state="readonly")
        combo_id["value"]=("Aadhaar Card","Driving License","Passport","Student ID","Differntly Abled ID","Voter ID","Ration ID")
        combo_id.current(0)
        combo_id.grid(row=7,column=1)

        #idnumber
        lblidno=Label(labelframeleft,text="ID Number",font=("ubuntu",12,"bold"),padx=2,pady=6)
        lblidno.grid(row=8,column=0,sticky=W)

        txtidno=ttk.Entry(labelframeleft,textvariable=self.var_id_no,width=29,font=("ubuntu",13,"bold"))
        txtidno.grid(row=8,column=1)

        #address
        lbladdress=Label(labelframeleft,text="Address",font=("ubuntu",12,"bold"),padx=2,pady=6)
        lbladdress.grid(row=9,column=0,sticky=W)

        txtaddress=ttk.Entry(labelframeleft,textvariable=self.var_address,width=29,font=("ubuntu",13,"bold"))
        txtaddress.grid(row=9,column=1)

        #buttons
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("ubuntu",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("ubuntu",11,"bold"),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("ubuntu",11,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="Reset",command=self.reset,font=("ubuntu",11,"bold"),bg="black",fg="gold",width=10)
        btnreset.grid(row=0,column=3,padx=1)

        #tableframe search system
        tableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search",font=("ubuntu",12,"bold"),padx=2)
        tableframe.place(x=435,y=50,width=860,height=490)

        lblsearch=Label(tableframe,text="Search By:",font=("ubuntu",12,"bold"),bg="red",fg="white")
        lblsearch.grid(row=0,column=0,sticky=W)

        self.serch_var=StringVar()

        combo_search=ttk.Combobox(tableframe,textvariable=self.serch_var,font=("ubuntu",13,"bold"),width=24,state="readonly")
        combo_search["value"]=("Mobile","Ref")
        combo_search.current(0)
        combo_search.grid(row=0,column=1)

        self.txt_search=StringVar()
        txtsearch=ttk.Entry(tableframe,textvariable=self.txt_search,width=24,font=("ubuntu",13,"bold"))
        txtsearch.grid(row=0,column=2)

        btnSearch=Button(tableframe,text="Search",command=self.search,font=("ubuntu",11,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowall=Button(tableframe,text="Show All",command=self.fetch_data,font=("ubuntu",11,"bold"),bg="black",fg="gold",width=10)
        btnShowall.grid(row=0,column=4,padx=1)

        #show data table
        details_table=Frame(tableframe,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("Ref","First Name","Last Name","Gender","Pincode","Mobile",
                                                            "E-Mail_ID","IDProofType","IDNumber","Address"),
                                     xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("Ref", text="Ref")
        self.Cust_Details_Table.heading("First Name", text="First Name")
        self.Cust_Details_Table.heading("Last Name", text="Last Name")
        self.Cust_Details_Table.heading("Gender", text="Gender")
        self.Cust_Details_Table.heading("Pincode", text="Pincode")
        self.Cust_Details_Table.heading("Mobile", text="Mobile Number")
        self.Cust_Details_Table.heading("E-Mail_ID", text="E-Mail ID")
        self.Cust_Details_Table.heading("IDProofType", text="ID Proof Type")
        self.Cust_Details_Table.heading("IDNumber", text="ID Number")
        self.Cust_Details_Table.heading("Address", text="Address")

        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("Ref",width=100)
        self.Cust_Details_Table.column("First Name",width=100)
        self.Cust_Details_Table.column("Last Name",width=100)
        self.Cust_Details_Table.column("Gender",width=100)
        self.Cust_Details_Table.column("Pincode",width=100)
        self.Cust_Details_Table.column("Mobile",width=100)
        self.Cust_Details_Table.column("E-Mail_ID",width=100)
        self.Cust_Details_Table.column("IDProofType",width=100)
        self.Cust_Details_Table.column("Address",width=100)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_last_name.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else :
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Manipal@26",database="mydata")
                my_cursor=conn.cursor()
                my_cursor.execute("Insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_ref.get(),
                                                                                self.var_first_name.get(),
                                                                                self.var_last_name.get(),
                                                                                self.var_gender.get(),
                                                                                self.var_pincode.get(),
                                                                                self.var_mobile.get(),
                                                                                self.var_email.get(),
                                                                                self.var_id_proof.get(),
                                                                                self.var_id_no.get(),
                                                                                self.var_address.get()
                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Manipal@26",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    def get_cuersor(self,event=""):
        cusrsor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cusrsor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_first_name.set(row[1]),
        self.var_last_name.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_pincode.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_id_proof.set(row[7]),
        self.var_id_no.set(row[8]),
        self.var_address.set(row[9])

    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Manipal@26",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set fname=%s,lname=%s,gender=%s,pincode=%s,mobile=%s,email=%s,id_proof=%s,id_number=%s,address=%s where ref=%s",(
                                                                                
                                                                                self.var_first_name.get(),
                                                                                self.var_last_name.get(),
                                                                                self.var_gender.get(),
                                                                                self.var_pincode.get(),
                                                                                self.var_mobile.get(),
                                                                                self.var_email.get(),
                                                                                self.var_id_proof.get(),
                                                                                self.var_id_no.get(),
                                                                                self.var_address.get(),
                                                                                self.var_ref.get()
                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details updated successfully",parent=self.root)


    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to Delete This Customer",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Manipal@26",database="mydata")
            my_cursor=conn.cursor()
            query="Delete from customer where ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        #self.var_ref.set(""),
        self.var_first_name.set(""),
        self.var_last_name.set(""),
        #self.var_gender.set(""),
        self.var_pincode.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_id_proof.set(""),
        self.var_id_no.set(""),
        self.var_address.set("")

        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Manipal@26",database="mydata")
        my_cursor=conn.cursor()

        my_cursor.execute("Select * from customer where "+str(self.serch_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
        


            



if __name__=="__main__":


    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()
