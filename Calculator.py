from tkinter import *
from tkinter import messagebox

#window setter
root = Tk()
root.title("Calculator")

#entry box 
e = Entry(root, width=50, borderwidth=2, font=("Segoe Print", 45), justify="right")
e.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=20, pady=20)

#click 
def click(number):
    current = e.get()  
    if number == "." and "." in current:  #for decimal
            return
    e.insert(END, str(number)) 
    
#clear full entry
def clear(): 
    e.delete(0,END)

#erase single character from the last
def erase(): 
    current=e.get()
    if len(current) > 0:
        e.delete(len(current)-1,END)

#add
def add(): 
    fn= e.get()
    global f
    global math
    math="add"
    f=float(fn)
    e.delete(0,END)

#subtract
def sub():
    fn= e.get()
    global f
    global math
    math="sub"
    f=float(fn)
    e.delete(0,END)

#multiply
def mul():
    fn= e.get()
    global f
    global math
    math="multiply"
    f=float(fn)
    e.delete(0,END)

#divide
def div():
    fn= e.get()
    global f
    global math
    math="divide"
    f=float(fn)
    e.delete(0,END)

#modulus
def mod():
    fn= e.get()
    global f
    global math
    math="modulo"
    f=float(fn)
    e.delete(0,END)

#negate
def neg():
    fn = e.get()
    if fn:  
        e.delete(0, END)
        e.insert(0, str(float(fn) * -1))
        
#operation
def equal():
    sn=e.get()
    e.delete(0, END)
    if math=="add":
        e.insert(0,f+float(sn))
    if math=="sub":
        e.insert(0,f-float(sn))
    if math=="multiply":
            e.insert(0,f*float(sn))
    if math=="divide":
        if float(sn)==0.0:
            messagebox.showinfo("ERROR","CANNOT DIVIDE BY ZERO")
        else:
            e.insert(0,f/float(sn))
    if math=="modulo":
        e.insert(0,f%float(sn))

#numbers
b0 = Button(root, text="0", height=2,width=6 , command= lambda: click(0), font=("Segoe Print", 15))
b1 = Button(root, text="1", height=2,width=6 , command= lambda: click(1), font=("Segoe Print", 15))
b2 = Button(root, text="2", height=2,width=6 , command= lambda: click(2), font=("Segoe Print", 15))
b3 = Button(root, text="3", height=2,width=6 , command= lambda: click(3), font=("Segoe Print", 15))
b4 = Button(root, text="4", height=2,width=6 , command= lambda: click(4), font=("Segoe Print", 15))
b5 = Button(root, text="5", height=2,width=6 , command= lambda: click(5), font=("Segoe Print", 15))
b6 = Button(root, text="6", height=2,width=6 , command= lambda: click(6), font=("Segoe Print", 15))
b7 = Button(root, text="7", height=2,width=6 , command= lambda: click(7), font=("Segoe Print", 15))
b8 = Button(root, text="8", height=2,width=6 , command= lambda: click(8), font=("Segoe Print", 15))
b9 = Button(root, text="9", height=2,width=6 , command= lambda: click(9), font=("Segoe Print", 15))

#operators
bac = Button(root, text="AC", height=2,width=6 , command=clear, font=("Segoe Print", 15))
bback = Button(root, text="X", height=2,width=6 , command=erase, font=("Segoe Print", 15))
bneg = Button(root, text="+/-", height=2,width=6 , command=neg, font=("Segoe Print", 15))
bdiv = Button(root, text="/", height=2,width=6 , command=div, font=("Segoe Print", 15))
bmul = Button(root, text="*", height=2,width=6 , command=mul, font=("Segoe Print", 15))
bmin = Button(root, text="-", height=2,width=6 , command=sub, font=("Segoe Print", 15))
badd = Button(root, text="+", height=2,width=6 , command=add, font=("Segoe Print", 15))
bequal = Button(root, text="=", height=2,width=6 , command=equal, font=("Segoe Print", 15))
bmod = Button(root, text="%", height=2,width=6 , command=mod, font=("Segoe Print", 15))
bdeci = Button(root, text=".", height=2,width=6 , command=lambda: click("."), font=("Segoe Print", 15))

#layout
b0.grid(row=5, column=1, sticky="nsew", padx=3, pady=3)
b1.grid(row=4, column=0, sticky="nsew", padx=3, pady=3)
b2.grid(row=4, column=1, sticky="nsew", padx=3, pady=3)
b3.grid(row=4, column=2, sticky="nsew", padx=3, pady=3)
b4.grid(row=3, column=0, sticky="nsew", padx=3, pady=3)
b5.grid(row=3, column=1, sticky="nsew", padx=3, pady=3)
b6.grid(row=3, column=2, sticky="nsew", padx=3, pady=3)
b7.grid(row=2, column=0, sticky="nsew", padx=3, pady=3)
b8.grid(row=2, column=1, sticky="nsew", padx=3, pady=3)
b9.grid(row=2, column=2, sticky="nsew", padx=3, pady=3)
bac.grid(row=1, column=0, sticky="nsew", padx=3, pady=3)
bback.grid(row=1, column=1, sticky="nsew", padx=3, pady=3)
bneg.grid(row=1, column=2, sticky="nsew", padx=3, pady=3)
bdiv.grid(row=1, column=3, sticky="nsew", padx=3, pady=3)
bmul.grid(row=2, column=3, sticky="nsew", padx=3, pady=3)
bmin.grid(row=3, column=3, sticky="nsew", padx=3, pady=3)
badd.grid(row=4, column=3, sticky="nsew", padx=3, pady=3)
bequal.grid(row=5, column=3, sticky="nsew", padx=3, pady=3)
bmod.grid(row=5, column=0, sticky="nsew", padx=3, pady=3)
bdeci.grid(row=5, column=2, sticky="nsew", padx=3, pady=3)
root.grid_columnconfigure([0, 1, 2, 3], weight=1)
root.grid_rowconfigure([1, 2, 3, 4, 5], weight=1)

#window layout
root.configure(bg="#2bdb0f")
root.geometry("350x500")
root.mainloop()

