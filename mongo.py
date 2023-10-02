import certifi, pprint, os
from pymongo import MongoClient

password = os.getenv("mongopassword")

mongo_uri = f"mongodb+srv://richardogundele:{password}@cluster0.jfqn1lj.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(mongo_uri, tlsCAFile=certifi.where())

# Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

db = client.get_database("chatapp")  

# client_info = {
#     "email":"lucianorichard@gmail.com",
#     "prompt": "where can i find a story",
#     "completion": "you can find a story in different places"
# }

# client.chatapp.data.insert_one(client_info)
# d = db.data.find().next()
# pprint.pprint(d)