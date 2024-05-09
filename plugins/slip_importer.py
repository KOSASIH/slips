# plugins/slip_importer.py
import csv
import io
import fitz  # PyMuPDF
from typing import List, Dict

class SlipImporter:
    def import_slips(self, file_path: str, format: str) -> List[Dict]:
        if format == "pdf":
            return self.import_slips_from_pdf(file_path)
        elif format == "csv":
            return self.import_slips_from_csv(file_path)
        else:
            raise ValueError(f"Unsupported format: {format}")

    def import_slips_from_pdf(self, file_path: str) -> List[Dict]:
        slips: List[Dict] = []

        with fitz.open(file_path) as doc:
            for page in doc:
                text = page.get_text()
                slip_text = text.strip()

                slip_id = len(slips) + 1
                slip_title = f"SLIP {slip_id}"
                slip_description = slip_text

                slips.append({"id": slip_id, "title": slip_title, "description": slip_description})

        return slips

    def import_slips_from_csv(self, file_path: str) -> List[Dict]:
        with open(file_path, "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            slips = [row for row in reader]

        return slips
