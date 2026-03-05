from pymongo import MongoClient
import json

# Connect to local MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Select database
db = client["locay_referrals"]

# Select collection
collection = db["professionals"]

# Load generated profiles
with open("professional_profiles.json", "r") as f:
    profiles = json.load(f)

# Insert into MongoDB
result = collection.insert_many(profiles)

print(f"Inserted {len(result.inserted_ids)} profiles into MongoDB.")