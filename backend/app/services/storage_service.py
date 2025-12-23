import json
from pathlib import Path

DATA_FILE = Path("data/data.json")

def load_data():
    if not DATA_FILE.exists():
        return {"persons": [], "next_person_id": 1, "next_doc_id": 1}

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
