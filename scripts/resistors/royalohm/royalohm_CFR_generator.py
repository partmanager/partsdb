from common.value_series import e24, e24_e96
from .royalohm_common import RoyalohmResistorBase


class RoyalohmCFRGenerator(RoyalohmResistorBase):
    def __init__(self):
        super().__init__("Royalohm",
                         "Resistor Carbon Film",
                         "CFR",
                         "Carbon Film Resistors",
                         operating_temp_range='-55°C ~ 155°C',
                         storage_temp_range='-55°C ~ 125°C',
                         size_code={'CFR0': 'CFR0'},
                         package={'CFR0': 'Resistor Axial'},
                         tolerance={'L': '±0.01%', 'W': '±0.05%', 'B': '±0.1%', 'C': '±0.25%', 'D': '±0.5%',
                                    'F': '±1%', 'G': '±2%', 'J': '±5%', 'K': '±10%'},
                         tcr={'100': '±100ppm/°C', '200': '±200ppm/°C', '350': '±350ppm/°C', '400': '±400ppm/°C',
                              '800': '±800ppm/°C',
                              '+0/-450': '+0 ~ -400ppm/°C', '+0/-700': '+0 ~ -700ppm/°C', '+0/-1500': '+0 ~ -1500ppm/°C'},
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
                                             '07': '0.75W',  # '3/4W',
                                             'U2': '0.5W',  # '1/2W',
                                             '2U': '2W',
                                             '3U': '3W'},
                         product_url='',
                         notes='')
        self.special_feature = ['0', '9']
        self.multiplier_str = {-3: 'L', -2: 'K', -1: 'J', 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6'}
        self.short_value_code_tolerance_list = ['G', 'J', 'K']
        self.max_operating_voltage = {'CFR0W8': '200V', 'CFR0W4': '250V', 'CFR0W2': '350', 'CFR01W': '500V',
                                      'CFR02W': '500V',
                                      'CFR0S4': '200V', 'CFRFU2': '250V', 'CFR0S2': '350V', 'CFRF1U': '350V',
                                      'CFR01S': '500V', 'CFR02U': '500V', 'CFR02S': '500V', 'CFR03U': '500V',
                                      'CFR03S': '500V'}
        self.max_overload_voltage = {'CFR0W8': '400V', 'CFR0W4': '500V', 'CFR0W2': '700', 'CFR01W': '1000V',
                                     'CFR02W': '1000V',
                                     'CFR0S4': '400V', 'CFRFU2': '500V', 'CFR0S2': '700V', 'CFRF1U': '700V',
                                     'CFR01S': '1000V', 'CFR02U': '1000V', 'CFR02S': '1000V', 'CFR03U': '1000V',
                                     'CFR03S': '1000V'}
        self.dielectric_withstanding_voltage = {'CFR0W8': '400V', 'CFR0W4': '500V', 'CFR0W2': '700', 'CFR01W': '1000V',
                                                'CFR02W': '1000V',
                                                'CFR0S4': '400V', 'CFRFU2': '500V', 'CFR0S2': '700V', 'CFRF1U': '700V',
                                                'CFR01S': '1000V', 'CFR02U': '1000V', 'CFR02S': '1000V',
                                                'CFR03U': '1000V', 'CFR03S': '1000V'}
        self.dimensions = {'CFR0W8': {'Length': 'max. 3.5mm', 'Diameter': 'max. 1.85mm', 'Lead diameter': '0.45mm±0.05mm',
                                      'Lead length': '28mm±3mm', 'Lead spacing': 'min. 5mm'},
                           'CFR0W4': {'Length': 'max. 6.8mm', 'Diameter': 'max. 2.5mm',
                                      'Lead diameter': '0.54mm±0.05mm', 'Lead length': '28mm±3mm',
                                      'Lead spacing': 'min. 9mm'},
                           'CFR0W2': {'Length': 'max. 10mm', 'Diameter': 'max. 3.5mm',
                                      'Lead diameter': '0.54mm±0.05mm', 'Lead length': '28mm±3mm',
                                      'Lead spacing': 'min. 12mm'},
                           'CFR01W': {'Length': 'max. 16mm', 'Diameter': 'max. 5.5mm', 'Lead diameter': '0.7mm±0.05mm',
                                      'Lead length': '28mm±3mm', 'Lead spacing': 'min. 18mm'},
                           'CFR02W': {'Length': 'max. 17.5mm', 'Diameter': 'max. 6.5mm', 'Lead diameter': '0.75mm±0.05mm',
                                      'Lead length': '28mm±3mm', 'Lead spacing': 'min. 19.5mm'},
                           'CFR0S4': {'Length': 'max. 3.5mm', 'Diameter': 'max. 1.85mm',
                                      'Lead diameter': '0.45mm±0.05mm',
                                      'Lead length': '28mm±3mm', 'Lead spacing': 'min. 5mm'},
                           'CFR0S2': {'Length': 'max. 9mm', 'Diameter': 'max. 3mm',
                                      'Lead diameter': '0.54mm±0.05mm',
                                      'Lead length': '28mm±3mm', 'Lead spacing': 'min. 11mm'},
                           'CFR01S': {'Length': 'max. 12mm', 'Diameter': 'max. 5mm',
                                      'Lead diameter': '0.7mm±0.05mm',
                                      'Lead length': '28mm±3mm', 'Lead spacing': 'min. 14mm'},
                           'CFR02U': {'Length': 'max. 12mm', 'Diameter': 'max. 5mm',
                                      'Lead diameter': '0.7mm±0.05mm',
                                      'Lead length': '28mm±3mm', 'Lead spacing': 'min. 14mm'},
                           'CFR02S': {'Length': 'max. 16mm', 'Diameter': 'max. 5.5mm',
                                      'Lead diameter': '0.7mm±0.05mm',
                                      'Lead length': '28mm±3mm', 'Lead spacing': 'min. 18mm'},
                           'CFR03S': {'Length': 'max. 17.5mm', 'Diameter': 'max. 6.5mm',
                                      'Lead diameter': '0.75mm±0.05mm',
                                      'Lead length': '28mm±3mm', 'Lead spacing': 'min. 20mm'},
                           'CFR03U': {'Length': 'max. 16mm', 'Diameter': 'max. 5.5mm',
                                      'Lead diameter': '0.70mm±0.05mm',
                                      'Lead length': '28mm±3mm', 'Lead spacing': 'min. 18mm'}
                           }
        self.packaging_type = {'A': 'Tape / Box', 'T': 'Tape / Reel', 'B': 'Bulk / Box'}
        self.packaging_qty = {'1': '1000', '2': '2000', '4': '4000', '5': '5000', 'A': '500', 'B': '2500', '0': ''}

    def get_package_dimension(self,  size_code, power_rating_code):
        return self.dimensions[size_code + power_rating_code]

    def get_max_working_voltage(self, size_code, power_rating_code):
        return self.max_operating_voltage[size_code + power_rating_code]

    def get_max_overload_voltage(self, size_code, power_rating_code):
        return self.max_overload_voltage[size_code + power_rating_code]

    def get_dielectric_withstanding_voltage(self, size_code, power_rating_code):
        return self.dielectric_withstanding_voltage[size_code + power_rating_code]

    def get_resistance_range(self, size, tolerance, tcr, power_rating_code, special_feature):
        if tolerance in ['F', 'G', 'J', 'K']:
            assert tolerance in ['F', 'G', 'J', 'K']
            series = e24 if tolerance in ['G', 'J', 'K'] else e24_e96
            part = size + power_rating_code
            if part in ['CFR0W8', 'CFR0S4'] and special_feature == '0':
                if tcr == '350':
                    return {'ranges': [[series, "[1, 10]"]]}
                elif tcr == '+0/-450':
                    return {'ranges': [[series, "[11, 99000]"]]}
                elif tcr == '+0/-700':
                    return {'ranges': [[series, "[100000, 1000000]"]]}
            elif part in ['CFR0W4', 'CFR0W2', 'CFR0S2', 'CFR01S', 'CFR02U'] and special_feature == '0':
                if tcr == '350':
                    return {'ranges': [[series, "[1, 10]"]]}
                elif tcr == '+0/-450':
                    return {'ranges': [[series, "[11, 99000]"]]}
                elif tcr == '+0/-700':
                    return {'ranges': [[series, "[100000, 1000000]"]]}
                elif tcr == '+0/-1500':
                    return {'ranges': [[series, "[1100000, 10000000]"]]}
            elif part in ['CFR01W', 'CFR02W', 'CFR02S', 'CFR03U', 'CFR03S'] and special_feature == '9':
                if tcr == '350':
                    return {'ranges': [[series, "[1, 10]"]]}
                elif tcr == '+0/-450':
                    return {'ranges': [[series, "[11, 99000]"]]}
                elif tcr == '+0/-700':
                    return {'ranges': [[series, "[100000, 1000000]"]]}
                elif tcr == '+0/-1500':
                    return {'ranges': [[series, "[1100000, 10000000]"]]}

    def packaging_data(self, size_code, power_rating_code, packaging_code):
        part = size_code + power_rating_code
        if part in ['CFR0W4', 'CFR0S4'] and packaging_code in ['A5']:
                packaging = {'Packaging Code': packaging_code,
                             'Packaging Type': self.packaging_type[packaging_code[:1]],
                             'Packaging Qty': self.packaging_qty[packaging_code[-1:]],
                             'Packaging Data': None}
                return packaging
        elif part in ['CFR0S2', 'CFR01S', 'CFR02U', 'CFR02S', 'CFR03U', 'CFR03S'] and packaging_code in ['A1']:
                packaging = {'Packaging Code': packaging_code,
                             'Packaging Type': self.packaging_type[packaging_code[:1]],
                             'Packaging Qty': self.packaging_qty[packaging_code[-1:]],
                             'Packaging Data': None}
                return packaging

    def get_files(self, partnumber, ordernumber):
        return {}

