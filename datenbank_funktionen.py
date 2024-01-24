import sqlite3

def show_all():
     conn = sqlite3.connect('terminal.db')
     cur = conn.cursor()

     print("Flugzeuge")

     cur.execute("SELECT rowid, * FROM flugzeuge")
     items = cur.fetchall()
     
     for item in items:
          print(item)

     print("Anbieter")

     cur.execute("SELECT rowid, * FROM anbieter")
     items = cur.fetchall()
     
     for item in items:
          print(item)

     print("Ziele")

     cur.execute("SELECT rowid, * FROM ziele")
     items = cur.fetchall()
     
     for item in items:
          print(item)

     conn.commit()
     conn.close()

def show_flugzeuge():
     conn = sqlite3.connect('terminal.db')
     cur = conn.cursor()      
     cur.execute("SELECT rowid, * FROM flugzeuge")
     items = cur.fetchall()

     for item in items:
          print(item)

     conn.commit()
     conn.close()

def show_anbieter():
     conn = sqlite3.connect('terminal.db')
     cur = conn.cursor()      
     cur.execute("SELECT rowid, * FROM anbieter")
     items = cur.fetchall()

     for item in items:
          print(item)

     conn.commit()
     conn.close()

def show_ziele():
     conn = sqlite3.connect('terminal.db')
     cur = conn.cursor()      
     cur.execute("SELECT rowid, * FROM ziele")
     items = cur.fetchall()

     for item in items:
          print(item)

     conn.commit()
     conn.close()

def add_flugzeug(name,code,leer,max):
     conn = sqlite3.connect('terminal.db')
     cur = conn.cursor()
     cur.execute("INSERT INTO flugzeuge VALUES (?,?,?,?)", (name,code,leer,max))
     conn.commit()
     conn.close()

def add_anbieter(name,code):
     conn = sqlite3.connect('terminal.db')
     cur = conn.cursor()
     cur.execute("INSERT INTO anbieter VALUES (?,?)", (name,code))
     conn.commit()
     conn.close()

def add_ziel(name,code):
     conn = sqlite3.connect('terminal.db')
     cur = conn.cursor()
     cur.execute("INSERT INTO ziele VALUES (?,?)", (name,code))
     conn.commit()
     conn.close()





















