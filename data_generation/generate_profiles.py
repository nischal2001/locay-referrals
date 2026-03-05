import random
import uuid
from datetime import datetime
import json

cities = [
    "Pune",
    "Bangalore",
    "Hyderabad",
    "Mumbai",
    "Chennai"
]

roles = [
    "Backend Engineer",
    "Frontend Engineer",
    "DevOps Engineer",
    "Data Engineer",
    "QA Automation Engineer"
]

company_tiers = [
    "Product",
    "Startup",
    "Service",
    "Enterprise"
]

backend_stack = [
    "Python",
    "Java",
    "Node.js",
    "Go",
    "Kubernetes",
    "AWS",
    "Docker"
]

frontend_stack = [
    "React",
    "Angular",
    "TypeScript"
]

def generate_profile():
    role = random.choice(roles)

    if role == "Frontend Engineer":
        tech_stack = random.sample(frontend_stack, 2)
    else:
        tech_stack = random.sample(backend_stack, 3)

    profile = {
        "professional_id": f"p_{uuid.uuid4().hex[:8]}",
        "name": f"Professional_{random.randint(1000,9999)}",
        "city": random.choice(cities),
        "role": role,
        "company": f"Company_{random.randint(1,200)}",
        "company_tier": random.choice(company_tiers),
        "tech_stack": tech_stack,
        "years_experience": random.randint(1, 12),
        "domain": "SaaS",
        "mutual_connections": random.randint(0, 10),
        "summary": f"{role} experienced in {', '.join(tech_stack)} working in SaaS product environment.",
        "created_at": datetime.utcnow().isoformat()
    }

    return profile


profiles = []

for _ in range(500):
    profiles.append(generate_profile())


# Save to JSON (optional but useful for inspection)
with open("professional_profiles.json", "w") as f:
    json.dump(profiles, f, indent=4)

print("500 professional profiles generated successfully.")