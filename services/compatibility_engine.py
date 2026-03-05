import os
import requests
import json
import re
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL")
MODEL = os.getenv("LLM_MODEL")


class CompatibilityEngine:

    @staticmethod
    def evaluate(user_query, candidate_profile):

        prompt = f"""
You are an AI system evaluating job referral compatibility.

User Request:
{user_query}

Candidate Profile:
{candidate_profile}

Evaluate compatibility.

Return ONLY valid JSON in this format:

{{
  "score": number between 0 and 1,
  "reason": "short explanation"
}}
"""

        response = requests.post(
            f"{OPENROUTER_BASE_URL}/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": MODEL,
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            }
        )

        result = response.json()

        # Debug print
        print("LLM Response:", result)

        if "choices" not in result:
            raise Exception(f"OpenRouter API Error: {result}")

        content = result["choices"][0]["message"]["content"]

        # Remove markdown code blocks if present
        content = re.sub(r"```json|```", "", content).strip()

        try:
            return json.loads(content)
        except Exception:
            return {
                "score": 0,
                "reason": content
            }