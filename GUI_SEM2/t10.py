from tkinter import *
root=Tk()
root.title("Tkinter")
root.geometry("700x400+200+50")
root.resizable(False,False)
def show_data():
    print(Text_field.get('1.0',END))

Text_field=Text(root,bd=10,relief="sunken")
Text_field.place(x=150,y=80,width=400,height=150)
bt1=Button(root,text="Click Me",activebackground="red",activeforeground="white",cursor="hand2",command=show_data).place(x=300,y=310)


root.mainloop()