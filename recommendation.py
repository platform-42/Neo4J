#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Filename: recommendation.py
    Author: diederick de Buck (diederick.de.buck@gmail.com)
    Date: 2025-10-07
    Version: 1.0
    Description: 
        Amazon style recommendation
"""
import os

from neo4j import GraphDatabase, Driver, basic_auth
from lib.models.recommendation import edges
from lib.models.recommendation import vertices
from lib.models.recommendation import cypher

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
        session.execute_write(cypher.create_users, vertices.create_users())
        session.execute_write(cypher.create_movies, vertices.create_movies())
        session.execute_write(cypher.create_genres, vertices.create_genres())
        session.execute_write(cypher.create_likes, edges.create_likes())

    driver.close()
