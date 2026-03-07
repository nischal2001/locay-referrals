from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# MongoDB connection string from environment
MONGO_URI = os.getenv("MONGO_URI")

# Database name
DB_NAME = "locay_referrals"


def get_database():
    if not MONGO_URI:
        raise Exception("MONGO_URI not found in environment variables")

    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]

    return db


# Optional test block (for local testing only)
if __name__ == "__main__":
    db = get_database()
    print("Connected to MongoDB successfully")
    print("Collections:", db.list_collection_names())