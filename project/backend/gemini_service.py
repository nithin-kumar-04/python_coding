import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "meta-llama/llama-3.1-8b-instruct"


def generate_recipes(
    ingredients: list[str],
    dietary_preference: str = None,
    num_recipes: int = 3,
) -> list[dict]:
    ingredients_str = ", ".join(ingredients)
    dietary_note = (
        f" The recipes should be {dietary_preference}." if dietary_preference else ""
    )

    prompt = f"""You are a helpful chef assistant. Based on these available ingredients: {ingredients_str}, suggest exactly {num_recipes} delicious recipes.{dietary_note}

Respond ONLY with valid JSON in this exact format, no markdown, no extra text:
{{
  "recipes": [
    {{
      "title": "Recipe Name",
      "ingredients": "• 1 cup ingredient1\\n• 2 tbsp ingredient2\\n• ...",
      "instructions": "1. First step.\\n2. Second step.\\n3. Continue...",
      "cuisine_type": "Italian",
      "prep_time": "30 minutes",
      "difficulty": "Easy"
    }}
  ]
}}

Difficulty must be one of: Easy, Medium, Hard."""

    response = requests.post(
        OPENROUTER_URL,
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": MODEL,
            "messages": [{"role": "user", "content": prompt}],
        },
        timeout=30,
    )

    if not response.ok:
        raise Exception(f"OpenRouter error {response.status_code}: {response.text}")
    data = response.json()
    if "error" in data:
        raise Exception(data["error"].get("message", str(data["error"])))
    text = data["choices"][0]["message"]["content"].strip()

    # Strip markdown code fences if present
    if text.startswith("```"):
        lines = text.split("\n")
        text = "\n".join(lines[1:-1])

    result = json.loads(text)
    return result.get("recipes", [])
