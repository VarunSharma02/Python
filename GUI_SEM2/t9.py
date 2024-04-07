# Textfield and print the text below the textfield
from tkinter import *
root=Tk()
root.title("Tkinter")
root.geometry("700x400+200+50")
root.resizable(False,False)
def show():
    #print(En1.get())
    lb1_result.config(text=str(En1.get()))


lb1=Label(root,text="USER INPUT",font=('',30,"bold"),bg="Blue",fg="White").pack(fill=X)
lb0=Label(root,text="RESULT",font=("",10,"bold")).place(x=0,y=150)
En1=Entry(root,font=('',10,""),bg="light yellow",fg="Black",bd=8,relief="groove")
En1.pack(pady=5,padx=10,fill=X)
bt1=Button(root,text="Click Me",activebackground="red",activeforeground="white",cursor="hand2",command=show).place(x=300,y=110)
#activeforeground=change color of text when button is hit & activebackground=change color of button when button is
lb1_result=Label(root,font=('',30,"bold"),bg="Black",fg="White")
lb1_result.place(x=0,y=200,relwidth=1)
root.mainloop() 