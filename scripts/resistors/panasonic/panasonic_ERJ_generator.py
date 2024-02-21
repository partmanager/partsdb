from common.value_series import e24, e24_e96
from resistors.common import resistance_to_str_multiplier, resistance_to_str_multiplier_coma
from .panasonic_common import PanasonicResistorBase


class PanasonicERJResistorBase(PanasonicResistorBase):
    def __init__(self):
        super().__init__(part_type="Resistor Thick Film",
                         series="ERJ",
                         series_description="Precision Thick Film Chip Resistors",
                         operating_temp_range='-55°C ~ 155°C',
                         storage_temp_range='5°C ~ 35°C',
                         size_code={'ERJ1RH': '0201', 'ERJ2RH': '0402', 'ERJ2RK': '0402', 'ERJ3RB': '0603',
                                    'ERJ3RE': '0603', 'ERJ6RB': '0805', 'ERJ6RE': '0805', 'ERJXGN': '01005',
                                    'ERJ1GN': '0201', 'ERJ2RC': '0402', 'ERJ3EK': '0603',
                                    'ERJ6EN': '0805', 'ERJ8EN': '1206', 'ERJ14N': '1210', 'ERJ12N': '1812',
                                    'ERJ12S': '2010', 'ERJ1TN': '2512'},
                         package={'ERJ1RH': 'Chip 0201', 'ERJ2RH': 'Chip 0402', 'ERJ2RK': 'Chip 0402', 'ERJ3RB': 'Chip 0603',
                                  'ERJ3RE': 'Chip 0603', 'ERJ6RB': 'Chip 0805', 'ERJ6RE': 'Chip 0805', 'ERJXGN': 'Chip 01005',
                                  'ERJ1GN': 'Chip 0201', 'ERJ2RC': 'Chip 0402', 'ERJ3EK': 'Chip 0603',
                                  'ERJ6EN': 'Chip 0805', 'ERJ8EN': 'Chip 1206', 'ERJ14N': 'Chip 1210', 'ERJ12N': 'Chip 1812',
                                  'ERJ12S': 'Chip 2010', 'ERJ1TN': 'Chip 2512'},
                         packaging=['C', 'X', 'V', 'U', 'Y'],
                         power_rating_codes={'1R': '0.05W', '2R': '0.063W', '3R': '0.1W', '6R': '0.1W', 'XGN': '0.031W',
                                             '1GN': '0.05W', '2RC': '0.1W', '2RK': '0.1W', '3EK': '0.1W',
                                             '6EN': '0.125W', '8EN': '0.25W', '14N': '0.5W', '12N': '0.75W',
                                             '12S': '0.75W', '1TN': '1W'},
                         product_url='',
                         notes="Generated based on data from datasheet: 12 Sep. 2018")
        self.max_working_voltage = {'ERJ1RH': '15V', 'ERJ2RH': '50V', 'ERJ2RK': '50V', 'ERJ3RB': '50V',
                                    'ERJ3RE': '50V', 'ERJ6RB': '150V', 'ERJ6RE': '150V',
                                    'ERJXGN': '15V', 'ERJ1GN': '25V', 'ERJ2RC': '50V', 'ERJ3EK': '75V',
                                    'ERJ6EN': '150V', 'ERJ8EN': '200V', 'ERJ14N': '200V', 'ERJ12N': '200V',
                                    'ERJ12S': '200V', 'ERJ1TN': '200V',
                                    'ERJ2GE': '50V', 'ERJ3GE': '75V', 'ERJ6GE': '150V'}
        self.max_overload_voltage = {'ERJ1RH': '30V', 'ERJ2RH': '100V', 'ERJ2RK': '100V', 'ERJ3RB': '100V',
                                     'ERJ3RE': '100V', 'ERJ6RB': '200V', 'ERJ6RE': '200V',
                                     'ERJXGN': '30V', 'ERJ1GN': '50V', 'ERJ2RC': '100V', 'ERJ3EK': '150V',
                                     'ERJ6EN': '200V', 'ERJ8EN': '400V', 'ERJ14N': '400V', 'ERJ12N': '500V',
                                     'ERJ12S': '500V', 'ERJ1TN': '500V',
                                     'ERJ2GE': '100V', 'ERJ3GE': '150V', 'ERJ6GE': '200V'}
        self.dimensions = {'01005': {'Length': '0.40mm ±0.02', 'Width': '0.20mm ±0.02', 'Height': '0.13mm±0.02',
                                     't1': '0.10mm±0.03', 't2': '0.10±0.03mm'},
                           '0201': {'Length': '0.60mm ±0.03', 'Width': '0.30mm ±0.03', 'Height': '0.23mm±0.03',
                                    't1': '0.15mm±0.05', 't2': '0.15±0.05mm'},
                           '0402': {'Length': '1.00mm ±0.10', 'Width': '0.50mm +0.1mm/-0.05mm', 'Height': '0.35mm±0.05',
                                    't1': '0.15mm±0.10', 't2': '0.35±0.05mm'},
                           '0603': {'Length': '1.60mm ±0.20', 'Width': '0.80mm ±0.20', 'Height': '0.45mm±0.10',
                                    't1': '0.3mm±0.20', 't2': '0.3mm±0.20'},
                           '0805': {'Length': '2.00mm ±0.20', 'Width': '1.25mm ±0.10', 'Height': '0.50mm±0.10',
                                    't1': '0.40mm±0.25', 't2': '0.4mm±0.25'},
                           '1206': {'Length': '3.20mm ±0.20', 'Width': '1.60mm +0.05mm/-0.15mm',
                                    'Height': '0.60mm±0.10',
                                    't1': '0.50mm±0.25', 't2': '0.50mm±0.25'},
                           '1210': {'Length': '3.20mm ±0.20', 'Width': '2.50mm ±0.20', 'Height': '0.60mm±0.10',
                                    't1': '0.50mm±0.20', 't2': '0.50mm±0.20'},
                           '1812': {'Length': '4.50mm ±0.20', 'Width': '3.20mm ±0.20', 'Height': '0.60mm±0.10',
                                    't1': '0.50mm±0.20', 't2': '0.50mm±0.20'},
                           '2010': {'Length': '5.00mm ±0.20', 'Width': '2.50mm ±0.20', 'Height': '0.60mm±0.10',
                                    't1': '0.65mm±0.20', 't2': '0.60mm±0.20'},
                           '2512': {'Length': '6.40mm ±0.20', 'Width': '3.20mm ±0.20', 'Height': '0.60mm±0.10',
                                    't1': '0.65mm±0.20', 't2': '0.60mm±0.20'}
                           }

    def packaging_data(self, size, power_rating_code, code):
        if code == 'Y' and size in ['ERJXGN']:
            packaging = {
                'Packaging Code': 'Y', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 20000,
                'Packaging Data': {
                    'Reel Diameter': '178.5mm', 'Reel Width': '12.5mm',
                    'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '1.75mm±0.1mm', 'Tape F': '3.50mm±0.05mm',
                    'Tape SO': '',
                    'Tape P0': '4mm±0.10mm', 'Tape P1': '2mm', 'Tape P2': '2mm±0.05mm', 'Tape D': '',
                    'Tape D1': '',
                    'Tape A0': '', 'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            return packaging
        elif code == 'U' and size in ['ERJXGN']:
            packaging = {
                'Packaging Code': 'U', 'Packaging Type': 'Embossed Tape / Reel', 'Packaging Qty': 40000,
                'Packaging Data': {
                    'Reel Diameter': '178.5mm', 'Reel Width': '12.5mm',
                    'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '1.75mm±0.1mm', 'Tape F': '3.50mm±0.05mm',
                    'Tape SO': '',
                    'Tape P0': '4mm±0.10mm', 'Tape P1': '2mm', 'Tape P2': '2mm±0.05mm', 'Tape D': '',
                    'Tape D1': '',
                    'Tape A0': '', 'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            return packaging
        elif code == 'C' and size in ['ERJ1R', 'ERJ1GN']:
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
        elif code == 'X' and size in ['ERJ2R', 'ERJ2RC', 'ERJ2RK', 'ERJ2GE']:
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
        elif code == 'V' and size in ['ERJ3R', 'ERJ6R', 'ERJ3EK', 'ERJ6EN', 'ERJ8EN', 'ERJ3GE', 'ERJ6GE']:
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
        elif code == 'U' and size in ['ERJ14N', 'ERJ12N', 'ERJ12S']:
            packaging = {
                'Packaging Code': 'U', 'Packaging Type': 'Embossed Tape / Reel', 'Packaging Qty': 5000,
                'Packaging Data': {
                    'Reel Diameter': '178.5mm', 'Reel Width': '12.5mm',
                    'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '1.75mm±0.1mm', 'Tape F': '3.50mm±0.05mm',
                    'Tape SO': '',
                    'Tape P0': '4mm±0.10mm', 'Tape P1': '4mm', 'Tape P2': '2mm±0.05mm', 'Tape D': '', 'Tape D1': '',
                    'Tape A0': '',
                    'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            return packaging
        elif code == 'U' and size in ['ERJ1TN']:
            packaging = {
                'Packaging Code': 'U', 'Packaging Type': 'Embossed Tape / Reel', 'Packaging Qty': 4000,
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


class PanasonicERJ_05_ResistorGenerator(PanasonicERJResistorBase):
    def get_resistance_range(self, size_code, tolerance_code, tcr_code, power_rating_code, special_feature):
        size = self.size_code[size_code]
        if tolerance_code == 'D':
            if size == '0201' and tcr_code == 'H':
                return {'ranges': [[e24_e96, '[1000, 1000000]']]}
            elif size == '0402':
                if tcr_code == 'H':
                    return {'ranges': [[e24_e96, '[100, 100000]']]}
                elif tcr_code == 'K':
                    return {'ranges': [[e24_e96, '[10, 1000000]']]}
            elif size == '0603':
                if tcr_code == 'B':
                    return {'ranges': [[e24_e96, '[100, 100000]']]}
                elif tcr_code == 'E':
                    return {'ranges': [[e24_e96, '[10, 1000000]']]}
            elif size == '0805':
                if tcr_code == 'B':
                    return {'ranges': [[e24_e96, '[100, 100000]']]}
                elif tcr_code == 'E':
                    return {'ranges': [[e24_e96, '[10, 1000000]']]}

    def get_part_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type, taping_reel):
        if size_code == "ERJ" + power_rating_code:
            value_str = resistance_to_str_multiplier(value)
            assert len(value_str) == 4, value_str
            packing_type = '#'
            return f"{size_code}{tcr_code}{tolerance_code}{value_str}{packing_type}"

    def get_order_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type,
                         taping_reel):
        if size_code == "ERJ" + power_rating_code:
            value_str = resistance_to_str_multiplier(value)
            assert len(value_str) == 4, value_str
            return f"{size_code}{tcr_code}{tolerance_code}{value_str}{packing_type}"


class PanasonicERJ_1_ResistorGenerator(PanasonicERJResistorBase):
    def get_resistance_range(self, size_code, tolerance_code, tcr_code, power_rating_code, special_feature):
        if tolerance_code == 'F' and size_code == 'ERJ' + power_rating_code:
            if size_code == 'ERJXGN':
                if tcr_code == '300':
                    return {'ranges': [[e24_e96, '[10, 100)']]}
                elif tcr_code == '200':
                    return {'ranges': [[e24_e96, '[100, 1000000]']]}
            elif size_code == 'ERJ1GN' and tcr_code == '200':
                return {'ranges': [[e24_e96, '[10, 1000000]']]}

            elif size_code == 'ERJ2RC' and tcr_code == '-100+600':
                return {'ranges': [[e24_e96, '[1, 9.76]']]}

            elif size_code == 'ERJ2RK' and tcr_code == 'K':
                return {'ranges': [[e24_e96, '[10, 1000000]']]}
            elif size_code == 'ERJ3EK' and tcr_code == 'K':
                return {'ranges': [[e24_e96, '[10, 1000000]']]}
            elif size_code in ['ERJ6EN', 'ERJ8EN'] and tcr_code == 'K':
                return {'ranges': [[e24_e96, '[10, 2200000]']]}
            elif size_code in ['ERJ14N', 'ERJ12N', 'ERJ12S', 'ERJ1TN'] and tcr_code == 'K':
                return {'ranges': [[e24_e96, '[10, 1000000]']]}

    def get_part_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type, taping_reel):
        assert tolerance_code == 'F'
        if size_code == "ERJ" + power_rating_code:
            value_str = resistance_to_str_multiplier_coma(value)
            assert len(value_str) == 4, value_str
            packing_type = '#'
            return f"{size_code}{tolerance_code}{value_str}{packing_type}"

    def get_order_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type,
                         taping_reel):
        assert tolerance_code == 'F'
        if size_code == "ERJ" + power_rating_code:
            value_str = resistance_to_str_multiplier_coma(value)
            assert len(value_str) == 4, value_str
            return f"{size_code}{tolerance_code}{value_str}{packing_type}"


class PanasonicERJ_5_ResistorGenerator(PanasonicERJResistorBase):
    def __init__(self):
        super().__init__()
        self.size_code = {'ERJXGN': '01005', 'ERJ1GN': '0201', 'ERJ2GE': '0402', 'ERJ3GE': '0603', 'ERJ6GE': '0805'}
        self.package = {'ERJXGN': 'Chip 01005', 'ERJ1GN': 'Chip 0201', 'ERJ2GE': 'Chip 0402', 'ERJ3GE': 'Chip 0603', 'ERJ6GE': 'Chip 0805'}
        self.power_rating_codes = {'XGN': '0.031W', '1GN': '0.05W', '2GE': '0.1W', '3GE': '0.1W', '6GE': '0.125W'}

    def get_resistance_range(self, size_code, tolerance_code, tcr_code, power_rating_code, special_feature):
        if tolerance_code == 'J' and size_code == 'ERJ' + power_rating_code:
            if size_code == 'ERJXGN':
                if tcr_code == '-100+600':
                    return {'ranges': [[e24, '[1, 10)']]}
                if tcr_code == '300':
                    return {'ranges': [[e24, '[10, 100)']]}
                elif tcr_code == '200':
                    return {'ranges': [[e24, '[100, 1000000]']]}
            elif size_code in ['ERJ1GN', 'ERJ2GE', 'ERJ3GE', 'ERJ6GE']:
                if tcr_code == '-100+600':
                    return {'ranges': [[e24, '[1, 10)']]}
                elif tcr_code == '200':
                    return {'ranges': [[e24, '[10, 1000000)']]}
                elif tcr_code == '-400+150':
                    return {'ranges': [[e24, '[1000000, 10000000]']]}

    def get_part_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type, taping_reel):
        assert tolerance_code == 'J'
        if size_code == "ERJ" + power_rating_code:
            packing_type = '#'
            return self.generate_part_number_no_tcr_with_marking(size_code, value, tolerance_code, tcr_code,
                                                                 power_rating_code, packing_type, taping_reel)

    def get_order_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type,
                         taping_reel):
        assert tolerance_code == 'J'
        if size_code == "ERJ" + power_rating_code:
            return self.generate_part_number_no_tcr_with_marking(size_code, value, tolerance_code, tcr_code,
                                                                 power_rating_code, packing_type, taping_reel)
