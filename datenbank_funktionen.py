import sqlite3
import util
import datetime

dbFile = f"{util.get_data_folder()}terminal.db"
def show_all():
     conn = sqlite3.connect(dbFile)
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

def show_all2():
    tables = ["flugzeuge", "anbieter", "ziele"]
    with sqlite3.connect(dbFile) as conn:
        cur = conn.cursor()
        for table in tables:
            print(table.capitalize())
            cur.execute(f"SELECT rowid, * FROM {table}")
            items = cur.fetchall()
            for item in items:
                print(item)
        conn.commit()
        

def show_flugzeuge():
     conn = sqlite3.connect(dbFile)
     cur = conn.cursor()      
     cur.execute("SELECT rowid, * FROM flugzeuge")
     items = cur.fetchall()

     for item in items:
          print(item)

     conn.commit()
     conn.close()

def show_anbieter():
     conn = sqlite3.connect(dbFile)
     cur = conn.cursor()      
     cur.execute("SELECT rowid, * FROM anbieter")
     items = cur.fetchall()

     for item in items:
          print(item)

     conn.commit()
     conn.close()

def show_ziele():
     conn = sqlite3.connect(dbFile)
     cur = conn.cursor()      
     cur.execute("SELECT rowid, * FROM ziele")
     items = cur.fetchall()

     for item in items:
          print(item)

     conn.commit()
     conn.close()

def add_flugzeug(name,code,leer,max):
     conn = sqlite3.connect(dbFile)
     cur = conn.cursor()
     cur.execute("INSERT INTO flugzeuge VALUES (?,?,?,?)", (name,code,leer,max))
     conn.commit()
     conn.close()

def add_anbieter(name,code):
     conn = sqlite3.connect(dbFile)
     cur = conn.cursor()
     cur.execute("INSERT INTO anbieter VALUES (?,?)", (name,code))
     conn.commit()
     conn.close()

def add_ziel(name,code):
     conn = sqlite3.connect(dbFile)
     cur = conn.cursor()
     cur.execute("INSERT INTO ziele VALUES (?,?)", (name,code))
     conn.commit()
     conn.close()


def set_Ankuftzeit(zeit:datetime)->bool:
     pass

def set_Abflugzeit(zeit:datetime)->bool:
     pass
     
def set_gate(gate:str)->bool:
     pass

def set_status(status:str)->bool:
     pass

def set_all(ankuftzeit: datetime, abflugzeit: datetime, gate: str, status: str)->bool:
    # Alle werte einmal setzen
    pass

def get_Ankuftzeit()->datetime:
     pass

def get_Abflugzeit()->datetime:
     pass
     
def get_gate()->str:
     pass

def get_status()->str:
     pass

def get_all()->tuple:
     return (get_Ankuftzeit(), get_Abflugzeit(),get_gate(),get_status())
