from common.value_series import e24, e24_e96
from .royalohm_common import RoyalohmResistorBase


class RoyalohmGeneralPurposeThickFilmChipResistorGenerator(RoyalohmResistorBase):
    def __init__(self):
        super().__init__("Royalohm",
                         "Resistor Thick Film",
                         "Generic Thick Film Chip Resistors",
                         "Thick Film Chip Resistors",
                         operating_temp_range='-55°C ~ 155°C',
                         storage_temp_range='-55°C ~ 125°C',
                         size_code={'0201': '0201', '0402': '0402', '0603': '0603', '0805': '0805', '1206': '1206',
                                    '1210': '1210', '1812': '1812', '2010': '2010', '2512': '2512'},
                         package={'0201': 'Chip 0201', '0402': 'Chip 0402', '0603': 'Chip 0603', '0805': 'Chip 0805',
                                  '1206': 'Chip 1206', '1210': 'Chip 1210', '1812': 'Chip 1812', '2010': 'Chip 2010',
                                  '2512': 'Chip 2512'},
                         tolerance={'L': '±0.01%', 'W': '±0.05%', 'B': '±0.1%', 'C': '±0.25%', 'D': '±0.5%',
                                    'F': '±1%', 'G': '±2%', 'J': '±5%'},
                         tcr={'100': '±100ppm/°C', '200': '±200ppm/°C', '400': '±400ppm/°C', '800': '±800ppm/°C'},
                         packaging=['T1', 'T2', 'T4', 'T5', 'TA', 'TC', 'TD', 'TE'],
                         power_rating_codes={'WH': '0.03125W',  # '1/32W',
                                             'WM': '0.05W',  # '1/20W',
                                             'WG': '0.0625',  # '1/16W',
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
        self.max_working_voltage = {'0201': '25V', '0402': '50V', '0603': '75V', '0805': '150V', '1206': '200V',
                                    '1210': '200V', '1812': '200V', '2010': '200V', '2512': '200V'}
        self.max_overload_voltage = {'0201': '50V', '0402': '100V', '0603': '150V', '0805': '300V', '1206': '400V',
                                     '1210': '500V', '1812': '500V', '2010': '500V', '2512': '500V'}
        self.dielectric_withstanding_voltage = {'0201': '', '0402': '100V', '0603': '300V', '0805': '500V',
                                                '1206': '500V', '1210': '500V', '1812': '500V', '2010': '500V',
                                                '2512': '500V'}

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
        self.short_value_code_tolerance_list = ['J']
        self.special_feature = 'E'

    def get_resistance_range(self, size, tolerance, tcr, power_rating_code, special_feature):
        if size == '0201' and power_rating_code == 'WM':
            if tolerance in ['F', 'G']:
                if tcr == '-100+350':
                    return {'ranges': [[e24_e96, "[10, 10]"]]}
                elif tcr == '200':
                    return {'ranges': [[e24_e96, "(10, 10000000]"]]}
            elif tolerance == 'J':
                if tcr == '-100+350':
                    return {'ranges': [[e24, "[1, 10]"]]}
                elif tcr == '200':
                    return {'ranges': [[e24, "(10, 10000000]"]]}
        if size == '0402' and power_rating_code == 'WG':
            if tolerance in ['D', 'F', 'G']:
                if tcr == '200':
                    return {'ranges': [[e24_e96, "[1, 10]"]]}
                elif tcr == '100':
                    return {'ranges': [[e24_e96, "(10, 10000000]"]]}
            elif tolerance == 'J':
                if tcr == '200':
                    return {'ranges': [[e24, "[1, 10]"]]}
                elif tcr == '100':
                    return {'ranges': [[e24, "(10, 10000000]"]]}
        if size == '0603' and power_rating_code in ['WA', 'SA']:
            if tolerance == 'D':
                if tcr == '200':
                    return {'ranges': [[e24_e96, "[1, 10]"]]}
                elif tcr == '100':
                    return {'ranges': [[e24_e96, "(10, 10000000]"]]}
            elif tolerance in ['F', 'G']:
                if tcr == '800':
                    return {'ranges': [[e24_e96, "[0.1, 1)"]]}
                elif tcr == '200':
                    return {'ranges': [[e24_e96, "[1, 10]"]]}
                elif tcr == '100':
                    return {'ranges': [[e24_e96, "(10, 10000000]"]]}
            elif tolerance == 'J':
                if tcr == '800':
                    return {'ranges': [[e24, "[0.1, 1)"]]}
                elif tcr == '200':
                    return {'ranges': [[e24, "[1, 10]"]]}
                elif tcr == '100':
                    return {'ranges': [[e24, "(10, 10000000]"]]}
        elif size == '0805':
            if power_rating_code in ['W8', 'S8']:
                if tolerance == 'D':
                    if tcr == '200':
                        return {'ranges': [[e24_e96, "[1, 10]"]]}
                    elif tcr == '100':
                        return {'ranges': [[e24_e96, "(10, 10000000]"]]}
                elif tolerance in ['F', 'G']:
                    if tcr == '800':
                        return {'ranges': [[e24_e96, "[0.1, 1)"]]}
                    elif tcr == '200':
                        return {'ranges': [[e24_e96, "[1, 10]"]]}
                    elif tcr == '100':
                        return {'ranges': [[e24_e96, "(10, 10000000]"]]}
                elif tolerance == 'J':
                    if tcr == '800':
                        return {'ranges': [[e24, "[0.1, 1)"]]}
                    elif tcr == '200':
                        return {'ranges': [[e24, "[1, 10]"]]}
                    elif tcr == '100':
                        return {'ranges': [[e24, "(10, 10000000]"]]}
            elif power_rating_code == 'W4':
                if tolerance in ['F', 'G']:
                    if tcr == '1500':
                        return {'ranges': [[e24_e96, "[0.01, 0.015]"]]}
                    if tcr == '1000':
                        return {'ranges': [[e24_e96, "(0.015, 0.03]"]]}
                    elif tcr == '800':
                        return {'ranges': [[e24_e96, "(0.03, 0.1)"]]}
                elif tolerance == 'J':
                    if tcr == '1500':
                        return {'ranges': [[e24, "[0.01, 0.015]"]]}
                    if tcr == '1000':
                        return {'ranges': [[e24, "(0.015, 0.03]"]]}
                    elif tcr == '800':
                        return {'ranges': [[e24, "(0.03, 0.1)"]]}
        elif size == '1206':
            if power_rating_code in ['W4', 'S4']:
                return self.common_resistance_range(tolerance, tcr)
            elif power_rating_code == 'W3':
                if tolerance in ['F', 'G']:
                    if tcr == '1500':
                        return {'ranges': [[e24_e96, "[0.01, 0.015]"]]}
                    if tcr == '1000':
                        return {'ranges': [[e24_e96, "(0.015, 0.03]"]]}
                    elif tcr == '800':
                        return {'ranges': [[e24_e96, "(0.03, 0.1)"]]}
                elif tolerance == 'J':
                    if tcr == '1500':
                        return {'ranges': [[e24, "[0.01, 0.015]"]]}
                    if tcr == '1000':
                        return {'ranges': [[e24, "(0.015, 0.03]"]]}
                    elif tcr == '800':
                        return {'ranges': [[e24, "(0.03, 0.1)"]]}
        elif size == '1210' and power_rating_code in ['W2', 'U2']:
            return self.common_resistance_range(tolerance, tcr)
        elif size == '1812' and power_rating_code == '34':
            return self.common_resistance_range(tolerance, tcr)
        elif size == '2010' and power_rating_code in ['34', '07']:
            return self.common_resistance_range(tolerance, tcr)
        elif size == '2512' and power_rating_code == '1W':
            return self.common_resistance_range(tolerance, tcr)

    def common_resistance_range(self, tolerance, tcr):
        if tolerance == 'D':
            if tcr == '200':
                return {'ranges': [[e24_e96, "[1, 10]"]]}
            elif tcr == '100':
                return {'ranges': [[e24_e96, "(10, 10000000]"]]}
        if tolerance in ['F', 'G']:
            if tcr == '1500':
                return {'ranges': [[e24_e96, "[0.01, 0.015]"]]}
            if tcr == '1000':
                return {'ranges': [[e24_e96, "(0.015, 0.03]"]]}
            elif tcr == '800':
                return {'ranges': [[e24_e96, "(0.03, 1)"]]}
            elif tcr == '200':
                return {'ranges': [[e24_e96, "[1, 10]"]]}
            elif tcr == '100':
                return {'ranges': [[e24_e96, "(10, 10000000]"]]}
        elif tolerance == 'J':
            if tcr == '1500':
                return {'ranges': [[e24, "[0.01, 0.015]"]]}
            if tcr == '1000':
                return {'ranges': [[e24, "(0.015, 0.03]"]]}
            elif tcr == '800':
                return {'ranges': [[e24, "(0.03, 1)"]]}
            elif tcr == '200':
                return {'ranges': [[e24, "[1, 10]"]]}
            elif tcr == '100':
                return {'ranges': [[e24, "(10, 10000000]"]]}

    def get_files(self, partnumber, ordernumber):
        return {'datasheet': 'www.royalohm.com/pdf/product2017/GeneralPurpose.pdf'}
