from tkinter import *
import tkinter.messagebox
root =Tk()
root.title("Employee Registration Form")
root.geometry('600x500')
root.configure(background = "yellow")

label1=Label(root ,text= " Registration Form ", font=("bold", 20)).grid(row =0, column=2)
Firstname = Label(root ,text = "First Name",width=20,font=("bold", 10)).grid(row = 1,column = 1)
LastName = Label(root ,text = "Last Name",width=20,font=("bold", 10)).grid(row = 2,column = 1)
Dateofbirth = Label(root ,text = "Dateofbirth",width=20,font=("bold", 10)).grid(row = 5,column = 1)
Empid= Label(root,text = "Empid",width=20,font=("bold", 10)).grid(row = 4,column = 1)
Address = Label(root,text = "Address",width=20,font=("bold", 10)).grid(row = 3,column = 1)
Qualification = Label(root ,text = "Qualification",width=20,font=("bold", 10)).grid(row = 7,column = 1)
list1 = ['B.E','B.Tech','MBA','BCA','MCA','Others'];
a=StringVar()
droplist=OptionMenu(root,a, *list1)
droplist.config(width=15)
a.set('select your qualification')
droplist.grid(row = 7,column = 2)
Mobile = Label(root ,text = "Contact Number",width=20,font=("bold", 10)).grid(row = 8,column = 1)
Email = Label(root ,text = "Email Id",width=20,font=("bold", 10)).grid(row = 9,column = 1)
Gender =Label(root ,text = "Gender",width=20,font=("bold", 10)).grid(row = 10,column = 1)
var = IntVar()
Radiobutton(root, text="Male",padx = 30, variable=var, value=1).grid(row = 10,column = 2)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).grid(row = 10,column = 3)
label_1 = Label(root, text="Languages Known",width=20,font=("bold", 10))
label_1.grid(row = 12,column = 1)
var1 = IntVar()
Checkbutton(root, text="English", variable=var1).grid(row = 12,column = 2)
var2 = IntVar()
Checkbutton(root, text="Tamil", variable=var2).grid(row = 12,column = 3)
var3 = IntVar()
Checkbutton(root, text="Hindi", variable=var3).grid(row = 12,column = 4) 

Firstname1 = Entry(root).grid(row = 1,column = 2)
Lastname1 = Entry(root).grid(row = 2,column = 2)
Adderss1=Entry(root).grid(row = 3,column = 2)
dob1=Entry(root).grid(row = 4,column = 2)
empid=Entry(root).grid(row = 5,column = 2)
Email1 = Entry(root).grid(row = 9,column = 2)
Mobile1 = Entry(root).grid(row = 8,column = 2)
def onClick():
    tkinter.messagebox.showinfo("Welcome", "Yor Details Submitted  Successfully !")


Button(root, text="Submit", command=onClick,width=20,bg='red',fg='white').grid(row = 14,column = 2)


root.mainloop()