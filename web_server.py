import util
from datetime import datetime
import os
import json
from abc import ABC, abstractmethod
from flask import Flask, request
import threading
from time import sleep
import webbrowser


class web_server(ABC):
    """
    Abstrakte Basisklasse für einen Webserver.

    Attributes:
    app (Flask): Die Flask-App für den Webserver.
    port (int): Der Port, auf dem der Webserver läuft (Standardwert: 8080).
    """

    app = Flask(__name__, template_folder=f"{util.get_data_folder()}/templates/")

    def __init__(self):
        """
        Initialisiert eine Instanz der Webserver-Klasse.
        Der Standardport ist 8080.
        """
        self.port = 8080

    def run(self):
        """
        Startet den Webserver und öffnet den Standardwebbrowser auf der entsprechenden Adresse.
        """
        webbrowser.open(f"http://localhost:{self.port}")
        web_server.app.run(port=self.port, debug=False)

    @abstractmethod
    def render_page(content_name, text=None):
        """
        Abstrakte Methode zum Rendern einer Seite mit optionalen Textinhalten.

        Parameters:
        content_name (str): Der Name des Seiteninhalts.
        text (str): Optionaler Textinhalt für die Seite.

        Raises:
        NotImplementedError: Wenn die Methode in der abgeleiteten Klasse nicht implementiert ist.
        """
        pass

    
    def home():
        """
        Abstrakte Methode für die Startseite des Webservers.

        Raises:
        NotImplementedError: Wenn die Methode in der abgeleiteten Klasse nicht implementiert ist.
        """
        pass
    
    def abflug(self):
        """
        Abstrakte Methode für die Abflüge.

        Raises:
        NotImplementedError: Wenn die Methode in der abgeleiteten Klasse nicht implementiert ist.
        """
        pass

    def ankuft(self):
        """
        Abstrakte Methode für die Anküfte.

        Raises:
        NotImplementedError: Wenn die Methode in der abgeleiteten Klasse nicht implementiert ist.
        """
        pass


