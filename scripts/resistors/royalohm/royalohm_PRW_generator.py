from common.value_series import e24, e24_e96
from common.value_encoder import digits_multiplier_encoder
from .royalohm_common import RoyalohmResistorBase


class RoyalohmPRWGenerator(RoyalohmResistorBase):
    def __init__(self):
        super().__init__("Royalohm",
                         "Resistor",
                         "Generic Thick Film Chip Resistors",
                         "Thick Film Chip Resistors",
                         operating_temp_range='-55°C ~ 155°C',
                         storage_temp_range='-55°C ~ 125°C',
                         size_code={'PRW0': 'PRW0', 'PRWA': 'PRWA'},
                         package={'PRW0': 'Axial Cermet', 'PRWA': 'Axial Cermet'},
                         tolerance={'L': '±0.01%', 'W': '±0.05%', 'B': '±0.1%', 'C': '±0.25%', 'D': '±0.5%',
                                    'F': '±1%', 'G': '±2%', 'J': '±5%', 'K': '±10%'},
                         tcr={'100': '±100ppm/°C', '200': '±200ppm/°C', '350': '±350ppm/°C', '400': '±400ppm/°C',
                              '800': '±800ppm/°C'},
                         packaging=['T1', 'T2', 'T4', 'T5', 'TA', 'TC', 'TD', 'TE', 'B0'],
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
                                             '07': '0.75W',  # '3/4W',
                                             'U2': '0.5W'  # '1/2W'
                                             },
                         product_url='',
                         notes='')
        self.multiplier_str = {-3: 'L', -2: 'K', -1: 'J', 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6'}
        self.short_value_code_tolerance_list = ['J', 'K']
        self.special_feature = ['P0', 'W0']
        self.dimensions = {'PRW01W': {'Length': '14mm±1mm', 'Width': '6mm±1mm', 'Height': '6mm±1mm',
                                      'Lead diameter': '0.7mm±0.05mm', 'Lead length': '25mm±5mm',
                                      'Lead spacing': 'min. 16mm'},
                           'PRW02W': {'Length': '18mm±1mm', 'Width': '7mm±1mm', 'Height': '7mm±1mm',
                                      'Lead diameter': '0.75mm±0.05mm', 'Lead length': '28mm±5mm',
                                      'Lead spacing': 'min. 20mm'},
                           'PRW03W': {'Length': '22mm±1mm', 'Width': '8mm±1mm', 'Height': '8mm±1mm',
                                      'Lead diameter': '0.75mm±0.05mm', 'Lead length': '32mm±5mm',
                                      'Lead spacing': 'min. 24mm'},
                           'PRW05W': {'Length': '22mm±1mm', 'Width': '10mm±1mm', 'Height': '9mm±1mm',
                                      'Lead diameter': '0.75mm±0.05mm', 'Lead length': '35mm±5mm',
                                      'Lead spacing': 'min. 24mm'},
                           'PRW07W': {'Length': '35mm±1mm', 'Width': '10mm±1mm', 'Height': '9mm±1mm',
                                      'Lead diameter': '0.75mm±0.05mm', 'Lead length': '35mm±5mm',
                                      'Lead spacing': 'min. 37mm'},
                           'PRW0AW': {'Length': '49mm±1mm', 'Width': '10mm±1mm', 'Height': '9mm±1mm',
                                      'Lead diameter': '0.75mm±0.05mm', 'Lead length': '35mm±5mm',
                                      'Lead spacing': 'min. 51mm'},
                           'PRW0FW': {'Length': '49mm±1mm', 'Width': '12.5mm±1mm', 'Height': '11.5mm±1mm',
                                      'Lead diameter': '0.75mm±0.05mm', 'Lead length': '35mm±5mm',
                                      'Lead spacing': 'min. 51mm'},
                           'PRW020': {'Length': '60mm±1mm', 'Width': '14.5mm±1mm', 'Height': '13.5mm±1mm',
                                      'Lead diameter': '0.75mm±0.05mm', 'Lead length': '35mm±5mm',
                                      'Lead spacing': 'min. 62mm'},
                           'PRW025': {'Length': '64mm±1mm', 'Width': '14.5mm±1mm', 'Height': '13.5mm±1mm',
                                      'Lead diameter': '0.75mm±0.05mm', 'Lead length': '35mm±5mm',
                                      'Lead spacing': 'min. 66mm'},
                           }

    def get_package_dimension(self,  size_code, power_rating_code):
        return self.dimensions[size_code.replace('PRWA', 'PRW0') + power_rating_code]

    def get_max_working_voltage(self, size_code, power_rating_code):
        return '500V'

    def get_max_overload_voltage(self, size_code, power_rating_code):
        return '1000V'

    def get_dielectric_withstanding_voltage(self, size_code, power_rating_code):
        return ''

    def get_part_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type, special_feature):
        special_feature_convert = {'P0': 'P', 'W0': 'W'}
        resistance_str = special_feature_convert[special_feature] + digits_multiplier_encoder(value, digits=2, multiplier_str=self.multiplier_str)
        special_feature = '0'
        partnumber = f"{size_code}{power_rating_code}{tolerance_code}{resistance_str}##{special_feature}"
        assert len(partnumber) == 14
        return partnumber

    def get_order_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type, special_feature):
        special_feature_convert = {'P0': 'P', 'W0': 'W'}
        resistance_str = special_feature_convert[special_feature] + digits_multiplier_encoder(value, digits=2,
                                                                                              multiplier_str=self.multiplier_str)
        special_feature = '0'
        ordernumber = f"{size_code}{power_rating_code}{tolerance_code}{resistance_str}{packing_type}{special_feature}"
        assert len(ordernumber) == 14
        return ordernumber

    def get_resistance_range(self, size, tolerance, tcr, power_rating_code, special_feature):
        if size == 'PRW0' and tolerance in ['J', 'K']:
            return self.prw0_resistance_ranges(size, tolerance, tcr, power_rating_code, special_feature)
        elif size == 'PRWA' and tolerance in ['J', 'K']:
            return self.prwa_resistance_ranges(size, tolerance, tcr, power_rating_code, special_feature)

    def packaging_data(self, size_code, power_rating_code, code):
        if size_code in ['PRW0', 'PRWA'] and code == 'B0':
            packaging = {
                'Packaging Code': 'B0', 'Packaging Type': 'Bulk / Box', 'Packaging Qty': '', 'Packaging Data': None}
            return packaging

    def get_files(self, partnumber, ordernumber):
        return {'File Datasheet': 'www.royalohm.com/pdf/product2017/CementAxialPRW.pdf'}

    def prw0_resistance_ranges(self, size, tolerance, tcr, power_rating_code, special_feature):
        assert size == 'PRW0'
        assert tolerance in ['J', 'K']

        if power_rating_code == '1W':
            if special_feature == 'W0':
                if tcr == '400':
                    return {'ranges': [[e24, "[1, 20)"]]}
                elif tcr == '350':
                    return {'ranges': [[e24, "[20, 27]"]]}
            elif special_feature == 'P0' and tcr == '350':
                return {'ranges': [[e24, "[28, 33000]"]]}
        elif power_rating_code == '2W':
            if special_feature == 'W0':
                if tcr == '400':
                    return {'ranges': [[e24, "[0.1, 20)"]]}
                elif tcr == '350':
                    return {'ranges': [[e24, "[20, 27]"]]}
            elif special_feature == 'P0' and tcr == '350':
                return {'ranges': [[e24, "[28, 33000]"]]}
        elif power_rating_code == '3W':
            if special_feature == 'W0':
                if tcr == '400':
                    return {'ranges': [[e24, "[0.1, 20)"]]}
                elif tcr == '350':
                    return {'ranges': [[e24, "[20, 39]"]]}
            elif special_feature == 'P0' and tcr == '350':
                return {'ranges': [[e24, "[40, 56000]"]]}
        elif power_rating_code == '5W':
            if special_feature == 'W0':
                if tcr == '400':
                    return {'ranges': [[e24, "[0.1, 20)"]]}
                elif tcr == '350':
                    return {'ranges': [[e24, "[20, 47]"]]}
            elif special_feature == 'P0' and tcr == '350':
                return {'ranges': [[e24, "[48, 100000]"]]}
        elif power_rating_code == '7W':
            if special_feature == 'W0':
                if tcr == '400':
                    return {'ranges': [[e24, "[0.1, 20)"]]}
                elif tcr == '350':
                    return {'ranges': [[e24, "[20, 680]"]]}
            elif special_feature == 'P0' and tcr == '350':
                return {'ranges': [[e24, "[681, 200000]"]]}
        elif power_rating_code == 'AW':
            if special_feature == 'W0':
                if tcr == '400':
                    return {'ranges': [[e24, "[0.1, 20)"]]}
                elif tcr == '350':
                    return {'ranges': [[e24, "[20, 910]"]]}
            elif special_feature == 'P0' and tcr == '350':
                return {'ranges': [[e24, "[911, 200000]"]]}
        elif power_rating_code == 'FW' and special_feature == 'W0':
                if tcr == '400':
                    return {'ranges': [[e24, "[1, 20)"]]}
                elif tcr == '350':
                    return {'ranges': [[e24, "[20, 1000]"]]}
        elif power_rating_code == '20' and special_feature == 'W0':
            if tcr == '400':
                return {'ranges': [[e24, "[2, 20)"]]}
            elif tcr == '350':
                return {'ranges': [[e24, "[20, 1200]"]]}
        elif power_rating_code == '25' and special_feature == 'W0':
            if tcr == '400':
                return {'ranges': [[e24, "[2, 20)"]]}
            elif tcr == '350':
                return {'ranges': [[e24, "[20, 1200]"]]}

    def prwa_resistance_ranges(self, size, tolerance, tcr, power_rating_code, special_feature):
        assert size == 'PRWA'
        assert tolerance in ['J', 'K']

        if power_rating_code == '2W':
            if special_feature == 'W0':
                if tcr == '400':
                    return {'ranges': [[e24, "[0.1, 20)"]]}
                elif tcr == '350':
                    return {'ranges': [[e24, "[20, 27]"]]}
            elif special_feature == 'P0' and tcr == '350':
                return {'ranges': [[e24, "[28, 33000]"]]}
        elif power_rating_code == '3W':
            if special_feature == 'W0':
                if tcr == '400':
                    return {'ranges': [[e24, "[0.1, 20)"]]}
                elif tcr == '350':
                    return {'ranges': [[e24, "[20, 39]"]]}
            elif special_feature == 'P0' and tcr == '350':
                return {'ranges': [[e24, "[40, 56000]"]]}
        elif power_rating_code == '5W':
            if special_feature == 'W0':
                if tcr == '400':
                    return {'ranges': [[e24, "[0.1, 20)"]]}
                elif tcr == '350':
                    return {'ranges': [[e24, "[20, 47]"]]}
            elif special_feature == 'P0' and tcr == '350':
                return {'ranges': [[e24, "[48, 100000]"]]}
        elif power_rating_code == '7W':
            if special_feature == 'W0':
                if tcr == '400':
                    return {'ranges': [[e24, "[0.1, 20)"]]}
                elif tcr == '350':
                    return {'ranges': [[e24, "[20, 680]"]]}
            elif special_feature == 'P0' and tcr == '350':
                return {'ranges': [[e24, "[681, 200000]"]]}
        elif power_rating_code == 'AW':
            if special_feature == 'W0':
                if tcr == '400':
                    return {'ranges': [[e24, "[0.1, 20)"]]}
                elif tcr == '350':
                    return {'ranges': [[e24, "[20, 910]"]]}
            elif special_feature == 'P0' and tcr == '350':
                return {'ranges': [[e24, "[911, 200000]"]]}

