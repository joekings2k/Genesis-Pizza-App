from cProfile import label
from tkinter import *
import menu as m
from matplotlib.pyplot import grid


window= Tk()
window.title("Genesis Pizza System")
window.geometry("800x600")
def viewMenu():
    listboxmenu.delete(0,END)
    for i in m.Menu():
        listboxmenu.insert(END,i)


lblMenu = Label(window,text="MENU",font=("Helvetica Bold",26))
lblMenu.grid(row=0,column=1,columnspan=4)
listboxmenu = Listbox(window,width=45,height=10,font=("Arial Bold",16),fg="#643173")
listboxmenu.grid(column=1,row=1,rowspan=4,columnspan=6)

lblName =Label(window,text="Name:",font=("Arial",17))
lblName.grid(row=6,column=0)

entryName= Entry(window,width=30,font=("Arial",15))
entryName.grid(row=6,column=1,columnspan=4)

lblPizza= Label(window,text="PIZZA",font=("Arial",14))
lblPizza.grid(row=7,column=0)

selected = IntVar()
rad1 = Radiobutton(window,text="Small",value=1,variable=selected)
rad2 = Radiobutton(window,text="Medium",value=2,variable=selected)
rad3 = Radiobutton(window,text="Large",value=3,variable=selected)

rad1.grid(column=1,row=7)
rad2.grid(column=2,row=7)
rad3.grid(column=3,row=7)


pepchk_state =BooleanVar()
pepchk_state.set(False)
pepchk = Checkbutton(window,text="Pepperoni", var=pepchk_state,font=("Arial",15))
pepchk.grid(column=0,row=8)

cheechk_state =BooleanVar()
cheechk_state.set(False)
cheechk = Checkbutton(window,text="Extra Cheese", var=cheechk_state,font=("Arial",15))
cheechk.grid(column=0,row=9)

btnPlaceOder= Button(window,text="place your order",font=("Arial",18))
btnPlaceOder.grid(column=1,row=10)

viewMenu()





window.mainloop()
