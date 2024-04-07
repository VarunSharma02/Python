#simple GUI from
from tkinter import *
root=Tk()
root.title("Tkinter")
root.geometry("700x400+200+50")
lb1=Label(root,text="USER LOGIN PAGE",font=('',30,"bold"),bg="Blue",fg="White").pack(fill=X)
lb1=Label(root,text="USERNAME:",font=('',15,"bold")).place(x=40,y=70)
def get_data():
    if var_check.get()==1:
      result="USERNAME:"+var_username.get()+","+"\t PASSWORD:"+var_password.get()+"\t GENDER:"+var_gender.get()
      lb1_result.config(text=str(result))
    else:
       lb1_result.config(text="Please Accept Our T&C")

var_username=StringVar()
var_password=StringVar()
var_gender=StringVar()
var_check=IntVar()

En1=Entry(root,font=('',15),bg="white",textvariable=var_username,fg="Black",width=30)
En1.place(x=170,y=70)
lb2=Label(root,text="PASSWORD:",font=('',15,"bold")).place(x=40,y=120)
En2=Entry(root,font=('',15),bg="white",fg="Black",width=30,textvariable=var_password)
En2.place(x=170,y=120)
gender=Label(root,text="GENDER:",font=("",15,"bold"))
gender.place(x=40,y=160)
male=Radiobutton(root,text="MALE",variable=var_gender,value="male",font=("times new roman",12,"bold")).place(x=170,y=160)
female=Radiobutton(root,text="FEMALE",value="female",variable=var_gender,font=("times new roman",12,"bold")).place(x=280,y=160)
check_bt=Checkbutton(root,onvalue=1,offvalue=0,variable=var_check,text="Accpet Our Terms And Conditions",font=("times new roman",15,"bold")).place(x=40,y=210)
btn=Button(root,text="Show data",command=get_data,font=("times new roman",12,"bold"),bg="grey",fg="white").place(x=300,y=250)
lb1_result=Label(root,text="",font=("times new roman",15,))
lb1_result.place(x=0,y=360,relwidth=1)
root.mainloop()