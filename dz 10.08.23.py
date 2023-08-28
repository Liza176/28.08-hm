from tkinter import *
import random

tk = Tk()
canvas = Canvas(tk,width=1300,height = 1000)
canvas.pack()

canvas.create_oval(200,800,300,900,fill='#A9A9A9')
canvas.create_oval(450,800,550,900,fill='#A9A9A9')
canvas.create_oval(700,800,800,900,fill='#A9A9A9')
canvas.create_oval(800,800,900,900,fill='#A9A9A9')
canvas.create_oval(1000,800,1100,900,fill='#A9A9A9')
canvas.create_oval(1100,800,1200,900,fill='#A9A9A9')

canvas.create_rectangle(100,650,350,800,fill='#ae3127')
canvas.create_rectangle(220,650,150,450,fill='#b22222')
canvas.create_rectangle(350,450,600,800,fill='#c35047')
canvas.create_rectangle(550,650,400,500,fill='#a4c3d8')
canvas.create_rectangle(600,750,700,750)
canvas.create_rectangle(1200,550,700,800,fill='#e6c85c')

canvas.create_oval(200,350,250,400,fill='#afeeee')
canvas.create_oval(340,340,240,240,fill='#91cae1')
canvas.create_oval(510,160,410,260,fill='#87CEEB')

tk.mainloop()

from tkinter import *
import random

tk = Tk()
canvas = Canvas(tk,width=130,height = 100)
canvas.pack()

canvas.create_oval(20,80,30,90,fill='#A9A9A9')
canvas.create_oval(45,80,55,90,fill='#A9A9A9')
canvas.create_oval(70,80,80,90,fill='#A9A9A9')
canvas.create_oval(80,80,90,90,fill='#A9A9A9')
canvas.create_oval(100,80,110,90,fill='#A9A9A9')
canvas.create_oval(110,80,120,90,fill='#A9A9A9')

canvas.create_rectangle(10,65,35,80,fill='#ae3127')
canvas.create_rectangle(22,65,15,45,fill='#b22222')
canvas.create_rectangle(35,45,60,80,fill='#c35047')
canvas.create_rectangle(55,65,40,50,fill='#a4c3d8')
canvas.create_rectangle(60,75,70,75)
canvas.create_rectangle(120,55,70,80,fill='#e6c85c')

canvas.create_oval(20,35,25,40,fill='#afeeee')
canvas.create_oval(34,34,24,24,fill='#91cae1')
canvas.create_oval(51,16,41,26,fill='#87CEEB')

tk.mainloop()