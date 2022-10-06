import sqlite3 as sql3
from os.path import exists
file_exists = exists("GENSISPIZZA.db")



def Menu ():
    items =["Small Box = N1500........Pepperoni = N200", "Medium Box = N2000------Pepperoni = N300","Large Box = N2500------Perpperoni = N300", "Extra Cheese = N100"]
    return items

def create():
    conn = sql3.connect("GENSISPIZZA.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS orders (ID INTEGER PRIMARY KEY,  NAME TEXT, PIZZASIZE TEXT, PEPPERONI TEXT, CHEESE TEXT, TOTAL REAL)")
    conn.commit()
    conn.close()

def update(id, pizzasze, pep, chee, total):
    conn = sql3.connect("GENSISPIZZA.db")
    cursor = conn.cursor()
    cursor.execute(f'UPDATE orders SET PIZZASIZE={pizzasze}, PEPPERONI={pep}, CHEESE={chee}, TOTAL={total}, WHERE ID={id}')
    conn.commit()
    conn.close()