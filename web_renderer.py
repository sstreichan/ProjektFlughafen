from web_server import web_server
import os
from flask import Flask, render_template
import util

class web_renderer(web_server):
    app = None
    def __init__(self):
        super().__init__()
        app = web_server.app
        
    def render_page(self, content_name, text=None):
        """
        Rendert eine HTML-Seite basierend auf Vorlagen und Inhalten.

        Args:
            content_name (str): Der Name des Inhalts, der gerendert werden soll.
            text (str, optional): Ein zusätzlicher Text, der in die Seite eingefügt werden soll.

        Returns:
            str: Der gerenderte HTML-Code für die Seite.
        """
        with open(
            f"{util.get_data_folder()}/templates/index.html", "r", encoding="utf8"
        ) as f:
            result = f.read()
        with open(
            f"{util.get_data_folder()}/templates/head.html", "r", encoding="utf8"
        ) as f:
            result = result.replace("$head$", f.read())

        with open(
            f"{util.get_data_folder()}/templates//nav.html", "r", encoding="utf8"
        ) as f:
            result = result.replace("$nav$", f.read())

        if os.path.exists(f"{util.get_data_folder()}/templates/{content_name}.html"):
            with open(
                f"{util.get_data_folder()}/templates/{content_name}.html",
                "r",
                encoding="utf8",
            ) as f:
                result = result.replace("$content$", f.read())
        else:
            result = result.replace("$content$", content_name)

        if text is not None:
            result = result.replace("$text$", text)

        with open(
            f"{util.get_data_folder()}/templates/foot.html", "r", encoding="utf8"
        ) as f:
            result = result.replace("$head$", f.read())

        return result
    
    
    #@app.route("/old")
    def home_old(self):
        try:
            with open(
                f"{util.get_data_folder()}/data/Flugzeug.json", "r", encoding="utf8"
            ) as f:
                data = json.load(f)
        except FileNotFoundError:
            with open("/data/Flugzeug.json", "r", encoding="utf8") as f:
                data = json.loads(f.read())

        sorted_data = {
            k: v
            for k, v in sorted(
                data.items(), key=lambda item: item[1]["Flugdaten"]["abflugzeit"]
            )
        }

        sorted_data = dict(
            sorted(data.items(), key=lambda item: item[1]["Flugdaten"]["abflugzeit"])
        )

        for flight_data in data.items():
            flight_data["Flugdaten"]["abflugzeit"] = datetime.strptime(
                flight_data["Flugdaten"]["abflugzeit"], "%Y-%m-%dT%H:%M:%S.%f"
            )
        for flight_data in data.items():
            flight_data["Flugdaten"]["ankunftzeit"] = datetime.strptime(
                flight_data["Flugdaten"]["ankunftzeit"], "%Y-%m-%dT%H:%M:%S.%f"
            )

        print(sorted_data)
        result = render_template("FlugplanOld.html", data=sorted_data)

        return web_renderer.render_page(result)

    @web_server.app.route("/")
    def home():
        data = util.get_all()

        # data = datenbank_funktionen.get_all() # Wenn sql implementiert

        sorted_data = dict(
            sorted(data.items(), key=lambda item: item[1]["flugdaten"]["abflugzeit"])
        )
        result = render_template("Flugplan.html", data=sorted_data)
        return web_renderer.render_page(None, result)

    @web_server.app.route("/erweitert")
    def erweitert(self):
        return "todo"