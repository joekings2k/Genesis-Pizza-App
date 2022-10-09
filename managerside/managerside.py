from tkinter import *


window = Tk()
window.title("Genesis Pizza Manager System")
window.geometry("800x600")

listboxOrders = Listbox(window,width=40,height=10,font=("Arial Bold",16))
listboxOrders.grid(column=1,row=1,rowspan=4,columnspan=6,padx=10,pady=20)
#vertical scroll bar 
scb1 = Scrollbar(window,orient=VERTICAL)
scb1.grid(row=0,column=7,rowspan=6)
#horizontal scroll bar
scb2 = Scrollbar(window,orient=HORIZONTAL)
scb2.grid(row=5,column=1,columnspan=4)





#binding the vertical scroll bar
listboxOrders.configure(yscrollcommand=scb1.set)
scb1.configure(command=listboxOrders.yview)

#binding the horizontal scroll bar 
listboxOrders.configure(xscrollcommand=scb2.set)
scb2.configure(command=listboxOrders.xview)


window.mainloop()