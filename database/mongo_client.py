from pymongo import MongoClient

# MongoDB connection string
MONGO_URI = "mongodb://localhost:27017"

# Database name
DB_NAME = "locay_referrals"


def get_database():
    client = MongoClient(MONGO_URI)
    return client[DB_NAME]