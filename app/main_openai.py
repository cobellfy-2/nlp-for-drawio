from fastapi import FastAPI
from pydantic import BaseModel
import openai
from openai import OpenAI
import os
import json
# API-Key in Umgebungsvariable setzen: export OPENAI_API_KEY="..."

client = OpenAI(
  api_key="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"
)

response = client.responses.create(
  model="gpt-4o-mini",
  input="write a haiku about ai",
  store=True,
)

print(response.output_text)
# API-Key in Umgebungsvariable setzen: export OPENAI_API_KEY="..."
'''

app = FastAPI(title="Natural Language to Diagram API")

class ProcessInput(BaseModel):
    text: str

@app.post("/process")
def process_text(input: ProcessInput):
    text = input.text
    
    prompt = f"""
    Analysiere diesen Prozess in Alltagssprache:
    \"\"\"{text}\"\"\"
    Gib eine JSON-Struktur zurück mit:
    {{
      "roles": ["Liste der Rollen, z.B. Kunde, Lager, Versand"],
      "steps": ["Liste der Tasks/Schritte"],
      "decisions": ["Liste der Entscheidungen/Gateways"]
    }}
    """
    
    response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Analysiere diesen Text ..."}
    ],
    temperature=0
)

    
    # GPT liefert Text, wir parsen JSON
    gpt_text = response.choices[0].message.content
    try:
        data = json.loads(gpt_text)
    except json.JSONDecodeError:
        data = {"error": "GPT konnte keine valide JSON zurückgeben", "raw": gpt_text}
    
    return data
'''