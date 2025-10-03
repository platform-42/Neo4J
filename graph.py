import os

from neo4j import GraphDatabase, Driver, basic_auth
from lib import edges
from lib import vertices
from lib import cypher

if __name__ == '__main__':
    db_uri = os.getenv("NEO4J_URI")
    db_username = os.getenv("NEO4J_USERNAME")  
    db_password = os.getenv("NEO4J_PASSWORD")
    db_database = os.getenv("NEO4J_DATABASE")

    driver: Driver = GraphDatabase.driver(
        db_uri, 
        auth=basic_auth(db_username, db_password)
    )
    with driver.session(database=db_database) as session:
        for city in vertices.cities():
            session.execute_write(cypher.create_city, city)
        for city1, city2, distance, max_speed in edges.roads():
            session.execute_write(cypher.create_road, city1, city2, distance, max_speed)
    driver.close()

