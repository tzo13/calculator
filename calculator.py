from tkinter import *
from tkinter.ttk import *

screen = Tk()

def calculate():
    b = oeo.get()
    a = eval(b)
    oeo.delete(0,END)
    oeo.insert(END, a)


def press(num):
    oeo.insert(END, num)




def clear():
    oeo.delete(0,END)




a0 = Button(screen,text="0",command = lambda :press("0"))
a1= Button(screen,text ="1",command = lambda :press("1"))
a2= Button(screen,text ="2",command = lambda :press("2"))
a3= Button(screen,text ="3",command = lambda :press("3"))
a4= Button(screen,text ="4",command = lambda :press("4"))
a5= Button(screen,text ="5",command = lambda :press("5"))
a6= Button(screen,text ="6",command = lambda :press("6"))
a7= Button(screen,text ="7",command = lambda :press("7"))
a8= Button(screen,text ="8",command = lambda :press("8"))
a9= Button(screen,text ="9",command = lambda :press("9"))
c = Button(screen,text ="C",command = clear)
di= Button(screen,text ="/",command = lambda :press("/"))
po= Button(screen,text ="*",command = lambda :press("*"))
pro= Button(screen,text ="+",command = lambda :press("+"))
af= Button(screen,text ="-",command = lambda :press("-"))
ison= Button(screen,text="=",command =calculate)
komma = Button(screen,text=",",command = lambda :press(","))
oeo = Entry(screen, width=30)




a7.grid(row = 0, column = 0)
a8.grid(row = 0, column = 1)
a9.grid(row = 0, column = 2)
a4.grid(row = 1, column = 0)
a5.grid(row = 1, column = 1)
a6.grid(row = 1, column = 2)
a1.grid(row = 2, column = 0)
a2.grid(row = 2, column = 1)
a3.grid(row = 2, column = 2)
c.grid(row = 3,column = 0)
di.grid(row = 3, column = 3)
af.grid(row = 2,column = 3)
pro.grid(row = 0, column = 3)
po.grid(row = 1,column = 3)
a0.grid(row = 3, column = 1)
ison.grid(row = 4, column =0)
komma.grid(row = 3,column = 2)
oeo.grid(row= 4, column = 1,columnspan= 3)




screen.mainloop()