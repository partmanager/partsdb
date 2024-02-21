from common.value_series import e24_e96
from .panasonic_common import PanasonicResistorBase


class PanasonicERAResistorGenerator(PanasonicResistorBase):
    def __init__(self):
        super().__init__(part_type="Resistor Thin Film",
                         series="ERA",
                         series_description="Metal Film (Thin Film) Chip Resistors, High Reliability Type",
                         operating_temp_range='-55°C ~ 155°C',
                         storage_temp_range='5°C ~ 35°C',
                         size_code={'ERA1A': '0201', 'ERA2A': '0402', 'ERA3A': '0603', 'ERA6A': '0805',
                                    'ERA8A': '1206'},
                         package={'ERA1A': 'Chip 0201', 'ERA2A': 'Chip 0402', 'ERA3A': 'Chip 0603', 'ERA6A': 'Chip 0805',
                                  'ERA8A': 'Chip 1206'},
                         packaging=['C', 'X', 'V'],
                         power_rating_codes={'1A': '0.05W', '2A': '0.063W', '3A': '0.1W', '6A': '0.125W',
                                             '8A': '0.25W'},
                         product_url='',
                         notes="Generated based on data from datasheet: 12 Sep. 2018")
        self.max_working_voltage = {'ERA1A': '25V', 'ERA2A': '50V', 'ERA3A': '75V', 'ERA6A': '100V',
                                    'ERA8A': '150V'}
        self.max_overload_voltage = {'ERA1A': '50V', 'ERA2A': '100V', 'ERA3A': '150V', 'ERA6A': '200V',
                                     'ERA8A': '300V'}
        self.dimensions = {'0201': {'Length': '0.60mm ±0.03', 'Width': '0.30mm ±0.03', 'Height': '0.23mm±0.03',
                                    't1': '0.15mm±0.05', 't2': '0.15±0.05mm'},
                           '0402': {'Length': '1.00mm ±0.10', 'Width': '0.50mm +0.1mm/-0.05mm', 'Height': '0.35mm±0.05',
                                    't1': '0.15mm±0.10', 't2': '0.35±0.05mm'},
                           '0603': {'Length': '1.60mm ±0.20', 'Width': '0.80mm ±0.20', 'Height': '0.45mm±0.10',
                                    't1': '0.3mm±0.20', 't2': '0.3mm±0.20'},
                           '0805': {'Length': '2.00mm ±0.20', 'Width': '1.25mm ±0.10', 'Height': '0.50mm±0.10',
                                    't1': '0.40mm±0.25', 't2': '0.4mm±0.25'},
                           '1206': {'Length': '3.20mm ±0.20', 'Width': '1.60mm +0.05mm/-0.15mm',
                                    'Height': '0.60mm±0.10',
                                    't1': '0.50mm±0.25', 't2': '0.50mm±0.25'}}

    def get_package_dimension(self, size_code, power_rating_code):
        dimensions = {'ERA1A': self.dimensions['0201'],
                      'ERA2A': self.dimensions['0402'],
                      'ERA3A': self.dimensions['0603'],
                      'ERA6A': self.dimensions['0805'],
                      'ERA8A': self.dimensions['1206']}
        return dimensions[size_code]

    def get_part_number(self, size, value, tolerance_code, tcr_code, power_rating_code, packing_type, taping_reel):
        packing_type = '#'
        return self.generate_part_number_in_e24(size, value, tolerance_code, tcr_code, power_rating_code, packing_type,
                                                taping_reel)

    def get_order_number(self, size, value, tolerance_code, tcr_code, power_rating_code, packing_type, taping_reel):
        return self.generate_part_number_in_e24(size, value, tolerance_code, tcr_code, power_rating_code, packing_type,
                                                taping_reel)

    def get_resistance_range(self, size_code, tolerance_code, tcr_code, power_rating_code, special_feature):
        size = self.size_code[size_code]
        if size == '0201':
            if tcr_code == 'E' and tolerance_code in ['B', 'C']:  # 25ppm
                return {'ranges': [[e24_e96, '[100, 10000]']]}
            elif tcr_code == 'R':  # 10ppm
                if tolerance_code in ['B', 'C']:  # 0.25%, 0.1%
                    return {'ranges': [[e24_e96, '[100, 10000]']]}
                elif tolerance_code == 'W':  # 0.05%
                    return {'ranges': [[e24_e96, '[1000, 10000]']]}
        elif size == '0402':
            if tcr_code == 'K' and tolerance_code == 'D':  # 100ppm, 0.5%
                return {'ranges': [[e24_e96, '[10, 46.4]']]}
            elif tcr_code == 'E' and tolerance_code in ['D', 'C', 'B']:  # 25ppm
                return {'ranges': [[e24_e96, '[47, 100000]']]}
            elif tcr_code in ['R', 'P'] and tolerance_code in ['B', 'C']:  # 15ppm, 10ppm
                return {'ranges': [[e24_e96, '[47, 100000]']]}
        elif size == '0603':
            if tcr_code == 'H' and tolerance_code == 'D':  # 50ppm, 0.5%
                return {'ranges': [[e24_e96, '[10, 46.4]']]}
            elif tcr_code == 'E' and tolerance_code in ['D', 'C', 'B']:  # 25ppm
                return {'ranges': [[e24_e96, '[47, 330000]']]}
            elif tcr_code == 'P' and tolerance_code in ['C', 'B']:  # 15ppm
                return {'ranges': [[e24_e96, '[470, 100000]']]}
            elif tcr_code == 'R' and tolerance_code in ['W', 'C', 'B']:  # 10ppm
                return {'ranges': [[e24_e96, '[1000, 100000]']]}
        elif size in ['0805', '1206']:
            if tcr_code == 'H' and tolerance_code == 'D':  # 50ppm, 0.5%
                return {'ranges': [[e24_e96, '[10, 46.4]']]}
            elif tcr_code == 'E' and tolerance_code in ['D', 'C', 'B']:  # 25ppm
                return {'ranges': [[e24_e96, '[47, 1000000]']]}
            elif tcr_code == 'P' and tolerance_code in ['C', 'B']:  # 15ppm
                return {'ranges': [[e24_e96, '[470, 100000]']]}
            elif tcr_code == 'R' and tolerance_code in ['W', 'C', 'B']:  # 10ppm
                return {'ranges': [[e24_e96, '[1000, 100000]']]}

    def packaging_data(self, size_code, power_rating_code, code):
        size = self.size_code[size_code]
        if code == 'C' and size == '0201':
            packaging = {
                'Packaging Code': 'C', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 15000,
                'Packaging Data': {
                    'Reel Diameter': '178.5mm', 'Reel Width': '12.5mm',
                    'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '1.75mm±0.1mm', 'Tape F': '3.50mm±0.05mm',
                    'Tape SO': '',
                    'Tape P0': '4mm±0.10mm', 'Tape P1': '2mm', 'Tape P2': '2mm±0.05mm', 'Tape D': '',
                    'Tape D1': '',
                    'Tape A0': '', 'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            return packaging
        elif code == 'X' and size == '0402':
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
        elif code == 'V' and size in ['0603', '0805', '1206']:
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
        assert 'ERA3AEB102#' in self.parts
        part = self.parts['ERA3AEB102#']
        assert part['manufacturer'] == 'Panasonic'
        assert part['partNumber'] == 'ERA3AEB102#'
        assert part['partType'] == 'Resistor Thin Film'
        assert part['series']['name'] == 'ERA', part['series']['name']
        assert part['series']['description'] == 'Metal Film (Thin Film) Chip Resistors, High Reliability Type', part['series']['description']
        parameters = part['parameters']
        assert parameters['Resistance']['value'] == "1000.00R \u00b10.1%", parameters['Resistance']
        assert parameters['TCR']['value'] == "\u00b125ppm/\u00b0C"
        assert parameters['Rated Power']['value'] == "max. 0.1W"
        assert parameters['Working Voltage']['value'] == 'max. 75V'
        assert parameters['Overload Voltage']['value'] == 'max. 150V'
        assert part['package']['type'] == 'Chip 0603'
        assert part['symbol&footprint']['symbolName'] == 'resistor'

        assert 'ERA3AEB102V' in part['orderNumbers']
        order_number = part['orderNumbers']['ERA3AEB102V']
        assert 'V' == order_number['Packaging Code']
        assert 'Paper Tape / Reel' == order_number['Packaging Type']
        assert 5000 == order_number['Packaging Qty']
        # --------------------------------------------------------------------------------------------------------------
        assert 'ERA3AEB1051#' in self.parts
        part = self.parts['ERA3AEB1051#']
        assert part['manufacturer'] == 'Panasonic'
        assert part['partNumber'] == 'ERA3AEB1051#'
        assert part['partType'] == 'Resistor Thin Film'
        assert part['series']['name'] == 'ERA', part['series']['name']
        assert part['series']['description'] == 'Metal Film (Thin Film) Chip Resistors, High Reliability Type', \
        part['series']['description']
        parameters = part['parameters']
        assert parameters['Resistance']['value'] == "1050.00R \u00b10.1%", parameters['Resistance']
        assert parameters['TCR']['value'] == "\u00b125ppm/\u00b0C"
        assert parameters['Rated Power']['value'] == "max. 0.1W"
        assert parameters['Working Voltage']['value'] == 'max. 75V'
        assert parameters['Overload Voltage']['value'] == 'max. 150V'
        assert part['package']['type'] == 'Chip 0603'
        assert part['symbol&footprint']['symbolName'] == 'resistor'

        assert 'ERA3AEB1051V' in part['orderNumbers']
        order_number = part['orderNumbers']['ERA3AEB1051V']
        assert 'V' == order_number['Packaging Code']
        assert 'Paper Tape / Reel' == order_number['Packaging Type']
        assert 5000 == order_number['Packaging Qty']
        return True
