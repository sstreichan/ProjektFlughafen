import sqlite3
from datetime import datetime, timedelta
import util
import random


class Database:
    def __init__(self, db_name='fluge.db'):
        self.tables = ["Ankunft", "Abflug"]
        self.db_name = db_name
        self.create_all_tables()
        
    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass
    
    def create_all_tables(self):
        for table in self.tables:
            self.create_table(table)
        
    def create_table(self, table):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {table} (flight_code TEXT ,"+
                    "timestamp TEXT, abflugzeit TEXT, ankunftzeit TEXT,"+
                    "fluggesellschaft TEXT,gate TEXT,status TEXT,ziel TEXT)")

    def set_entries(self, table, data):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            for flight_code, flight_data in data.items():
                cursor.execute(f"INSERT INTO {table} VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (
                    flight_code,
                    datetime.now().strftime("%H:%M:%S %d.%m.%Y"),
                    flight_data["flugdaten"]["abflugzeit"].strftime("%Y-%m-%d %H:%M:%S"),
                    flight_data["flugdaten"]["ankunftzeit"].strftime("%Y-%m-%d %H:%M:%S"),
                    flight_data["flugdaten"]["fluggesellschaft"],
                    flight_data["flugdaten"]["gate"],
                    flight_data["flugdaten"]["status"],
                    flight_data["flugdaten"]["ziel"]
                ))

    def get_entries(self, table):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {table}")
            rows = cursor.fetchall()
            entries = {}
            for row in rows:
                flight_code = row[0]
                timestamp = row[1]
                abflugzeit = datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S")
                ankunftzeit = datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S")
                fluggesellschaft = row[4]
                gate = row[5]
                status = row[6]
                ziel = row[7]
                entries[flight_code] = {
                    #"timestamp": timestamp,
                    "flugdaten": {
                        "abflugzeit": abflugzeit,
                        "ankunftzeit": ankunftzeit,
                        "fluggesellschaft": fluggesellschaft,
                        "gate": gate,
                        "status": status,
                        "ziel": ziel
                    }
                }
            return entries

    def check_all_entries(self):
        for table in self.tables:
            self.check_entries(table)
            
    def check_entries(self, table):
        current_time = datetime.now()
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {table}")
            rows = cursor.fetchall()
            for row in rows:
                timestamp = datetime.strptime(row[1], "%H:%M:%S %d.%m.%Y")
                if current_time - timestamp > timedelta(minutes=1) and random.randint(0, 2) >0:
                    return True
            return False

    def get_datetime(self, table=None):
        if table is None:
            for table_tmp in self.tables:
                table = table_tmp
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT timestamp FROM {table}")
            return cursor.fetchone()[0]
        
    def delete_all_entries(self):
        for table in self.tables:
            self.delete_entries(table)

    def delete_entries(self, table):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM {table}")

