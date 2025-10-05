#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Filename: cities.py
    Author: diederick de Buck (diederick.de.buck@gmail.com)
    Date: 2025-10-05
    Version: 1.0
    Description: 
        Generates graph consisting of cities in Netherlands with connecting roads
        for exploring Neo4J
"""
import os

from neo4j import GraphDatabase, Driver, basic_auth
from lib.models.cities import edges
from lib.models.cities import vertices
from lib.models.cities import cypher

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

        # Create all cities (nodes)
        for city in vertices.cities():
            session.execute_write(cypher.create_city, city)
        
        # Create all roads (edges)
        for city1, city2, distance, max_speed in edges.roads():
            session.execute_write(cypher.create_road, city1, city2, distance, max_speed)
    
    driver.close()
