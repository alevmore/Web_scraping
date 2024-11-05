from pymongo import MongoClient
import json

# Connection to MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['quotes']
collection = db['quotes']

# Downloading data from a JSON file and importing it into a collection
with open('C:\Users\DELL\Desktop\data_analityka\hw_3\quotes\quotes.json', 'r') as file:
    data = json.load(file)
    collection.insert_many(data)

db = client['quotes']
collection = db['authors']

# Downloading data from a JSON file and importing it into a collection
with open('C:\Users\DELL\Desktop\data_analityka\hw_3\quotes\authors.json', 'r') as file_1:
    data_1 = json.load(file_1)
    collection.insert_many(data_1)
    
