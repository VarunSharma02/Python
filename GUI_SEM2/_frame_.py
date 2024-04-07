from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("ListBox")
root.geometry("800x500+250+50")
window1=Frame(root,bg="lightgrey",bd=10,relief=GROOVE)
window1.place(x=50,y=50,height=340,width=300)
show=Button(window1,text="Show",bg="grey",fg="white").place(x=120,y=250)
window2=LabelFrame(root,text="Student Details",bg="lightgrey",bd=10,relief=GROOVE)
window2.place(x=400,y=50,height=340,width=300)
show2=Button(window2,text="Show",bg="grey",fg="white").place(x=120,y=250)

root.mainloop()