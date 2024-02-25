from .yageo_common import *
from common.value_series import e24, e24_e96

allowed_taping_reel = {'0075': ['7N'], '0100': ['07', '13', '7N'], '0201': ['07', '10', '13'],
                       '0402': ['07', '10', '13', '7W', '3W'], '0603': ['07', '10', '13', '7W', '3W'],
                       '0805': ['07', '10', '13', '7W', '3W'], '1206': ['07', '10', '13', '7W', '3W'],
                       '1210': ['07', '10', '13'], '1218': ['07'], '2010': ['07'], '2512': ['07', '7W']}


class YageoRCLResistorGenerator(YageoResistorBase):
    def __init__(self):
        super().__init__(part_type="Resistor Thick Film",
                         series="RC_L",
                         series_description="General Purpose Chip Resistors",
                         operating_temp_range='-55°C ~ 155°C',
                         storage_temp_range='5°C ~ 35°C',
                         size_code={'RC0075': '0075', 'RC0100': '0100', 'RC0201': '0201', 'RC0402': '0402',
                                    'RC0603': '0603', 'RC0805': '0805', 'RC1206': '1206', 'RC1210': '1210',
                                    'RC1218': '1218', 'RC2010': '2010', 'RC2512': '2512'},
                         package={'RC0075': 'Chip 0075', 'RC0100': 'Chip 0100', 'RC0201': 'Chip 0201',
                                  'RC0402': 'Chip 0402', 'RC0603': 'Chip 0603', 'RC0805': 'Chip 0805',
                                  'RC1206': 'Chip 1206', 'RC1210': 'Chip 1210', 'RC1218': 'Chip 1218',
                                  'RC2010': 'Chip 2010', 'RC2512': 'Chip 2512'},
                         packaging=['R_07', 'R_10', 'R_13', 'R_7W', 'R_3W', 'K_07', 'K_10', 'K_13', 'K_7W', 'K_3W',
                                    'S_7N'],
                         power_rating_codes={'1/20W': '50mW', '1/16W': '62.5mW', '1/8W': '125mW', '1/10W': '100mW',
                                             '1/5W': '0.2W', '1/4W': '0.25W', '1/2W': '0.5W', '1W': '1W', '1.5W': '1.5W',
                                             '3/4W': '0.75W', '1.25W': '1.25W', '2W': '2W',
                                             '1/20D': '50mW', '1/16D': '62.5mW', '1/8D': '125mW', '1/10D': '0.1W',
                                             '1/5D': '0.2W', '1/4D': '0.25W', '1/2D': '0.5W', '1D': '1W', '1.5D': '1.5W',
                                             '3/4D': '0.75W', '1.25D': '1.25W', '2D': '2W'},  # D indicates dual power
                         product_url='',
                         notes="Generated based on data from datasheet: Revision: 201304")
        self.max_working_voltage = {'RC0075': '10V', 'RC0100': '15V', 'RC0201': '25V', 'RC0402': '50V', 'RC0603': '75V',
                                    'RC0805': '150V', 'RC1206': '200V', 'RC1210': '200V', 'RC1218': '200V',
                                    'RC2010': '200V', 'RC2512': '200V'}
        self.max_overload_voltage = {'RC0075': '25V', 'RC0100': '30V', 'RC0201': '50V', 'RC0402': '100V',
                                     'RC0603': '150V', 'RC0805': '300V', 'RC1206': '400V', 'RC1210': '500V',
                                     'RC1218': '500V', 'RC2010': '500V', 'RC2512': '500V'}
        self.dielectric_withstanding_voltage = {'RC0075': '25V', 'RC0100': '30V', 'RC0201': '50V', 'RC0402': '100V',
                                                'RC0603': '150V', 'RC0805': '300V', 'RC1206': '500V', 'RC1210': '500V',
                                                'RC1218': '500V', 'RC2010': '500V', 'RC2512': '500V'}
        self.max_temperature = {'RC0075': '125', 'RC0100': '125', 'RC0201': '125', 'RC0402': '155', 'RC0603': '155',
                                'RC0805': '155', 'RC1206': '155', 'RC1210': '155', 'RC1218': '155', 'RC2010': '155',
                                'RC2512': '155'}
        self.dimensions = {
            '0075': {'Length': '0.30mm ±0.015', 'Width': '0.15mm ±0.015', 'Height': '0.13mm±0.02', 't1': '0.08mm±0.03',
                     't2': '0.08±0.03mm'},
            '0100': {'Length': '0.40mm ±0.02', 'Width': '0.20mm ±0.02', 'Height': '0.13mm±0.02', 't1': '0.10mm±0.03',
                     't2': '0.10±0.03mm'},
            '0201': {'Length': '0.60mm ±0.03', 'Width': '0.30mm ±0.03', 'Height': '0.23mm±0.03', 't1': '0.10mm±0.05',
                     't2': '0.15±0.05mm'},
            '0402': {'Length': '1.00mm ±0.05', 'Width': '0.50mm ±0.05', 'Height': '0.35mm±0.05', 't1': '0.20mm±0.10',
                     't2': '0.25±0.10mm'},
            '0603': {'Length': '1.60mm ±0.10', 'Width': '0.80mm ±0.10', 'Height': '0.45mm±0.10', 't1': '0.25mm±0.15',
                     't2': '0.25mm±0.15'},
            '0805': {'Length': '2.00mm ±0.10', 'Width': '1.25mm ±0.10', 'Height': '0.5mm±0.10', 't1': '0.35mm±0.20',
                     't2': '0.35mm±0.20'},
            '1206': {'Length': '3.10mm ±0.15', 'Width': '1.60mm ±0.10', 'Height': '0.55mm±0.10', 't1': '0.45mm ±0.20',
                     't2': '0.45mm±0.20'},
            '1210': {'Length': '3.10mm ±0.10', 'Width': '2.60mm ±0.15', 'Height': '0.55mm±0.10', 't1': '0.45mm ±0.15',
                     't2': '0.5mm±0.20'},
            '1218': {'Length': '3.10mm ±0.10', 'Width': '4.60mm ±0.10', 'Height': '0.55mm±0.10', 't1': '0.45mm ±0.20',
                     't2': '0.40mm±0.20'},
            '2010': {'Length': '5.00mm ±0.10', 'Width': '2.50mm ±0.15', 'Height': '0.55mm±0.10', 't1': '0.45mm ±0.15',
                     't2': '0.5mm±0.20'},
            '2512': {'Length': '6.35mm ±0.10', 'Width': '3.10mm ±0.15', 'Height': '0.55mm±0.10', 't1': '0.6mm ±0.20',
                     't2': '0.5mm ±0.20'}}

    def get_operating_temperature_range(self, size_code, power_rating_code, partnumber):
        return '-55°C ~ {}°C'.format(self.max_temperature[size_code])

    def get_resistance_range(self, size_code, tolerance_code, tcr_code, power_rating_code, special_feature):
        if size_code == 'RC0075' and tolerance_code in ['F', 'J'] and power_rating_code == '1/50W':
            if tolerance_code == 'F':
                if tcr_code == '-200+600':
                    return {'ranges': [[e24_e96, '[10, 100)']]}
                elif tcr_code == '200':
                    return {'ranges': [[e24_e96, '[100, 1000000]']]}
            elif tolerance_code == 'J':
                if tcr_code == '-200+600':
                    return {'ranges': [[e24, '[10, 100)']]}
                elif tcr_code == '200':
                    return {'ranges': [[e24, '[100, 1000000]']]}
        elif size_code == 'RC0100' and power_rating_code == '1/32W':
            if tolerance_code == 'D':
                if tcr_code == '300':
                    return {'ranges': [[e24_e96, '[33, 100)']]}
                elif tcr_code == '200':
                    return {'ranges': [[e24_e96, '[10, 470000]']]}
            elif tolerance_code == 'F':
                if tcr_code == '-200+600':
                    return {'ranges': [[e24_e96, '[1, 10)']]}
                elif tcr_code == '300':
                    return {'ranges': [[e24_e96, '[10, 100)']]}
                elif tcr_code == '200':
                    return {'ranges': [[e24_e96, '[100, 10000000]']]}
            elif tolerance_code == 'J':
                if tcr_code == '-200+600':
                    return {'ranges': [[e24, '[1, 10)']]}
                elif tcr_code == '300':
                    return {'ranges': [[e24, '[10, 100)']]}
                elif tcr_code == '200':
                    return {'ranges': [[e24, '[100, 10000000]']]}
                elif tcr_code == '250':
                    return {'ranges': [[e24, '(10000000, 22000000]']]}
        elif size_code == 'RC0201' and power_rating_code == '1/20W':
            if tolerance_code == 'B':
                if tcr_code == '-100+350':
                    return {'ranges': [[e24_e96, '[10, 10]']]}
                elif tcr_code == '200':
                    return {'ranges': [[e24_e96, '(10, 1000000]']]}
            elif tolerance_code == 'D':
                if tcr_code == '-100+350':
                    return {'ranges': [[e24_e96, '[1, 10]']]}
                elif tcr_code == '200':
                    return {'ranges': [[e24_e96, '(10, 1000000]']]}
            elif tolerance_code == 'F':
                if tcr_code == '-100+350':
                    return {'ranges': [[e24_e96, '[1, 10]']]}
                elif tcr_code == '200':
                    return {'ranges': [[e24_e96, '(10, 10000000]']]}
            elif tolerance_code == 'J':
                if tcr_code == '-100+350':
                    return {'ranges': [[e24, '[1, 10]']]}
                elif tcr_code == '200':
                    return {'ranges': [[e24, '(10, 10000000]']]}
        elif size_code == 'RC0402':
            if power_rating_code == '1/16W':
                if tolerance_code == 'B':
                    if tcr_code == '200':
                        return {'ranges': [[e24_e96, '[10, 10]']]}
                    elif tcr_code == '100':
                        return {'ranges': [[e24_e96, '(10, 1000000]']]}
                elif tolerance_code == 'D':
                    if tcr_code == '200':
                        return {'ranges': [[e24_e96, '[1, 10]']]}
                    elif tcr_code == '100':
                        return {'ranges': [[e24_e96, '(10, 1000000]']]}
                elif tolerance_code == 'F':
                    if tcr_code == '200':
                        return {'ranges': [[e24_e96, '[1, 10]']]}
                    elif tcr_code == '100':
                        return {'ranges': [[e24_e96, '(10, 10000000]']]}
                elif tolerance_code == 'J':
                    if tcr_code == '200':
                        return {'ranges': [[e24, '[1, 10]'], [e24, '(10000000, 22000000]']]}
                    elif tcr_code == '100':
                        return {'ranges': [[e24, '(10, 10000000]']]}
            elif power_rating_code == '1/8D':
                if tolerance_code == 'F' and tcr_code == '200':
                    return {'ranges': [[e24_e96, '[1, 1000000]']]}
                elif tolerance_code == 'J' and tcr_code == '200':
                    return {'ranges': [[e24, '[1, 1000000]']]}
        elif size_code == 'RC0603':
            if power_rating_code == '1/10W':
                if tolerance_code == 'B':
                    if tcr_code == '200':
                        return {'ranges': [[e24_e96, '[10, 10]']]}
                    elif tcr_code == '100':
                        return {'ranges': [[e24_e96, '(10, 1000000]']]}
                elif tolerance_code == 'D':
                    if tcr_code == '200':
                        return {'ranges': [[e24_e96, '[1, 10]']]}
                    elif tcr_code == '100':
                        return {'ranges': [[e24_e96, '(10, 1000000]']]}
                elif tolerance_code == 'F':
                    if tcr_code == '200':
                        return {'ranges': [[e24_e96, '[1, 10]']]}
                    elif tcr_code == '100':
                        return {'ranges': [[e24_e96, '(10, 10000000]']]}
                elif tolerance_code == 'J':
                    if tcr_code == '200':
                        return {'ranges': [[e24, '[1, 10]'], [e24, '(10000000, 22000000]']]}
                    elif tcr_code == '100':
                        return {'ranges': [[e24, '(10, 10000000]']]}
            elif power_rating_code == '1/5D':
                if tolerance_code == 'F' and tcr_code == '200':
                    return {'ranges': [[e24_e96, '[1, 1000000]']]}
                elif tolerance_code == 'J' and tcr_code == '200':
                    return {'ranges': [[e24, '[1, 1000000]']]}
        elif size_code == 'RC0805':
            if power_rating_code == '1/8W':
                if tolerance_code == 'B':
                    if tcr_code == '200':
                        return {'ranges': [[e24_e96, '[10, 10]']]}
                    elif tcr_code == '100':
                        return {'ranges': [[e24_e96, '(10, 1000000]']]}
                elif tolerance_code == 'D':
                    if tcr_code == '200':
                        return {'ranges': [[e24_e96, '[1, 10]']]}
                    elif tcr_code == '100':
                        return {'ranges': [[e24_e96, '(10, 1000000]']]}
                elif tolerance_code == 'F':  # 1%
                    if tcr_code == '200':
                        return {'ranges': [[e24_e96, '[1, 10]']]}
                    elif tcr_code == '100':
                        return {'ranges': [[e24_e96, '(10, 10000000]']]}
                elif tolerance_code == 'J':  # 5%
                    if tcr_code == '200':
                        return {'ranges': [[e24, '[1, 10]'], [e24, '(10000000, 22000000]']]}
                    elif tcr_code == '100':
                        return {'ranges': [[e24, '(10, 10000000]']]}
                    elif tcr_code == '300':
                        return {'ranges': [[e24, '(24000000, 100000000]']]}
                #elif tolerance_code in ['', '']:  # 10%, 20%
                #    if tcr_code == '300':
                #        return {'ranges': [[e24, '[24000000, 100000000]']]}
            elif power_rating_code == '1/4D':
                if tolerance_code == 'F' and tcr_code == '200':
                    return {'ranges': [[e24_e96, '[1, 1000000]']]}
                elif tolerance_code == 'J' and tcr_code == '200':
                    return {'ranges': [[e24, '[1, 1000000]']]}
        elif size_code == 'RC1206':
            if power_rating_code == '1/4W':
                if power_rating_code == '1/8W':
                    if tolerance_code == 'B':
                        if tcr_code == '200':
                            return {'ranges': [[e24_e96, '[10, 10]']]}
                        elif tcr_code == '100':
                            return {'ranges': [[e24_e96, '(10, 1000000]']]}
                    elif tolerance_code == 'D':
                        if tcr_code == '200':
                            return {'ranges': [[e24_e96, '[1, 10]']]}
                        elif tcr_code == '100':
                            return {'ranges': [[e24_e96, '(10, 1000000]']]}
                    elif tolerance_code == 'F':  # 1%
                        if tcr_code == '200':
                            return {'ranges': [[e24_e96, '[1, 10]']]}
                        elif tcr_code == '100':
                            return {'ranges': [[e24_e96, '(10, 10000000]']]}
                    elif tolerance_code == 'J':  # 5%
                        if tcr_code == '200':
                            return {'ranges': [[e24, '[1, 10]'], [e24, '(10000000, 22000000]']]}
                        elif tcr_code == '100':
                            return {'ranges': [[e24, '(10, 10000000]']]}
                        elif tcr_code == '300':
                            return {'ranges': [[e24, '(24000000, 100000000]']]}
                    # elif tolerance_code in ['', '']:  # 10%, 20%
                    #    if tcr_code == '300':
                    #        return {'ranges': [[e24, '[24000000, 100000000]']]}
                elif power_rating_code == '1/2D':
                    if tolerance_code == 'F' and tcr_code == '200':
                        return {'ranges': [[e24_e96, '[1, 1000000]']]}
                    elif tolerance_code == 'J' and tcr_code == '200':
                        return {'ranges': [[e24, '[1, 1000000]']]}
        elif size_code == 'RC1210' and power_rating_code == '1/2W':
            if tolerance_code == 'B':
                if tcr_code == '200':
                    return {'ranges': [[e24_e96, '[10, 10]']]}
                elif tcr_code == '100':
                    return {'ranges': [[e24_e96, '(10, 1000000]']]}
            elif tolerance_code == 'D':
                if tcr_code == '200':
                    return {'ranges': [[e24_e96, '[10, 10]']]}
                elif tcr_code == '100':
                    return {'ranges': [[e24_e96, '(10, 1000000]']]}
            elif tolerance_code == 'F':  # 1%
                if tcr_code == '200':
                    return {'ranges': [[e24_e96, '[1, 10]']]}
                elif tcr_code == '100':
                    return {'ranges': [[e24_e96, '(10, 10000000]']]}
            elif tolerance_code == 'J':  # 5%
                if tcr_code == '200':
                    return {'ranges': [[e24, '[1, 10]'], [e24, '(10000000, 22000000]']]}
                elif tcr_code == '100':
                    return {'ranges': [[e24, '(10, 10000000]']]}
        elif size_code == 'RC1218' and power_rating_code == '1W':
            if tolerance_code in ['B', 'D']:
                if tcr_code == '200':
                    return {'ranges': [[e24_e96, '[10, 10]']]}
                elif tcr_code == '100':
                    return {'ranges': [[e24_e96, '(10, 1000000]']]}
            elif tolerance_code == 'F':  # 1%
                if tcr_code == '200':
                    return {'ranges': [[e24_e96, '[1, 10]']]}
                elif tcr_code == '100':
                    return {'ranges': [[e24_e96, '(10, 1000000]']]}
            elif tolerance_code == 'J':  # 5%
                if tcr_code == '200':
                    return {'ranges': [[e24, '[1, 10]']]}
                elif tcr_code == '100':
                    return {'ranges': [[e24, '(10, 1000000]']]}
        elif size_code == 'RC2010' and power_rating_code == '3/4W':
            if tolerance_code in ['B', 'D']:
                if tcr_code == '200':
                    return {'ranges': [[e24_e96, '[10, 10]']]}
                elif tcr_code == '100':
                    return {'ranges': [[e24_e96, '(10, 1000000]']]}
            elif tolerance_code == 'F':  # 1%
                if tcr_code == '200':
                    return {'ranges': [[e24_e96, '[1, 10]']]}
                elif tcr_code == '100':
                    return {'ranges': [[e24_e96, '(10, 10000000]']]}
            elif tolerance_code == 'J':  # 5%
                if tcr_code == '200':
                    return {'ranges': [[e24, '[1, 10]'], [e24, '(10000000, 22000000]']]}
                elif tcr_code == '100':
                    return {'ranges': [[e24, '(10, 1000000]']]}
        elif size_code == 'RC2512':
            if power_rating_code == '1W':
                if tolerance_code in ['B', 'D']:
                    if tcr_code == '200':
                        return {'ranges': [[e24_e96, '[10, 10]']]}
                    elif tcr_code == '100':
                        return {'ranges': [[e24_e96, '(10, 1000000]']]}
                elif tolerance_code == 'F':  # 1%
                    if tcr_code == '200':
                        return {'ranges': [[e24_e96, '[1, 10]']]}
                    elif tcr_code == '100':
                        return {'ranges': [[e24_e96, '(10, 10000000]']]}
                elif tolerance_code == 'J':  # 5%
                    if tcr_code == '200':
                        return {'ranges': [[e24, '[1, 10]'], [e24, '(10000000, 22000000]']]}
                    elif tcr_code == '100':
                        return {'ranges': [[e24, '(10, 1000000]']]}
            elif power_rating_code == '2D':
                if tolerance_code == 'F' and tcr_code == '200':
                    return {'ranges': [[e24_e96, '[1, 1000000]']]}
                elif tolerance_code == 'J' and tcr_code == '200':
                    return {'ranges': [[e24, '[1, 1000000]']]}

    def packaging_data(self, size_code, power_rating_code, packaging_code):
        packaging_type, taping_reel = packaging_code.split('_')
        return self.get_packaging_detail(size_code, packaging_type, taping_reel)

    def get_files(self, partnumber, ordernumber):
        return {}

    # def packaging_data(self, size_code, power_rating_code, packaging_code):
    #     packaging = {'Packaging Code': packaging_code, 'Packaging Type': '', 'Packaging Qty': ''}
    #     return packaging
    #
    # def get_packaging_information(self, size, packaging_type, taping_reel):
    #     qty = self.get_packaging_quantity(size, packaging_type, taping_reel)
    #     if qty:
    #         return {'Packaging Qty': qty,
    #                 'Packaging Type': "Paper Tape / Reel" if packaging_type == 'R' else "Embossed Tape / Reel",
    #                 'Reel Diameter': self.reel_size[taping_reel] + '"',
    #                 'Tape Pin 1 Quadrant': 'Q1',
    #                 'Tape W': '8mm'
    #                 }

    # def get_packaging_code(self, packaging_type, taping_reel):
    #     return f"{packaging_type}-{taping_reel}"

    # def get_packaging_quantity(self, size, packaging_type, taping_reel):
    #     qty = {'0075': {'7_R': None, '10_R': None, '13_R': None, '7_S': 20000, '7_K': None},
    #            '0100': {'7_R': 20000, '10_R': None, '13_R': 80000, '7_S': 40000, '7_K': None},
    #            '0201': {'7_R': 10000, '10_R': 20000, '13_R': 50000, '7_S': None, '7_K': None},
    #            '0402': {'7_R': 10000, '10_R': 20000, '13_R': 50000, '7_S': None, '7_K': None},
    #            '0603': {'7_R': 5000, '10_R': 10000, '13_R': 20000, '7_S': None, '7_K': None},
    #            '0805': {'7_R': 5000, '10_R': 10000, '13_R': 20000, '7_S': None, '7_K': None},
    #            '1206': {'7_R': 5000, '10_R': 10000, '13_R': 20000, '7_S': None, '7_K': None},
    #            '1210': {'7_R': 5000, '10_R': 10000, '13_R': 20000, '7_S': None, '7_K': None},
    #            '1218': {'7_R': None, '10_R': None, '13_R': None, '7_S': None, '7_K': 4000},
    #            '2010': {'7_R': None, '10_R': None, '13_R': None, '7_S': None, '7_K': 4000},
    #            '2512': {'7_R': None, '10_R': None, '13_R': None, '7_S': None, '7_K': 4000},
    #            }
    #     key = self.reel_size[taping_reel] + '_' + packaging_type
    #     return qty[size][key] if key in qty[size] else None
