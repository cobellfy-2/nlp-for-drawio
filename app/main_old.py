from fastapi import FastAPI
from pydantic import BaseModel
import re

app = FastAPI(title="Natural Language to BPMN API")

class ProcessInput(BaseModel):
    text: str

@app.post("/process")
def process_text(input: ProcessInput):
    text = input.text
    
    # 1️⃣ Text in Schritte splitten (bei Komma oder Pfeil)
    steps = [s.strip() for s in re.split(r',|→', text)]
    
    # 2️⃣ Rollen automatisch extrahieren (sehr simpel: erstes Wort in jedem Schritt)
    roles = []
    for step in steps:
        match = re.match(r'(\w+)', step)
        if match:
            role = match.group(1)
            if role not in roles:
                roles.append(role)
    
    # 3️⃣ Entscheidungen/Gateways erkennen (Platzhalter)
    decisions = []
    for step in steps:
        # Wenn das Wort "wenn" oder "falls" vorkommt, nehmen wir es als Entscheidung
        if re.search(r'\b(wenn|falls)\b', step, re.IGNORECASE):
            decisions.append(step)
    
    return {
        "original_text": text,
        "steps": steps,
        "roles": roles,
        "decisions": decisions
    }
