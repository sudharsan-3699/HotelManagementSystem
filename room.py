from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk   
from tkinter import messagebox
from time import strftime
from datetime import datetime
import random
import mysql.connector

class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        #variable
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()

        #=========title===========================
        lbl_title=Label(self.root,text="Room Booking Details",font=("ubuntu",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #==========logo======================================= 
        img2=Image.open(r"D:\Academics\2year\4 semester\DBMS\project\taj_logo.jpg")
        img2=img2.resize((230,50),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=50)

        #========labelFrame========================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Details",font=("ubuntu",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #label&entry
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("ubuntu",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=20,font=("ubuntu",13,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)

        #fetch data button
        btnFetchData=Button(labelframeleft,command=self.Fetch_contact,text="Fetch Data",font=("ubuntu",11,"bold"),bg="black",fg="gold",width=10)
        btnFetchData.place(x=320,y=3)

        #check_in
        check_in_date=Label(labelframeleft,font=("ubuntu",12,"bold"),text="Check_in Date",padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,font=("ubuntu",13,"bold"),width=29)
        txtcheck_in_date.grid(row=1,column=1)

        #check_out        
        check_in_date=Label(labelframeleft,font=("ubuntu",12,"bold"),text="Check_out Date",padx=2,pady=6)
        check_in_date.grid(row=2,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkout,font=("ubuntu",13,"bold"),width=29)
        txtcheck_in_date.grid(row=2,column=1)

        #roomtype
        label_RoomType=Label(labelframeleft,font=("ubuntu",12,"bold"),text="Room Type",padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="Manipal@26",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide=my_cursor.fetchall()

        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("ubuntu",13,"bold"),width=27,state="readonly")
        combo_RoomType["value"]=ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)

        #available_room
        lblRoomAvailable=Label(labelframeleft,font=("ubuntu",12,"bold"),text="Available Room",padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)
        #txtRoomAvailable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,font=("ubuntu",13,"bold"),width=29)
        #txtRoomAvailable.grid(row=4,column=1)

        conn=mysql.connector.connect(host="localhost",username="root",password="Manipal@26",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()

        combo_RoomNo=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=("ubuntu",13,"bold"),width=27,state="readonly")
        combo_RoomNo["value"]=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4,column=1)

        #meal
        lblMeal=Label(labelframeleft,font=("ubuntu",12,"bold"),text="Meal",padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)
        txtMeal=ttk.Entry(labelframeleft,textvariable=self.var_meal,font=("ubuntu",13,"bold"),width=29)
        txtMeal.grid(row=5,column=1)

        #no of days
        lblNoOfDays=Label(labelframeleft,font=("ubuntu",12,"bold"),text="No Of Days",padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,font=("ubuntu",13,"bold"),width=29)
        txtNoOfDays.grid(row=6,column=1)

        #paid tax
        lblNoOfDays=Label(labelframeleft,font=("ubuntu",12,"bold"),text="Paid Tax",padx=2,pady=6)
        lblNoOfDays.grid(row=7,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,font=("ubuntu",13,"bold"),width=29)
        txtNoOfDays.grid(row=7,column=1)

        #sub total
        lblNoOfDays=Label(labelframeleft,font=("ubuntu",12,"bold"),text="Sub Total",padx=2,pady=6)
        lblNoOfDays.grid(row=8,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,font=("ubuntu",13,"bold"),width=29)
        txtNoOfDays.grid(row=8,column=1)

        #total cost
        lblIdNumber=Label(labelframeleft,font=("ubuntu",12,"bold"),text="Total Cost:",padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_total,font=("ubuntu",13,"bold"),width=29)
        txtIdNumber.grid(row=9,column=1)

        #bill button
        btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("ubuntu",11,"bold"),bg="black",fg="gold",width=10)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)

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

        #right side image\
        img3=Image.open(r"D:\Academics\2year\4 semester\DBMS\project\bed.jpg")
        img3=img3.resize((530,300),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg.place(x=760,y=55,width=530,height=200)


        #tableframe search system
        tableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search",font=("ubuntu",12,"bold"),padx=2)
        tableframe.place(x=435,y=280,width=860,height=260)

        lblsearch=Label(tableframe,text="Search By:",font=("ubuntu",12,"bold"),bg="red",fg="white")
        lblsearch.grid(row=0,column=0,sticky=W)

        self.serch_var=StringVar()

        combo_search=ttk.Combobox(tableframe,textvariable=self.serch_var,font=("ubuntu",13,"bold"),width=24,state="readonly")
        combo_search["value"]=("Contact","Room")
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
        details_table.place(x=0,y=50,width=860,height=180)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype","roomavailable","meal",
                                                            "noOfdays","IDProofType","IDNumber","Address"),
                                     xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact", text="Contact")
        self.room_table.heading("checkin", text="Check-in")
        self.room_table.heading("checkout", text="Check-out")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading("roomavailable", text="Room no")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noOfdays", text="NoOfDays")

        self.room_table["show"]="headings"

        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noOfdays",width=100)

        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()

    #add data    
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else :
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Manipal@26",database="mydata")
                my_cursor=conn.cursor()
                my_cursor.execute("INSERT INTO room (contact, check_in, check_out, roomtype, room, meal, noofdays) VALUES (%s, %s, %s, %s, %s, %s, %s)", (
                self.var_contact.get(),
                self.var_checkin.get(),
                self.var_checkout.get(),
                self.var_roomtype.get(),
                self.var_roomavailable.get(),
                self.var_meal.get(),
                self.var_noofdays.get(),
            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong: {str(es)}",parent=self.root)


    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Manipal@26",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # get cursor
    def get_cuersor(self,event=""):
        cusrsor_row=self.room_table.focus()
        content=self.room_table.item(cusrsor_row)
        row=content["values"]

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])

    #update

    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Manipal@26",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check_in=%s, check_out=%s, roomtype=%s, room=%s, meal=%s, noofdays=%s where contact=%s",(
                                                                            
                                                                            self.var_checkin.get(),
                                                                            self.var_checkout.get(),
                                                                            self.var_roomtype.get(),
                                                                            self.var_roomavailable.get(),
                                                                            self.var_meal.get(),
                                                                            self.var_noofdays.get(),
                                                                            self.var_contact.get()
                                                                            
                                                                        ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details updated successfully",parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to Delete This Customer",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Manipal@26",database="mydata")
            my_cursor=conn.cursor()
            query="Delete from room where contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")



    #all data fetch
    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter contact number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Manipal@26",database="mydata")
            my_cursor=conn.cursor()
            query=("select fname from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This number is not found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=450,y=55,width=300,height=180)

                lblfname=Label(showDataframe,text="Name:",font=("ubuntu",12,"bold"))
                lblfname.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("ubuntu",12,"bold"))
                lbl.place(x=90,y=0)
                
                #gender
                conn=mysql.connector.connect(host="localhost",username="root",password="Manipal@26",database="mydata")
                my_cursor=conn.cursor()
                query=("select gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Gender:",font=("ubuntu",12,"bold"))
                lblGender.place(x=0,y=30)

                lbl2=Label(showDataframe,text=row,font=("ubuntu",12,"bold"))
                lbl2.place(x=90,y=30)

                #email
                conn=mysql.connector.connect(host="localhost",username="root",password="Manipal@26",database="mydata")
                my_cursor=conn.cursor()
                query=("select email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblemail=Label(showDataframe,text="E-mail:",font=("ubuntu",12,"bold"))
                lblemail.place(x=0,y=60)

                lbl3=Label(showDataframe,text=row,font=("ubuntu",12,"bold"))
                lbl3.place(x=90,y=60)

                #address
                conn=mysql.connector.connect(host="localhost",username="root",password="Manipal@26",database="mydata")
                my_cursor=conn.cursor()
                query=("select address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblemail=Label(showDataframe,text="Address:",font=("ubuntu",12,"bold"))
                lblemail.place(x=0,y=90)

                lbl3=Label(showDataframe,text=row,font=("ubuntu",12,"bold"))
                lbl3.place(x=90,y=90)

    #search system

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Manipal@26",database="mydata")
        my_cursor=conn.cursor()

        my_cursor.execute("Select * from room where "+str(self.serch_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)

        if (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Luxury"):
            ql=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(ql+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Single"):
            ql=float(200)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(ql+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Double"):
            ql=float(250)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(ql+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Single"):
            ql=float(200)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(ql+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):
            ql=float(250)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(ql+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Luxury"):
            ql=float(400)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(ql+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
    




if __name__=="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()
