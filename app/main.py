from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os
import json
# API-Key in Umgebungsvariable setzen: export OPENAI_API_KEY="..."
openai.api_key = os.getenv("OPENAI_API_KEY")



# API-Key in Umgebungsvariable setzen: export OPENAI_API_KEY="..."


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
