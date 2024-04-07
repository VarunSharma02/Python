from tkinter import *
window=Tk()
window.title("First Tkinter")
window.geometry("1960x800")
lb1=Label(window,text="Hello World")
lb1.pack()
bt1=Button(window,text="Click Here")
bt1.pack()
window.mainloop()
