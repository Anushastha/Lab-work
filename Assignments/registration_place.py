from tkinter import*
root=Tk()
root.title("Registration Form")
def submit():
    print("Registration successfully done!")
myLabel=Label(root,text="Registration form",font=('bold',20))
myLabel.place(x=130,y=53)
root.geometry("500x500")
name=Label(root, text="Full Name").place (x=80,y=130)
entry_1=Entry(root)
entry_1.place(width=180,x=240,y=130)
email= Label(root,text="Email").place(x=80,y=180)
entry_2 = Entry(root)
entry_2.place(width=180,x=240,y=180)
Password= Label(root,text="Password").place(x=80,y=230)
entry_3 = Entry(root)
entry_3.place(width=180,x=240,y=230)
Password_2= Label(root,text="Confirm Password").place(x=80,y=280)
entry_4 = Entry(root)
entry_4.place(width=180 ,x=240,y=280)
Button(root,text="Submit",width=20,bg="blue",fg="white",command=submit()).place(x=170,y=380)
root.mainloop()
