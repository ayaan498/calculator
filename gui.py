from tkinter import *
root = Tk()
root.resizable(0,0)
root.geometry('436x450')
root.configure(bg='lightblue')
root.title('Simple Calculator')

e = Entry(root,width=20,font=('Times New Roman',30,'bold'))
e.grid(row=0,column=0,columnspan=6,padx=10,pady=40)

def btn_click(number):
    a = e.get()
    e.delete(0,END)
    e.insert(0, str(a) + str(number))

def btn_clear():
    e.delete(0,END)

def btn_add():
    global num_add 
    num_add = e.get()
    e.delete(0,END)
    global math
    math = 'add'

def btn_sub():
    global num_sub
    num_sub = e.get()
    e.delete(0,END)
    global math
    math = 'sub'

def btn_multi():
    global num_multi
    num_multi = e.get()
    e.delete(0,END)
    global math
    math = 'multi'

def btn_div():
    global num_div
    num_div = e.get()
    e.delete(0,END)
    global math
    math = 'div'

def btn_equal():
    global num_equal
    num_equal = e.get()
    e.delete(0,END)
    if math == 'add':
        result = int(num_add) + int(num_equal)
    elif math == 'sub':
        result = int(num_sub) - int(num_equal)
    elif math == 'multi':
        result = int(num_multi) * int(num_equal)
    elif math == 'div':
        result = int(num_div) / int(num_equal)
        result = int(result)
    
    e.insert(0, str(result))

b_clear = Button(root,text='Clear',padx=125,pady=20,width=10,bg='lightblue',command=btn_clear)
b_add = Button(root,text='+',padx=15,pady=20,width=10,bg='skyblue',command=btn_add)
b_sub = Button(root,text='-',padx=15,pady=20,width=10,bg='skyblue',command=btn_sub)
b_mult = Button(root,text='x',padx=15,pady=20,width=10,bg='skyblue',command=btn_multi)
b_div = Button(root,text='/',padx=15,pady=20,width=10,bg='skyblue',command=btn_div)
b_eq = Button(root,text='=',padx=15,pady=20,width=10,bg='skyblue',command=btn_equal)
b_perc = Button(root,text='%',padx=15,pady=20,width=10,bg='lightblue')
b_dec = Button(root,text='.',padx=15,pady=20,width=10,bg='lightblue')

b1 = Button(root,text='1',padx=15,pady=20,width=10,bg='lightblue',command=lambda: btn_click(1))
b2 = Button(root,text='2',padx=15,pady=20,width=10,bg='lightblue',command=lambda: btn_click(2))
b3 = Button(root,text='3',padx=15,pady=20,width=10,bg='lightblue',command=lambda: btn_click(3))
b4 = Button(root,text='4',padx=15,pady=20,width=10,bg='lightblue',command=lambda: btn_click(4))
b5 = Button(root,text='5',padx=15,pady=20,width=10,bg='lightblue',command=lambda: btn_click(5))
b6 = Button(root,text='6',padx=15,pady=20,width=10,bg='lightblue',command=lambda: btn_click(6))
b7 = Button(root,text='7',padx=15,pady=20,width=10,bg='lightblue',command=lambda: btn_click(7))
b8 = Button(root,text='8',padx=15,pady=20,width=10,bg='lightblue',command=lambda: btn_click(8))
b9 = Button(root,text='9',padx=15,pady=20,width=10,bg='lightblue',command=lambda: btn_click(9))
b0 = Button(root,text='0',padx=15,pady=20,width=10,bg='lightblue',command=lambda: btn_click(0))

b_clear.grid(row=1,column=0,columnspan=3)
b_add.grid(row=1,column=3)
b_sub.grid(row=2,column=3)
b_mult.grid(row=3,column=3)
b_div.grid(row=4,column=3)
b_eq.grid(row=5,column=3)
b_perc.grid(row=5,column=1)
b_dec.grid(row=5,column=2)

b1.grid(row=2,column=0)
b2.grid(row=2,column=1)
b3.grid(row=2,column=2)
b4.grid(row=3,column=0)
b5.grid(row=3,column=1)
b6.grid(row=3,column=2)
b7.grid(row=4,column=0)
b8.grid(row=4,column=1)
b9.grid(row=4,column=2)
b0.grid(row=5,column=0)

root.mainloop()
