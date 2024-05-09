# core/slip_generator.py
import random
from typing import List, Dict
from .slip_manager import SlipManager

class SlipGenerator:
    def __init__(self, slip_manager: SlipManager):
        self.slip_manager = slip_manager

    def generate_random_slips(self, count: int) -> None:
        titles = [
            "Slip Title {}".format(i) for i in range(1, count + 1)
        ]
        descriptions = [
            "Slip Description {}".format(i) for i in range(1, count + 1)
        ]

        for i in range(count):
            slip_data = {
                "title": titles[i],
                "description": descriptions[i],
            }
            self.slip_manager.create_slip(slip_data)

    def generate_slips_from_template(self, template: Dict, count: int) -> None:
        for i in range(count):
            slip_data = template.copy()
            slip_data["title"] = "Slip Title {}".format(i)
            slip_data["description"] = "Slip Description {}".format(i)
            self.slip_manager.create_slip(slip_data)
