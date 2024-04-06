from pymongo import MongoClient
import json

# Підключення до MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['quotes']
collection = db['quotes']

# Завантаження даних з файлу JSON та імпорт у колекцію
with open('C:\Users\DELL\Desktop\data_analityka\hw_3\quotes\quotes.json', 'r') as file:
    data = json.load(file)
    collection.insert_many(data)

db = client['quotes']
collection = db['authors']

# Завантаження даних з файлу JSON та імпорт у колекцію
with open('C:\Users\DELL\Desktop\data_analityka\hw_3\quotes\authors.json', 'r') as file_1:
    data_1 = json.load(file_1)
    collection.insert_many(data_1)
    