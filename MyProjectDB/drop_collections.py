# Script to drop (delete) all collections in the DB
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client["MyProjectDB"]

collections = db.list_collection_names()
for col in collections:
    db[col].drop()
    print(f"🗑 Dropped collection: {col}")
