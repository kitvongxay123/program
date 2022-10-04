from tkinter import *
import tkinter.messagebox as Msg
def KIT():
    chBath=bath.get()
    if bath.get()=='':
        Msg.showinfo("info","Enter bath please!!!",icon='warning')
        txt1.focus_set()
    elif rate.get()=='':
        Msg.showinfo("info", "Enter rate please!!!", icon='warning')
        txt2.focus_set()
    elif chBath.isalpha():
        Msg.showinfo("info", "Enter bath is only please!!!", icon='warning')
        txt2.focus_set()
    else:
        b=int(bath.get())
        r=int(rate.get())
        k=b*r
        kip.set(f'{k:,}kip')
def AllClear():
    bath.set('')
    rate.set('')
    kip.set('')
    txt1.focus()
root=Tk()
root.title("Exchange")
root.geometry("500x400")

bath=StringVar()
rate=StringVar()
kip=StringVar()



lb1=Label(root,font=('Times new Roman',16),text='bath to kip')
lb1.place(x=200,y=50)
lb2=Label(root,font=('Times new Roman',16),text='Enter bath:')
lb2.place(x=50,y=100)
txt1=Entry(root,font=('Times new Roman',16),textvariable=bath)
txt1.place(x=150,y=100)

lb3=Label(root,font=('Times new Roman',16),text='Enter Rate:')
lb3.place(x=50,y=150)
txt2=Entry(root,font=('Times new Roman',16),textvariable=rate)
txt2.place(x=150,y=150)
btn1=Button(root,font=('Times new Roman',16),width=10,text='Exchange',command=KIT)
btn1.place(x=100,y=200)
btn2=Button(root,font=('Times new Roman',16),width=10,text='clear',command=AllClear)
btn2.place(x=250,y=200)

lb4=Label(root,font=('Times new Roman',16),width=10,text='Total:')
lb4.place(x=50,y=300)
txt3=Entry(root,font=('Times new Roman',16),textvariable=kip)
txt3.place(x=150,y=300)



root.mainloop()
