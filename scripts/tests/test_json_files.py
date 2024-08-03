import json
import unittest
from pathlib import Path
from common import load_files, load_manufacturers, load_part_types


class TestJsonFiles(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manufacturers = load_manufacturers()
        cls.part_types = load_part_types()
        cls.files = load_files(Path('./components'))
        cls.json_files = []
        for f in cls.files:
            with open(str(f)) as jsonfile:
                cls.json_files.append({'file': f, 'data': json.load(jsonfile)})

    def test_required_fields(self):
        required_fields = ["manufacturer", "partNumber", "partType"]
        for json_file in self.json_files:
            for part in json_file['data']:
                for required_field in required_fields:
                    self.assertIn(required_field, part,
                                  msg=f"for part {part['partNumber']}, in: {json_file['file']}")

    def test_validate_manufacturer(self):
        for json_file in self.json_files:
            for part in json_file['data']:
                self.assertIn(part['manufacturer'], self.manufacturers,
                              msg=f"for part {part['partNumber']}, in: {json_file['file']}")

    def test_validate_partType(self):
        for json_file in self.json_files:
            for part in json_file['data']:
                self.assertIn(part['partType'], self.part_types,
                              msg=f"for part {part['partNumber']}, in: {json_file['file']}")


if __name__ == '__main__':
    unittest.main()
