import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.search_professionals_tool import SearchProfessionalsTool
from services.ranking_engine import RankingEngine


query = {
    "city": "Pune",
    "role": "Backend Engineer",
    "company_tier": "Product"
}

# Step 1: Search candidates
candidates = SearchProfessionalsTool.run(**query)

# Step 2: Rank them
results = RankingEngine.rank_candidates(query, candidates)

print("\nTop Matches:\n")

for r in results:

    c = r["candidate"]

    print(f"{c['name']} | Score: {r['score']}")
    print(f"Reason: {r['reason']}")
    print("-----")