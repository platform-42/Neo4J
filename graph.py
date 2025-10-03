from neo4j import GraphDatabase, Transaction, Driver, basic_auth
from lib import edges
from lib import vertices

URI = "neo4j+s://64de9e83.databases.neo4j.io"
USERNAME = "neo4j"
PASSWORD = "3oWWBg2lrkWrdQVi9RHQpDd2C51SqYl9RT04LDrngpA"

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

if __name__ == '__main__':
    driver: Driver = GraphDatabase.driver(URI, auth=basic_auth(USERNAME, PASSWORD))
    with driver.session() as session:
        for city in vertices.cities():
            session.execute_write(create_city, city)
        for city1, city2, distance, max_speed in edges.roads():
            session.execute_write(create_road, city1, city2, distance, max_speed)
    driver.close()

