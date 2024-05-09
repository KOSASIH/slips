# data/slip_data_loader.py
import csv
import json
from typing import List, Dict

def load_slips_from_csv(file_path: str) -> List[Dict]:
    slips: List[Dict] = []

    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            slips.append({"id": int(row["id"]), "title": row["title"], "description": row["description"]})

    return slips

def load_slips_from_json(file_path: str) -> List[Dict]:
    with open(file_path, "r") as jsonfile:
        slips = json.load(jsonfile)

    return slips
