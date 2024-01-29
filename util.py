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
    """
    Generiert und gibt eine zufällige Datetime-Instanz zurück.

    Returns:
    datetime: Eine zufällige Datetime-Instanz im Jahr 2024, im Zeitraum von 0 bis 23 Stunden,
             0 bis 59 Minuten und 0 bis 59 Sekunden.
    """    
    return  datetime(2024, 10, 31, random.randint(0, 23), random.randint(0, 59), random.randint(0, 59))

def get_rnd_time():
    """
    Generiert und gibt eine zufällige Uhrzeit im Format HH:MM zurück.

    Returns:
    str: Eine zufällige Uhrzeit im Format HH:MM.
    """
    return f"{random.randint(0, 23)}:{random.randint(0, 59)}"

def get_rnd_fluggesellschaft():
    """
    Gibt zufällige Fluggesellschaftsdaten zurück.

    Returns:
    tuple: Ein Tupel bestehend aus dem Namen der Fluggesellschaft und einer zufälligen Kennung.
    """
    with open(f"{get_data_folder()}/data/randomData.json", "r", encoding="utf8") as f:
        data = json.loads(f.read())
        fluggesellschaft = random.choice(data["fluggesellschaften"])
        return fluggesellschaft["name"], f"{fluggesellschaft['kennung']}{random.randint(1000, 9999)}"


def get_rnd_ziel():
    """
    Gibt ein zufälliges Flugziel zurück.

    Returns:
    str: Das zufällige Flugziel.
    """
    with open(f"{get_data_folder()}/data/randomData.json", "r", encoding="utf8") as f:
        data = json.loads(f.read())
        flugziel = random.choice(data["flugziele"])
        return flugziel["ziel"]
        
def get_rnd_gate():
    """
    Gibt ein zufälliges Gate zurück.

    Returns:
    str: Der Name eines zufälligen Gates.
    """
    return f"Gate {random.randint(1, 10)}"

def get_rnd_Status():
    """
    Gibt einen zufälligen Flugstatus zurück.

    Returns:
    str: Ein zufälliger Flugstatus (Normal, Verspätet oder Fällt aus) basierend auf Gewichtungen.
    """
    status = [["Normal", 0.5], ["Verspätet", 0.2], ["Fällt aus", 0.1]]
    return f"{random.choices([i[0] for i in status], weights = [i[1] for i in status])[0]}"

def get_all():
    data = {}
    for _ in range(random.randint(10, 15)):
        fluggessellschaft, flugnummer = get_rnd_fluggesellschaft()
        data[f"{flugnummer}"] = {
            "flugdaten": {
                "abflugzeit": get_rnd_datetime(),
                "ankunftzeit": get_rnd_datetime(),
                "fluggesellschaft": fluggessellschaft,
                "gate": get_rnd_gate(),
                "status": get_rnd_Status(),
                "ziel": get_rnd_ziel(),
            }
        }
    return data
        
