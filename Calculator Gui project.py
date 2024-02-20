from tkinter import *
on_exp =""
def num_change(x):
    global on_exp
    on_exp = on_exp+x
    dis.config(text=on_exp)
def solve_exp():
        global on_exp
        try:
            solve=eval(on_exp)
            dis.config(text=solve)
        except:
            dis.config(text="Error")

def clear_deta():
    global on_exp
    on_exp =""
    dis.config(text="")
win = Tk()
win.geometry("490x530")
win.resizable(False,False)
win.config(bg="#050f1f")
win.iconbitmap(r"C:\Users\91969\Documents\Downloads\141163-picture-calculator-scientific-download-hd-thumb.ico")
win.title("Calculator")
dis =Label(text="",font=("",20))
dis.config(bg="#17171a")
dis.place(x=20,y=20,width=(458),height=70)
b9 =Button(text="9",font=(40),command=lambda :num_change("9"))
b9.config(bg="#40404d")
b9.place(x=20,y=110,width=107,height=70)
b8 =Button(text="8",font=(40),command=lambda :num_change("8"))
b8.config(bg="#40404d")
b8.place(x=137,y=110,width=107,height=70)
b7 =Button(text="7",font=(40),command=lambda :num_change("7"))
b7.config(bg="#40404d")
b7.place(x=254,y=110,width=107,height=70)
div =Button(text="÷",font=(40),command=lambda :num_change("÷"))
div.config(bg="#40404d")
div.place(x=371,y=110,width=107,height=70)
#`2````````````````````````````````````````````````
b6 =Button(win,text="6",font=(40),command=lambda :num_change("6"))
b6.config(bg="#40404d")
b6.place(x=20,y=190,width=107,height=70)
b5 =Button(win,text="5",font=(40),command=lambda :num_change("5"))
b5.config(bg="#40404d")
b5.place(x=137,y=190,width=107,height=70)
b4 =Button(win,text="4",font=(40),command=lambda :num_change("4"))
b4.config(bg="#40404d")
b4.place(x=254,y=190,width=107,height=70)
mul =Button(win,text="x",font=(40),command=lambda :num_change("x"))
mul.config(bg="#40404d")
mul.place(x=371,y=190,width=107,height=70)
#``````````````````````````````````````````````````
b3 =Button(win,text="3",font=(40),command=lambda :num_change("3"))
b3.config(bg="#40404d")
b3.place(x=20,y=270,width=107,height=70)
b2 =Button(win,text="2",font=(40),command=lambda :num_change("2"))
b2.config(bg="#40404d")
b2.place(x=137,y=270,width=107,height=70)
b1 =Button(win,text="1",font=(40),command=lambda :num_change("1"))
b1.config(bg="#40404d")
b1.place(x=254,y=270,width=107,height=70)
multiply =Button(win,text="-",font=(40),command=lambda :num_change("-"))
multiply.config(bg="#40404d")
multiply.place(x=371,y=270,width=107,height=70)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~```

b0 =Button(win,text="0",font=(40),command=lambda :num_change("0"))
b0.config(bg="#40404d")
b0.place(x=137,y=350,width=107,height=70)
dot =Button(win,text=".",font=(40),command=lambda :num_change("."))
dot.config(bg="#40404d")
dot.place(x=20,y=350,width=107,height=70)
clear =Button(win,text="clear",font=(40),command=clear_deta)
clear.config(bg="#40404d")
clear.place(x=254,y=350,width=107,height=70)

add =Button(win,text="+",font=(40),command=lambda :num_change("+"))
add.config(bg="#40404d")
add.place(x=371,y=350,width=107,height=70)
equal =Button(win,text="=",font=(40),command=solve_exp)
equal.config(bg="#40404d")
equal.place(x=143,y=430,width=214,height=70)




win.mainloop()