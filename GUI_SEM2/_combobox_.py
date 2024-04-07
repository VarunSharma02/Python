from tkinter import *
from tkinter import ttk
root=Tk()
root.title("Tkinter")
root.geometry("700x400+200+50")
cmb=ttk.Combobox(root,values=("PHP","PYTHON","JAVA","C++","R","C","CSS","HTML","DBMS"),state="readonly",justify=CENTER)
cmb.place(x=100,y=50,width=200,height=40)
cmb.current(0)

root.mainloop()