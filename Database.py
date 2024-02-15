import sqlite3
from datetime import datetime, timedelta
import random

class Database:
    def __init__(self, db_name='fluge.db'):
        """
        Initialisiert eine Datenbank mit einem Standardnamen.

        Args:
            db_name (str, optional): Der Name der Datenbank (default ist 'fluge.db').

        Returns:
            None
        """
        self.tables = ["Ankunft", "Abflug"]
        self.db_name = db_name
        self.create_all_tables()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def create_all_tables(self):
        """
        Erstellt alle Tabellen in der Datenbank.

        Returns:
            None
        """
        for table in self.tables:
            self.create_table(table)

    def create_table(self, table):
        """
        Erstellt eine Tabelle in der Datenbank.

        Args:
            table (str): Der Name der Tabelle.

        Returns:
            None
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {table} (flight_code TEXT ,"+
                    "timestamp TEXT, abflugzeit TEXT, ankunftzeit TEXT,"+
                    "fluggesellschaft TEXT,gate TEXT,status TEXT,ziel TEXT)")

    def set_entries(self, table, data):
        """
        Fügt Datensätze in eine Tabelle ein.

        Args:
            table (str): Der Name der Tabelle.
            data (dict): Ein Dictionary von Flugdaten.

        Returns:
            None
        """
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
        """
        Ruft alle Datensätze aus einer Tabelle ab.

        Args:
            table (str): Der Name der Tabelle.

        Returns:
            dict: Ein Dictionary von Flugdaten.
        """
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
        """
        Überprüft alle Datensätze in allen Tabellen auf Verfallszeit.

        Returns:
            None
        """
        for table in self.tables:
            self.check_entries(table)

    def check_entries(self, table):
        """
        Überprüft die Datensätze in einer Tabelle auf Verfallszeit.

        Args:
            table (str): Der Name der Tabelle.

        Returns:
            bool: True, wenn mindestens ein Datensatz veraltet ist, andernfalls False.
        """
        current_time = datetime.now()
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {table}")
            rows = cursor.fetchall()
            for row in rows:
                timestamp = datetime.strptime(row[1], "%H:%M:%S %d.%m.%Y")
                if current_time - timestamp > timedelta(minutes=1) and random.randint(0, 2) > 0:
                    return True
            return False

    def get_datetime(self, table=None):
        """
        Ruft den Zeitstempel des ersten Datensatzes in einer Tabelle ab.

        Args:
            table (str, optional): Der Name der Tabelle (default ist None, um die erste Tabelle zu verwenden).

        Returns:
            str: Der Zeitstempel im Format "%H:%M:%S %d.%m.%Y".
        """
        if table is None:
            for table_tmp in self.tables:
                table = table_tmp
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT timestamp FROM {table}")
            return cursor.fetchone()[0]

    def delete_all_entries(self):
        """
        Löscht alle Datensätze in allen Tabellen.

        Returns:
            None
        """
        for table in self.tables:
            self.delete_entries(table)

    def delete_entries(self, table):
        """
        Löscht alle Datensätze in einer Tabelle.

        Args:
            table (str): Der Name der Tabelle.

        Returns:
            None
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM {table}")
