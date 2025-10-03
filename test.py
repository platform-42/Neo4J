from neo4j import GraphDatabase
import random

# 🔹 Replace these with your Aura credentials
URI = "neo4j+s://<your-instance-id>.databases.neo4j.io"
USERNAME = "<your-username>"
PASSWORD = "<your-password>"

# 🔹 Your 15 cities
cities = [
    "Amsterdam", "Rotterdam", "Utrecht", "Den Haag", "Alkmaar",
    "Goes", "Veere", "Leiden", "Delft", "Hengelo",
    "Enschede", "Assen", "Maastricht", "Zwolle", "Eindhoven"
]

# 🔹 Example edges between cities with random distances and maxSpeeds
roads = [
    ("Amsterdam", "Rotterdam"), ("Amsterdam", "Utrecht"),
    ("Rotterdam", "Den Haag"), ("Alkmaar", "Amsterdam"),
    ("Goes", "Veere"), ("Leiden", "Delft"), ("Hengelo", "Enschede"),
    ("Assen", "Zwolle"), ("Maastricht", "Eindhoven"), ("Utrecht", "Delft"),
    ("Rotterdam", "Delft"), ("Zwolle", "Utrecht"), ("Eindhoven", "Den Haag")
]

# Connect to Neo4j Aura
driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

def create_cities(tx):
    # Create City nodes
    for city in cities:
        tx.run("MERGE (:City {name: $name})", name=city)

def create_roads(tx):
    # Create ROAD relationships with distance and maxSpeed
    for a, b in roads:
        distance = random.randint(30, 200)  # km
        maxSpeed = random.choice([80, 100, 120, 130])
        tx.run("""
            MATCH (c1:City {name: $a}), (c2:City {name: $b})
            MERGE (c1)-[:ROAD {distance: $distance, maxSpeed: $maxSpeed}]->(c2)
            MERGE (c2)-[:ROAD {distance: $distance, maxSpeed: $maxSpeed}]->(c1)
        """, a=a, b=b, distance=distance, maxSpeed=maxSpeed)

with driver.session(database="DIJKSTRA") as session:
    session.write_transaction(create_cities)
    session.write_transaction(create_roads)

print("✅ Cities and roads created successfully!")
driver.close()
