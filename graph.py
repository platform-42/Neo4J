import random

from neo4j import GraphDatabase, Transaction, Driver, basic_auth
from typing import List, Tuple

URI = "neo4j+s://64de9e83.databases.neo4j.io"
USERNAME = "neo4j"  # your Aura account email
PASSWORD = "3oWWBg2lrkWrdQVi9RHQpDd2C51SqYl9RT04LDrngpA"

def cities() -> List[str]:
    return [
        "Amsterdam", 
        "Rotterdam", 
        "Utrecht", 
        "Den Haag", 
        "Alkmaar",
        "Goes",
        "Veere", 
        "Leiden", 
        "Delft", 
        "Hengelo",
        "Enschede", 
        "Assen", 
        "Maastricht", 
        "Zwolle", 
        "Eindhoven"
    ]

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

def create_city(tx: Transaction, name: str) -> None:
    tx.run(
        """
            MERGE (:City {name: $name})
        """, 
        name=name
    )

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

driver: Driver = GraphDatabase.driver(URI, auth=basic_auth(USERNAME, PASSWORD))
with driver.session() as session:
    for city in cities():
        session.execute_write(create_city, city)
    for city1, city2, distance, max_speed in roads():
        session.execute_write(create_road, city1, city2, distance, max_speed)
driver.close()

