import sys
import os
import json
import random
from datetime import datetime, timedelta

def get_data_folder():
    """
    Gibt den Pfad zum Datenordner zurück, unabhängig davon, ob das Skript als ausführbare Datei oder als Skript ausgeführt wird.

    Returns:
        str: Der Pfad zum Datenordner.
    """
    if getattr(sys, 'frozen', False):
        data_folder_path = sys._MEIPASS
    else:
        data_folder_path = os.path.dirname(
            os.path.abspath(sys.modules['__main__'].__file__)
        )
    return data_folder_path


def get_rnd_datetime():
    _dateTime = datetime(2024, 10, 31, random.randint(0, 23), random.randint(0, 59), random.randint(0, 59))
    return _dateTime

    random_time = f"{hour:02d}:{minute:02d}:{second:02d}"
    start_date = datetime(2024, 1, 1)  # Startdatum
    end_date = datetime(2024, 12, 31)  # Enddatum
    random_days = random.randint(0, (end_date - start_date).days)
    random_date = start_date + timedelta(days=random_days)
    return f"{random_date}{random_time}"


def get_rnd_time():
    _dateTime = f"{random.randint(0, 23)}:{random.randint(0, 59)}"
    return _dateTime

def get_rnd_fluggesellschaft():
    with open(f"{get_data_folder()}/data/randomData.json", "r", encoding="utf8") as f:
        data = json.loads(f.read())
        fluggesellschaft = random.choice(data["fluggesellschaften"])
        return fluggesellschaft["name"], f"{fluggesellschaft['kennung']}{random.randint(1000, 9999)}"

def get_rnd_ziel():
    with open(f"{get_data_folder()}/data/randomData.json", "r", encoding="utf8") as f:
        data = json.loads(f.read())
        flugziel = random.choice(data["flugziele"])
        return flugziel["ziel"]
        
def get_rnd_gate():
    return f"Gate {random.randint(1, 10)}"

def get_rnd_Status():
    status = [["Normal", 0.5], ["Verspätet", 0.2], ["Fällt aus", 0.1]]
    return f"{random.choices([i[0] for i in status], weights = [i[1] for i in status])[0]}"