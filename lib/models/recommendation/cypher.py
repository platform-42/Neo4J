from neo4j import Transaction
from typing import List, Dict, Tuple

def clear_database(tx: Transaction) -> None:
    tx.run("MATCH (n) DETACH DELETE n")

def create_users(tx: Transaction, users: List[Dict[str, str]]) -> None:
    for u in users:
        tx.run("CREATE (:User {name: $name})", name=u["name"])

def create_movies(tx: Transaction, movies: List[Dict[str, str]]) -> None:
    for m in movies:
        tx.run("CREATE (:Movie {title: $title})", title=m["title"])

def create_genres(tx: Transaction, genres: List[Dict[str, str]]) -> None:
    for g in genres:
        tx.run("CREATE (:Genre {name: $name})", name=g["name"])

def create_likes(tx: Transaction, likes: List[Tuple[str, str, Dict[str, int | str]]]) -> None:
    for username, movie_title, props in likes:
        tx.run("""
            MATCH (u:User {name: $username}), (m:Movie {title: $movie_title})
            CREATE (u)-[:LIKED {
                rating: $rating,
                watched_times: $watched_times,
                timestamp: datetime($timestamp)
            }]->(m)
        """, username=username, movie_title=movie_title,
             rating=props["rating"], watched_times=props["watched_times"],
             timestamp=props["timestamp"])