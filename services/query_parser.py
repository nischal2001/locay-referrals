import os
import json
import requests
from dotenv import load_dotenv
import re

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL")
MODEL = os.getenv("LLM_MODEL")


class QueryParser:

    @staticmethod
    def parse(user_input: str):

        prompt = f"""
Extract structured fields from the request.

Normalize values.

Allowed values:

city: Pune, Bangalore, Hyderabad, Delhi
role: Backend Engineer, Frontend Engineer, Data Engineer
company_tier: Product, Startup, Service

User request:
{user_input}

Return ONLY JSON:

{{
  "city": "",
  "role": "",
  "company_tier": ""
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

        if "choices" not in result:
            raise Exception(result)

        content = result["choices"][0]["message"]["content"]

        # remove markdown if present
        content = re.sub(r"```json|```", "", content).strip()

        try:
            return json.loads(content)
        except:
            return {
                "city": None,
                "role": None,
                "company_tier": None
            }