from database.mongo_client import get_database

class ProfessionalRepository:

    @staticmethod
    def find_professionals(city=None, role=None, company_tier=None, limit=5):

        db = get_database()
        collection = db["professionals"]

        query = {}

        if city:
            query["city"] = city

        if role:
            query["role"] = role

        if company_tier:
            query["company_tier"] = company_tier

        results = collection.find(query).limit(limit)

        return list(results)