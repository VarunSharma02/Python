from tkinter import *
class SearchApp():
    def __init__(self,root):
        self.root = root
        self.root.title("Seach App | Developed By Varun Sharma")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#262626")

        title=Label(self.root,text="Search Application",font=("times new roman",40,"bold"),bg="white",fg="#262626")
        title.place(x=0,y=0,relwidth=1)
        lb1_word=Label(self.root,text="Enter Word",font=("times new roman",30,"bold"),bg="#262626",fg="white").place(x=10,y=70)
        txt_word=Entry(self.root,font =("times new roman",20,"bold")).place(x=300,y=100)
        
root=Tk()
obj=SearchApp(root)
root.mainloop()
