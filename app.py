import json
import pymongo
import myConfig
from os import listdir

#set db info from config file
conn_str = myConfig.connection()

# set a 5-second connection timeout
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)

# set db/collection
db = client[myConfig.database()]
col = db[myConfig.collection()]

#test connection
#try:
#    print(client.server_info())
#except Exception:
#    print("Unable to connect to the server.")

# make a list of files in the data folder
filenames = listdir("data/")
# print(filenames) 

# loop over filenames
i = 0
while i < len(filenames):
    file = open("data/" + filenames[i], "r", encoding='utf-8') #encoding for special characters
    try:
        file = json.load(file) #parse and validate json
        print("validated " + filenames[i] + "\n")
        x = col.insert_one(file)
    except Exception:
        print("Error loading file:" + filenames[i])

    i += 1






