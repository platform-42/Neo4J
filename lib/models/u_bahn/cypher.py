from neo4j import Transaction
from strenum import StrEnum

class Line(StrEnum):
    U1 = "U1"
    U2 = "U2"
    U3 = "U3"
    U6 = "U6"

def clear_database(tx: Transaction) -> None:
    tx.run("MATCH (n) DETACH DELETE n")

def create_station(tx: Transaction, name: str) -> None:
    tx.run("MERGE (:Station {name: $name})", name=name)

def create_track(tx: Transaction, city1: str, city2: str, line: str, distance: float) -> None:
    tx.run(
        """
            MATCH (a:Station {name: $city1}), (b:Station {name: $city2})
            MERGE (a)-[:TRACK {line: $line, distance: $distance}]->(b)
            MERGE (b)-[:TRACK {line: $line, distance: $distance}]->(a)
        """,
        city1=city1, 
        city2=city2, 
        line=line, 
        distance=distance
    )