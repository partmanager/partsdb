from common.value_series import e24, e24_e96
from common.value_encoder import digits_multiplier_encoder
from .royalohm_common import RoyalohmResistorBase


class RoyalohmMFGenerator(RoyalohmResistorBase):
    def __init__(self):
        super().__init__("Royalohm",
                         "Resistor Metal Film",
                         "MF",
                         "Precision Metal Film Resistors",
                         operating_temp_range='-55°C ~ 155°C',
                         storage_temp_range='-55°C ~ 125°C',
                         size_code={'MF0': 'MF0', 'MFF': 'MFF'},
                         package={'MF0': 'Resistor Axial', 'MFF': 'Resistor Axial'},
                         tolerance={'L': '±0.01%', 'W': '±0.05%', 'B': '±0.1%', 'C': '±0.25%', 'D': '±0.5%',
                                    'F': '±1%', 'G': '±2%', 'J': '±5%', 'K': '±10%'},
                         tcr={'F': '±50ppm/°C', 'G': '±100ppm/°C', 'J': '±200ppm/°C', '350': '±350ppm/°C',
                              '400': '±400ppm/°C',
                              '800': '±800ppm/°C',
                              '+0/-450': '+0 ~ -400ppm/°C', '+0/-700': '+0 ~ -700ppm/°C',
                              '+0/-1500': '+0 ~ -1500ppm/°C'},
                         packaging=['A1', 'A5', 'T1', 'T2', 'T4', 'T5', 'TA', 'TC', 'TD', 'TE', 'B0'],
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
                                             '5W': '5W',
                                             '7W': '7W',
                                             'AW': '10W',
                                             'FW': '15W',
                                             '04': '0.4W',
                                             '06': '0.6W',
                                             '07': '0.75W',  # '3/4W',
                                             '20': '20W',
                                             '25': '25W',
                                             'SA': '0.1W',  # '1/10W',
                                             'S8': '0.125W',  # '1/8W',
                                             'S4': '0.25W',  # '1/4W',
                                             'S3': '0.333333333W',  # '1/3W',
                                             'S2': '0.5W',  # '1/2W',
                                             '1S': '1W',
                                             '2S': '2W',
                                             '3S': '3W',
                                             'U2': '0.5W',  # '1/2W',
                                             '2U': '2W',
                                             '3U': '3W',
                                             'M7': '0.75W'},
                         product_url='',
                         notes='')
        self.special_feature = ['0', '9']
        self.multiplier_str = {-3: 'L', -2: 'K', -1: 'J', 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6'}
        self.short_value_code_tolerance_list = ['G', 'J', 'K']
        self.max_operating_voltage = {'MF0W8': '200V', 'MF0S4': '200V', 'MFF04': '200V', 'MF0W4': '250V',
                                      'MF006': '250V', 'MFFU2': '250V', 'MF0W2': '350V', 'MF0S2': '350V',
                                      'MF0M7': '350V', 'MF01S': '350V', 'MF02S': '500V', 'MF03S': '500V',
                                      'MF01W': '500V', 'MF02W': '500V', 'MF03W': '500V'}
        self.max_overload_voltage = {'MF0W8': '400V', 'MF0S4': '400V', 'MFF04': '400V', 'MF0W4': '500V',
                                     'MF006': '500V', 'MFFU2': '500V', 'MF0W2': '700V', 'MF0S2': '700V',
                                     'MF0M7': '700V', 'MF01S': '700V', 'MF02S': '1000V', 'MF03S': '1000V',
                                     'MF01W': '1000V', 'MF02W': '1000V', 'MF03W': '1000V'}
        self.dielectric_withstanding_voltage = {'MF0W8': '400V', 'MF0S4': '400V', 'MFF04': '400V', 'MF0W4': '500V',
                                                'MF006': '500V', 'MFFU2': '250V', 'MF0W2': '700V', 'MF0S2': '700V',
                                                'MF0M7': '700V', 'MF01S': '700V', 'MF02S': '1000V', 'MF03S': '1000V',
                                                'MF01W': '1000V', 'MF02W': '1000V', 'MF03W': '1000V'}
        self.dimensions = {
            'MF0W8': {'Length': 'max. 3.5mm', 'Diameter': 'max. 1.85mm', 'Lead diameter': '0.45mm±0.05mm',
                      'Lead length': '28mm±3mm', 'Lead spacing': 'min. 5mm'},
            'MF0W4': {'Length': 'max. 6.8mm', 'Diameter': 'max. 2.5mm', 'Lead diameter': '0.54mm±0.05mm',
                      'Lead length': '28mm±3mm', 'Lead spacing': 'min. 9mm'},
            'MF0W2': {'Length': 'max. 10mm', 'Diameter': 'max. 3.5mm', 'Lead diameter': '0.54mm±0.05mm',
                      'Lead length': '28mm±3mm', 'Lead spacing': 'min. 12mm'},
            'MF01W': {'Length': 'max. 12mm', 'Diameter': 'max. 5mm', 'Lead diameter': '0.7mm±0.05mm',
                      'Lead length': '25mm±3mm', 'Lead spacing': 'min. 14mm'},
            'MF02W': {'Length': 'max. 16mm', 'Diameter': 'max. 5.5mm', 'Lead diameter': '0.7mm±0.05mm',
                      'Lead length': '28mm±3mm', 'Lead spacing': 'min. 18mm'},
            'MF03W': {'Length': 'max. 17.5mm', 'Diameter': 'max. 6.5mm', 'Lead diameter': '0.75mm±0.05mm',
                      'Lead length': '28mm±3mm', 'Lead spacing': 'min. 19.5mm'},
            'MF0S4': {'Length': 'max. 3.5mm', 'Diameter': 'max. 1.85mm', 'Lead diameter': '0.45mm±0.05mm',
                      'Lead length': '28mm±3mm', 'Lead spacing': 'min. 5mm'},
            'MFF04': {'Length': 'max. 3.7mm', 'Diameter': 'max. 1.9mm', 'Lead diameter': '0.45mm±0.05mm',
                      'Lead length': '28mm±3mm', 'Lead spacing': 'min. 5mm'},
            'MFFU2': {'Length': 'max. 6.8mm', 'Diameter': 'max. 2.5mm', 'Lead diameter': '0.54mm±0.05mm',
                      'Lead length': '28mm±3mm', 'Lead spacing': 'min. 9mm'},
            'MF0S2': {'Length': 'max. 9mm', 'Diameter': 'max. 3mm', 'Lead diameter': '0.54mm±0.05mm',
                      'Lead length': '28mm±3mm', 'Lead spacing': 'min. 11mm'},
            'MF006': {'Length': 'max. 6.8mm', 'Diameter': 'max. 2.5mm', 'Lead diameter': '0.54mm±0.05mm',
                      'Lead length': '28mm±3mm', 'Lead spacing': 'min. 9mm'},
            'MF0M7': {'Length': 'max. 10mm', 'Diameter': 'max. 3.5mm', 'Lead diameter': '0.54mm±0.05mm',
                      'Lead length': '28mm±3mm', 'Lead spacing': 'min. 12mm'},
            'MF01S': {'Length': 'max. 10mm', 'Diameter': 'max. 3.5mm', 'Lead diameter': '0.54mm±0.05mm',
                      'Lead length': '28mm±3mm', 'Lead spacing': 'min. 12mm'},
            'MF02S': {'Length': 'max. 12mm', 'Diameter': 'max. 5mm', 'Lead diameter': '0.7mm±0.05mm',
                      'Lead length': '28mm±3mm', 'Lead spacing': 'min. 14mm'},
            'MF03S': {'Length': 'max. 16mm', 'Diameter': 'max. 5.5mm', 'Lead diameter': '0.7mm±0.05mm',
                      'Lead length': '28mm±3mm', 'Lead spacing': 'min. 18mm'},
        }
        self.packaging_type = {'A': 'Tape / Box', 'T': 'Tape / Reel', 'B': 'Bulk / Box'}
        self.packaging_qty = {'1': '1000', '2': '2000', '4': '4000', '5': '5000', 'A': '500', 'B': '2500', '0': ''}

    def get_package_dimension(self, size_code, power_rating_code):
        return self.dimensions[size_code + power_rating_code]

    def get_max_working_voltage(self, size_code, power_rating_code):
        return self.max_operating_voltage[size_code + power_rating_code]

    def get_max_overload_voltage(self, size_code, power_rating_code):
        return self.max_overload_voltage[size_code + power_rating_code]

    def get_dielectric_withstanding_voltage(self, size_code, power_rating_code):
        return self.dielectric_withstanding_voltage[size_code + power_rating_code]

    def get_part_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type,
                        special_feature):
        if tolerance_code in self.short_value_code_tolerance_list:
            resistance_str = '0' + digits_multiplier_encoder(value, digits=2, multiplier_str=self.multiplier_str)
        else:
            resistance_str = digits_multiplier_encoder(value, multiplier_str=self.multiplier_str)
        partnumber = f"{size_code}{power_rating_code}{tolerance_code}{tcr_code}{resistance_str}##{special_feature}"
        assert len(partnumber) == 14
        return partnumber

    def get_order_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type,
                         special_feature):
        if tolerance_code in self.short_value_code_tolerance_list:
            resistance_str = '0' + digits_multiplier_encoder(value, digits=2, multiplier_str=self.multiplier_str)
        else:
            resistance_str = digits_multiplier_encoder(value, multiplier_str=self.multiplier_str)
        ordernumber = f"{size_code}{power_rating_code}{tolerance_code}{tcr_code}{resistance_str}{packing_type}{special_feature}"
        assert len(ordernumber) == 14
        return ordernumber

    def get_resistance_range(self, size, tolerance, tcr, power_rating_code, special_feature):
        if tolerance in ['F', 'G', 'J']:
            assert tolerance in ['F', 'G', 'J']
            series = e24 if tolerance in ['G', 'J', 'K'] else e24_e96
            part = size + power_rating_code
            if part in ['MF0W8', 'MF0S4', 'MFF04'] and special_feature == '0':
                if (tolerance == 'F' and tcr == 'F') or (tolerance == 'G' and tcr == 'G'):
                    return {'ranges': [[series, "[10, 1000000]"]]}
                elif tolerance == 'J' and tcr == 'J':
                    return {'ranges': [[series, "[1, 1000000]"]]}
            elif part in ['MF0W4', 'MF006', 'MFFU2'] and special_feature == '0':
                if (tolerance == 'F' and tcr == 'F') or (tolerance == 'G' and tcr == 'G'):
                    return {'ranges': [[series, "[10, 1000000]"]]}
                elif tolerance == 'J' and tcr == 'J':
                    return {'ranges': [[series, "[1, 1000000]"]]}
            elif part in ['MF0W2', 'MF0S2', 'MF0M7', 'MF01S'] and special_feature == '0':
                if (tolerance == 'F' and tcr == 'F') or (tolerance == 'G' and tcr == 'G'):
                    return {'ranges': [[series, "[10, 1000000]"]]}
                elif tolerance == 'J' and tcr == 'J':
                    return {'ranges': [[series, "[1, 1000000]"]]}
            elif part in ['MF02S', 'MF01W'] and special_feature == '0':
                if (tolerance == 'F' and tcr == 'F') or (tolerance == 'G' and tcr == 'G'):
                    return {'ranges': [[series, "[51.1, 1000000]"]]}
                elif tolerance == 'J' and tcr == 'J':
                    return {'ranges': [[series, "[10, 1000000]"]]}
            elif part in ['MF03S', 'MF02W', 'MF03W'] and special_feature == '9':
                if (tolerance == 'F' and tcr == 'F') or (tolerance == 'G' and tcr == 'G'):
                    return {'ranges': [[series, "[51.1, 1000000]"]]}
                elif tolerance == 'J' and tcr == 'J':
                    return {'ranges': [[series, "[10, 1000000]"]]}

    def packaging_data(self, size_code, power_rating_code, packaging_code):
        part = size_code + power_rating_code
        if part in ['MF0W8', 'MF0W4', 'MF0S4', 'MFF04', 'MFFU2', 'MF006'] and packaging_code in ['A5']:
            packaging = {'Packaging Code': packaging_code,
                         'Packaging Type': self.packaging_type[packaging_code[:1]],
                         'Packaging Qty': self.packaging_qty[packaging_code[-1:]],
                         'Packaging Data': None}
            return packaging
        elif part in ['MF0W2', 'MF01W', 'MF02W', 'MF0M7', 'MF01S', 'MF02S', 'MF03S'] and packaging_code in ['A1']:
            packaging = {'Packaging Code': packaging_code,
                         'Packaging Type': self.packaging_type[packaging_code[:1]],
                         'Packaging Qty': self.packaging_qty[packaging_code[-1:]],
                         'Packaging Data': None}
            return packaging
        elif part in ['MF0W4'] and packaging_code in ['B0']:
            packaging = {'Packaging Code': packaging_code,
                         'Packaging Type': self.packaging_type[packaging_code[:1]],
                         'Packaging Qty': '5000',
                         'Packaging Data': None}
            return packaging

    def get_files(self, partnumber, ordernumber):
        return {'File Datasheet': ''}
