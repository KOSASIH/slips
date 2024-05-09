import json
import os
import unittest
from slip_utils import SlipUtils

class TestSlipUtils(unittest.TestCase):
    def setUp(self):
        self.slip_utils = SlipUtils()

    def test_validate_slip_data(self):
        valid_slip_data = "END\x01,field1:value1,field2:value2"
        invalid_slip_data = "INVALID_SLIP_DATA"
        self.assertTrue(self.slip_utils.validate_slip_data(valid_slip_data))
        self.assertFalse(self.slip_utils.validate_slip_data(invalid_slip_data))

    def test_format_slip_data(self):
        slip_data = "END\x01,field1:value1,field2:value2"
        formatted_slip_data = self.slip_utils.format_slip_data(slip_data)
        self.assertIsInstance(formatted_slip_data, str)

    def test_extract_slip_fields(self):
        slip_data = "END\x01,field1:value1,field2:value2"
        fields = self.slip_utils.extract_slip_fields(slip_data)
        self.assertIsInstance(fields, dict)
        self.assertIn("field1", fields)
        self.assertIn("field2", fields)

    def test_generate_slip_checksum(self):
        slip_data = "END\x01,field1:value1,field2:value2"
        checksum = self.slip_utils.generate_slip_checksum(slip_data)
        self.assertIsInstance(checksum, str)
        self.assertEqual(len(checksum), 2)

    def test_slip_data_to_dict(self):
        slip_data = "END\x01,field1:value1,field2:value2"
        slip_dict = self.slip_utils.slip_data_to_dict(slip_data)
        self.assertIsInstance(slip_dict, dict)
        self.assertIn("field1", slip_dict)
        self.assertIn("field2", slip_dict)

    def test_dict_to_slip_data(self):
        slip_dict = {"field1": "value1", "field2": "value2"}
        slip_data = self.slip_utils.dict_to_slip_data(slip_dict)
        self.assertIsInstance(slip_data, str)

if __name__ == "__main__":
    unittest.main()
