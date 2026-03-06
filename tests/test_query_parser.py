import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.query_parser import QueryParser


query = "I'm in Pune this weekend. Find backend engineers at product companies."

parsed = QueryParser.parse(query)

print("\nParsed Query:\n")
print(parsed)