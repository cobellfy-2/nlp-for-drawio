from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Natural Language to Diagram API")
app.mount("/", StaticFiles(directory="app/static", html=True), name="static")




# Für CORS, damit JS vom Browser an API darf
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

MISTRAL_URL = "http://127.0.0.1:1234/v1/chat/completions"
MODEL = "mistralai/mistral-7b-instruct-v0.3"

class ProcessInput(BaseModel):
    text: str

@app.post("/process")
def process_text(input: ProcessInput):
    prompt = f"""
    Analysiere diesen Prozess in Alltagssprache:
    \"\"\"{input.text}\"\"\"
    Gib als Antwort eine draw.io kompatible XML-Struktur zurück mit:
    {{
      "roles": ["Liste der Rollen, z.B. Kunde, Lager, Versand"],
      "steps": ["Liste der Tasks/Schritte"],
      "decisions": ["Liste der Entscheidungen/Gateways"]
      
    }}
    """

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    r = requests.post(MISTRAL_URL, json=payload)
    if r.status_code != 200:
        return {"error": r.text}

    gpt_text = r.json()["choices"][0]["message"]["content"]
    try:
        data = json.loads(gpt_text)
    except json.JSONDecodeError:
        data = {"error": "Modell konnte keine valide JSON zurückgeben", "raw": gpt_text}

    return data
