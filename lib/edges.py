from typing import List, Tuple

def roads() -> List[Tuple[str, str, int, int]]:
    return [
        ("Amsterdam", "Rotterdam", 100, 130), 
        ("Amsterdam", "Utrecht", 35, 130),
        ("Rotterdam", "Den Haag", 35, 100), 
        ("Alkmaar", "Amsterdam", 20, 100),
        ("Goes", "Veere", 20, 100), 
        ("Leiden", "Delft", 10, 100),
        ("Hengelo", "Enschede", 15, 130),
        ("Assen", "Zwolle", 80, 130), 
        ("Maastricht", "Eindhoven", 120, 130), 
        ("Utrecht", "Delft", 80, 100),
        ("Rotterdam", "Delft", 35, 100), 
        ("Zwolle", "Utrecht", 60, 100), 
        ("Eindhoven", "Den Haag", 120, 100)
    ]