from tkinter import *
root=Tk()
root.title("ListBox")
root.geometry("800x500+250+50")
def get_data():
    get_cursor=language_list.curselection()
    #print(get_cursor,language_list.get( get_cursor))
    language_list.delete(get_cursor)    

language_list=Listbox(root,font=("times new roman",15),bg="#262626",fg="white")
language_list.place(x=100,y=50,width=150)
for i in range(1,21):
    language_list.insert(i,"Language:"+str(i))

btn=Button(root,text="Show data",command=get_data,font=("times new roman",12,"bold"),bg="grey",fg="white").place(x=300,y=250)
root.mainloop()