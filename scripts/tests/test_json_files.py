import json
import unittest
from pathlib import Path
from common import load_files, load_manufacturers, load_part_types, load_packaging_types, load_msl_classification


class TestJsonFiles(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manufacturers = load_manufacturers()
        cls.part_types = load_part_types()
        cls.packaging_types = load_packaging_types()
        cls.msl_classification = load_msl_classification()
        cls.order_number_allowed_fields = ['Alias', 'Status', 'Code', 'Type', 'Qty', 'PackagingData']
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

    def test_validate_packaging_type(self):
        for json_file in self.json_files:
            for part in json_file['data']:
                for order_number in part['orderNumbers']:
                    order = part['orderNumbers'][order_number]
                    if 'Packaging Type' in order:
                        self.assertIn(order['Packaging Type'], self.packaging_types,
                                      msg=f"for part {part['partNumber']}, in: {json_file['file']}")

    def test_validate_order_number_fields(self):
        for json_file in self.json_files:
            for part in json_file['data']:
                for order_number in part['orderNumbers']:
                    order = part['orderNumbers'][order_number]
                    for field in order:
                        self.assertIn(field, self.order_number_allowed_fields,
                                      msg=f"for part {part['partNumber']}, in: {json_file['file']}")

    def test_validate_msl_field(self):
        for json_file in self.json_files:
            for part in json_file['data']:
                if 'storageConditions' in part and 'MSLevel' in part['storageConditions']:
                    self.assertIn(part['storageConditions']['MSLevel'], self.msl_classification,
                                  msg=f"for part {part['partNumber']}, in: {json_file['file']}")


if __name__ == '__main__':
    unittest.main()
