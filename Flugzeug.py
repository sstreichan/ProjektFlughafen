import random
import json
import util
from Fahrzeug import Fahrzeug


class Flugzeug(Fahrzeug):
    anzahl_flugzeuge = 0  # Klassenvariablen
    anzahl_passagiere_gesamt = 0

    def __init__(
        self,
        _name="",
        _speed=0,
        _passagiere=0,
        _gewicht=0,
        flugnummer="",
        abflugzeit="",
        ankunftzeit="",
        fluggesellschaft="",
    ):
        """
        Initialisiert ein Flugzeug-Objekt unter Berücksichtigung der geladenen Daten.

        Args:
            _name (str, optional): Der Name des Flugzeugs.
            _speed (int, optional): Die Geschwindigkeit des Flugzeugs.
            _passagiere (int, optional): Die Anzahl der Passagiere im Flugzeug.
            _gewicht (int, optional): Das Gewicht des Flugzeugs.

        Returns:
            None
        """
        self.data = self.load_json(__name__)
        super().__init__(_name, _speed, _passagiere, _gewicht)

        self.maxFlughoehe = int(self.data["maxFlughoehe"])
        Flugzeug.anzahl_flugzeuge += 1
        Flugzeug.anzahl_passagiere_gesamt += _passagiere

        self.flugnummer = random.randint(100000, 999999)
        self.abflugzeit = abflugzeit
        self.ankunftzeit = ankunftzeit
        self.fluggesellschaft = ""

    def load_json(self, name):
        """
        Lädt Daten aus einer JSON-Datei und aktualisiert das 'data'-Attribut der Klasse.

        Args:
            name (str): Der Name der JSON-Datei (ohne die Dateierweiterung).

        Returns:
            None
        """
        try:
            with open(
                f"{util.get_data_folder()}/data/{name}.json", "r", encoding="utf8"
            ) as f:
                return json.loads(f.read())
        except FileNotFoundError:
            with open(f"/data/{name}.json", "r", encoding="utf8") as f:
                return json.loads(f.read())

