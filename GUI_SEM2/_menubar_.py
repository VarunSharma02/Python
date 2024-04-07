from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("ListBox")
root.geometry("800x500+250+50")
root.config(bg="#262626")
def employeeDetails():
     messagebox.showinfo("EmployeeMenu","This is Employee Menu Bar")

Mymenu=Menu(root)

root.config(menu=Mymenu)
Mymenu.add_command(label="Employee",command=employeeDetails)
root.mainloop()