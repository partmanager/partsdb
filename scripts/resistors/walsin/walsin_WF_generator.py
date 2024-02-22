from common.value_series import e24, e24_e96
from resistors.common import resistance_to_str_multiplier_coma
from resistors.resistor_generator_base import ResistorGeneratorBase


class WalsinWFResistorGenerator(ResistorGeneratorBase):
    def __init__(self):
        super().__init__(manufacturer='Walsin',
                         part_type="Resistor Thick Film",
                         series="WF",
                         series_description="High Power Chip Resistors",
                         operating_temp_range='-55°C ~ 155°C',
                         storage_temp_range='5°C ~ 35°C',
                         size_code={'WF08P': '0805', 'WF06P': '0603'},
                         package={'WF08P': '0805', 'WF06P': '0603'},
                         tolerance={'W': '±0.05%', 'B': '±0.1%', 'C': '±0.25%', 'D': '±0.5%', 'F': '±1%', 'J': '±5%'},
                         tcr={'100': '±100ppm/°C', '150': '±150ppm/°C'},
                         packaging=['T'],
                         power_rating_codes={'WF08P': '0.25W', 'WF06P': '0.125W'},
                         product_url='http://www.passivecomponent.com/products/resistors/#resistors',
                         notes="Generated based on data from datasheet: Jul. 2010")
        self.max_working_voltage = None
        self.max_overload_voltage = {'WF08P': '300V', 'WF06P': '100V'}
        self.dimensions = {'0603': {'Length': '1.60mm ±0.10', 'Width': '0.80mm ±0.10', 'Height': '0.45mm ±0.15',
                                    't1': '0.30mm ±0.15', 't2': '0.30mm±0.10'},
                           '0805': {'Length': '2.00mm ±0.10', 'Width': '1.25mm ±0.10', 'Height': '0.50mm ±0.15',
                                    't1': '0.40mm ±0.20', 't2': '0.40mm±0.20'}}
        self.max_working_voltage = {'WF08P': '150V', 'WF06P': '50V'}
        self.dielectric_withstanding_voltage = {'WF08P': '', 'WF06P': ''}
        self.termination_code = 'L'

    def get_part_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type, special_feature):
        packing_type = '#'
        if tolerance_code == 'J':
            resistance_str = resistance_to_str_multiplier_coma(value, digits=2)
        else:
            resistance_str = resistance_to_str_multiplier_coma(value)
        return f"{size_code}{resistance_str}{tolerance_code}{packing_type}{self.termination_code}"

    def get_order_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type, special_feature):
        if tolerance_code == 'J':
            resistance_str = resistance_to_str_multiplier_coma(value, digits=2)
        else:
            resistance_str = resistance_to_str_multiplier_coma(value)
        return f"{size_code}{resistance_str}{tolerance_code}{packing_type}{self.termination_code}"

    def get_package_dimension(self, size_code, power_rating_code):
        size = self.size_code[size_code]
        return self.dimensions[size]

    def get_max_working_voltage(self, size_code, power_rating_code):
        return self.max_working_voltage[size_code]

    def get_dielectric_withstanding_voltage(self, size_code, power_rating_code):
        return self.dielectric_withstanding_voltage[size_code]

    def get_resistance_range(self, size_code, tolerance_code, tcr_code, power_rating_code, special_feature):
        series = e24 if tolerance_code == 'J' else e24_e96

        if size_code == 'WF06P' and power_rating_code == 'WF06P':
            if tolerance_code in ['F', 'J']:  # 1%, 5%
                if tcr_code == '150':
                    return {'ranges': [[series, '[1, 10)']]}
                elif tcr_code == '100':
                    return {'ranges': [[series, '[10, 1000000]']]}
        if size_code == 'WF08P' and power_rating_code == 'WF08P':
            if tolerance_code in ['F', 'J']:  # 1%, 5%
                if tcr_code == '150':
                    return {'ranges': [[series, '[1, 10)']]}
                elif tcr_code == '100':
                    return {'ranges': [[series, '[10, 1000000]']]}

    def packaging_data(self, size_code, power_rating_code, packaging_code):
        if size_code == 'WF06P':
            packaging = {
                'Packaging Code': 'T', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 5000,
                'Packaging Data': {
                    'Reel Diameter': '178mm ±2.0mm', 'Reel Width': '9mm ±0.5mm',
                    'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm ±0.30mm', 'Tape E': '1.75mm±0.1mm',
                    'Tape F': '3.50mm±0.20mm',
                    'Tape SO': '',
                    'Tape P0': '4mm±0.10mm', 'Tape P1': '4mm±0.10mm', 'Tape P2': '2mm', 'Tape D': '1.5mm +0.1mm/-0.0mm',
                    'Tape D1': '',
                    'Tape A0': '1.9mm±0.2mm', 'Tape A1': '', 'Tape B0': '1.1mm±0.2mm', 'Tape B1': '',
                    'Tape T': '0.65mm±0.05mm', 'Tape K': ''}}
            return packaging
        elif size_code == 'WF08P':
            packaging = {
                'Packaging Code': 'T', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 5000,
                'Packaging Data': {
                    'Reel Diameter': '178mm ±2.0mm', 'Reel Width': '9mm ±0.5mm',
                    'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm ±0.30mm', 'Tape E': '1.75mm±0.1mm',
                    'Tape F': '3.50mm±0.20mm',
                    'Tape SO': '',
                    'Tape P0': '4mm±0.10mm', 'Tape P1': '4mm±0.10mm', 'Tape P2': '2mm', 'Tape D': '1.5mm +0.1mm/-0.0mm',
                    'Tape D1': '',
                    'Tape A0': '2.4mm±0.2mm', 'Tape A1': '', 'Tape B0': '1.65mm±0.2mm', 'Tape B1': '', 'Tape T': '1mm',
                    'Tape K': ''}}
            return packaging

    def get_files(self, partnumber, ordernumber):
        return {'datasheet': 'http://www.passivecomponent.com/wp-content/uploads/chipR/ASC_WF08-06P.pdf'}
