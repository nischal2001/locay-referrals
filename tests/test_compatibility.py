import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.search_professionals_tool import SearchProfessionalsTool
from services.compatibility_engine import CompatibilityEngine

query = "Backend engineers in Pune working in product companies"

candidates = SearchProfessionalsTool.run(
    city="Pune",
    role="Backend Engineer",
    company_tier="Product"
)

for candidate in candidates:

    result = CompatibilityEngine.evaluate(query, candidate)

    print("\nCandidate:", candidate["name"])
    print(result)