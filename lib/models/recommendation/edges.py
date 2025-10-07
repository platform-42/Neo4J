from typing import List, Tuple, Dict

def create_likes() -> List[Tuple[str, str, Dict[str, int | str]]]:
    return [
        ("Alice", "Inception", {"rating": 5, "watched_times": 3, "timestamp": "2025-10-01"}),
        ("Alice", "Avatar", {"rating": 4, "watched_times": 2, "timestamp": "2025-09-20"}),
        ("Bob", "Interstellar", {"rating": 5, "watched_times": 4, "timestamp": "2025-10-02"}),
        ("Bob", "Inception", {"rating": 4, "watched_times": 1, "timestamp": "2025-09-15"}),
        ("Bob", "Dog Soldier", {"rating": 5, "watched_times": 1, "timestamp": "2025-10-01"}),
        ("Carol", "Basic Instinct", {"rating": 5, "watched_times": 2, "timestamp": "2025-09-10"}),
        ("Carol", "Titanic", {"rating": 5, "watched_times": 2, "timestamp": "2025-09-10"}),
        ("Carol", "Avatar", {"rating": 4, "watched_times": 3, "timestamp": "2025-10-01"}),
        ("Kiran", "Titanic", {"rating": 5, "watched_times": 7, "timestamp": "2025-10-01"}),
        ("Diederick", "Few Good Men", {"rating": 5, "watched_times": 1, "timestamp": "2025-10-01"}),
        ("Diederick", "39 Steps", {"rating": 5, "watched_times": 1, "timestamp": "2025-10-01"}),
        ("Sachin", "Night Moves", {"rating": 5, "watched_times": 1, "timestamp": "2025-10-01"}),
    ]

def create_movie_genres() -> List[Tuple[str, str]]:
    return [
        ("Inception", "Sci-Fi"),
        ("Interstellar", "Sci-Fi"),
        ("Avatar", "Sci-Fi"),
        ("Titanic", "Romance"),
        ("Basic Instinct", "Romance"),
        ("Dog Soldier", "Drama"),
        ("Few Good Men", "Drama"),
        {"39 Steps", "Thriller"},
        {"Night Moves", "Drama"}
]
