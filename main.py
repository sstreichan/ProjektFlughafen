import random
from datetime import datetime
import os
import json
from flask import Flask, render_template
import util
from Flugzeug import Flugzeug


def render_page(content_name, text=None):
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


def main():
    app = Flask(__name__, template_folder=f"{util.get_data_folder()}/templates/")
    """
        Route für die Jeweiligen Seiten.
        
        Returns:
            str: Die gerenderte HTML-Seite für die Homepage.
    """

    @app.route("/old")
    def home_old():
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

        return render_page(result)

    @app.route("/")
    def home():
        data = util.get_all()

        sorted_data = dict(
            sorted(data.items(), key=lambda item: item[1]["flugdaten"]["abflugzeit"])
        )
        result = render_template("Flugplan.html", data=sorted_data)
        return render_page(result)

    @app.route("/erweitert")
    def erweitert():
        return "todo"

    app.run(port=8080, debug=True)


if __name__ == "__main__":
    main()
