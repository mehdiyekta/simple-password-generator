import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import time
import re
realtimeofuser=time.asctime(time.localtime(time.time()))
win_main=tk.Tk()
win_main.title('Simple Password Generator')
win_main.resizable(0,0)
Label_intro=ttk.Label(win_main,text='.:SPG:.')
Label_intro.grid(column=1,row=0)
label_pass_generated=ttk.Label(win_main,text='Pass will be here!',foreground='red')
label_pass_generated.grid(column=1,row=4)
label_len=ttk.Label(win_main,text='How many word? ')
label_len.grid(column=0,row=2)
label_name=ttk.Label(win_main,text='Name for password'+'\n'+'(e.g: smith\'s instagram)')
label_name.grid(column=0,row=3)
name_stringvar=tk.StringVar()
get_name=ttk.Entry(win_main,textvariable=name_stringvar)
get_name.grid(column=2,row=3)
getpasslen=tk.IntVar()
getpasslen_box=ttk.Entry(win_main,textvariable=getpasslen)
getpasslen_box.grid(column=2,row=2)
def generating_pass():
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    passlen =getpasslen.get()
    if passlen==0:
        messagebox.showerror('Error!','This is not possible')
    else:
        p = "".join(random.sample(s,int(passlen) ))
        print(passlen)
        label_pass_generated.config(text=p,foreground='Green')
        def save_pass():
            with open('pass.txt','a') as file_name:
                getname=name_stringvar.get()
                c=str(getname)+': '+'\n'+(('-')*15)+str(realtimeofuser)+('-'*15)+'\n'+str(p)+'\n'+('-'*54)+'\n'
                file_name.write(c)
                file_name.close
                messagebox.showinfo('Success!','Password saved successfuly')
        button_save=ttk.Button(win_main,text='Save pass',command=save_pass)
        button_save.grid(column=1,row=6)
button_generate=ttk.Button(win_main,text='Generate',command=generating_pass)
button_generate.grid(column=1,row=5)
def exit_code():
    exit()
button_exit=ttk.Button(win_main,text='Exit',command=exit_code)
button_exit.grid(column=1,row=7)
win_main.mainloop()
