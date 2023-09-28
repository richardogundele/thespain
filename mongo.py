import certifi, pprint
from pymongo.mongo_client import MongoClient

username = "richie"
password = "1ULjTj9f24oHi98K"

uri = f"mongodb+srv://{username}:{password}@cluster0.7zotxnu.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))
client = MongoClient(uri, tlsCAFile=certifi.where())

# Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

db = client.get_database("thespian")   #data
# data = db.brokers.find().next()

# import pprint
# pprint.pprint(data)

# client_info = {
#     "email":"lucianorichard@gmail.com",
#     "prompt": "where can i find a story",
#     "completion": "you can find a story in different places"
# }

# client.thespian.data.insert_one(client_info)
# d = db.data.find().next()

# pprint.pprint(d)
