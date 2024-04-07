from tkinter import *
from tkinter import filedialog,messagebox
root=Tk()
root.title("ListBox")
root.geometry("800x500+250+50")
def openfiles():
    
    op=filedialog.askopenfile(title="Select File",filetypes=(("text file",".txt"),))
    print(op)
    if op!=None:
        var_filename.set(str(op.name))
        lb1_name.config(text="FileName:"+str(op.name.split("/")[-1]))
        for i in op:
            text_.insert(END,str(i))
        op.close()
def saveAs():
    op=filedialog.asksaveasfile(title="Save As",filetypes=(("text file",".txt"),))
    if op!=None:
        var_filename.set(str(op.name))
        lb1_name.config(text="FileName:"+str(op.name.split("/")[-1])) 
        op.write(text_.get("1.0",END))
        op.close()
        messagebox.showinfo("Save As","File has been saved")
def Save_file():
    if var_filename.get()=="":
        saveAs()
    else:
      op=open(var_filename.get(),"w")
      op.write(text_.get("1.0",END))
      op.close()
      messagebox.showinfo("Save","File has been saved")
btn=Button(root,text="Open",command=openfiles).place(x=50,y=50,width=100)
btn=Button(root,text="Save",command=Save_file).place(x=150,y=50,width=100)
btn=Button(root,text="Save As",command=saveAs).place(x=250,y=50,width=100)
var_filename=StringVar()
lb1_name=Label(root,text="Filename",font=("times new roman",12))
lb1_name.place(x=50,y=100)
text_=Text(root,font=("times new roman",12),bd=2,relief=RIDGE)
text_.place(x=50,y=130,width=400,height=250)
root.mainloop()