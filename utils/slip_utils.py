import re
import json
from typing import Union, List, Dict

class SlipUtils:
    """
    A collection of utility functions for working with SLIP data.
    """

    @staticmethod
    def validate_slip_data(data: Union[str, bytes]) -> bool:
        """
        Validate SLIP data against the SLIP specification.

        Args:
            data: The SLIP data to validate.

        Returns:
            True if the data is valid, False otherwise.
        """
        # Implement SLIP data validation logic here
        # For demonstration purposes, we'll use a simple regex pattern
        pattern = r"^END(\x00|\x01|\x02|\x03){1,3}$"
        if isinstance(data, str):
            data = data.encode()
        return bool(re.match(pattern, data))

    @staticmethod
    def format_slip_data(data: Union[str, bytes], pretty: bool = False) -> str:
        """
        Format SLIP data for human readability.

        Args:
            data: The SLIP data to format.
            pretty: Whether to pretty-print the data (default: False).

        Returns:
            The formatted SLIP data as a string.
        """
        if isinstance(data, bytes):
            data = data.decode()
        if pretty:
            return json.dumps(json.loads(data), indent=4)
        return data

    @staticmethod
    def extract_slip_fields(data: Union[str, bytes]) -> Dict[str, str]:
        """
        Extract individual fields from SLIP data.

        Args:
            data: The SLIP data to extract fields from.

        Returns:
            A dictionary containing the extracted fields.
        """
        if isinstance(data, bytes):
            data = data.decode()
        fields = {}
        # Implement field extraction logic here
        # For demonstration purposes, we'll use a simple split
        for field in data.split(","):
            key, value = field.split(":", 1)
            fields[key.strip()] = value.strip()
        return fields

    @staticmethod
    def generate_slip_checksum(data: Union[str, bytes]) -> str:
        """
        Generate a checksum for SLIP data.

        Args:
            data: The SLIP data to generate a checksum for.

        Returns:
            The generated checksum as a string.
        """
        if isinstance(data, str):
            data = data.encode()
        # Implement checksum generation logic here
        # For demonstration purposes, we'll use a simple XOR checksum
        checksum = 0
        for byte in data:
            checksum ^= byte
        return f"{checksum:02x}"

    @staticmethod
    def slip_data_to_dict(data: Union[str, bytes]) -> Dict[str, str]:
        """
        Convert SLIP data to a dictionary.

        Args:
            data: The SLIP data to convert.

        Returns:
            A dictionary containing the SLIP data.
        """
        if isinstance(data, bytes):
            data = data.decode()
        return dict(item.split(":") for item in data.split(","))

    @staticmethod
    def dict_to_slip_data(data: Dict[str, str]) -> str:
        """
        Convert a dictionary to SLIP data.

        Args:
            data: The dictionary to convert.

        Returns:
            The converted SLIP data as a string.
        """
        return ",".join(f"{key}:{value}" for key, value in data.items())
