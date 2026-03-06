import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from workflows.referral_workflow import build_workflow


workflow = build_workflow()

user_input = "I'm in Pune this weekend. Find backend engineers at product companies."

result = workflow.invoke({
    "user_input": user_input
})

print("\nTop Matches:\n")

for r in result["results"]:

    c = r["candidate"]

    print(f"{c['name']} | Score: {r['score']}")
    print(f"Reason: {r['reason']}")
    print("-----")