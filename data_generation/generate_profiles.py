import random
import uuid
from datetime import datetime
import json


# Cities
cities = [
    "Pune",
    "Bangalore",
    "Hyderabad",
    "Mumbai",
    "Chennai",
    "Vizag"
]


# Roles
roles = [
    "Backend Engineer",
    "Frontend Engineer",
    "DevOps Engineer",
    "Data Engineer",
    "QA Automation Engineer"
]


# Company tiers
company_tiers = [
    "Product",
    "Startup",
    "Service",
    "Enterprise"
]


# Tech stacks
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


# Indian name datasets
first_names = [
    "Arjun","Rohit","Aman","Karan","Vikram","Rahul","Aditya","Ankit",
    "Nikhil","Varun","Siddharth","Pranav","Akshay","Manish","Harsh",
    "Neha","Sneha","Priya","Ananya","Riya","Pooja","Kavya","Megha",
    "Shreya","Tanvi","Aditi","Ishita","Divya","Ritika"
]

last_names = [
    "Sharma","Patel","Reddy","Verma","Gupta","Singh","Agarwal",
    "Mehta","Jain","Chopra","Nair","Iyer","Kulkarni","Deshmukh",
    "Joshi","Pandey","Malhotra","Kapoor","Bansal","Mittal"
]


def generate_profile():

    role = random.choice(roles)

    if role == "Frontend Engineer":
        tech_stack = random.sample(frontend_stack, 2)
    else:
        tech_stack = random.sample(backend_stack, 3)

    # Generate Indian name
    first = random.choice(first_names)
    last = random.choice(last_names)
    name = f"{first} {last}"

    # Generate email (Yopmail)
    email = f"{first.lower()}.{last.lower()}{random.randint(1,999)}@yopmail.com"

    profile = {
        "professional_id": f"p_{uuid.uuid4().hex[:8]}",
        "name": name,
        "email": email,
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


# Save to JSON
with open("professional_profiles.json", "w") as f:
    json.dump(profiles, f, indent=4)

print("500 professional profiles generated successfully.")