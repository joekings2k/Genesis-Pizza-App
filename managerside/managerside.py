from cProfile import label
from tkinter import *
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

#function to view all orders from the database
def viewAllOrders():
    listboxOrders.delete(0,END)
    for row in mdb.view_all():
        listboxOrders.insert(END,row)

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

listboxOrders = Listbox(window,width=40,height=10,font=("Arial Bold",16))
listboxOrders.grid(column=1,row=1,rowspan=4,columnspan=6,padx=10,pady=20)
#vertical scroll bar 
scb1 = Scrollbar(window,orient=VERTICAL)
scb1.grid(row=0,column=7,rowspan=6)
#horizontal scroll bar
scb2 = Scrollbar(window,orient=HORIZONTAL)
scb2.grid(row=5,column=1,columnspan=4)

btnViewDetails= Button(window,text="View Datails",font=("Arial",14),command=viewdetailsDialog)
btnViewDetails.grid(column=8,row=1)

btnUpadateOrders =Button(window,text="Upadte Order",font=("Arial",14),)
btnUpadateOrders.grid(column=8,row=2)



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