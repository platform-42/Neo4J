from typing import List, Tuple

def u2_line() -> List[Tuple[str, str, float]]:
    return [
        ("Pankow","Vinetastraße", 1.2),
        ("Vinetastraße","Schönhauser Allee", 0.9),
        ("Schönhauser Allee","Eberswalder Straße", 1.1),
        ("Eberswalder Straße","Senefelderplatz", 1.0),
        ("Senefelderplatz","Rosa-Luxemburg-Platz", 0.8),
        ("Rosa-Luxemburg-Platz","Alexanderplatz", 0.7),
        ("Alexanderplatz","Klosterstraße", 1.0),
        ("Klosterstraße","Märkisches Museum", 0.6),
        ("Märkisches Museum","Spittelmarkt", 0.8),
        ("Spittelmarkt","Hausvogteiplatz", 0.7),
        ("Hausvogteiplatz","Stadtmitte", 0.5),
        ("Stadtmitte","Mohrenstraße", 0.6),
        ("Mohrenstraße","Potsdamer Platz", 0.7),
        ("Potsdamer Platz","Mendelssohn-Bartholdy-Park", 0.8),
        ("Mendelssohn-Bartholdy-Park","Gleisdreieck", 0.9),
        ("Gleisdreieck","Bülowstraße", 0.8),
        ("Bülowstraße","Nollendorfplatz", 1.0),
        ("Nollendorfplatz","Wittenbergplatz", 0.9),
        ("Wittenbergplatz","Zoologischer Garten", 1.2),
        ("Zoologischer Garten","Ernst-Reuter-Platz", 1.1),
        ("Ernst-Reuter-Platz","Deutsche Oper", 0.9),
        ("Deutsche Oper","Bismarckstraße", 0.7),
        ("Bismarckstraße","Sophie-Charlotte-Platz", 0.8),
        ("Sophie-Charlotte-Platz","Kaiserdamm", 0.7),
        ("Kaiserdamm","Theodor-Heuss-Platz", 1.0),
        ("Theodor-Heuss-Platz","Neu-Westend", 0.8),
        ("Neu-Westend","Olympia-Stadion", 1.5),
        ("Olympia-Stadion","Ruhleben", 1.2)
    ]

def u6_line() -> List[Tuple[str, str, float]]:
    return [
        ("Französische Straße", "Stadtmitte", 0.7),
        ("Stadtmitte", "Kochstraße", 0.8)
    ]
