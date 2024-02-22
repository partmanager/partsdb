from .royalohm_common import RoyalohmResistorBase
from decimal import Decimal
from common.value_series import e24, e24_e96
from common.value_encoder import digits_multiplier_encoder


class RoyalohmKNPGenerator(RoyalohmResistorBase):
    def __init__(self):
        super().__init__("Royalohm",
                         "Resistor Thick Film",
                         "KNP",
                         "Wire-Wound Fixed Resistors",
                         operating_temp_range='-55°C ~ 155°C',
                         storage_temp_range='-55°C ~ 125°C',
                         size_code={'KNP0W2': 'KNP0W2', 'KNP01W': 'KNP01W', 'KNP02W': 'KNP02W', 'KNP03W': 'KNP03W',
                                    'KNP05W': 'KNP05W', 'KNP07W': 'KNP07W', 'KNP08W': 'KNP08W',
                                    'KNP01S': 'KNP01S', 'KNP02S': 'KNP02S', 'KNP03S': 'KNP03S', 'KNP05S': 'KNP05S',
                                    'KNP07S': 'KNP07S', 'KNP08S': 'KNP08S', 'KNP09S': 'KNP09S', 'KNP0AS': 'KNP0AS',
                                    'KNP01U': 'KNP01U', 'KNP02U': 'KNP02U', 'KNP03U': 'KNP03U', 'KNP04U': 'KNP04U',
                                    'KNP0AU': 'KNP0AU',
                                    'KNPA1W': 'KNPA1W', 'KNPA2W': 'KNPA3W', 'KNPA3W': 'KNPA3W', 'KNPA5W': 'KNPA5W'},
                         package={'KNP0W2': 'Axial', 'KNP01W': 'Axial', 'KNP02W': 'Axial', 'KNP03W': 'Axial',
                                  'KNP05W': 'Axial', 'KNP07W': 'Axial', 'KNP08W': 'Axial',
                                  'KNP01S': 'Axial', 'KNP02S': 'Axial', 'KNP03S': 'Axial', 'KNP05S': 'Axial',
                                  'KNP07S': 'Axial', 'KNP08S': 'Axial', 'KNP09S': 'Axial', 'KNP0AS': 'Axial',
                                  'KNP01U': 'Axial', 'KNP02U': 'Axial', 'KNP03U': 'Axial', 'KNP04U': 'Axial',
                                  'KNP0AU': 'Axial',
                                  'KNPA1W': 'Axial', 'KNPA2W': 'Axial', 'KNPA3W': 'Axial', 'KNPA5W': 'Axial'},
                         tolerance={'L': '±0.01%', 'W': '±0.05%', 'B': '±0.1%', 'C': '±0.25%', 'D': '±0.5%',
                                    'F': '±1%', 'G': '±2%', 'J': '±5%', 'K': '±10%'},
                         tcr={'100': '±100ppm/°C', '200': '±200ppm/°C', '300': '±300ppm/°C', '400': '±400ppm/°C',
                              '800': '±800ppm/°C'},
                         packaging=['A10', 'AA9', 'A19', 'B00'],
                         power_rating_codes={'WH': '0.03125W',  # '1/32W',
                                             'WM': '0.05W',  # '1/20W',
                                             'WG': '0.0625W',  # '1/16W',
                                             'WA': '0.1W',  # '1/10W',
                                             'W8': '0.125W',  # '1/8W',
                                             'W5': '0.2W',  # '1/5W',
                                             'W4': '0.25W',  # '1/4W',
                                             'W3': '0.333333333W',  # '1/3W',
                                             'W2': '0.5W',  # '1/2W',
                                             '34': '0.75W',  # '3/4W',
                                             '1W': '1W',
                                             '2W': '2W',
                                             '3W': '3W',
                                             '4W': '4W',
                                             '5W': '5W',
                                             '6W': '6W',
                                             'SA': '0.1W',  # '1/10W',
                                             'S8': '0.125W',  # '1/8W',
                                             'S4': '0.25W',  # '1/4W',
                                             'S3': '0.333333333W',  # '1/3W',
                                             '07': '0.75W',  # '3/4W',
                                             '1S': '1W',
                                             '2S': '2W',
                                             '3S': '3W',
                                             '5S': '5W',
                                             '7S': '7W',
                                             '8S': '8W',
                                             '9S': '9W',
                                             'AS': '10W',
                                             'U2': '0.5W',  # '1/2W',
                                             '1U': '1W',
                                             '2U': '2W',
                                             '3U': '3W',
                                             '4U': '4W',
                                             'AU': '10W'},
                         product_url='',
                         notes='')

        self.max_overload_voltage = {'KNP0W2': '1000V', 'KNP01W': '1000V', 'KNP02W': '1000V',
                                     'KNP03W': '1000V', 'KNP05W': '1000V', 'KNP07W': '1000V',
                                     'KNP08W': '1000V', 'KNP09W': '1000V',
                                     'KNP01S': '1000V', 'KNP02S': '1000V',
                                     'KNP03S': '1000V', 'KNP05S': '1000V', 'KNP07S': '1000V',
                                     'KNP08S': '1000V', 'KNP09S': '1000V', 'KNP0AS': '1000V',
                                     'KNP01U': '1000V', 'KNP02U': '1000V', 'KNP03U': '1000V',
                                     'KNP04U': '1000V', 'KNP0AU': '1000V',
                                     'KNPA1W': '1000V', 'KNPA2W': '1000V', 'KNPA3W': '1000V', 'KNPA5W': '1000V'}

        self.dimensions = {'KNP0W2': {'Length': '10mm±1mm', 'Diameter': '3.5mm±1mm', 'Lead diameter': '0.54mm±0.05mm',
                                      'Lead length': '28mm±3mm', 'Lead spacing': 'min. 12mm'},
                           'KNP01W': {'Length': '12mm±1mm', 'Diameter': '5.0mm±1mm', 'Lead diameter': '0.70mm±0.05mm',
                                      'Lead length': '25mm±3mm', 'Lead spacing': 'min. 14mm'},
                           'KNP02W': {'Length': '16mm±1mm', 'Diameter': '5.5mm±1mm', 'Lead diameter': '0.70mm±0.05mm',
                                      'Lead length': '28mm±3mm', 'Lead spacing': 'min. 18mm'},
                           'KNP03W': {'Length': '17.5mm±1mm', 'Diameter': '6.5mm±1mm', 'Lead diameter': '0.75mm±0.05mm',
                                      'Lead length': '28mm±3mm', 'Lead spacing': 'min. 20mm'},
                           'KNP05W': {'Length': '25mm±1mm', 'Diameter': '8.5mm±1mm', 'Lead diameter': '0.75mm±0.05mm',
                                      'Lead length': '38mm±3mm', 'Lead spacing': 'min. 27mm'},
                           'KNP07W': {'Length': '30mm±1mm', 'Diameter': '8.5mm±1mm', 'Lead diameter': '0.75mm±0.05mm',
                                      'Lead length': '38mm±3mm', 'Lead spacing': 'min. 32mm'},
                           'KNP08W': {'Length': '40mm±1mm', 'Diameter': '8.5mm±1mm', 'Lead diameter': '0.75mm±0.05mm',
                                      'Lead length': '38mm±3mm', 'Lead spacing': 'min. 42mm'},
                           'KNP09W': {'Length': '53mm±1mm', 'Diameter': '8.5mm±1mm', 'Lead diameter': '0.75mm±0.05mm',
                                      'Lead length': '38mm±3mm', 'Lead spacing': 'min. 55mm'},

                           'KNP01S': {'Length': '10mm±1mm', 'Diameter': '3.5mm±1mm', 'Lead diameter': '0.54mm±0.05mm',
                                      'Lead length': '28mm±3mm', 'Lead spacing': 'min. 12mm'},
                           'KNP02S': {'Length': '12mm±1mm', 'Diameter': '5.0mm±1mm', 'Lead diameter': '0.70mm±0.05mm',
                                      'Lead length': '25mm±3mm', 'Lead spacing': 'min. 14mm'},
                           'KNP03S': {'Length': '16mm±1mm', 'Diameter': '5.5mm±1mm', 'Lead diameter': '0.70mm±0.05mm',
                                      'Lead length': '28mm±3mm', 'Lead spacing': 'min. 18mm'},
                           'KNP05S': {'Length': '17.5mm±1mm', 'Diameter': '6.5mm±1mm', 'Lead diameter': '0.75mm±0.05mm',
                                      'Lead length': '28mm±3mm', 'Lead spacing': 'min. 20mm'},
                           'KNP07S': {'Length': '25mm±1mm', 'Diameter': '8.5mm±1mm', 'Lead diameter': '0.75mm±0.05mm',
                                      'Lead length': '38mm±3mm', 'Lead spacing': 'min. 27mm'},
                           'KNP08S': {'Length': '30mm±1mm', 'Diameter': '8.5mm±1mm', 'Lead diameter': '0.75mm±0.05mm',
                                      'Lead length': '38mm±3mm', 'Lead spacing': 'min. 32mm'},
                           'KNP09S': {'Length': '40mm±1mm', 'Diameter': '8.5mm±1mm', 'Lead diameter': '0.75mm±0.05mm',
                                      'Lead length': '38mm±3mm', 'Lead spacing': 'min. 42mm'},
                           'KNP0AS': {'Length': '53mm±1mm', 'Diameter': '8.5mm±1mm', 'Lead diameter': '0.75mm±0.05mm',
                                      'Lead length': '38mm±3mm', 'Lead spacing': 'min. 55mm'},

                           'KNP01U': {'Length': '9mm±1mm', 'Diameter': '3mm±1mm', 'Lead diameter': '0.54mm±0.05mm',
                                      'Lead length': '28mm±3mm', 'Lead spacing': 'min. 11mm'},
                           'KNP02U': {'Length': '10mm±1mm', 'Diameter': '3.5mm±1mm', 'Lead diameter': '0.54mm±0.05mm',
                                      'Lead length': '28mm±3mm', 'Lead spacing': 'min. 12mm'},
                           'KNP03U': {'Length': '13.5mm±1mm', 'Diameter': '5.5mm±1mm', 'Lead diameter': '0.70mm±0.05mm',
                                      'Lead length': '28mm±3mm', 'Lead spacing': 'min. 15.5mm'},
                           'KNP04U': {'Length': '16mm±1mm', 'Diameter': '5.5mm±1mm', 'Lead diameter': '0.70mm±0.05mm',
                                      'Lead length': '28mm±3mm', 'Lead spacing': 'min. 18mm'},
                           'KNP0AU': {'Length': '40mm±1mm', 'Diameter': '8.5mm±1mm', 'Lead diameter': '0.75mm±0.05mm',
                                      'Lead length': '38mm±3mm', 'Lead spacing': 'min. 42mm'},
                           }
        self.multiplier_str = {-3: 'L', -2: 'K', -1: 'J', 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6'}
        self.short_value_code_tolerance_list = ['G', 'J', 'K']

    def get_package_dimension(self, size_code, power_rating_code):
        size_code = size_code.replace('KNPA', 'KNP0')
        size = self.size_code[size_code]
        return self.dimensions[size]

    def get_max_working_voltage(self, size_code, power_rating_code):
        return '500V'

    def get_dielectric_withstanding_voltage(self, size_code, power_rating_code):
        return '350V' if size_code in ['KNP0W2', 'KNP01S'] else '500V'

    def get_part_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type, special_feature):
        special_feature = '#'
        if tolerance_code in self.short_value_code_tolerance_list:
            resistance_str = '0' + digits_multiplier_encoder(value, digits=2, multiplier_str=self.multiplier_str)
        else:
            resistance_str = digits_multiplier_encoder(value, multiplier_str=self.multiplier_str)
        partnumber = f"{size_code}{tolerance_code}{resistance_str}##{special_feature}"
        assert len(partnumber) == 14, partnumber
        return partnumber

    def get_order_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type, special_feature):
        special_feature = ''
        if tolerance_code in self.short_value_code_tolerance_list:
            resistance_str = '0' + digits_multiplier_encoder(value, digits=2, multiplier_str=self.multiplier_str)
        else:
            resistance_str = digits_multiplier_encoder(value, multiplier_str=self.multiplier_str)
        ordernumber = f"{size_code}{tolerance_code}{resistance_str}{packing_type}{special_feature}"
        assert len(ordernumber) == 14
        return ordernumber

    def get_resistance_range(self, size_code, tolerance_code, tcr_code, power_rating_code, special_feature):
        if tolerance_code in ['F', 'G', 'J', 'K']:
            series = e24_e96 if tolerance_code == 'F' else e24
            if size_code == 'KNP0W2' and power_rating_code == 'W2':
                if tcr_code == '400':
                    return {'ranges': [[series, "[0.06, 9.9]"], [series, "[10, 20)"]]}
                elif tcr_code == '300':
                    return {'ranges': [[series, "[20, 39]"], [series, "[40, 560]"]]}
            elif size_code in ['KNP01W', 'KNPA1W'] and power_rating_code == '1W':
                if tcr_code == '400':
                    return {'ranges': [[series, "[0.1, 9.9]"], [series, "[10, 20)"]]}
                elif tcr_code == '300':
                    return {'ranges': [[series, "[20, 50]"], [series, "[51, 1000]"]]}
            elif size_code in ['KNP02W', 'KNPA2W'] and power_rating_code == '2W':
                if tcr_code == '400':
                    return {'ranges': [[series, "[0.15, 9.9]"], [series, "[10, 20)"]]}
                elif tcr_code == '300':
                    return {'ranges': [[series, "[20, 120]"], [series, "[121, 2000]"]]}
            elif size_code in ['KNP03W', 'KNPA3W'] and power_rating_code == '3W':
                if tcr_code == '400':
                    return {'ranges': [[series, "[0.25, 9.9]"], [series, "[10, 20)"]]}
                elif tcr_code == '300':
                    return {'ranges': [[series, "[20, 200]"], [series, "[201, 3000]"]]}
            elif size_code in ['KNP05W', 'KNPA5W'] and power_rating_code == '5W':
                if tcr_code == '400':
                    return {'ranges': [[series, "[0.5, 9.9]"], [series, "[10, 20)"]]}
                elif tcr_code == '300':
                    return {'ranges': [[series, "[20, 470]"], [series, "[471, 5000]"]]}
            elif size_code == 'KNP07W' and power_rating_code == '7W':
                if tcr_code == '400':
                    return {'ranges': [[series, "[0.65, 9.9]"], [series, "[10, 20)"]]}
                elif tcr_code == '300':
                    return {'ranges': [[series, "[20, 470]"], [series, "[471, 6000]"]]}
            elif size_code == 'KNP08W' and power_rating_code == '8W':
                if tcr_code == '400':
                    return {'ranges': [[series, "[1, 9.9]"], [series, "[10, 20)"]]}
                elif tcr_code == '300':
                    return {'ranges': [[series, "[20, 1500]"], [series, "[1600, 10000]"]]}
            elif size_code == 'KNP09W' and power_rating_code == '9W':
                if tcr_code == '400':
                    return {'ranges': [[series, "[1, 9.9]"], [series, "[10, 20)"]]}
                elif tcr_code == '300':
                    return {'ranges': [[series, "[20, 1500]"], [series, "[1600, 15000]"]]}

            elif size_code == 'KNP01S' and power_rating_code == '1S':
                if tcr_code == '400':
                    return {'ranges': [[series, "[0.06, 9.9]"], [series, "[10, 20)"]]}
                elif tcr_code == '300':
                    return {'ranges': [[series, "[20, 39]"], [series, "[40, 560]"]]}
            elif size_code == 'KNP02S' and power_rating_code == '2S':
                if tcr_code == '400':
                    return {'ranges': [[series, "[0.1, 9.9]"], [series, "[10, 20)"]]}
                elif tcr_code == '300':
                    return {'ranges': [[series, "[20, 50]"], [series, "[51, 1000]"]]}
            elif size_code == 'KNP03S' and power_rating_code == '3S':
                if tcr_code == '400':
                    if tolerance_code == 'J':
                        return {'ranges': [[series, "[0.15, 9.9]"], [series, "[10, 20)"]],
                                'extra_values': [Decimal('0.1'), Decimal('0.11'), Decimal('0.12'), Decimal('0.13')]}
                    else:
                        return {'ranges': [[series, "[0.15, 9.9]"], [series, "[10, 20)"]]}
                elif tcr_code == '300':
                    return {'ranges': [[series, "[20, 120]"], [series, "[121, 2000]"]]}
            elif size_code == 'KNP05S' and power_rating_code == '5S':
                if tcr_code == '400':
                    if tolerance_code == 'J':
                        return {'ranges': [[series, "[0.1, 9.9]"], [series,
                                                                    "[10, 20)"]]}  # this values can be found in distributors but they they deffinition can't be found in datasheet
                    else:
                        return {'ranges': [[series, "[0.25, 9.9]"], [series, "[10, 20)"]]}
                elif tcr_code == '300':
                    return {'ranges': [[series, "[20, 200]"], [series, "[201, 3000)"]]}
            elif size_code == 'KNP07S' and power_rating_code == '7S':
                if tcr_code == '400':
                    return {'ranges': [[series, "[0.5, 9.9]"], [series, "[10, 20)"]]}
                elif tcr_code == '300':
                    return {'ranges': [[series, "[20, 470]"], [series, "[471, 5000]"]]}
            elif size_code == 'KNP08S' and power_rating_code == '8S':
                if tcr_code == '400':
                    return {'ranges': [[series, "[0.65, 9.9]"], [series, "[10, 20)"]]}
                elif tcr_code == '300':
                    return {'ranges': [[series, "[20, 470]"], [series, "[471, 6000]"]]}
            elif size_code == 'KNP09S' and power_rating_code == '9S':
                if tcr_code == '400':
                    return {'ranges': [[series, "[1, 9.9]"], [series, "[10, 20)"]]}
                elif tcr_code == '300':
                    return {'ranges': [[series, "[20, 1500]"], [series, "[1600, 10000]"]]}
            elif size_code == 'KNP0AS' and power_rating_code == 'AS':
                if tcr_code == '400':
                    return {'ranges': [[series, "[1, 9.9]"], [series, "[10, 20)"]]}
                elif tcr_code == '300':
                    return {'ranges': [[series, "[20, 1500]"], [series, "[1600, 15000]"]]}

            elif size_code == 'KNP01U' and power_rating_code == '1U':
                if tcr_code == '400':
                    return {'ranges': [[series, "[0.1, 9.9]"], [series, "[10, 20)"]]}
                elif tcr_code == '300':
                    if tolerance_code == 'J':
                        return {'ranges': [[series, "[20, 39]"], [series, "[40, 180]"]],
                                'extra_values': [Decimal('200')]}
                    else:
                        return {'ranges': [[series, "[20, 39]"], [series, "[40, 180]"]]}
            elif size_code == 'KNP02U' and power_rating_code == '2U':
                if tcr_code == '400':
                    return {'ranges': [[series, "[0.1, 9.9]"], [series, "[10, 20)"]]}
                elif tcr_code == '300':
                    return {'ranges': [[series, "[20, 39]"], [series, "[40, 220]"]]}
            elif size_code == 'KNP03U' and power_rating_code == '3U':
                if tcr_code == '400':
                    return {'ranges': [[series, "[0.2, 9.9]"], [series, "[10, 20)"]]}
                elif tcr_code == '300':
                    return {'ranges': [[series, "[20, 50]"], [series, "[51, 620]"]]}
            elif size_code == 'KNP04U' and power_rating_code == '4U':
                if tcr_code == '400':
                    return {'ranges': [[series, "[0.2, 9.9]"], [series, "[10, 20)"]]}
                elif tcr_code == '300':
                    return {'ranges': [[series, "[20, 120]"], [series, "[121, 750]"]]}
            elif size_code == 'KNP0AU' and power_rating_code == 'AU':
                if tcr_code == '400':
                    return {'ranges': [[series, "[1, 9.9]"], [series, "[10, 20)"]]}
                elif tcr_code == '300':
                    return {'ranges': [[series, "[20, 1500]"], [series, "[1600, 5000]"]]}

    def packaging_data(self, size_code, power_rating_code, code):
        if size_code in ['KNP0W2', 'KNP01W', 'KNP01S', 'KNP02S', 'KNP01U', 'KNP02U', 'KNPA1W'] and code == 'A10':
            packaging = {
                'Packaging Code': code, 'Packaging Type': 'Paper Tape / Box', 'Packaging Qty': 1000,
                'Packaging Data': {}}
            return packaging
        elif size_code in ['KNP02W', 'KNP03W', 'KNP03S', 'KNP04S', 'KNP05S', 'KNP03U', 'KNP04U', 'KNPA2W',
                           'KNPA3W'] and code == 'AA9':
            packaging = {
                'Packaging Code': code, 'Packaging Type': 'Paper Tape / Box', 'Packaging Qty': 500,
                'Packaging Data': {}}
            return packaging
        elif size_code in ['KNP02W', 'KNP03S', 'KNPA2W'] and code == 'A19':
            packaging = {
                'Packaging Code': code, 'Packaging Type': 'Paper Tape / Box', 'Packaging Qty': 1000,
                'Packaging Data': {}}
            return packaging
        elif size_code in ['KNP05W', 'KNP07W', 'KNP08W', 'KNP09W', 'KNP07S', 'KNP08S', 'KNP09S', 'KNP0AS', 'KNP0AU',
                           'KNPA5W'] and code == 'B00':
            packaging = {
                'Packaging Code': code, 'Packaging Type': 'Bulk / Box', 'Packaging Qty': '',
                'Packaging Data': {}}
            return packaging

    def get_files(self, partnumber, ordernumber):
        return {}
