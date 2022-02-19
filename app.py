import json
import pymongo
import myConfig

#set connection string from config file
conn_str = myConfig.connection()

# set a 5-second connection timeout
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)


try:
    print(client.server_info())
except Exception:
    print("Unable to connect to the server.")