from typing import List

def stations_u2() -> List[str]:
    return [
        "Pankow",
        "Vinetastraße",
        "Schönhauser Allee",
        "Eberswalder Straße",
        "Senefelderplatz",
        "Rosa-Luxemburg-Platz",
        "Alexanderplatz",      # major interchange (U2, U5, U8)
        "Klosterstraße",
        "Märkisches Museum",
        "Spittelmarkt",
        "Hausvogteiplatz",
        "Stadtmitte",          # interchange (U2, U6)
        "Mohrenstraße",
        "Potsdamer Platz",
        "Mendelssohn-Bartholdy-Park",
        "Gleisdreieck",        # interchange (U1, U3)
        "Bülowstraße",
        "Nollendorfplatz",     # interchange (U1, U3, U4)
        "Wittenbergplatz",     # interchange (U1, U3)
        "Zoologischer Garten",
        "Ernst-Reuter-Platz",
        "Deutsche Oper",
        "Bismarckstraße",      # interchange (U7)
        "Sophie-Charlotte-Platz",
        "Kaiserdamm",
        "Theodor-Heuss-Platz",
        "Neu-Westend",
        "Olympia-Stadion",
        "Ruhleben"
    ]

def stations_u3() -> List[str]:
    return [
        "Krumme Lanke",
        "Onkel Toms Hütte",
        "Oskar-Helene-Heim",
        "Freie Universität (Thielplatz)",
        "Dahlem-Dorf",
        "Podbielskiallee",
        "Breitenbachplatz",
        "Rüdesheimer Platz",
        "Heidelberger Platz",
        "Fehrbelliner Platz",
        "Hohenzollernplatz",
        "Spichernstraße",     # interchange with U9
        "Augsburger Straße",
        "Wittenbergplatz"     # <-- Important! Interchange with U1 & U2
    ]

def stations_u6() -> List[str]:
    return [
        "Alt-Tegel",
        "Borsigwerke",
        "Holzhauser Straße",
        "Otisstraße",
        "Scharnweberstraße",
        "Kurt-Schumacher-Platz",
        "Afrikanische Straße",
        "Rehberge",
        "Seestraße",
        "Leopoldplatz",
        "Wedding",
        "Reinickendorfer Straße",
        "Schwartzkopffstraße",
        "Naturkundemuseum",
        "Oranienburger Tor",
        "Friedrichstraße",
        "Französische Straße",
        "Stadtmitte",
        "Kochstraße",
        "Hallesches Tor",
        "Mehringdamm",
        "Platz der Luftbrücke",
        "Paradestraße",
        "Tempelhof",
        "Alt-Tempelhof",
        "Kaiserin-Augusta-Straße",
        "Ullsteinstraße",
        "Westphalweg",
        "Alt-Mariendorf"
    ]

def stations(*station_lists: List[str]) -> List[str]:
    stations: List[str] = []
    stations_processed: set[str] = set()

    for station in [s for station_list in station_lists for s in station_list]:
        if station not in stations_processed:
            stations_processed.add(station)
            stations.append(station)
    return stations
