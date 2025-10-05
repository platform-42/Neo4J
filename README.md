# GRAPH DB EXPERIMENT

`cities.py` is a Python pogram that utilizes Cypher interface to create and query a cities/road graph in Neo4J.

The setup is such that `cities.py` is a client app that can run anywhere. `cities.py` utilizes bolt driver to execute Cypher commands.

`u_bahn.py` is a new graph that lays out U-bahn in Berlin.
* U1 (Uhlandstraße/Warschauer Straße)
* U2 (Pankow/Ruhleben) 
* U3 (Krumme Lanke/Wittenbergplatz)
* U6 (Alt Tegel/Alt-Mariendorf)


## PROJECT STRUCTURE

* `./doc/CypherV2.pdf` -> explanation of Cypher.  
* `./models/cities/vertices.py` -> graph nodes (cities).  
* `./models/cities/edges.py` -> graph relationships (roads).  
* `./models/cities/cypher.py` -> cypher commands to create nodes and relationships.  
* `./models/u_bahn/vertices.py` -> graph nodes (stations).  
* `./models/u_bahn/edges.py` -> graph relationships (line).  
* `./models/u_bahn/cypher.py` -> cypher commands to create nodes and relationships.  
* `./etc/graph.env` -> environment file with NEO4J Aura settings, derived from downloaded NEO4J Aura.  
* `./ops/cities.sh` -> shell script to run cities.py.  
* `./ops/u_bahn.sh` -> shell script to run u_bahn.py.  
* `./cities.py` -> main program cities graph.  
* `./u_bahn.py` -> main program u_bahn graph.  


## NEO4J Aura
In order to avoid Neo4J installation on-prem, you just create one in the cloud using Neo4J Aura. The account that you create is a `PROJECT_ADMIN` account. That account has NO access to graph database or graph tools. It is to setup your project in Neo4J Aura (cloud version). It can only be used to login into the Neo4J webinterface.

Once you created an instance of a database, you will get your database user and credentials in the form of a download link. Don't forget to download it. If you don't do, you are marooned. Just delete the instance of your database and recreate it in order to get your credentials file. This account can be used to access the database via the Python program (and bolt driver). The contents of this file is stored in `./etc/graph.env`


## DEV
From the downloaded file, you see these entries:

```
NEO4J_URI=neo4j+s://64de9e83.databases.neo4j.io
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=3oWWBg2lrkWrdQVi9RHQpDd2C51SqYl9RT04LDrngpA
NEO4J_DATABASE=neo4j

AURA_INSTANCEID=64de9e83
AURA_INSTANCENAME=Neumann
```

Don't worry, they are stored in `./env/graph.env` so that they can be used as environment variables. 


## LOGIN INTO AURA
user: `diederick.de.buck@gmail.com`.  
password: `M8rioAndretti!`.  

When you go to query, the Graph interface doesn't show you a graph that you expect. Once you execute your query against the graph, the query is bounded and only then you see a correct representation of your paths within the graph.


## RUNNING GRAPH PROGRAM
```
# pip3 install neo4j
# cd ops
# sh cities.sh
# sh u_bahn.sh
```

Check in the Neo4J webadmin tool if the graph is created.
