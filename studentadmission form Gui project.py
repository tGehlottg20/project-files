from tkinter import *
win = Tk()

win.config(bg="#399bc4")
win.geometry("1300x700")
win.resizable(False,False)




S_i = Label(win,text="student info",font=("Time New Roman",30),fg="Black",bg="#399bc4")
S_i.place(x = 0,y=40,width=260,height=50)
S_Name = Label(win,text="Student Name",font=("Time New Roman",20),fg="Black",bg="#399bc4")
S_Name.place(x = 20,y=100,width=190,height=50)
SS = Entry(win,font=("Time New Roman",20,"bold"))
SS.place(x=230,y=100,width=320,height=50)
FName = Label(win,text="Father Name",font=("Time New Roman",20),fg="Black",bg="#399bc4")
FName.place(x = 20,y=160,width=180,height=50)
FName = Entry(win,font=("Time New Roman",20,"bold"))
FName.place(x=230,y=160,width=320,height=50)
MName = Label(win,text="Mother Name",font=("Time New Roman",20),fg="Black",bg="#399bc4")
MName.place(x = 20,y=220,width=180,height=50)
MName = Entry(win,font=("Time New Roman",20,"bold"))
MName.place(x=230,y=160,width=320,height=50)
MName = Entry(win,font=("Time New Roman",20,"bold"))
MName.place(x=230,y=220,width=320,height=50)
Add = Label(win,text="Address",font=("Time New Roman",20),fg="Black",bg="#399bc4")
Add.place(x = 10,y=285,width=180,height=50)
Add = Entry(win,font=("Time New Roman",20,"bold"))
Add.place(x=230,y=280,width=320,height=50)
PhNo = Label(win,text="Phone Number",font=("Time New Roman",20),fg="Black",bg="#399bc4")
PhNo.place(x = 10,y=340,width=210,height=50)
PhNo = Entry(win,font=("Time New Roman",20,"bold"))
PhNo.place(x=230,y=340,width=320,height=50)
CardNo = Label(win,text="Card Number",font=("Time New Roman",20),fg="Black",bg="#399bc4")
CardNo.place(x = 10,y=400,width=210,height=50)
CardNo = Entry(win,font=("Time New Roman",20,"bold"))
CardNo.place(x=230,y=400,width=320,height=50)
bc = Button(win, text="Done",font=("Time New Roman",20,))
bc.place(x = 300,y=490,width = 100,height = 50)

SF_i = Label(win,text="Student Fee",font=("Time New Roman",30),fg="Black",bg="#399bc4")
SF_i.place(x =550,y=40,width=400,height=50)
CNo = Label(win,text="Card Number",font=("Time New Roman",20),fg="Black",bg="#399bc4")
CNo.place(x =550,y=100,width=400,height=50)
CNo = Entry(win,font=("Time New Roman",20,"bold"))
CNo.place(x=860,y=100,width=360,height=50)
PNo = Label(win,text="Phone Number",font=("Time New Roman",20),fg="Black",bg="#399bc4")
PNo.place(x =550,y=160,width=400,height=50)
PNo = Entry(win,font=("Time New Roman",20,"bold"))
PNo.place(x=860,y=160,width=360,height=50)
St_F = Label(win,text="Student Fee",font=("Time New Roman",20),fg="Black",bg="#399bc4")
St_F.place(x =550,y=220,width=400,height=50)
St_F = Entry(win,font=("Time New Roman",20,"bold"))
St_F.place(x=860,y=220,width=360,height=50)
bcc = Button(win, text="Done",font=("Time New Roman",20,))
bcc.place(x = 890,y=300,width = 100,height = 50)
win.mainloop()



















