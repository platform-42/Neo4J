from neo4j import GraphDatabase, Driver, basic_auth
from lib import edges
from lib import vertices
from lib import cypher

URI = "neo4j+s://64de9e83.databases.neo4j.io"
USERNAME = "neo4j"
PASSWORD = "3oWWBg2lrkWrdQVi9RHQpDd2C51SqYl9RT04LDrngpA"

if __name__ == '__main__':
    driver: Driver = GraphDatabase.driver(URI, auth=basic_auth(USERNAME, PASSWORD))
    with driver.session() as session:
        for city in vertices.cities():
            session.execute_write(cypher.create_city, city)
        for city1, city2, distance, max_speed in edges.roads():
            session.execute_write(cypher.create_road, city1, city2, distance, max_speed)
    driver.close()

