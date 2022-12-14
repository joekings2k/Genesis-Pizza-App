
from tkinter import *


from numpy import True_
import managersidedb as mdb

window = Tk()
window.title("Genesis Pizza Manager System")
window.geometry("800x600")

#function to get selected rows
def getSelectedRow(event):
    try:
        global selectedTuple
        index = listboxOrders.curselection()[0]
        selectedTuple = listboxOrders.get(index)
    except:
        pass
def sumTotal():
    total=mdb.sumTotal()
    return total

#function to view all orders from the database
def viewAllOrders():
    listboxOrders.delete(0,END)
    for row in mdb.view_all():
        listboxOrders.insert(END,row)

def updateOrder(id,pizzasize,pep,chee,total):
    mdb.updateModi(id,pizzasize,pep,chee,total)
    viewAllOrders()
def deleteOrder(id):
    mdb.delete(id)
    viewAllOrders()


def viewdetailsDialog():
    try:
        viewDetails = Toplevel(window)
        lblName = Label(viewDetails,text=f"Customer Name : {selectedTuple[1]}")
        lblName.grid(column=0,row=0)
        lblPizza = Label(viewDetails,text=f"Pizza Size : {selectedTuple[2]}")
        lblPizza.grid(column=0,row=1)
        lblPep = Label(viewDetails,text=f"Pepperoni : {selectedTuple[3]}")
        lblPep.grid(column=0,row=2)
        lblChee = Label(viewDetails,text=f"Cheese : {selectedTuple[4]}")
        lblChee.grid(column=0,row=3)
        lblTotal = Label(viewDetails,text=f"Total bill : {selectedTuple[5]}")
        lblTotal.grid(column=0,row=4)
        

    except:
        lblselect =Label(viewDetails,text="select an order")
        lblselect.grid(column=0,row=0)
        pass


def updateOrdersDialog ():

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
        updateOrder(selectedTuple[0],selectedSize.upper(),pepStatment.upper(),cheeStatment.upper(),bill)
        return selectedSize,bill,pepStatment,cheeStatment

    

    
    updateOrders = Toplevel(window)
    lblName  =Label(updateOrders,text=f"Name :  {selectedTuple[1]}",font=("Arial",20))
    lblName.grid(column=0,row=0,columnspan=4)

    selected = IntVar()
    rad1 = Radiobutton(updateOrders,text="Small",value=1,variable=selected,font=("Arial",16))
    rad2 = Radiobutton(updateOrders,text="Medium",value=2,variable=selected,font=("Arial",16))
    rad3 = Radiobutton(updateOrders,text="Large",value=3,variable=selected,font=("Arial",16))
    
    rad1.grid(column=0,row=1)
    rad2.grid(column=1,row=1)
    rad3.grid(column=2,row=1)


    pepchk_state =BooleanVar()
    pepchk_state.set(False)
    pepchk = Checkbutton(updateOrders,text="Pepperoni", var=pepchk_state,font=("Arial",15))
    pepchk.grid(column=0,row=3)

    cheechk_state =BooleanVar()
    cheechk_state.set(True)
    cheechk = Checkbutton(updateOrders,text="Extra Cheese", var=cheechk_state,font=("Arial",15))
    cheechk.grid(column=0,row=4)

    pesate = BooleanVar()
    pesate.set(False)



    btnconfrim  = Button(updateOrders,text="confirm",command=checkSelectedSize)
    btnconfrim.grid(column=0,row=6)

def viewTotaldialog ():
    viewTotal = Toplevel(window)
    sumPUll  = sumTotal()
    for i in sumPUll:

        lblTotal =Label(viewTotal,text=f"TOTAL MONEY MADE :{i}" ,font=("Arial",20))
        lblTotal.grid(column=0,row=0)

    




listboxOrders = Listbox(window,width=40,height=10,font=("Arial Bold",16))
listboxOrders.grid(column=1,row=1,rowspan=4,columnspan=6,padx=10,pady=20)
#vertical scroll bar 
scb1 = Scrollbar(window,orient=VERTICAL)
scb1.grid(row=0,column=7,rowspan=6)
#horizontal scroll bar
scb2 = Scrollbar(window,orient=HORIZONTAL)
scb2.grid(row=5,column=1,columnspan=4)

btnViewDetails= Button(window,text="View Datails",font=("Arial",14),width=12,command=viewdetailsDialog)
btnViewDetails.grid(column=8,row=1)

btnUpadateOrders =Button(window,text="Update Order",font=("Arial",14),width=12,command=updateOrdersDialog)
btnUpadateOrders.grid(column=8,row=2)

btnDeleteOrders = Button(window,text="Delete Order",font=("Arial",14),width=12,command=lambda: deleteOrder(selectedTuple[0]))
btnDeleteOrders.grid(column=8,row=3)

btnAddAll = Button(window,text="view total",font=("Arial",14),width=12,command=viewTotaldialog)
btnAddAll.grid(column=8,row=4)


#to get selected row
listboxOrders.bind("<<ListboxSelect>>",getSelectedRow)

#binding the vertical scroll bar
listboxOrders.configure(yscrollcommand=scb1.set)
scb1.configure(command=listboxOrders.yview)

#binding the horizontal scroll bar 
listboxOrders.configure(xscrollcommand=scb2.set)
scb2.configure(command=listboxOrders.xview)
viewAllOrders()

window.mainloop()