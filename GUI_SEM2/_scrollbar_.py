from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("ListBox")
root.geometry("800x500+250+50")
Frame1=Frame(root,bd=2,relief=RIDGE)    
Frame1.place(x=250,y=50,height=300,width=200)
scroll1=Scrollbar(Frame1,orient=VERTICAL)
scroll1.pack(side=RIGHT,fill=Y)

data=Listbox(Frame1,font=("Arial",20,""),justify=CENTER,yscrollcommand=scroll1.set)
data.pack() 
scroll1.config(command=data.yview)  
for i in range(1,101):
    data.insert(i,"Data:"+str(i))  

root.mainloop()