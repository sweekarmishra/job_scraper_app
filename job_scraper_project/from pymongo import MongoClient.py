from pymongo import MongoClient

try:
    client = MongoClient("mongodb://localhost:27017/")
    print("Connected to MongoDB!")
    databases = client.list_database_names()
    print("Databases:", databases)
except Exception as e:
    print("Error:", e)