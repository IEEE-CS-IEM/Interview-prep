# Script to insert a sample document into a collection
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client["MyProjectDB"]

# Insert a sample user
test_user = {
    "name": "Yash",
    "email": "yash@example.com",
    "role": "admin",
    "active": True
}

users_collection = db["users"]
result = users_collection.insert_one(test_user)
print(f"Inserted test user with _id: {result.inserted_id}")
