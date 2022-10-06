from cProfile import label
from tkinter import *
import menu as m
from matplotlib.pyplot import grid
# import calculatePrice as CP


window= Tk()
window.title("Genesis Pizza System")
window.geometry("800x600")

def orderInfoDialog ():
    orderInfo = Toplevel(window)
    orderInfo.geometry("200x200")
    orderNameLabel = Label(orderInfo,text=f"Name: {entryName.get()}",font=("Arial",16))
    orderNameLabel.grid(column=0,row=0)
    
    PizzaSize = Label(orderInfo,text=f"Pizza Size : {selectedSize}",font=("Arial",16))
    PizzaSize.grid(column=0,row=1)

    Pepperoni = Label(orderInfo,text=f"Pepperoni:{pepStatment}",font=("Arial",16))
    Pepperoni.grid(column=0,row=2) 

    cheese = Label(orderInfo,text=f"Cheese:{cheeStatment}",font=("Arial",16))
    cheese.grid(column=0,row=3) 
    btnConfirm = Button(orderInfo,text="CONFIRM",font=("Arial",16),fg="green")
    btnConfirm.grid(column=0,row=4)
   



def viewMenu():
    listboxmenu.delete(0,END)
    for i in m.Menu():
        listboxmenu.insert(END,i)

def checkSelectedSize ():
    global bill
    global selectedSize
    global pepStatment
    global cheeStatment
    bill  = 0
    if selected.get()==1:
        selectedSize = "Small"
        bill = 1500
        print(bill)
    elif selected.get()==2:
        selectedSize ="Medium"
        bill = 2000
    elif selected.get()==3:
        selectedSize ="Large"
        bill =2500
    
    if pepchk_state.get() == True:
        pepStatment = "Yes"
        print(pepStatment)
        if selected.get()==1 :
            bill+=200
        else:
            bill+=300
    elif pepchk_state.get() == False: 
        pepStatment="No"
        print(pepStatment)

    if cheechk_state.get()==True:
        cheeStatment ="Yes"
        bill+=100
        
        print(cheeStatment)
    elif cheechk_state.get()==False:
        cheeStatment ="No"
        print(cheeStatment)
    orderInfoDialog()

    return selectedSize,bill,pepStatment,cheeStatment
    



lblMenu = Label(window,text="MENU",font=("Helvetica Bold",26))
lblMenu.grid(row=0,column=1,columnspan=4)
listboxmenu = Listbox(window,width=45,height=10,font=("Arial Bold",16),fg="#643173")
listboxmenu.grid(column=1,row=1,rowspan=4,columnspan=6)

lblName =Label(window,text="Name:",font=("Arial",17))
lblName.grid(row=6,column=0)

entryName= Entry(window,width=30,font=("Arial",20))
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

btnPlaceOder= Button(window,text="place your order",font=("Arial",18),command= checkSelectedSize )
btnPlaceOder.grid(column=1,row=10)

viewMenu()
window.mainloop()
