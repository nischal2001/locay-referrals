import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.search_professionals_tool import SearchProfessionalsTool

results = SearchProfessionalsTool.run(
    city="Pune",
    role="Backend Engineer",
    company_tier="Product"
)

for r in results:
    print(r)