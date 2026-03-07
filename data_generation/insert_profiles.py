from pymongo import MongoClient
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Mongo URI from .env
MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise Exception("MONGO_URI not found in environment variables")

# Connect to MongoDB Atlas
client = MongoClient(MONGO_URI)

# Select database
db = client["locay_referrals"]

# Select collection
collection = db["professionals"]

# Load generated profiles
with open("professional_profiles.json", "r") as f:
    profiles = json.load(f)

# Insert into MongoDB
result = collection.insert_many(profiles)

print(f"Inserted {len(result.inserted_ids)} profiles into MongoDB Atlas.")