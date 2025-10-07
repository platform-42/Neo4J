from typing import List, Dict

def create_users() -> List[Dict[str, str]]:
    return [
        {"name": "Alice"},
        {"name": "Bob"},
        {"name": "Carol"}
    ]

def create_movies() -> List[Dict[str, str]]:
    return [
        {"title": "Inception"},
        {"title": "Interstellar"},
        {"title": "Avatar"},
        {"title": "Titanic"}
    ]

def create_genres() -> List[Dict[str, str]]:
    return [
        {"name": "Sci-Fi"},
        {"name": "Romance"},
        {"name": "Bollywood"}
    ]
