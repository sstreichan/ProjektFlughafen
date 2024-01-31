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