import os

from neo4j import GraphDatabase, Driver, basic_auth
from lib.u_bahn import edges
from lib.u_bahn import vertices
from lib.u_bahn import cypher

if __name__ == "__main__":
    db_uri = os.getenv("NEO4J_URI")
    db_username = os.getenv("NEO4J_USERNAME")
    db_password = os.getenv("NEO4J_PASSWORD")
    db_database = os.getenv("NEO4J_DATABASE")

    driver: Driver = GraphDatabase.driver(
        db_uri,
        auth=basic_auth(db_username, db_password)
    )
    
    with driver.session(database=db_database) as session:
        session.execute_write(cypher.clear_database)

        # Create all stations (nodes)
        for name in vertices.stations(vertices.stations_u2(), vertices.stations_u3(), vertices.stations_u6()):
            session.execute_write(cypher.create_station, name)

        # Create U2 tracks (edges)
        for city1, city2, distance in edges.u2_line():
            session.execute_write(cypher.create_track, city1, city2, "U2", distance)

        for city1, city2, distance in edges.u3_line():
            session.execute_write(cypher.create_track, city1, city2, "U3", distance)

        # Create U6 tracks (edges)
        for city1, city2, distance in edges.u6_line():
            session.execute_write(cypher.create_track, city1, city2, "U6", distance)

    driver.close()
