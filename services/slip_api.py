# services/slip_api.py
import requests
import json
from typing import List, Dict

class SlipApi:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key

    def get_slips(self) -> List[Dict]:
        url = f"{self.base_url}/slips"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return json.loads(response.text)
        else:
            raise Exception(f"Error fetching slips: {response.text}")

    def create_slip(self, slip: Dict) -> Dict:
        url = f"{self.base_url}/slips"
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}

        response = requests.post(url, headers=headers, json=slip)

        if response.status_code == 201:
            return json.loads(response.text)
        else:
            raise Exception(f"Error creating slip: {response.text}")

    def update_slip(self, slip_id: int, slip: Dict) -> Dict:
        url = f"{self.base_url}/slips/{slip_id}"
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}

        response = requests.put(url, headers=headers, json=slip)

        if response.status_code == 200:
            return json.loads(response.text)
        else:
            raise Exception(f"Error updating slip: {response.text}")

    def delete_slip(self, slip_id: int) -> None:
        url = f"{self.base_url}/slips/{slip_id}"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        response = requests.delete(url, headers=headers)

        if response.status_code != 204:
            raise Exception(f"Error deleting slip: {response.text}")
