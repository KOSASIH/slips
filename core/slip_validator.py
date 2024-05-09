# core/slip_validator.py
from typing import Dict

class SlipValidator:
    def validate(self, slip_data: Dict) -> bool:
        required_fields = ["title", "description"]

        for field in required_fields:
            if field not in slip_data or not slip_data[field]:
                return False

        return True
