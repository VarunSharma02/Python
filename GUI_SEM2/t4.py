from tkinter.simpledialog import *
from tkinter import *
from tkinter.filedialog import askopenfile
top=Tk()
top.geometry("100x100")
# to take integer as input
def show():
    num= askinteger("Input", "Input an Integer")
    print(num)
# To take float as input
def show1():
    num = askfloat("Input", "Input a floating point number")
    print(num)
# To take string as input  
def show():
   name = askstring("Input", "Enter you name")
   print(name)

# To read the file
def show():
   filename = askopenfile()
   print(filename)
B1 = Button(top, text ="Click", command = show)
B1.place(x=50,y=50)
B2=Button(top, text ="Click Here", command = show1)
B2.place(x=50,y=50)

top.mainloop()