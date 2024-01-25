from Fahrzeug import Fahrzeug

class Feuerwehr(Fahrzeug):

    def __init__(self, _name="", _speed=0, _passagiere=0, _gewicht=0):
        self.load(__name__)
        super().__init__(_name, _speed, _passagiere, _gewicht)

    def __str__(self):
        return (
            f"{super().__str__()} "
            f"löschwassermenge: {self.loeschwassermenge}"
            )