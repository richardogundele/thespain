from pymongo import MongoClient

# Configure MongoDB connection settings
MONGO_URI = "mongodb://localhost:27017/"
MONGO_DB_NAME = "richard"  # Replace with your database name
MONGO_COLLECTION_NAME = "input_data"  # Replace with your collection name

# Create a MongoDB client
client = MongoClient(MONGO_URI)
db = client[MONGO_DB_NAME]
input_collection = db[MONGO_COLLECTION_NAME]


import os

mongodb_uri = os.environ.get("MONGODB_URI")

if mongodb_uri is None:
    raise Exception("MONGODB_URI environment variable is not set")

# Configure MongoDB connection
client = MongoClient(mongodb_uri)

