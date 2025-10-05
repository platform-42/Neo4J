from typing import List, Tuple

def u2_line() -> List[Tuple[str, str, float]]:
    return [
        ("Pankow", "Vinetastraße", 1.2),
        ("Vinetastraße", "Schönhauser Allee", 0.9),
        ("Schönhauser Allee", "Eberswalder Straße", 1.1),
        ("Eberswalder Straße", "Senefelderplatz", 1.0),
        ("Senefelderplatz", "Rosa-Luxemburg-Platz", 0.8),
        ("Rosa-Luxemburg-Platz", "Alexanderplatz", 0.7),
        ("Alexanderplatz", "Klosterstraße", 1.0),
        ("Klosterstraße", "Märkisches Museum", 0.6),
        ("Märkisches Museum", "Spittelmarkt", 0.8),
        ("Spittelmarkt", "Hausvogteiplatz", 0.7),
        ("Hausvogteiplatz", "Stadtmitte", 0.5),
        ("Stadtmitte", "Mohrenstraße", 0.6), # in with U6
        ("Mohrenstraße", "Potsdamer Platz", 0.7),
        ("Potsdamer Platz", "Mendelssohn-Bartholdy-Park", 0.8),
        ("Mendelssohn-Bartholdy-Park", "Gleisdreieck", 0.9),
        ("Gleisdreieck", "Bülowstraße", 0.8),
        ("Bülowstraße", "Nollendorfplatz", 1.0),
        ("Nollendorfplatz", "Wittenbergplatz", 0.9),
        ("Wittenbergplatz", "Zoologischer Garten", 1.2),
        ("Zoologischer Garten", "Ernst-Reuter-Platz", 1.1),
        ("Ernst-Reuter-Platz", "Deutsche Oper", 0.9),
        ("Deutsche Oper", "Bismarckstraße", 0.7),
        ("Bismarckstraße", "Sophie-Charlotte-Platz", 0.8),
        ("Sophie-Charlotte-Platz", "Kaiserdamm", 0.7),
        ("Kaiserdamm", "Theodor-Heuss-Platz", 1.0),
        ("Theodor-Heuss-Platz", "Neu-Westend", 0.8),
        ("Neu-Westend", "Olympia-Stadion", 1.5),
        ("Olympia-Stadion", "Ruhleben", 1.2)
    ]

def u3_line() -> List[Tuple[str, str, float]]:
    return [
    ]

def u6_line() -> List[Tuple[str, str, float]]:
    return [
        ("Alt-Tegel", "Borsigwerke", 0.9),
        ("Borsigwerke", "Holzhauser Straße", 0.8),
        ("Holzhauser Straße", "Otisstraße", 0.7),
        ("Otisstraße", "Scharnweberstraße", 1.0),
        ("Scharnweberstraße", "Kurt-Schumacher-Platz", 1.2),
        ("Kurt-Schumacher-Platz", "Afrikanische Straße", 1.4),
        ("Afrikanische Straße", "Rehberge", 0.8),
        ("Rehberge", "Seestraße", 0.9),
        ("Seestraße", "Leopoldplatz", 0.7),
        ("Leopoldplatz", "Wedding", 0.9),
        ("Wedding", "Reinickendorfer Straße", 0.7),
        ("Reinickendorfer Straße", "Schwartzkopffstraße", 0.9),
        ("Schwartzkopffstraße", "Naturkundemuseum", 0.8),
        ("Naturkundemuseum", "Oranienburger Tor", 0.7),
        ("Oranienburger Tor", "Friedrichstraße", 0.6),
        ("Friedrichstraße", "Französische Straße", 0.5),
        ("Französische Straße", "Stadtmitte", 0.4),     # interchange with U2
        ("Stadtmitte", "Kochstraße", 0.6),
        ("Kochstraße", "Hallesches Tor", 1.2),
        ("Hallesches Tor", "Mehringdamm", 0.8),         # interchange with U1/U3
        ("Mehringdamm", "Platz der Luftbrücke", 1.0),
        ("Platz der Luftbrücke", "Paradestraße", 0.9),
        ("Paradestraße", "Tempelhof", 1.2),
        ("Tempelhof", "Alt-Tempelhof", 0.7),
        ("Alt-Tempelhof", "Kaiserin-Augusta-Straße", 0.8),
        ("Kaiserin-Augusta-Straße", "Ullsteinstraße", 0.7),
        ("Ullsteinstraße", "Westphalweg", 0.9),
        ("Westphalweg", "Alt-Mariendorf", 0.8),
    ]
