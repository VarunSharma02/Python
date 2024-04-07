from tkinter import *
root=Tk()
root.title("Tkinter")
root.geometry("700x400+200+50")
root.resizable(False,False)
root.config(bg="pink")
#----------Grid System---------------
#lb1=Label(root,text="Grid System").grid(row=0,column=0)
#---------Pack System-------------
#lb2=Label(root,text="Pack System").pack(side=LEFT)
#lb2=Label(root,text="Pack2 WITH FILL System").pack(fill=X)
#lb2=Label(root,text="Pack NORMAL System").pack()
#----------Place System----------
lb2=Label(root,text="PlaceSystem").place(x=400,y=350)
lb2=Label(root,text="Place  System").place(x=400,y=300)
lb2=Label(root,text="Place System").place(x=350,y=250)
lb1_title=Label(root,text="TITLE",font=("times new roman",40,"bold"),bg="red", fg="Blue").pack(fill=X)
lb2_title=Label(root,text="TITLE2",font=("italic",60,"bold"),bg="violet", fg="light yellow").pack(fill=X,pady=6,padx=9)
lb3_title=Label(root,text="TITLE3",font=("times new roman",20,"bold"),bg="red", fg="Blue").pack(fill=X)
root.mainloop()