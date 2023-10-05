import certifi, pprint, os
from pymongo import MongoClient

'''MONGODB DATABASE - to store user emails, conversations of users'''

password = os.getenv("mongopassword")

mongo_uri = f"mongodb+srv://richardogundele:{password}@cluster0.jfqn1lj.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(mongo_uri, tlsCAFile=certifi.where())

#Get or create database with name 'chatapp' to store the whole conversation and emails
db = client.get_database("chatapp")  