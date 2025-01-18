import json
import os

from common.value_generator import generate_values


class ResistorGeneratorBase:
    def __init__(self, manufacturer, part_type, series, series_description, operating_temp_range, storage_temp_range,
                 size_code, tolerance, tcr, power_rating_codes, package,
                 packaging, product_url, notes):
        self.manufacturer = manufacturer
        self.part_type = part_type
        self.series = series
        self.series_description = series_description
        self.operating_temp_range = operating_temp_range
        self.storage_temp_range = storage_temp_range
        self.size_code = size_code
        self.tolerance = tolerance
        self.tcr = tcr
        self.power_rating_codes = power_rating_codes
        self.package = package
        self.packaging = packaging
        #self.csv_header = header
        self.product_url = product_url
        self.notes = notes
        self.special_feature = [None]
        self.dielectric_withstanding_voltage = None
        self.parts = {}

    def get_operating_temperature_range(self, size_code, power_rating_code, partnumber):
        return self.operating_temp_range

    def get_package_dimension(self, size_code, power_rating_code):
        size = self.size_code[size_code]
        return self.dimensions[size]

    def get_max_working_voltage(self, size_code, power_rating_code):
        return self.max_working_voltage[size_code]

    def get_max_overload_voltage(self, size_code, power_rating_code):
        if self.max_overload_voltage:
            return self.max_overload_voltage[size_code]

    def get_dielectric_withstanding_voltage(self, size_code, power_rating_code):
        if self.dielectric_withstanding_voltage:
            return self.dielectric_withstanding_voltage[size_code]

    def save_file(self, filename):
        dirname = os.path.dirname(filename)
        part_list = list()
        for part in self.parts:
            copy = {}
            for key in self.parts[part]:
                if self.parts[part][key] is not None and len(self.parts[part][key]):
                    copy[key] = self.parts[part][key]
            part_list.append(copy)


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
        # for field in ['Manufacturer', 'Series', 'Series Description', 'Part Type', 'Product URL', 'Resistance', 'TCR',
        #               'Max Power', 'Working Voltage', 'Overload Voltage', 'Dielectric Withstanding Voltage', 'Symbol',
        #               'Package Type', 'Working Temp Range', 'Storage Temp Range', 'Notes']:
        #     assert (current_part[field] == part[field])
        for parameter in part['parameters']:
            if current_part['parameters'][parameter] != part['parameters'][parameter]:
                print('--------------------')
                print(parameter, ':', current_part['parameters'][parameter], '!=', part['parameters'][parameter])
                print(current_part)
                print(part)
            assert current_part['parameters'][parameter] == part['parameters'][parameter]
        for order_number in part['orderNumbers']:
            current_part['orderNumbers'][order_number] = part['orderNumbers'][order_number]

    def generate_resistor(self, filename):
        # with open(filename, 'w') as csv_file:
        #    writer = csv.DictWriter(csv_file, fieldnames=self.csv_header)
        #    writer.writeheader()
        for special_feature in self.special_feature:
            for size_code in self.size_code:
                for tolerance_code in self.tolerance:
                    for temperature_coefficient_code in self.tcr:
                        for power_rating_code in self.power_rating_codes:                            
                            for packing_type_code in self.packaging:
                                packaging_data = self.packaging_data(size_code, power_rating_code, packing_type_code)
                                if packaging_data:                                    
                                    for resistance in generate_values(
                                            self.get_resistance_range(size_code, tolerance_code,
                                                                      temperature_coefficient_code, power_rating_code,
                                                                      special_feature)):
                                        partnumber = self.get_part_number(size_code, resistance, tolerance_code,
                                                                          temperature_coefficient_code,
                                                                          power_rating_code, packing_type_code,
                                                                          special_feature)
                                        ordernumber = self.get_order_number(size_code, resistance, tolerance_code,
                                                                            temperature_coefficient_code,
                                                                            power_rating_code, packing_type_code,
                                                                            special_feature)

                                        dielectric_withstanding_voltage = self.get_dielectric_withstanding_voltage(
                                            size_code, power_rating_code)
                                        if partnumber:
                                            max_overload_voltage = self.get_max_overload_voltage(
                                                              size_code, power_rating_code)
                                            parameters = {'Resistance': {'value': "{}R {}".format(resistance, self.tolerance[tolerance_code])},
                                                          'TCR': {'value': self.tcr[temperature_coefficient_code]},
                                                          'Rated Power': {'value': 'max. ' + self.power_rating_codes[power_rating_code]},
                                                          'Working Voltage': {'value': 'max. ' + self.get_max_working_voltage(size_code, power_rating_code)}
                                                          }
                                            if max_overload_voltage:
                                                parameters['Overload Voltage'] = {'value': 'max. ' + max_overload_voltage}
                                            if dielectric_withstanding_voltage and len(dielectric_withstanding_voltage) > 0:
                                                parameters['Dielectric Withstanding Voltage'] = {'value': 'max.' + dielectric_withstanding_voltage}

                                            part = {
                                                'manufacturer': self.manufacturer,
                                                'partNumber': partnumber,
                                                'productionStatus': None,
                                                'markingCode': None,
                                                'partType': self.part_type,
                                                'series': {'name': self.series, 'description': self.series_description},
                                                'description': None,
                                                'productUrl': self.product_url,
                                                'notes': self.notes,
                                                'tags': [],
                                                'operatingConditions': {'temperature': self.get_operating_temperature_range(size_code, power_rating_code, partnumber),
                                                                        'humidity': None},
                                                'storageConditions': {'temperature': self.storage_temp_range,
                                                                      'humidity': None,
                                                                      'MSLevel': None},
                                                'parameters': parameters,
                                                'files': self.get_files(partnumber, ordernumber),
                                                'package': {'type': self.package[size_code],
                                                            'dimensions': self.get_package_dimension(size_code, power_rating_code)},
                                                'symbol&footprint': {'symbolName': 'resistor',
                                                                     'pinmap': {},
                                                                     'footprints': []},
                                                'orderNumbers': {ordernumber: packaging_data}
                                            }
                                            self.validate_part(part)
                                            self.create_or_update_part(part)
        assert self.pre_save_validate()
        self.save_file(filename)

    def validate_part(self, part):
        assert len(part['manufacturer']) > 0
        assert len(part['partNumber']) > 0
        assert part['partType'] in ['Resistor', 'Resistor Thin Film', 'Resistor Thick Film', 'Resistor Metal Film',
                                    'Resistor Carbon Film'], part['partType']

    def pre_save_validate(self):
        return True
