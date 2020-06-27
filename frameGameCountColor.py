from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
import time
import pygame
pygame.font.init()

colorset=['blue','red','yellow','pink','green','black','red','pink','green','black']
global i
i=0
global redcount
redcount=0
global greencount
greencount=0 
global canvas 
global canvas1 
global canvas2
global var

def startgame():
    global canvas 
    s=startclick()
    if s==1:
        time.sleep(5)
        messagebox.showinfo("answer","number of red ball:"+str(redcount)+"number of grren ball:"+str(greencount))
    t=txt1.get()
    t1=txt2.get()
    if (t==redcount and t1==greencount):
            messagebox.showinfo("your answer","your answer match")
    else:
            messagebox.showinfo("your answer","your answer not  match")
    

def countDown():
    '''start countdown 10 seconds before new year starts'''

    lbl1.config(height=3, font=('times', 20, 'bold'))
    for k in range(10, 0, -1):
        lbl1["text"] = k
        root.update()
        time.sleep(1)
    lbl1.config(bg='red')
    lbl1.config(fg='white')
    lbl1["text"] = "Happy new year!"
    return mat
    
def startclick():
    global i 
    global canvas
    global canvas2
    global canvas3
    global var
    global redcount 
    global greencount
    v=var.get()
    if v==1:
        for j in range(1,26):
            for i in range(1,26):
                m=random.randint(0,10)
            if m==1 or m==6:
                redcount=redcount+1
            if m==4 or m==8:
                greencount=greencount+1
            try:
                a=random.randint(50,250)
                b=random.randint(50,300)
                canvas.create_oval(a,b,a+50,b+50,outline="white",fill=colorset[m])
                canvas.update()
            except:
                print()
    elif v==2:
        for j in range(1,35):
            for i in range(1,35):
                m=random.randint(0,10)
            if m==1 or m==6:
                redcount=redcount+1
            if m==4 or m==8:
                greencount=greencount+1
            try:
                a=random.randint(50,250)
                b=random.randint(50,300)
                canvas.create_oval(a,b,a+50,b+50,outline="white",fill=colorset[m])
                canvas.update()
            except:
                print()
    elif v==3:
       for j in range(1,50):
            for i in range(1,50):
                m=random.randint(0,10)
            if m==1 or m==6:
                redcount=redcount+1
            if m==4 or m==8:
                greencount=greencount+1
            try:
                a=random.randint(50,250)
                b=random.randint(50,300)
                canvas.create_oval(a,b,a+50,b+50,outline="white",fill=colorset[m])
                canvas.update()
            except:
                print()
    return(1)
    
root=Tk()

root.title("count the color ")
root.geometry("800x650+20+20")
canvas=Canvas(width=500,height=500,bg='#89ceeb')
canvas.place(x=20,y=20)
print(time)
w=Label(root,text="can you count the color ball ?",bg="black",fg="yellow")
w.place(x=20,y=500)
y=Label(root,text="you have 10 sec to answer the quiz",bg="black",fg="red")
y.place(x=20,y=550)



b=Button(root,text="LOGIN",bg='#e79700',width=15,height=1,font=("Open Sans",13,'bold'),fg='white',command=startgame)
b.place(x=20,y=600)

canvas1=Canvas(width=300,height=300,bg='#ee7600')
canvas1.place(x=540,y=299)

d=Label(root,text="enter the red ball count:",bg="red",fg="black")
d.place(x=600,y=300)
txt1=Entry(root,width=8)
txt1.place(x=600,y=325)

d=Label(root,text="enter the green ball count:",bg="green",fg="black")
d.place(x=601,y=350)
txt2=Entry(root,width=8)
txt2.place(x=600,y=375)


canvas2=Canvas(width=300,height=200,bg='#e70066')
canvas2.place(x=540,y=30)
var = IntVar() 
var.set("Radio")
Radiobutton(root, text='Easy', variable=var, value=1).place(x=548,y=50)
Radiobutton(root, text='Mediam', variable=var, value=2).place(x=548,y=85)
Radiobutton(root, text='Hard', variable=var, value=3).place(x=548,y=120)

root.mainloop()
