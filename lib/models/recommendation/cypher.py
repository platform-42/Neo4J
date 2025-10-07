from neo4j import Transaction
from strenum import StrEnum
from typing import List, Dict

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
