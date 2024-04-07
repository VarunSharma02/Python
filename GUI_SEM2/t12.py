from tkinter import *
root=Tk()
root.title("Tkinter")
root.geometry("700x400+200+50")
root.resizable(False,False)
def check_but():
    print(check_var.get())
bt1=Button(root,text="Click Me",activebackground="red",activeforeground="white",cursor="hand2",command=check_but).place(x=300,y=210,width=150,height=50)
check_var=IntVar()
check_button=Checkbutton(root,text="Accept/Not",onvalue=1,offvalue=0,variable=check_var,font=("times new roman",13,"bold"))
check_button.place(x=260,y=140)
root.mainloop()