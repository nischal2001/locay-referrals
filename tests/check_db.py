import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.mongo_client import get_database

db = get_database()

print(db.professionals.count_documents({}))

print(list(db.professionals.find({"city": "Pune"}).limit(5)))