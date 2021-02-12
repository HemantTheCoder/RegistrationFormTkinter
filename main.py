from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x530")
root.title('Registration form')

#Creating Sub-Title
rf=Label(root,text="Registration form", bg='black',fg='white', width=20, font=("bold",20))
rf.place(x=90,y=60)

def exitwindow():
    root.destroy()


def submit():
    screen=Frame()
    screen.place(x=0, y=0, width=500, height=530)
    Done=Label(root,text="Registration Done!!", width=30, height=12, font=("bold",22))
    Done.pack(fill=X)
    button_for_ok=Button(root,text='ok' , width=20,bg="black",fg='white', command=exitwindow).place(x=165,y=280)
    
    
#Creating FullName
Full=Label(root,text="FullName", width=20,font=("bold",12))
Full.place(x=70,y=130)
#Creating Entry For FullName
entry_for_Fullname=Entry(root, width=23)
entry_for_Fullname.place(x=240,y=130)


#Creating Username
User=Label(root,text="Username", width=20,font=("bold",12))
User.place(x=68,y=180)
#Creating Entry For Username
entry_for_Username=Entry(root, width=23)
entry_for_Username.place(x=240,y=180)


#Creating Email Id
Mail=Label(root,text="Email Id", width=20,font=("bold",12))
Mail.place(x=70,y=230)
#Creating Entry For Email Id
entry_for_Email_Id=Entry(root, width=23)
entry_for_Email_Id.place(x=240,y=232)


#Creating Gender
Gender=Label(root,text="Gender",width=20,font=('bold',12))
Gender.place(x=70,y=280)

entry_for_Gender=ttk.Combobox(root)
entry_for_Gender['value']=("Male", "Female", "Others")
entry_for_Gender.place(x=240,y=280)



#Creating Password
Pass=Label(root,text="Password",width=20,font=('bold',12))
Pass.place(x=75,y=330)
#Creating Entry For Password
entry_for_Password=Entry(root, show="*", width=23)
entry_for_Password.place(x=240,y=332)




#Creating Confirm Password
Confirm=Label(root,text="Confirm Password",width=20,font=('bold',12))
Confirm.place(x=60,y=380)
#Creating Entry For Confirm Password
entry_for_Confirm_Password=Entry(root, width=23, bg="white")
entry_for_Confirm_Password.place(x=240,y=382)

#Creating Button For Submit
Button(root, text='Submit', width=14,bg="black",fg='white', command=submit).place(x=213,y=420)


#Clear All
def Clearall():
    entry_for_Fullname.delete(0, END)
    entry_for_Username.delete(0, END)
    entry_for_Email_Id.delete(0, END)
    entry_for_Gender.delete(0, END)
    entry_for_Password.delete(0, END)
    entry_for_Confirm_Password.delete(0, END)


def buttonchange():
     if(entry_for_Password["text"]=="unhide"):
        entry_for_Password.configure(text="hide")
     else:
        entry_for_Password.configure(text="unhide")

#Creating Button For Clear All
button_for_clearall=Button(root, text='Clear All' , width=14,bg="black",fg='white', command=Clearall).place(x=213,y=450)   

def hide():
     if(entry_for_Password['show']== "*"):
         entry_for_Password.configure(show="")
     else:
        entry_for_Password.configure(show="*")

#Creating Button For Clear All
button_for_hide=Button(root, text='Show/Hide Password' , width=14,bg="black",fg='white', command=lambda:[hide(), buttonchange()]).place(x=213,y=480)   



root.mainloop()
