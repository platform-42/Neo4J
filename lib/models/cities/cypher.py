from neo4j import Transaction

def clear_database(tx: Transaction) -> None:
    tx.run("MATCH (n) DETACH DELETE n")

def create_city(tx: Transaction, name: str) -> None:
    tx.run("MERGE (:City {name: $name})", name=name)

def create_road(tx: Transaction, city1: str, city2: str, distance: int, max_speed: int) -> None:
    tx.run(
        """
            MATCH (a:City {name: $city1}), (b:City {name: $city2})
            MERGE (a)-[:ROAD {distance: $distance, maxSpeed: $max_speed}]->(b)
        """,
        city1=city1,
        city2=city2,
        distance=distance,
        max_speed=max_speed
    )
