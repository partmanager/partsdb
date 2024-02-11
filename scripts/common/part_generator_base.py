import json
import os


class PartGeneratorBase:
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer
        self.parts = {}

    def get_files(self, partnumber, ordernumber):
        return {}

    def get_operating_temperature_range(self, size_code, power_rating_code, partnumber):
        return self.operating_temp_range

    def get_package_dimension(self, size_code, power_rating_code):
        return self.dimensions[size_code]

    def encode_parameter(self, value, tolerance=None, conditions=None):
        if tolerance:
            value_tolerance = value + ' ' + tolerance
        else:
            value_tolerance = value
        if conditions:
            return {'value': value_tolerance, 'conditions': conditions}
        return {'value': value_tolerance}

    def compress(self, part):
        copy = {}
        for key in part:
            if part[key] is not None and len(part[key]):
                copy[key] = part[key]
        return copy

    def save_file(self, filename):
        dirname = os.path.dirname(filename)
        part_list = list()
        for part in self.parts:
            part_list.append(self.compress(self.parts[part]))
        print("Saving file", filename, "with", len(self.parts), 'parts.')
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        with open(filename, 'w') as json_file:
            json.dump(part_list, json_file, indent='\t')

    def create_or_update_part(self, part):
        partnumber = part['partNumber']
        if partnumber in self.parts:
            #print("Part exist", partnumber)
            self.update_part(part)
        else:
            self.parts[partnumber] = part

    def update_part(self, part):
        part_number = part['partNumber']
        current_part = self.parts[part_number]
        # validate
        for parameter in part['parameters']:
            if current_part['parameters'][parameter] != part['parameters'][parameter]:
                print('--------------------')
                print(parameter, ':', current_part['parameters'][parameter], '!=', part['parameters'][parameter])
                print(current_part)
                print(part)
            assert current_part['parameters'][parameter] == part['parameters'][parameter]
        for order_number in part['orderNumbers']:
            current_part['orderNumbers'][order_number] = part['orderNumbers'][order_number]

    def generate(self, filename):
        self.generate_parts()
        assert self.pre_save_validate()
        self.save_file(filename)

    def validate_part(self, part):
        assert len(part['manufacturer']) > 0
        assert len(part['partNumber']) > 0
        self.validate_packaging(part)

    def pre_save_validate(self):
        return True

    def validate_packaging(self, part):
        for order_number in part['orderNumbers']:
            packaging = part['orderNumbers'][order_number]
            if packaging:
                print(part)
                assert packaging['Packaging Type'] in ['Paper Tape / Reel',
                                                       'Embossed Tape / Reel',
                                                       'Paper Tape / Box',
                                                       'Bulk / Box',
                                                       'Ammo',
                                                       'Bulk'], packaging['Packaging Type']
