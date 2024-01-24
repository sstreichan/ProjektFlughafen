import json
import random
from Utilities import get_data_folder
from abc import ABC, abstractmethod


class Fahrzeug(ABC):
    def __init__(self, _name="", _speed=0, _passagiere=0, _gewicht=0):
        """
        Initialisiert eine neue Instanz der Klasse.

        Parameter:
            _name (str): Der Name des Fahrzeugs. Falls leer, wird ein zufälliger Name gewählt.
            _speed (int): Die Geschwindigkeit des Fahrzeugs.
            _passagiere (int): Die Anzahl der Passagiere im Fahrzeug.
            _gewicht (int): Das Gewicht des Fahrzeugs.

        Rückgabe:
            Keine
        """
        try:           
            if _name == "":
                _name = random.choice(list(self.data.keys()))

            self.name = _name
            self.speed = _speed
            self.data = self.data[_name]

            self.speed_max = int(self.data["speed"])
            self.gewicht_leer = int(self.data["leerGewicht"])
            self.gewicht_max = int(self.data["maximalGewicht"])
            self.passagiere_max = int(self.data["passagiere"])
            self.tank = int(self.data["tank"])
            self.reichweite = int(self.data["reichweite"])

            self.verbrauch = round(self.tank / self.reichweite * 100)
            self.gewicht = _gewicht
            self.passagiere = 0


        except KeyError:
            print(f"Fahrzeug {_name} nicht in der Datenbank")
    
    @abstractmethod
    def loadJSON(name):
        pass    
    
    def __str__(self):
        """
        Gibt eine formatierte Zeichenkette (String) zurück, die Informationen über das Objekt enthält.

        Returns:
            str: Eine formatierte Zeichenkette mit den Attributen des Objekts, einschließlich Name, Geschwindigkeit,
                Gewicht, Anzahl der Passagiere und Verbrauch.
        """
        return (
            f"{self.name} geschwindigkeit (km/h): {self.speed}/{self.speed_max} "
            f"gewicht (kg): {self.gewicht}/{self.gewicht_max} passagiere: "
            f"{self.passagiere}/{self.passagiere_max} verbrauch(l/km): "
            f"{self.verbrauch}/100"
        )
