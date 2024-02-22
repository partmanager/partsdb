from common.value_series import e24, e24_e96
from resistors.common import resistance_to_str, resistance_to_str_v3, resistance_to_str_multiplier
from resistors.resistor_generator_base import ResistorGeneratorBase


class RoyalohmCQGenerator(ResistorGeneratorBase):
    def __init__(self):
        super().__init__("Royalohm",
                         "Resistor Thick Film",
                         "CQ",
                         "Common Quality Anti-Sulfurized Chip Resistor (AEC-Q200)",
                         operating_temp_range='-55°C ~ 155°C',
                         storage_temp_range='-55°C ~ 125°C',
                         size_code={'CQ02': '0402', 'CQ03': '0603', 'CQ05': '0805', 'CQ06': '1206',
                                    'CQ07': '1210', 'CQ10': '2010', 'CQ12': '2512'},
                         package={'CQ02': 'Chip 0402', 'CQ03': 'Chip 0603', 'CQ05': 'Chip 0805', 'CQ06': 'Chip 1206',
                                  'CQ07': 'Chip 1210', 'CQ10': 'Chip 2010', 'CQ12': 'Chip 2512'},
                         tolerance={'L': '±0.01%', 'W': '±0.05%', 'B': '±0.1%', 'C': '±0.25%', 'D': '±0.5%',
                                    'F': '±1%', 'G': '±2%', 'J': '±5%'},
                         tcr={'100': '±100ppm/°C', '200': '±200ppm/°C', '400': '±400ppm/°C', '800': '±800ppm/°C'},
                         packaging=['T1', 'T2', 'T4', 'T5', 'TA', 'TC', 'TD', 'TE'],
                         power_rating_codes={'WH': '0.03125W',  # '1/32W',
                                             'WM': '0.05W',  # '1/20W',
                                             'WG': '0.0625W',  # '1/16W',
                                             'WA': '0.1W',  # '1/10W',
                                             'W8': '0.125W',  # '1/8W',
                                             'W4': '0.25W',  # '1/4W',
                                             'W2': '0.5W',  # '1/2W',
                                             '1W': '1W',
                                             'SA': '0.1W',  # '1/10W',
                                             'S8': '0.125W',  # '1/8W',
                                             'S4': '0.25W',  # '1/4W',
                                             'S3': '0.333333333W',  # '1/3W',
                                             '07': '0.75W',  # '3/4W',
                                             'U2': '0.5W',  #'1/2W'
                                             },
                         product_url='',
                         notes='')
        self.max_working_voltage = {'CQ02': '50V', 'CQ03': '50V', 'CQ05': '150V', 'CQ06': '200V',
                                    'CQ07': '200V', 'CQ10': '200V', 'CQ12': '200V'}
        self.max_overload_voltage = {'CQ02': '100V', 'CQ03': '100V', 'CQ05': '300V', 'CQ06': '400V',
                                     'CQ07': '500V', 'CQ10': '500V', 'CQ12': '500V'}

        self.dimensions = {'0201': {'Length': '0.60mm ±0.03', 'Width': '0.30mm ±0.03', 'Height': '0.23mm±0.03',
                                    't1': '0.10mm±0.05', 't2': '0.15±0.05mm'},
                           '0402': {'Length': '1.00mm ±0.10', 'Width': '0.50mm ±0.05', 'Height': '0.35mm±0.05',
                                    't1': '0.20mm±0.10', 't2': '0.25±0.10mm'},
                           '0603': {'Length': '1.60mm ±0.10', 'Width': '0.80mm +0.15/-0.10', 'Height': '0.45mm±0.10',
                                    't1': '0.3mm±0.20', 't2': '0.3mm±0.20'},
                           '0805': {'Length': '2.00mm ±0.15', 'Width': '1.25mm +0.15/-0.10', 'Height': '0.4mm±0.10',
                                    't1': '0.4mm±0.20', 't2': '0.4mm±0.20'},
                           '1206': {'Length': '3.10mm ±0.15', 'Width': '1.55mm +0.15/-0.10', 'Height': '0.55mm±0.10',
                                    't1': '0.45mm±0.20', 't2': '0.45mm±0.20'},
                           '1210': {'Length': '3.10mm ±0.10', 'Width': '2.60mm ±0.15mm', 'Height': '0.5mm±0.10',
                                    't1': '0.5mm±0.25', 't2': '0.5mm±0.20'},
                           '1812': {'Length': '4.50mm ±0.20', 'Width': '3.20mm ±0.20', 'Height': '0.55mm±0.20',
                                    't1': '0.5mm±0.20', 't2': '0.5mm±0.20'},
                           '2010': {'Length': '5.00mm ±0.10', 'Width': '2.50mm ±0.15', 'Height': '0.55mm±0.10',
                                    't1': '0.6mm±0.25', 't2': '0.5mm±0.20'},
                           '2512': {'Length': '6.35mm ±0.10', 'Width': '3.20mm ±0.15', 'Height': '0.55mm±0.10',
                                    't1': '0.6mm±0.25', 't2': '0.5mm±0.20'}}
        self.special_feature = 'E'
        self.multiplier_str = {-3: 'L', -2: 'K', -1: 'J', 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6'}
        self.dielectric_withstanding_voltage = {'CQ02': '', 'CQ03': '', 'CQ05': '', 'CQ06': '',
                                                'CQ07': '', 'CQ10': '', 'CQ12': ''}

    def get_part_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type, special_feature):
        if tolerance_code in ['G', 'J']:
            resistance_str = '0' + resistance_to_str_multiplier(value, digits=2, multiplier_str=self.multiplier_str)
        else:
            resistance_str = resistance_to_str_multiplier(value, multiplier_str=self.multiplier_str)
        return f"{size_code}{power_rating_code}{tolerance_code}{resistance_str}##{special_feature}"

    def get_order_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type, special_feature):
        if tolerance_code in ['G', 'J']:
            resistance_str = '0' + resistance_to_str_multiplier(value, digits=2, multiplier_str=self.multiplier_str)
        else:
            resistance_str = resistance_to_str_multiplier(value, multiplier_str=self.multiplier_str)
        return f"{size_code}{power_rating_code}{tolerance_code}{resistance_str}{packing_type}{special_feature}"

    def resistance_ranges(self, tolerance, tcr):
        if tolerance in ['F']:  # 1%
            if tcr == '400':
                return {'ranges': [[e24_e96, '(10, 10]']]}
            elif tcr == '200':
                return {'ranges': [[e24_e96, '(10, 100]']]}
            elif tcr == '100':
                return {'ranges': [[e24_e96, '(100, 1000000]']]}
        elif tolerance in ['G', 'J']:  # 2%, 5%
            if tcr == '400':
                return {'ranges': [[e24, '[1, 10]']]}
            elif tcr == '200':
                return {'ranges': [[e24, '(10, 100]']]}
            elif tcr == '100':
                return {'ranges': [[e24, '(100, 10000000]']]}

    def get_resistance_range(self, size, tolerance, tcr, power_rating_code, special_feature):
        if size == 'CQ02' and power_rating_code == 'WG':
            return self.resistance_ranges(tolerance, tcr)
        elif size == 'CQ03' and power_rating_code in ['SA', 'WG']:
            return self.resistance_ranges(tolerance, tcr)
        elif size == 'CQ05' and power_rating_code in ['S8', 'WA']:
            return self.resistance_ranges(tolerance, tcr)
        elif size == 'CQ06' and power_rating_code in ['S4', 'W8']:
            return self.resistance_ranges(tolerance, tcr)
        elif size == 'CQ07' and power_rating_code in ['U2', 'S3', 'W4']:
            return self.resistance_ranges(tolerance, tcr)
        elif size == 'CQ10' and power_rating_code in ['07', 'W1']:
            return self.resistance_ranges(tolerance, tcr)
        elif size == 'CQ12' and power_rating_code in ['1W']:
            return self.resistance_ranges(tolerance, tcr)

    def packaging_data(self, size_code, power_rating_code, code):
        size = self.size_code[size_code]
        if size == '0201' and code == 'TC':
            packaging = {
                'Packaging Code': 'TC', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 10000,
                'Packaging Data': {
                    'Reel Diameter': '', 'Reel Width': '',
                    'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '', 'Tape F': '', 'Tape SO': '',
                    'Tape P0': '', 'Tape P1': '', 'Tape P2': '', 'Tape D': '', 'Tape D1': '', 'Tape A0': '',
                    'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            return packaging
        elif size == '0402' and code == 'TC':
            packaging = {
                'Packaging Code': 'TC', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 10000,
                'Packaging Data': {
                    'Reel Diameter': '', 'Reel Width': '',
                    'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '', 'Tape F': '', 'Tape SO': '',
                    'Tape P0': '', 'Tape P1': '', 'Tape P2': '', 'Tape D': '', 'Tape D1': '', 'Tape A0': '',
                    'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            return packaging
        elif size == '0603' and code == 'T5':
            packaging = {
                'Packaging Code': 'T5', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 5000,
                'Packaging Data': {
                    'Reel Diameter': '', 'Reel Width': '',
                    'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '', 'Tape F': '', 'Tape SO': '',
                    'Tape P0': '', 'Tape P1': '', 'Tape P2': '', 'Tape D': '', 'Tape D1': '', 'Tape A0': '',
                    'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            return packaging
        elif size == '0805' and code == 'T5':
            packaging = {
                'Packaging Code': 'T5', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 5000,
                'Packaging Data': {
                    'Reel Diameter': '', 'Reel Width': '',
                    'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '', 'Tape F': '', 'Tape SO': '',
                    'Tape P0': '', 'Tape P1': '', 'Tape P2': '', 'Tape D': '', 'Tape D1': '', 'Tape A0': '',
                    'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            return packaging
        elif size == '1206' and code == 'T5':
            packaging = {
                'Packaging Code': 'T5', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 5000,
                'Packaging Data': {
                    'Reel Diameter': '', 'Reel Width': '',
                    'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '', 'Tape F': '', 'Tape SO': '',
                    'Tape P0': '', 'Tape P1': '', 'Tape P2': '', 'Tape D': '', 'Tape D1': '', 'Tape A0': '',
                    'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            return packaging
        elif size == '1210' and code == 'T5':
            packaging = {
                'Packaging Code': 'T5', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 5000,
                'Packaging Data': {
                    'Reel Diameter': '', 'Reel Width': '',
                    'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '', 'Tape F': '', 'Tape SO': '',
                    'Tape P0': '', 'Tape P1': '', 'Tape P2': '', 'Tape D': '', 'Tape D1': '', 'Tape A0': '',
                    'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            return packaging
        elif size == '2010' and code == 'T4':
            packaging = {
                'Packaging Code': 'T4', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 4000,
                'Packaging Data': {
                    'Reel Diameter': '', 'Reel Width': '',
                    'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '', 'Tape F': '', 'Tape SO': '',
                    'Tape P0': '', 'Tape P1': '', 'Tape P2': '', 'Tape D': '', 'Tape D1': '', 'Tape A0': '',
                    'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            return packaging
        elif size == '2512' and code == 'T4':
            packaging = {
                'Packaging Code': 'T4', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 4000,
                'Packaging Data': {
                    'Reel Diameter': '', 'Reel Width': '',
                    'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '', 'Tape F': '', 'Tape SO': '',
                    'Tape P0': '', 'Tape P1': '', 'Tape P2': '', 'Tape D': '', 'Tape D1': '', 'Tape A0': '',
                    'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            return packaging

    def get_files(self, partnumber, ordernumber):
        return {}
