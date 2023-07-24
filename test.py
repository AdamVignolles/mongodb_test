from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://admin:admin@cluster0.65u1dbk.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
# Get the database
db = client.test
# Get all the documents from the collection
documents = db.test.find()
# Print each document
for document in documents:
    print(document)

# get one document by user
collection = db.test.find({"user": "test"})
for document in collection:
    print(document)


# insert a document
#db.test.insert_one({"user": "test", "password": "test", "email": "test.test@test.test"})