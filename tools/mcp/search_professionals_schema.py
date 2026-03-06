SEARCH_PROFESSIONALS_TOOL = {
    "name": "search_professionals",
    "description": "Find professionals for job referrals based on role, city and company tier",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "City where the professional works"
            },
            "role": {
                "type": "string",
                "description": "Job role of the professional"
            },
            "company_tier": {
                "type": "string",
                "description": "Type of company: Product, Startup, Service"
            }
        },
        "required": ["city", "role"]
    }
}