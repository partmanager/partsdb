from common.value_series import e24, e24_e96
from resistors.common import resistance_to_str
from .yageo_common import YageoResistorBase


class YageoMF0ResistorGenerator(YageoResistorBase):
    def __init__(self):
        super().__init__(part_type="Resistor Thick Film",
                         series="MF0",
                         series_description="Metal Film Resistors",
                         operating_temp_range='-55°C ~ 155°C',
                         storage_temp_range='5°C ~ 35°C',
                         size_code={'MF0204': 'MF0204', 'MF0207': 'MF0207'},
                         package={'MF0204': 'MF0204', 'MF0207': 'MF0207'},
                         packaging=['T', 'R', 'B'],
                         power_rating_codes={'MF0204': '0.4W', 'MF0207': '0.6W'},
                         product_url='',
                         notes="Generated based on data from datasheet: Revision: 201304")
        self.max_working_voltage = None
        self.max_overload_voltage = {'MF0204': '500V', 'MF0207': '700V'}
        self.dimensions = {'MF0204': {'Length': '3.40mm ±0.3', 'Diameter': '1.90mm ±0.2',
                                      'Lead diameter': '0.45mm ±0.05', 'Lead length': '28mm ±2',
                                      'Lead spacing': '4mm±0.05mm'},
                           'MF0207': {'Length': '6.30mm ±0.5', 'Diameter': '2.40mm ±0.2',
                                      'Lead diameter': '0.55mm ±0.05', 'Lead length': '28mm ±2',
                                      'Lead spacing': '4mm±0.05mm'}}
        self.dielectric_withstanding_voltage = {'MF0204': '300V', 'MF0207': '500V'}
        self.max_working_voltage = {'MF0204': '250V', 'MF0207': '350V'}
        self.forming_type = {'MF0204': '52-', 'MF0207': '52-'}

    def get_part_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type, special_feature):
        packing_type = '#'
        resistance_str = resistance_to_str(value)
        forming_type = self.forming_type[size_code]
        return f"{size_code}{tolerance_code}{packing_type}{tcr_code}{forming_type}{resistance_str}"

    def get_order_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type, special_feature):
        resistance_str = resistance_to_str(value)
        forming_type = self.forming_type[size_code]
        return f"{size_code}{tolerance_code}{packing_type}{tcr_code}{forming_type}{resistance_str}"

    def get_package_dimension(self, size_code, power_rating_code):
        return self.dimensions[size_code]

    def get_max_working_voltage(self, size_code, power_rating_code):
        return self.max_working_voltage[size_code]

    def get_dielectric_withstanding_voltage(self, size_code, power_rating_code):
        return self.dielectric_withstanding_voltage[size_code]

    def get_resistance_range(self, size_code, tolerance_code, tcr_code, power_rating_code, special_feature):
        if tcr_code == 'E':
            if size_code == 'MF0204' and power_rating_code == 'MF0204':
                if tolerance_code == 'J':  # 5%
                    return {'ranges': [[e24, '[1, 10000000]']]}
                elif tolerance_code in ['D', 'F']:  # 0.5%, 1%
                    return {'ranges': [[e24_e96, '[1, 10000000]']]}
            if size_code == 'MF0207' and power_rating_code == 'MF0207':
                if tolerance_code == 'J':  # 5%
                    return {'ranges': [[e24, '[1, 10000000]']]}
                elif tolerance_code in ['D', 'F']:  # 0.5%, 1%
                    return {'ranges': [[e24_e96, '[1, 10000000]']]}

    def packaging_data(self, size_code, power_rating_code, packaging_code):
        packaging = {'Packaging Code': packaging_code, 'Packaging Type': '', 'Packaging Qty': ''}
        return packaging

    def get_files(self, partnumber, ordernumber):
        return {'datasheet': 'https://www.yageo.com/upload/media/product/products/datasheet/lr/YAGEO%20MF0_datasheet_2021v0.pdf'}
