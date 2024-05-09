# plugins/slip_exporter.py
from typing import List, Dict

class SlipExporter:
    def export_slips(self, slips: List[Dict], format: str) -> None:
        if format == "pdf":
            self.export_slips_to_pdf(slips)
        elif format == "csv":
            self.export_slips_to_csv(slips)
        else:
            raise ValueError(f"Unsupported format: {format}")

    def export_slips_to_pdf(self, slips: List[Dict]) -> None:
        # Implement this method to export SLIPs to PDF format.
        pass

    def export_slips_to_csv(self, slips: List[Dict]) -> None:
        with open("slips.csv", "w", newline="") as csvfile:
            fieldnames = ["id", "title", "description"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for slip in slips:
                writer.writerow({"id": slip["id"], "title": slip["title"], "description": slip["description"]})
