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


def set_Ankuftzeit(row: int, zeit:datetime)->bool:
     pass

def set_Abflugzeit(row: int, zeit:datetime)->bool:
     pass
     
def set_gate(row: int, gate:str)->bool:
     pass

def set_status(row: int, status:str)->bool:
     pass

def set_all(rows: dict)->bool:     
     for row in rows:
          set_Ankuftzeit(row, row["ankuftzeit"])
          set_Abflugzeit(row, row["abflugzeit"])
          set_gate(row, row["gate"])
          set_status(row,row["status"])
     return True

def get_Ankuftzeit(row: int)->datetime:
     pass

def get_Abflugzeit(row: int)->datetime:
     pass
     
def get_gate(row: int)->str:
     pass

def get_status(row: int)->str:
     pass

def get_all()->dict:
     result = {}
     rows = 0 ##### Todo: die einzahl der rows setzen
     for row in rows:
          get_Ankuftzeit(row), get_Abflugzeit(row),get_gate(row),get_status(row)
     return result
