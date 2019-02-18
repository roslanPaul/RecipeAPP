from pymongo import MongoClient

HOST = 'localhost'
PORT = 27017

client = MongoClient(HOST, PORT)

database = client.cookbook
recipes  = database.recipes


#recipes.insert_one(recipe)
