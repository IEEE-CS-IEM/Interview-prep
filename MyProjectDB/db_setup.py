# Script to create required collections (like tables in SQL)
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client["MyProjectDB"]

collections = ["users", "products", "orders", "messages"]
for col in collections:
    if col not in db.list_collection_names():
        db.create_collection(col)
        print(f"✅ Created collection: {col}")
    else:
        print(f"⚠️ Collection already exists: {col}")
