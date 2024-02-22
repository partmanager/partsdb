from common.value_series import e24, e24_e96
from .viking_common import VikingResistorBase


class VikingARGenerator(VikingResistorBase):
    def __init__(self):
        super().__init__(part_type="Resistor Thin Film",
                         series="AR",
                         series_description="Thin Film Precision Chip Resistor",
                         product_url='https://www.viking.com.tw/en/category/Precision-Chip-Resistor-AR-Series/Resistor-ARBTC.html',
                         notes='Part generated based on data from AR Series datasheet: Edition: REV. F1, Revision 08-12-2020')
        self.max_operating_voltage_standard = {'AR01': '15V', 'AR02': '50V', 'AR03': '50V', 'AR05': '100V',
                                               'AR06': '150V', 'AR13': '150V', 'AR10': '150V', 'AR12': '150V'}
        self.max_overload_voltage_standard = {'AR01': '30V', 'AR02': '100V', 'AR03': '100V', 'AR05': '200V',
                                              'AR06': '300V', 'AR13': '300V', 'AR10': '300V', 'AR12': '300V'}
        self.max_operating_voltage_high_power = {'AR01': {'N': '25V'},
                                                 'AR02': {'X': '50V'},
                                                 'AR03': {'X': '75V', 'M': '100V'},
                                                 'AR05': {'W': '150V', 'V': '150V'},
                                                 'AR06': {'V': '200V', 'O': '200V'},
                                                 'AR13': {'O': '200V'},
                                                 'AR10': {'O': '200V', 'U': '200V'},
                                                 'AR12': {'Q': '200V', 'T': '200V'}}
        self.max_overload_voltage_high_power = {'AR01': {'N': '50V'},
                                                'AR02': {'X': '100V'},
                                                'AR03': {'X': '150V', 'M': '150V'},
                                                'AR05': {'W': '300V', 'V': '300V'},
                                                'AR06': {'V': '400V', 'O': '400V'},
                                                'AR13': {'O': '400V'},
                                                'AR10': {'O': '400V', 'U': '400V'},
                                                'AR12': {'Q': '400V', 'T': '400V'}}

    def get_max_working_voltage(self, size_code, power_rating_code):
        if power_rating_code in self.high_power_rating_code:
            return self.max_operating_voltage_high_power[size_code][power_rating_code]
        else:
            return self.max_operating_voltage_standard[size_code]

    def get_max_overload_voltage(self, size_code, power_rating_code):
        if power_rating_code in self.high_power_rating_code:
            return self.max_overload_voltage_high_power[size_code][power_rating_code]
        else:
            return self.max_overload_voltage_standard[size_code]

    def get_resistance_range(self, size_code, tolerance_code, tcr_code, power_rating_code, special_feature):
        if power_rating_code in self.high_power_rating_code:
            return self.get_high_power_resistance_range(size_code, tolerance_code, tcr_code, power_rating_code)
        else:
            if tcr_code in ['C', 'D']:
                if tolerance_code != 'T':
                    return self.get_standard_resistance_range(size_code, tolerance_code, tcr_code, power_rating_code)
            else:
                return self.get_special_resistance_range(size_code, tolerance_code, tcr_code, power_rating_code)

    def packaging_data(self, size_code, power_rating_code, packing_type_code):
        if size_code in ['AR01', 'AR02', 'AR03', 'AR05', 'AR06', 'AR13', 'AR10', 'AR12'] and packing_type_code == 'T':
            packaging = self.packing_type_and_qty[size_code]
            packaging.update(self.packaging_tape_size[size_code])
            return packaging

    def get_files(self, partnumber, ordernumber):
        return {'File Datasheet': 'https://www.viking.com.tw/Templates/att/AR_REV_F1-201208.pdf?lng=en'}

    def get_marking_code(self, size_code):
        #if size_code in ['AR01', 'AR02']:
        #    return 'N'
        #else:
        return ''

    def get_standard_resistance_range(self, size_code, tolerance_code, tcr_code, power_rating_code):
        assert tolerance_code in ['A', 'B', 'C', 'D', 'F'], tolerance_code
        assert tcr_code in ['C', 'D']

        if size_code == 'AR01' and power_rating_code == '1/32':
            if tolerance_code in ['B', 'C', 'D', 'F']:
                return {'ranges': [[e24_e96, "[22, 75000]"]]}
        elif size_code == 'AR02' and power_rating_code == '1/16':
            if tolerance_code == 'A':
                return {'ranges': [[e24_e96, "[49.9, 12000]"]]}
            else:
                return {'ranges': [[e24_e96, "[4, 511000]"]]}
        elif size_code == 'AR03' and power_rating_code == '1/16':
            if tolerance_code == 'A':
                return {'ranges': [[e24_e96, "[4.7, 332000]"]]}
            else:
                return {'ranges': [[e24_e96, "[1, 1000000]"]]}
        elif size_code == 'AR05' and power_rating_code == '1/10':
            if tolerance_code == 'A':
                return {'ranges': [[e24_e96, "[4.7, 1000000]"]]}
            else:
                return {'ranges': [[e24_e96, "[1, 2000000]"]]}
        elif size_code == 'AR06' and power_rating_code == '1/8':
            if tolerance_code == 'A':
                return {'ranges': [[e24_e96, "[4.7, 1000000]"]]}
            else:
                return {'ranges': [[e24_e96, "[1, 2500000]"]]}
        elif size_code == 'AR13' and power_rating_code == '1/4':
            if tolerance_code == 'A':
                return {'ranges': [[e24_e96, "[4.7, 1000000]"]]}
            else:
                return {'ranges': [[e24_e96, "[1, 2500000]"]]}
        elif size_code == 'AR10' and power_rating_code == '1/4':
            if tolerance_code == 'A':
                return {'ranges': [[e24_e96, "[4.7, 1000000]"]]}
            else:
                return {'ranges': [[e24_e96, "[1, 3000000]"]]}
        elif size_code == 'AR12' and power_rating_code == '1/2':
            if tolerance_code == 'A':
                return {'ranges': [[e24_e96, "[4.7, 1000000]"]]}
            else:
                return {'ranges': [[e24_e96, "[1, 3000000]"]]}

    def get_special_resistance_range(self, size_code, tolerance_code, tcr_code, power_rating_code):
        assert tolerance_code in ['T', 'A', 'B', 'C', 'D', 'F']
        assert tcr_code in ['5', 'X', 'O', 'S', 'B', 'N']

        if size_code == 'AR02' and power_rating_code == '1/16':
            if tcr_code in ['5', 'X', 'O'] and tolerance_code in ['T', 'A', 'B']:
                return {'ranges': [[e24, "[49.9, 4990]"]]}
            elif tcr_code == 'S':
                return {'ranges': [[e24, "[49.9, 20000]"]]}
            elif tcr_code in ['B', 'N']:
                if tolerance_code in ['T', 'A']:
                    return {'ranges': [[e24, "[49.9, 20000]"]]}
                else:
                    return {'ranges': [[e24, "[49.9, 100000]"]]}
        elif size_code == 'AR03' and power_rating_code == '1/16':
            if tcr_code in ['5', 'X', 'O'] and tolerance_code in ['T', 'A', 'B']:
                return {'ranges': [[e24, "[24.9, 15000]"]]}
            elif tcr_code == 'S':
                return {'ranges': [[e24, "[24.9, 60000]"]]}
            elif tcr_code in ['B', 'N']:
                if tolerance_code == 'T':
                    return {'ranges': [[e24, "[24.9, 100000]"]]}
                elif tolerance_code == 'A':
                    return {'ranges': [[e24, "[4.7, 332000]"]]}
                else:
                    return {'ranges': [[e24, "[4.7, 511000]"]]}
        elif size_code == 'AR05' and power_rating_code == '1/10':
            if tcr_code in ['5', 'X', 'O'] and tolerance_code in ['T', 'A', 'B']:
                return {'ranges': [[e24, "[24.9, 30000]"]]}
            elif tcr_code == 'S':
                return {'ranges': [[e24, "[24.9, 150000]"]]}
            elif tcr_code in ['B', 'N']:
                if tolerance_code == 'T':
                    return {'ranges': [[e24, "[24.9, 200000]"]]}
                else:
                    return {'ranges': [[e24, "[4.7, 1000000]"]]}
        elif size_code == 'AR06' and power_rating_code == '1/8':
            if tcr_code in ['5', 'X', 'O'] and tolerance_code in ['T', 'A', 'B']:
                return {'ranges': [[e24, "[24.9, 49900]"]]}
            elif tcr_code == 'S':
                return {'ranges': [[e24, "[24.9, 300000]"]]}
            elif tcr_code in ['B', 'N']:
                if tolerance_code == 'T':
                    return {'ranges': [[e24, "[24.9, 499000]"]]}
                else:
                    return {'ranges': [[e24, "[4.7, 1500000]"]]}
        elif size_code == 'AR13' and power_rating_code == '1/4':
            if tcr_code in ['5', 'X', 'O'] and tolerance_code in ['T', 'A', 'B']:
                return {'ranges': [[e24, "[24.9, 49900]"]]}
            elif tcr_code == 'S':
                return {'ranges': [[e24, "[24.9, 300000]"]]}
            elif tcr_code in ['B', 'N']:
                if tolerance_code == 'T':
                    return {'ranges': [[e24, "[24.9, 499000]"]]}
                else:
                    return {'ranges': [[e24, "[4.7, 1000000]"]]}
        elif size_code == 'AR10' and power_rating_code == '1/4':
            if tcr_code in ['5', 'X', 'O'] and tolerance_code in ['T', 'A', 'B']:
                return {'ranges': [[e24, "[24.9, 100000]"]]}
            elif tcr_code == 'S':
                return {'ranges': [[e24, "[24.9, 300000]"]]}
            elif tcr_code in ['B', 'N']:
                if tolerance_code == 'T':
                    return {'ranges': [[e24, "[24.9, 499000]"]]}
                else:
                    return {'ranges': [[e24, "[4.7, 1000000]"]]}
        elif size_code == 'AR12' and power_rating_code == '1/2':
            if tcr_code in ['5', 'X', 'O'] and tolerance_code in ['T', 'A', 'B']:
                return {'ranges': [[e24, "[24.9, 100000]"]]}
            elif tcr_code == 'S':
                return {'ranges': [[e24, "[24.9, 300000]"]]}
            elif tcr_code in ['B', 'N']:
                if tolerance_code == 'T':
                    return {'ranges': [[e24, "[24.9, 499000]"]]}
                else:
                    return {'ranges': [[e24, "[4.7, 1000000]"]]}

    def get_high_power_resistance_range(self, size_code, tolerance_code, tcr_code, power_rating_code):
        assert tolerance_code in ['T', 'A', 'B', 'C', 'D', 'F']
        assert tcr_code in ['5', 'X', 'O', 'S', 'B', 'N', 'C', 'D'], tcr_code

        if size_code == 'AR01' and power_rating_code == 'N':
            if tcr_code in ['C', 'D'] and tolerance_code in ['B', 'C', 'D', 'F']:
                return {'ranges': [[e24, "[22, 75000]"]]}
        elif size_code == 'AR02' and power_rating_code == 'X':
            if tcr_code in ['5', 'X', 'O'] and tolerance_code in ['T', 'A', 'B']:
                return {'ranges': [[e24, "[49.9, 4990]"]]}
            elif tcr_code == 'S':
                return {'ranges': [[e24, "[49.9, 20000]"]]}
            elif tcr_code in ['B', 'N']:
                if tolerance_code in ['T', 'A']:
                    return {'ranges': [[e24, "[49.9, 12000]"]]}
                else:
                    return {'ranges': [[e24, "[49.9, 100000]"]]}
            elif tcr_code in ['C', 'D']:
                if tolerance_code == 'T':
                    return None
                elif tolerance_code == 'A':
                    return {'ranges': [[e24, "[49.9, 12000]"]]}
                else:
                    return {'ranges': [[e24, "[4.7, 255000]"]]}
        elif size_code == 'AR03' and power_rating_code == 'X':
            if tcr_code in ['5', 'X', 'O'] and tolerance_code in ['T', 'A', 'B']:
                return {'ranges': [[e24, "[24.9, 15000]"]]}
            elif tcr_code == 'S':
                return {'ranges': [[e24, "[24.9, 60000]"]]}
            elif tcr_code in ['B', 'N']:
                if tolerance_code == 'T':
                    return {'ranges': [[e24, "[24.9, 100000]"]]}
                elif tolerance_code == 'A':
                    return {'ranges': [[e24, "[4.7, 332000]"]]}
                else:
                    return {'ranges': [[e24, "[4.7, 511000]"]]}
            elif tcr_code in ['C', 'D']:
                if tolerance_code == 'T':
                    return {'ranges': [[e24, "[24.9, 100000]"]]}
                elif tolerance_code == 'A':
                    return {'ranges': [[e24, "[4.7, 332000]"]]}
                else:
                    return {'ranges': [[e24, "[1, 1000000]"]]}
        elif size_code == 'AR03' and power_rating_code == 'M':
            if tcr_code in ['C', 'D'] and tolerance_code in ['A', 'B', 'C', 'D', 'F']:
                return {'ranges': [[e24, "[10, 332000]"]]}
        elif size_code == 'AR05' and power_rating_code == 'W':
            if tcr_code in ['5', 'X', 'O'] and tolerance_code in ['T', 'A', 'B']:
                return {'ranges': [[e24, "[24.9, 30000]"]]}
            elif tcr_code == 'S':
                return {'ranges': [[e24, "[24.9, 150000]"]]}
            elif tcr_code in ['B', 'N']:
                if tolerance_code == 'T':
                    return {'ranges': [[e24, "[24.9, 200000]"]]}
                elif tolerance_code == 'A':
                    return {'ranges': [[e24, "[4.7, 511000]"]]}
                else:
                    return {'ranges': [[e24, "[4.7, 1000000]"]]}
            elif tcr_code in ['C', 'D']:
                if tolerance_code == 'T':
                    return {'ranges': [[e24, "[24.9, 200000]"]]}
                elif tolerance_code == 'A':
                    return {'ranges': [[e24, "[4.7, 511000]"]]}
                else:
                    return {'ranges': [[e24, "[1, 1000000]"]]}
        elif size_code == 'AR05' and power_rating_code == 'V':
            if tcr_code in ['C', 'D'] and tolerance_code in ['A', 'B', 'C', 'D', 'F']:
                return {'ranges': [[e24, "[10, 499000]"]]}
        elif size_code == 'AR06' and power_rating_code == 'V':
            if tcr_code in ['5', 'X', 'O'] and tolerance_code in ['T', 'A', 'B']:
                return {'ranges': [[e24, "[24.9, 49900]"]]}
            elif tcr_code == 'S':
                return {'ranges': [[e24, "[24.9, 300000]"]]}
            elif tcr_code in ['B', 'N']:
                if tolerance_code == 'T':
                    return {'ranges': [[e24, "[24.9, 499000]"]]}
                else:
                    return {'ranges': [[e24, "[4.7, 1000000]"]]}
            elif tcr_code in ['C', 'D']:
                if tolerance_code == 'T':
                    return {'ranges': [[e24, "[24.9, 499000]"]]}
                else:
                    return {'ranges': [[e24, "[1, 1000000]"]]}
        elif size_code == 'AR06' and power_rating_code == 'O':
            if tcr_code in ['C', 'D'] and tolerance_code in ['A', 'B', 'C', 'D', 'F']:
                return {'ranges': [[e24, "[10, 1000000]"]]}
        elif size_code == 'AR13' and power_rating_code == 'O':
            if tcr_code in ['5', 'X', 'O'] and tolerance_code in ['T', 'A', 'B']:
                return {'ranges': [[e24, "[24.9, 49900]"]]}
            elif tcr_code == 'S':
                return {'ranges': [[e24, "[24.9, 300000]"]]}
            elif tcr_code in ['B', 'N']:
                if tolerance_code == 'T':
                    return {'ranges': [[e24, "[24.9, 499000]"]]}
                else:
                    return {'ranges': [[e24, "[4.7, 1000000]"]]}
            elif tcr_code in ['C', 'D']:
                if tolerance_code == 'T':
                    return {'ranges': [[e24, "[24.9, 499000]"]]}
                else:
                    return {'ranges': [[e24, "[1, 1000000]"]]}
        elif size_code == 'AR10' and power_rating_code == 'O':
            if tcr_code in ['5', 'X', 'O'] and tolerance_code in ['T', 'A', 'B']:
                return {'ranges': [[e24, "[24.9, 49900]"]]}
            elif tcr_code == 'S':
                return {'ranges': [[e24, "[24.9, 300000]"]]}
            elif tcr_code in ['B', 'N']:
                if tolerance_code == 'T':
                    return {'ranges': [[e24, "[24.9, 499000]"]]}
                else:
                    return {'ranges': [[e24, "[4.7, 1000000]"]]}
            elif tcr_code in ['C', 'D']:
                if tolerance_code == 'T':
                    return {'ranges': [[e24, "[24.9, 499000]"]]}
                else:
                    return {'ranges': [[e24, "[1, 1000000]"]]}
        elif size_code == 'AR10' and power_rating_code == 'U':
            if tcr_code in ['B', 'N', 'C', 'D']:
                if tolerance_code == 'T':
                    return {'ranges': [[e24, "[24.9, 2000]"]]}
                elif tolerance_code in ['A', 'B']:
                    return {'ranges': [[e24, "[4.7, 1000000]"]]}
                else:
                    return {'ranges': [[e24, "[1, 1000000]"]]}
        elif size_code == 'AR12' and power_rating_code == 'Q':
            if tcr_code in ['B', 'N', 'C', 'D']:
                if tolerance_code == 'T':
                    return {'ranges': [[e24, "[24.9, 2000]"]]}
                elif tolerance_code in ['A', 'B']:
                    return {'ranges': [[e24, "[4.7, 2000]"]]}
                else:
                    return {'ranges': [[e24, "[1, 2000]"]]}
        elif size_code == 'AR12' and power_rating_code == 'T':
            if tcr_code in ['B', 'N', 'C', 'D']:
                if tolerance_code == 'T':
                    return {'ranges': [[e24, "[24.9, 2000]"]]}
                elif tolerance_code in ['A', 'B']:
                    return {'ranges': [[e24, "[4.7, 1000000]"]]}
                else:
                    return {'ranges': [[e24, "[1, 1000000]"]]}
