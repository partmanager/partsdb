from common.value_series import e24, e24_e96
from .royalohm_common import RoyalohmResistorBase


class RoyalohmHPGenerator(RoyalohmResistorBase):
    def __init__(self):
        super().__init__("Royalohm",
                         "Resistor Thick Film",
                         "HP",
                         "High power thick film chip resistors",
                         operating_temp_range='-55°C ~ 155°C',
                         storage_temp_range='-55°C ~ 125°C',
                         size_code={'HP02': '0402', 'HP03': '0603', 'HP05': '0805', 'HP06': '1206',
                                    'HP07': '1210', 'HP10': '2010', 'HP12': '2512'},
                         package={'HP02': 'Chip 0402', 'HP03': 'Chip 0603', 'HP05': 'Chip 0805', 'HP06': 'Chip 1206',
                                  'HP07': 'Chip 1210', 'HP10': 'Chip 2010', 'HP12': 'Chip 2512'},
                         tolerance={'L': '±0.01%', 'W': '±0.05%', 'B': '±0.1%', 'C': '±0.25%', 'D': '±0.5%',
                                    'F': '±1%', 'G': '±2%', 'J': '±5%'},
                         tcr={'100': '±100ppm/°C', '200': '±200ppm/°C', '400': '±400ppm/°C', '800': '±800ppm/°C'},
                         packaging=['T1', 'T2', 'T4', 'T5', 'TA', 'TC', 'TD', 'TE'],
                         power_rating_codes={'WH': '0.03125W',  # '1/32W',
                                             'WM': '0.05W',  # '1/20W',
                                             'WG': '0.0625W',  # '1/16W',
                                             'WA': '0.1W',  # '1/10W',
                                             'W8': '0.125W',  # '1/8W',
                                             'W5': '0.2W',  # '1/5W',
                                             'W4': '0.25W',  # '1/4W',
                                             'W3': '0.333333333W',  # '1/3W',
                                             'W2': '0.5W',  # '1/2W',
                                             '1W': '1W',
                                             '2W': '2W',
                                             '34': '0.75W',  # '3/4W',
                                             'SA': '0.1W',  # '1/10W',
                                             'S8': '0.125W',  # '1/8W',
                                             'S4': '0.25W',  # '1/4W',
                                             'S3': '0.333333333W',  # '1/3W',
                                             '07': '0.75W',  # '3/4W',
                                             'U2': '0.5W',  # '1/2W'
                                             },
                         product_url='',
                         notes='')
        self.max_working_voltage = {'HP02': '50V', 'HP03': '50V', 'HP05': '150V', 'HP06': '200V',
                                    'HP07': '200V', 'HP10': '200V', 'HP12': '250V'}
        self.max_overload_voltage = {'HP02': '100V', 'HP03': '100V', 'HP05': '300V', 'HP06': '400V',
                                     'HP07': '500V', 'HP10': '500V', 'HP12': '500V'}
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
        self.multiplier_str = {-3: 'L', -2: 'K', -1: 'J', 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6'}
        self.short_value_code_tolerance_list = ['G', 'J']
        self.special_feature = 'E'

    def resistance_ranges(self, size, tolerance, tcr):
        if size == 'HP02':
            if tolerance in ['F']:  # 1%
                if tcr == '400':
                    return {'ranges': [[e24_e96, '[1, 10]']]}
                elif tcr == '200':
                    return {'ranges': [[e24_e96, '(10, 100]']]}
                elif tcr == '100':
                    return {'ranges': [[e24_e96, '(100, 10000000]']]}
            elif tolerance in ['J']:  #5%
                if tcr == '200':
                    return {'ranges': [[e24, '[1, 10]']]}
                elif tcr == '100':
                    return {'ranges': [[e24, '(10, 10000000]']]}
        else:
            if tolerance in ['F']:  # 1%
                if tcr == '200':
                    return {'ranges': [[e24_e96, '[1, 10]']]}
                elif tcr == '100':
                    return {'ranges': [[e24_e96, '(10, 10000000]']]}
            elif tolerance in ['J']:  #5%
                if tcr == '200':
                    return {'ranges': [[e24, '[1, 10]']]}
                elif tcr == '100':
                    return {'ranges': [[e24, '(10, 10000000]']]}

    def get_resistance_range(self, size, tolerance, tcr, power_rating_code, special_feature):
        if size == 'HP02' and power_rating_code == 'WA':
            return self.resistance_ranges(size, tolerance, tcr)
        elif size == 'HP03' and power_rating_code == 'W5':
            return self.resistance_ranges(size, tolerance, tcr)
        elif size == 'HP05' and power_rating_code == 'W3':
            return self.resistance_ranges(size, tolerance, tcr)
        elif size == 'HP06' and power_rating_code == 'W2':
            return self.resistance_ranges(size, tolerance, tcr)
        elif size == 'HP07' and power_rating_code == '34':
            return self.resistance_ranges(size, tolerance, tcr)
        elif size == 'HP10' and power_rating_code == '1W':
            return self.resistance_ranges(size, tolerance, tcr)
        elif size == 'HP12' and power_rating_code == '2W':
            return self.resistance_ranges(size, tolerance, tcr)

    def get_files(self, partnumber, ordernumber):
        return {}

