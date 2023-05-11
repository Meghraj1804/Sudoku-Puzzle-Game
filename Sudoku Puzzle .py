#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import * 
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Canvas
import numpy as np
import random
from datetime import datetime


win = tk.Tk()

# basic appearance
win.title("Sudoku")
win.geometry('625x650')
win.resizable(0,0)

for row in range (9):
    for col in range (9): 
        globals()[f"var{row}{col}"]=IntVar()
        globals()[f"e{row}{col}"]=Entry(win,textvariable=globals()[f"var{row}{col}"],width=3,font=('times new roman',20),justify = CENTER)
        globals()[f"e{row}{col}"].place(x=col*70,y=row*60)

        
can=Canvas(win, width=7, height=510)
can.place(x=400,y=0)
canvas=can.create_line(5,0,5,1100, fill="black", width=7)

can=Canvas(win, width=7, height=510)
can.place(x=193,y=0)
canvas=can.create_line(5,0,5,1100, fill="black", width=7)


can=Canvas(win, width=610, height=7)
can.place(x=0,y=160)
canvas=can.create_line(0,5,610,5, fill="black", width=7)

can=Canvas(win, width=610, height=7)
can.place(x=0,y=340)
canvas=can.create_line(0,5,610,5, fill="black", width=7)



def clear():
    for row in range (9):
        for col in range (9): 
            globals()[f"var{row}{col}"].set(0)
    global running
    running=False
    global counter
    counter=66600
            
b1=Button(win,text="Clear All",command=clear,width=10,font=('times new roman',15),justify = CENTER)
b1.place(x=10,y=600)



def New_Game():
    global s
    a=[2,3,5,6,4,7,9,8,1]
    b=[7,4,9,8,1,5,2,3,6]
    c=[6,1,8,9,2,3,7,4,5]
    d=[3,5,1,2,7,6,8,9,4]
    e=[8,7,6,3,9,4,5,1,2]
    f=[4,9,2,1,5,8,6,7,3]
    g=[9,8,4,5,6,1,3,2,7]
    h=[1,6,3,7,8,2,4,5,9]
    i=[5,2,7,4,3,9,1,6,8]
    s=np.array([a,b,c,d,e,f,g,h,i])
    
    

        #  to shuffle rows
    for j in range (9):
        i=random.randint(1,8)
        m=s[i]
        s=np.delete(s, i, axis=0)

        if (i>=0 and i<=2):
            n=random.randint(0,2)

        elif (i>=3 and i<=5):
            n=random.randint(3,5)

        elif (i>=6 and i<=8):
            n=random.randint(6,8)

        s=np.insert(s,n,m,axis=0)

         # to shuffle columns    
    for j in range (9):
        i=random.randint(1,8)
        m=s[:,i]
        s=np.delete(s, i, axis=1)

        if (i>=0 and i<=2):
            n=random.randint(0,2)

        elif (i>=3 and i<=5):
            n=random.randint(3,5)

        elif (i>=6 and i<=8):
            n=random.randint(6,8)

        s=np.insert(s,n,m,axis=1)

     # to shuffle row wise matraices
    for j in range (9):
        i=random.choice([0,3,6])
        m=s[i:i+3]
        s=np.delete(s,[i,i+1,i+2], axis=0)
        n=random.choice([0,3])
        s=np.insert(s,n,m,axis=0)

    # to shuffle column wise matraices
    for j in range (9):
        i=random.choice([0,3,6])
        m=s[0:,i:i+3]
        m=m.T
        s=np.delete(s,[i,i+1,i+2], axis=1)
        n=random.choice([0,3])
        s=np.insert(s,n,m,axis=1)


    for i in range (35):
        row=random.randint(0,8)
        col=random.randint(0,8)
        globals()[f"var{row}{col}"].set(s[row][col])
    print(s)
    
    global running
    running=True
    counter_label(label)

b2=Button(win,text="New Game",command=New_Game,width=10,font=('times new roman',15),justify = CENTER)
b2.place(x=150,y=600)


def check():
    count=0
    for row in range (9):
        for col in range (9): 
            globals()[f"x{row}{col}"]=globals()[f"var{row}{col}"].get()
            if globals()[f"x{row}{col}"]!=s[row][col]:
                count+=1
                globals()[f"e{row}{col}"].configure(bg='red')
            else :
                globals()[f"e{row}{col}"].configure(bg='white')
                
    if count==0:
        messagebox.showinfo('Congratulations','Correct Solution')
        global running
        running=False
        global counter
        counter=66600
    
            
b3=Button(win,text="Check",command=check,width=10,font=('times new roman',15),justify = CENTER)
b3.place(x=290,y=600)



def solution():
    count=0
    for row in range (9):
        for col in range (9): 
            globals()[f"x{row}{col}"]=globals()[f"var{row}{col}"].get()
            if globals()[f"x{row}{col}"]!=s[row][col]:
                count+=1
    
    global running
    running=False
    global counter
    counter=66600
    
    if count>0:
        messagebox.showinfo('Game Over','Wrong Solution')
    else:
        messagebox.showinfo('Congratulations','Correct Solution ')
        
    for row in range (9):
        for col in range (9): 
            globals()[f"e{row}{col}"].configure(bg='white')
            globals()[f"var{row}{col}"].set(s[row][col])
    
    

b4=Button(win,text="Solution",command=solution,width=10,font=('times new roman',15),justify = CENTER)
b4.place(x=430,y=600)


label = Label(win, text="00:00:00", fg="black", font="Verdana 30 bold")
label.place(x=175,y=530)
f = tk.Frame(win)

counter = 66600
running = False
def counter_label(label):
    def count():
        if running:
        
            global counter
            tt = datetime.fromtimestamp(counter)
            display = tt.strftime("%H:%M:%S")
            label['text']=display # Or label.config(text=display)
            label.after(1000, count)
            counter += 1
    count()	


win.mainloop()


# In[ ]:





# In[ ]:




