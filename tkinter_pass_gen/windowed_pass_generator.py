from tkinter import *
from tkinter import messagebox
import random

root=Tk()
root.title("Password Generator")
root.geometry("500x400")
root.configure(bg="#ade8f4")
def gen_pass():
    chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
    pass_entry.delete(0,END)
    pass_lenght=int(my_entry.get())
    password=''
    for i in range(pass_lenght):
        pass_chars=random.choice(chars)
        password +=pass_chars
    pass_entry.insert(0,password)

lf=LabelFrame(root, text="How many Characters?",bg="#ade8f4")
lf.pack(pady=20)

my_entry=Entry(lf,font=("Times",24))
my_entry.pack(pady=20, padx=20)


pass_entry=Entry(root, text='',font=("Times",24),bd=0,bg="#ade8f4")
pass_entry.pack(pady=20)

btn_frame=Frame(root,bg="#ade8f4")
btn_frame.pack(pady=20)

btn_pass_generate=Button(btn_frame,text="Generate password",command=gen_pass)
btn_pass_generate.grid(row=0, column=0, padx=10)




root.mainloop()
