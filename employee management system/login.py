from customtkinter import * 
from PIL import Image  
from tkinter import messagebox
def login():
    if usernameEntry.get()=="" or passwordEntry.get()=="":
          messagebox.showerror('Error','All filds are requires') 
    elif usernameEntry.get()=='kamal' and passwordEntry.get()=='1234':
         messagebox.showinfo('success','Login Successful')
         root.destroy()
         import ems
    else:
         messagebox.showerror('error','Wrong Credentials')          
          

root=CTk()
root.geometry('900x500')
root.resizable(0,0)
root.title('Login Page')
image=CTkImage(Image.open('image.png'),size=(700,500))
imageLable=CTkLabel(root,image=image,text='')
imageLable.place(x=200,y=0)
headinglable=CTkLabel(root,text='Employee Management System',bg_color='#ebebeb',font=('Goudy old style',14,'bold'),text_color='black')
headinglable.place(x=10,y=100)
usernameEntry=CTkEntry(root,placeholder_text='Enter Your Username',width=140)
usernameEntry.place(x=30,y=130)
passwordEntry=CTkEntry(root,placeholder_text='Enter Your Password',width=140,show='*')
passwordEntry.place(x=30,y=170)
loginButton=CTkButton(root,text='Login',cursor='hand2',command=login)
loginButton.place(x=30,y=210)

root.mainloop()