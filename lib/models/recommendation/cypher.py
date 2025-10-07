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

def create_movie_genres(tx: Transaction, movie_genres: List[Tuple[str, str]]) -> None:
    for movie_title, genre_name in movie_genres:
        tx.run("""
            MATCH (m:Movie {title: $movie_title}), (g:Genre {name: $genre_name})
            CREATE (m)-[:HAS_GENRE]->(g)
        """, movie_title=movie_title, genre_name=genre_name)


def recommend_movies_weighted(tx: Transaction, username: str) -> List[Dict[str, str | float | int]]:
    query: str = """
        MATCH (u:User {name: $username})-[r1:LIKED]->(m:Movie)-[:HAS_GENRE]->(g:Genre)<-[:HAS_GENRE]-(rec:Movie)<-[r2:LIKED]-(other:User)
        WHERE NOT (u)-[:LIKED]->(rec)
        WITH rec,
            SUM(r1.rating * r2.rating) AS collaborative_score,
            COUNT(DISTINCT g) AS genre_overlap
        RETURN rec.title AS recommendation, collaborative_score, genre_overlap
        ORDER BY collaborative_score DESC, genre_overlap DESC
        LIMIT 5
    """
#    print(f"{query}")
    result = tx.run(query, username=username)
    return [dict(record) for record in result]
