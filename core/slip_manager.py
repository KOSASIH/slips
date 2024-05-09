# core/slip_manager.py
from typing import List, Dict
from .slip_validator import SlipValidator

class SlipManager:
    def __init__(self):
        self.slips: Dict[int, Dict] = {}
        self.validator = SlipValidator()

    def create_slip(self, slip_data: Dict) -> int:
        if self.validator.validate(slip_data):
            slip_id = max(self.slips.keys(), default=-1) + 1
            self.slips[slip_id] = slip_data
            return slip_id
        else:
            raise ValueError("Invalid SLIP data")

    def edit_slip(self, slip_id: int, slip_data: Dict) -> None:
        if slip_id in self.slips and self.validator.validate(slip_data):
            self.slips[slip_id].update(slip_data)
        else:
            raise ValueError("Invalid SLIP ID or data")

    def delete_slip(self, slip_id: int) -> None:
        if slip_id in self.slips:
            del self.slips[slip_id]
        else:
            raise ValueError("Invalid SLIP ID")

    def get_slip(self, slip_id: int) -> Dict:
        if slip_id in self.slips:
            return self.slips[slip_id]
        else:
            raise ValueError("Invalid SLIP ID")

    def get_slips(self) -> List[Dict]:
        return list(self.slips.values())
