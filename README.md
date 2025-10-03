# GRAPH DB EXPERIMENT

graph.py is a python pogram that utilizes Cypher interface to create and query a graph in Neo4J

The setup is as such that graph.py is a client app that can run anywhere.
graph.py utilizes bolt driver to execute Cypher commands


## NEO4J Aura

In order to avoid an Neo4J installation on-prem, you just create on in the cloud
The account that you create is called a PROJECT_ADMIN account. That one has NO access to graph database or graph tools. It is to setup your project in Neo4J Aura (cloud version).

Once you create an instance of a database, you will get your database user and credentials in the form of a download link. Don't forget to download it. If you don't do, you are marooned. Just delete the instance and recreate

## DEV

From the downloaded file, you see these entries:
AURA_INSTANCENAME is not needed. AURA_INSTANCEID is the ID.
Beyond me, why they don't it in NEO4J_URI since there you see the same ID.

NEO4J_URI=neo4j+s://64de9e83.databases.neo4j.io
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=3oWWBg2lrkWrdQVi9RHQpDd2C51SqYl9RT04LDrngpA
NEO4J_DATABASE=neo4j

AURA_INSTANCEID=64de9e83
AURA_INSTANCENAME=Neumann

## CONNECTING FROM PYTHON

driver: Driver = GraphDatabase.driver(URI, auth=basic_auth(NEO4J_USERNAME, NEO4J_PASSWORD))
