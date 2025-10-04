# GRAPH DB EXPERIMENT

`graph.py` is a Python pogram that utilizes Cypher interface to create and query a graph in Neo4J.

The setup is such that `graph.py` is a client app that can run anywhere.
graph.py utilizes bolt driver to execute Cypher commands.


## PROJECT STRUCTURE
* `./doc/CypherV2.pdf` -> explanation of Cypher.  
* `./lib/vertices.py` -> graph nodes.  
* `./lib/edges.py` -> graph relationships.  
* `./lib/cypher.py` -> cypher commands to create nodes and relationships.  
* `./etc/graph.env` -> environment file with NEO4J Aura settings, derived from downloaded NEO4J Aura.  
* `./ops/start.sh` -> shell script to run graph.py.  
* `./graph.py` -> main program.  


## NEO4J Aura
In order to avoid Neo4J installation on-prem, you just create one in the cloud using Neo4J Aura. The account that you create is a `PROJECT_ADMIN` account. That account has NO access to graph database or graph tools. It is to setup your project in Neo4J Aura (cloud version). It can only be used to login into the Neo4J webinterface.

Once you created an instance of a database, you will get your database user and credentials in the form of a download link. Don't forget to download it. If you don't do, you are marooned. Just delete the instance and recreate. This account can be used to access the database via the Python program (and bolt driver).


## DEV
From the downloaded file, you see these entries:
`AURA_INSTANCENAME` is not needed. 
`AURA_INSTANCEID` is the ID of the instance
Beyond me, why they don't it in NEO4J_URI since there you see the same ID.

Contents of the downloaded file should look like:
* `NEO4J_URI=neo4j+s://64de9e83.databases.neo4j.io`
* `NEO4J_USERNAME=neo4j`
* `NEO4J_PASSWORD=3oWWBg2lrkWrdQVi9RHQpDd2C51SqYl9RT04LDrngpA`
* `NEO4J_DATABASE=neo4j`

* `AURA_INSTANCEID=64de9e83`
* `AURA_INSTANCENAME=Neumann`

Don't worry, they are stored in `./env/graph.env` so that they can be used as environment variables.


## CONNECTING FROM PYTHON
`driver: Driver = GraphDatabase.driver(URI, auth=basic_auth(NEO4J_USERNAME, NEO4J_PASSWORD))`


## LOGIN INTO AURA
* user: `diederick.de.buck@gmail.com`
* password: `M8rioAndretti!`


## RUNNING GRAPH PROGRAM
```
pip3 install neo4j
cd ops
sh start.sh
```

Check in the Neo4J webadmin tool if the graph is created.
