readme-nlp-for-draw.io 

# Natural Language to XML-Diagram API

![Python](https://img.shields.io/badge/python-3.12+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Enabled-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

Dieses Projekt erlaubt es, **Prozessbeschreibungen in Alltagssprache** in **draw.io-kompatible XML-Diagramme** zu übersetzen.  
Es nutzt ein **lokales Mistral 7B Instruct Modell** über LM Studio als Backend und FastAPI für die API.

---

## Features

- Web-Frontend für Textinput von Prozessbeschreibungen.   
- Ausgabe als draw.io-kompatibles XML, direkt importierbar.  
- Lokale Nutzung des LLMs, keine externen API-Kosten.  

---

## Projektstruktur

```

nlp-for-drawio/
├─ app/
│  ├─ main.py             # FastAPI Backend
│  └─ static/
│     └─ index.html       # Frontend

````

---

## Voraussetzungen

- Python 3.12+  
- FastAPI und Requests (`pip install fastapi uvicorn requests`)  
- LM Studio mit installiertem **Mistral 7B Instruct Modell**  

---

## Installation & Start

1. **Virtuelle Umgebung erstellen & aktivieren**

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
````


2. **Backend starten**

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

3. **Frontend im Browser öffnen**

```
http://127.0.0.1:8000/static/index.html
#API einsehen
http://127.0.0.1:8000/docs

```

---

## Nutzung

1. Prozessbeschreibung in das Textfeld eingeben.
2. Auf **Analysieren** klicken.
3. Ladeanzeige erscheint, danach wird die XML-Struktur im Bereich darunter angezeigt.
4. XML kann direkt in draw\.io importiert werden.

---

## Hinweise

* Das Projekt nutzt ein **lokales Modell** (Mistral 7B Instruct).
* Wenn die Ausgabe kein korrektes XML liefert, prüfe die Texteingabe oder ob das Modell in LM Studio korrekt läuft.
* CORS ist bereits für alle Domains aktiviert, damit das Frontend korrekt mit dem Backend kommunizieren kann.

---

## ToDo / Erweiterungen

* Frontend modernisieren.
* Streaming-Ausgabe während der Modellgenerierung.
* Validierung der XML-Ausgabe vor dem Download oder Import.

---

## Lizenz

MIT License

---
