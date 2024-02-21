from common.value_series import e24, e24_e96
from resistors.common import resistance_to_str_multiplier_coma
from .panasonic_common import PanasonicResistorBase


class PanasonicERJHResistorGenerator(PanasonicResistorBase):
    def __init__(self):
        super().__init__(part_type="Resistor Thick Film",
                         series="ERJH",
                         series_description="High Temperature Thick Film Chip Resistor",
                         operating_temp_range='-55°C ~ 175°C',
                         storage_temp_range='5°C ~ 35°C',
                         size_code={'ERJH2G': '0402', 'ERJH2C': '0402', 'ERJH2R': '0402', 'ERJH3G': '0603',
                                    'ERJH3E': '0603', 'ERJH3Q': '0603', 'ERJHP6': '0805'},
                         package={'ERJH2G': 'Chip 0402', 'ERJH2C': 'Chip 0402', 'ERJH2R': 'Chip 0402',
                                  'ERJH3G': 'Chip 0603', 'ERJH3E': 'Chip 0603', 'ERJH3Q': 'Chip 0603',
                                  'ERJHP6': 'Chip 0805'},
                         packaging=['X', 'V'],
                         power_rating_codes={'H2G': '0.1W', 'H2C': '0.1W', 'H2R': '0.1W', 'H3G': '0.125W',
                                             'H3E': '0.125W', 'H3Q': '0.25W', 'HP6': '0.5W'},
                         product_url='',
                         notes="Generated based on data from datasheet: 1-Oct-20")
        self.max_working_voltage = {'ERJH2G': '50V', 'ERJH2C': '50V', 'ERJH2R': '50V', 'ERJH3G': '75V',
                                    'ERJH3E': '75V', 'ERJH3Q': '', 'ERJHP6': '400V'}
        self.max_overload_voltage = {'ERJH2G': '100V', 'ERJH2C': '100V', 'ERJH2R': '100V', 'ERJH3G': '150V',
                                     'ERJH3E': '150V', 'ERJH3Q': '', 'ERJHP6': '600V'}
        self.dimensions = {
            '0201': {'Length': '0.60mm ±0.03', 'Width': '0.30mm ±0.03', 'Height': '0.23mm±0.03',
                     't1': '0.15mm±0.05', 't2': '0.15±0.05mm'},
            '0402': {'Length': '1.00mm ±0.10', 'Width': '0.50mm +0.1mm/-0.05mm', 'Height': '0.35mm±0.05',
                     't1': '0.15mm±0.10', 't2': '0.35±0.05mm'},
            '0603': {'Length': '1.60mm ±0.20', 'Width': '0.80mm ±0.20', 'Height': '0.45mm±0.10',
                     't1': '0.3mm±0.20', 't2': '0.3mm±0.20'},
            '0805': {'Length': '2.00mm ±0.20', 'Width': '1.25mm ±0.10', 'Height': '0.50mm±0.10',
                     't1': '0.40mm±0.25', 't2': '0.4mm±0.25'},
            '1206': {'Length': '3.20mm ±0.20', 'Width': '1.60mm +0.05mm/-0.15mm', 'Height': '0.60mm±0.10',
                     't1': '0.50mm±0.25', 't2': '0.50mm±0.25'}}

    def get_part_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type, taping_reel):
        if size_code == "ERJ" + power_rating_code:
            if tolerance_code == 'J':
                value_str = resistance_to_str_multiplier_coma(value, digits=2)
                assert len(value_str) == 3, f"{value} -> {value_str}"
            else:
                value_str = resistance_to_str_multiplier_coma(value)
                assert len(value_str) == 4, value_str
            packing_type = '#'
            return f"{size_code}{tolerance_code}{value_str}{packing_type}"

    def get_order_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type,
                         taping_reel):
        if size_code == "ERJ" + power_rating_code:
            if tolerance_code == 'J':
                value_str = resistance_to_str_multiplier_coma(value, digits=2)
                assert len(value_str) == 3, f"{value} -> {value_str}"
            else:
                value_str = resistance_to_str_multiplier_coma(value)
                assert len(value_str) == 4, value_str
            return f"{size_code}{tolerance_code}{value_str}{packing_type}"

    def get_resistance_range(self, size_code, tolerance_code, tcr_code, power_rating_code, special_feature):
        if size_code == 'ERJH2G' and tolerance_code == 'J':
            if tcr_code == '-100+600':  # 25ppm
                return {'ranges': [[e24, '[1, 10)']]}
            elif tcr_code == '200':  # 200ppm
                return {'ranges': [[e24, '[10, 300000]']]}
        elif size_code == 'ERJH2C' and tolerance_code == 'F' and tcr_code == '-100+600':
            return {'ranges': [[e24_e96, '[1, 9.76]']]}
        elif size_code == 'ERJH2R' and tcr_code == 'K' and tolerance_code in ['D', 'F']:
            return {'ranges': [[e24_e96, '[10, 300000]']]}
        elif size_code == 'ERJH3G' and tolerance_code == 'J':
            if tcr_code == '-100+600':
                return {'ranges': [[e24, '[1, 10)']]}
            elif tcr_code == '200':
                return {'ranges': [[e24, '[10, 300000]']]}
        elif size_code == 'ERJH3E' and tcr_code == 'K' and tolerance_code in ['D', 'F']:
            return {'ranges': [[e24_e96, '[10, 300000]']]}
        elif size_code == 'ERJH3Q' and tcr_code == '200':
            if tolerance_code in ['D', 'F']:
                return {'ranges': [[e24_e96, '[1, 9.76]']]}
            elif tolerance_code == 'J':
                return {'ranges': [[e24, '[1, 9.1]']]}
        elif size_code == 'ERJHP6':
            if tolerance_code == 'D':
                if tcr_code == '300':
                    return {'ranges': [[e24_e96, '[10, 33)']]}
                elif tcr_code == 'K':
                    return {'ranges': [[e24_e96, '[33, 300000]']]}
            elif tolerance_code == 'F':
                if tcr_code == '-100+600':
                    return {'ranges': [[e24_e96, '[1, 10)']]}
                elif tcr_code == '300':
                    return {'ranges': [[e24_e96, '[10, 33)']]}
                elif tcr_code == 'K':
                    return {'ranges': [[e24_e96, '[33, 300000]']]}
            if tolerance_code == 'J':
                if tcr_code == '-100+600':
                    return {'ranges': [[e24, '[1, 10)']]}
                elif tcr_code == '300':
                    return {'ranges': [[e24, '[10, 33)']]}
                elif tcr_code == 'K':
                    return {'ranges': [[e24, '[33, 300000]']]}

    def packaging_data(self, size_code, power_rating_code, code):
        if code == 'X' and size_code in ['ERJH2G', 'ERJH2C', 'ERJH2R']:
            packaging = {
                'Packaging Code': 'X', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 10000,
                'Packaging Data': {
                    'Reel Diameter': '178.5mm', 'Reel Width': '12.5mm',
                    'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '1.75mm±0.1mm', 'Tape F': '3.50mm±0.05mm',
                    'Tape SO': '',
                    'Tape P0': '4mm±0.10mm', 'Tape P1': '2mm', 'Tape P2': '2mm±0.05mm', 'Tape D': '', 'Tape D1': '',
                    'Tape A0': '',
                    'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            return packaging
        elif code == 'V' and size_code in ['ERJH3G', 'ERJH3E', 'ERJH3Q', 'ERJHP6']:
            packaging = {
                'Packaging Code': 'V', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 5000,
                'Packaging Data': {
                    'Reel Diameter': '178.5mm', 'Reel Width': '12.5mm',
                    'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '1.75mm±0.1mm', 'Tape F': '3.50mm±0.05mm',
                    'Tape SO': '',
                    'Tape P0': '4mm±0.10mm', 'Tape P1': '4mm', 'Tape P2': '2mm±0.05mm', 'Tape D': '', 'Tape D1': '',
                    'Tape A0': '',
                    'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            return packaging

    def get_files(self, partnumber, ordernumber):
        return {}

    def pre_save_validate(self):
        assert 'ERJH2RD1002#' in self.parts
        part = self.parts['ERJH2RD1002#']
        assert part['manufacturer'] == 'Panasonic'
        assert part['partNumber'] == 'ERJH2RD1002#'
        assert part['partType'] == 'Resistor Thick Film', part['partType']
        assert part['series']['name'] == 'ERJH', part['series']['name']
        assert part['series']['description'] == 'High Temperature Thick Film Chip Resistor', part['series']['description']
        parameters = part['parameters']
        assert parameters['Resistance']['value'] == "10000.00R \u00b10.5%", parameters['Resistance']
        assert parameters['TCR']['value'] == "\u00b1100ppm/\u00b0C", parameters['TCR']
        assert parameters['Rated Power']['value'] == "max. 0.1W"
        assert parameters['Working Voltage']['value'] == 'max. 50V'
        assert parameters['Overload Voltage']['value'] == 'max. 100V'
        assert part['package']['type'] == 'Chip 0402'
        assert part['symbol&footprint']['symbolName'] == 'resistor'

        assert 'ERJH2RD1002X' in part['orderNumbers']
        order_number = part['orderNumbers']['ERJH2RD1002X']
        assert 'X' == order_number['Packaging Code']
        assert 'Paper Tape / Reel' == order_number['Packaging Type']
        assert 10000 == order_number['Packaging Qty']
        return True
