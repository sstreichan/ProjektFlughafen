#                                       Importiere SQLite
# -----------------------------------------------------------------------------------------------
import sqlite3

#                           Erstelle/Verbinde eine Datenbank(immer nötig)
# -----------------------------------------------------------------------------------------------
# mit Dateipfad
# conn = sqlite3.connect('C:\\Localer\\pfad\\zur\\datenbank\\terminal.db')

# ohne dateipfad(nutzt den Pfad des Terminals)
conn = sqlite3.connect("terminal.db")

#                                     Erstelle einen Cursor
# -----------------------------------------------------------------------------------------------
cur = conn.cursor()

#                       Erstelle einen Table(mit Dogstring)[table:flugzeuge]
# -----------------------------------------------------------------------------------------------
# cur.execute("""CREATE TABLE IF NOT EXISTS flugzeuge (
#           name text,
#           code text,
#           leergewicht text,
#           maximalgewicht text
#     )""")

#                      Erstelle einen Table(mit Dogstring)[table:anbieter]
# -----------------------------------------------------------------------------------------------
# cur.execute("""CREATE TABLE IF NOT EXISTS anbieter (
#           name text,
#           kürzel text
#     )""")

#                      Erstelle einen Table(mit Dogstring)[table:ziele]
# -----------------------------------------------------------------------------------------------
# cur.execute("""CREATE TABLE IF NOT EXISTS ziele (
#           name text,
#           kürzel text
#     )""")

#                           Mehrere einträge erstellen(flugzeug)
# -----------------------------------------------------------------------------------------------
# fLugzeug_liste = [
#     ('Boeing 737-100', '731', '41145', '77565'),
#     ('Boeing 737-200', '732', '42080', '84000'),
#     ('Boeing 737-300', '733', '45230', '82080'),
#     ('Boeing 737-400', '734', '49800', '82080'),
#     ('Boeing 737-500', '735', '56400', '68000'),
#     ('Boeing 737-600', '736', '60830', '68000'),
#     ('Boeing 737-700', '737', '62820', '85100'),
#     ('Boeing 737-800', '738', '70440', '79015'),
#     ('Boeing 737-900', '739', '70430', '88265'),
#     ('Boeing 737 MAX', '740', '72500', '88300'),
#     ('Boeing 747-100', '741', '162400', '378840'),
#     ('Boeing 747-200', '742', '168380', '833000'),
#     ('Boeing 747-300', '743', '178756', '833000'),
#     ('Boeing 747-400', '744', '178756', '987000'),
#     ('Boeing 767-200', '745', '90001', '179170'),
#     ('Boeing 767-300', '746', '91636', '181610'),
#     ('Boeing 767-400', '747', '91999', '187700'),
#     ('Boeing 777-200', '748', '132200', '263610'),
#     ('Boeing 777-300', '749', '166930', '347810'),
#     ('Boeing 787-8', '750', '119500', '227930'),
#     ('Boeing 787-9', '751', '127900', '254011'),
# ]

# cur.executemany("INSERT INTO flugzeuge VALUES (?,?,?,?)", fLugzeug_liste)


#                           Mehrere einträge erstellen(anbieter)
# -----------------------------------------------------------------------------------------------
# anbieter_liste = [
#     ('StarWings', 'SW'),
#     ('AirExample', 'AE'),
#     ('SkyJet', 'SJ'),
#     ('GlobalFly', 'GF'),
# ]

# cur.executemany("INSERT INTO anbieter VALUES (?,?)", anbieter_liste)


#                           Mehrere einträge erstellen(ziele)
# -----------------------------------------------------------------------------------------------
# ziele_liste = [
#     ('Augsburg / Deutschland', 'AGB'),
#     ('Dortmund / Deutschland', 'DTM'),
#     ('Bremen / Deutschland', 'BRE'),
#     ('Berlin-Tegel / Deutschland', 'TXL'),
#     ('Agadir / Marokko', 'AGA'),
#     ('Djerba / Tunesien', 'DJE'),
#     ('Colombo / Sri Lanka	', 'CMB'),
#     ('Peking / China', 'PEK'),
#     ('Boston / USA', 'BOS'),
#     ('Calgary / Kanada', 'YYC'),
#     ('Fuerteventura / Spanien', 'FUE'),
#     ('Korfu / Griechenland', 'CFU'),
# ]

# cur.executemany("INSERT INTO ziele VALUES (?,?)", ziele_liste)


#                       Selecte den Table mit id (wähle zwischen diesen)
# -----------------------------------------------------------------------------------------------
# cur.execute("Select rowid, * FROM flugzeuge")

# cur.execute("Select rowid, * FROM anbieter")

# cur.execute("Select rowid, * FROM ziele")


#                                  einfache fetch befehle
# -----------------------------------------------------------------------------------------------
# print(cur.fetchone())

# print(cur.fetchmany())

# print(cur.fetchall())

#                              Reihen untereinander darstellen
# -----------------------------------------------------------------------------------------------

# items = cur.fetchall()

# for item in items:
#     print(item)

#                                           info print
# -----------------------------------------------------------------------------------------------
# print("Butterfinger")


#                               Lese alle table aus
# -----------------------------------------------------------------------------------------------
print("Flugzeuge")
cur.execute("Select rowid, * FROM flugzeuge")

items = cur.fetchall()

for item in items:
    print(item)

print("Anbieter")

cur.execute("Select rowid, * FROM anbieter")

items = cur.fetchall()

for item in items:
    print(item)

print("Ziele")

cur.execute("Select rowid, * FROM ziele")

items = cur.fetchall()

for item in items:
    print(item)

#                              ende bitte immer hinzufügen
# -----------------------------------------------------------------------------------------------

# #Absenden
conn.commit()

# Schließen
conn.close()
