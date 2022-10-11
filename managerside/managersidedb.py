import sqlite3 as sql3
from os.path import exists
file_exists = exists("GENSISPIZZA.db")


def create():
    conn = sql3.connect("GENSISPIZZA.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS orders (ID INTEGER PRIMARY KEY,  NAME TEXT, PIZZASIZE TEXT, PEPPERONI TEXT, CHEESE TEXT, TOTAL REAL)")
    conn.commit()
    conn.close()

def insert(namee, sizep, add_pep, extra_cheese, total):
    conn = sql3.connect("GENSISPIZZA.db")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO orders (NAME, PIZZASIZE, PEPPERONI, CHEESE, TOTAL) VALUES('{namee.upper()}', '{sizep.upper()}', '{add_pep.upper()}', '{extra_cheese.upper()}', '{int(total)}')")
    conn.commit()
    conn.close()

def update(id, pizzasize, pep, chee, total):
    conn = sql3.connect("GENSISPIZZA.db")
    cursor = conn.cursor()
    cursor.execute(f'UPDATE orders SET PIZZASIZE={pizzasize}, PEPPERONI={pep}, CHEESE={chee}, TOTAL={total} WHERE ID={id}')
    conn.commit()
    conn.close()

def updateModi(id,pizzasize, pep,chee,total):
    conn = sql3.connect('GENSISPIZZA.db') # Create the db 
    cursor = conn.cursor() # Create a cursor
    cursor.execute('UPDATE orders SET PIZZASIZE=?, PEPPERONI=?,CHEESE=?,TOTAL =? WHERE id=?', (pizzasize,pep,chee,total, id))
    conn.commit()
    conn.close()


def view_all():
    conn = sql3.connect("GENSISPIZZA.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows

if file_exists:
    pass
else:
    create()