
# start server:
#"C:\Program Files\MongoDB\Server\5.0\bin\mongod.exe" --dbpath d:\EXA_FHIR\EXA_FHIR\mongodb\data
#mongo shell: "C:\Program Files\MongoDB\Server\5.0\bin\mongo.exe"

#connection string
def connection():
    return "mongodb://localhost:27017"

# db name
def database():
    return "EXA"

# collection name
def collection():
    return "FHIRdata"

