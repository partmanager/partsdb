from common.value_series import e24, e24_e96
from .yageo_common import YageoResistorBase


class YageoACResistorGenerator(YageoResistorBase):
    def __init__(self):
        super().__init__(part_type="Resistor Thick Film",
                         series="AC",
                         series_description="HICK FILM CHIP RESISTORS AUTOMOTIVE GRADe",
                         operating_temp_range='-55°C ~ 155°C',
                         storage_temp_range='5°C ~ 35°C',
                         size_code={'AC0201': '0201', 'AC0402': '0402', 'AC0603': '0603', 'AC0805': '0805',
                                    'AC1206': '1206', 'AC1210': '1210', 'AC1218': '1218', 'AC2010': '2010',
                                    'AC2512': '2512'},
                         package={'AC0201': '0201', 'AC0402': '0402', 'AC0603': '0603', 'AC0805': '0805',
                                  'AC1206': '1206', 'AC1210': '1210', 'AC1218': '1218', 'AC2010': '2010',
                                  'AC2512': '2512'},
                         packaging=['R_07', 'R_10', 'R_13', 'R_7W', 'R_3W', 'E_07', 'E_10', 'E_13', 'E_7W', 'E_3W'],
                         power_rating_codes={'1/20W': '0.05W', '1/16W': '0.0625W', '1/8W': '0.125W', '1/10W': '0.1W',#52350
                                             '1/5W': '0.2W', '1/4W': '0.25W', '1/2W': '0.5W', '1W': '1W', '1.5W': '1.5W',
                                             '3/4W': '0.75W', '1.25W': '1.25W', '2W': '2W',
                                             '1/20D': '0.05W', '1/16D': '0.0625W', '1/8D': '0.125W', '1/10D': '0.1W',
                                             '1/5D': '0.2W', '1/4D': '0.25W', '1/2D': '0.5W', '1D': '1W', '1.5D': '1.5W',
                                             '3/4D': '0.75W', '1.25D': '1.25W', '2D': '2W'},  # D indicates dual power
                         product_url='',
                         notes="Generated based on data from datasheet: Mar. 19,2021 V.8")
        self.max_working_voltage = None
        self.max_overload_voltage = {'AC0201': '50V', 'AC0402': '100V', 'AC0603': '150V', 'AC0805': '300V',
                                     'AC1206': '400V', 'AC1210': '500V', 'AC1218': '500V', 'AC2010': '500V',
                                     'AC2512': '500V'}
        self.dimensions = {'0201': {'Length': '0.60mm ±0.03', 'Width': '0.30mm ±0.03', 'Height': '0.23mm ±0.03',
                                    't1': '0.12mm ±0.05', 't2': '0.15±0.05mm'},
                           '0402': {'Length': '1.00mm ±0.10', 'Width': '0.50mm ±0.05', 'Height': '0.32mm ±0.05',
                                    't1': '0.20mm ±0.10', 't2': '0.25±0.10mm'},
                           '0603': {'Length': '1.60mm ±0.10', 'Width': '0.80mm ±0.10', 'Height': '0.45mm ±0.10',
                                    't1': '0.25mm ±0.15', 't2': '0.25mm±0.15'},
                           '0805': {'Length': '2.00mm ±0.10', 'Width': '1.25mm ±0.10', 'Height': '0.50mm ±0.10',
                                    't1': '0.35mm ±0.20', 't2': '0.35mm±0.20'},
                           '1206': {'Length': '3.10mm ±0.10', 'Width': '1.60mm ±0.10', 'Height': '0.55mm ±0.10',
                                    't1': '0.45mm ±0.20', 't2': '0.40mm±0.20'},
                           '1210': {'Length': '3.10mm ±0.10', 'Width': '2.60mm ±0.15', 'Height': '0.55mm ±0.10',
                                    't1': '0.45mm ±0.15', 't2': '0.50mm ±0.20'},
                           '1218': {'Length': '3.10mm ±0.10', 'Width': '4.60mm ±0.10', 'Height': '0.55mm ±0.10',
                                    't1': '0.45mm ±0.20', 't2': '0.40mm±0.20'},
                           '2010': {'Length': '5.00mm ±0.10', 'Width': '2.50mm ±0.15', 'Height': '0.55mm ±0.10',
                                    't1': '0.55mm ±0.15', 't2': '0.50mm ±0.20'},
                           '2512': {'Length': '6.35mm ±0.10', 'Width': '3.20mm ±0.15', 'Height': '0.55mm ±0.10',
                                    't1': '0.60mm ±0.20', 't2': '0.50mm ±0.20'}}
        self.dielectric_withstanding_voltage = {'AC0201': '50V', 'AC0402': '100V', 'AC0603': '150V', 'AC0805': '300V',
                                                'AC1206': '500V', 'AC1210': '500V', 'AC1218': '500V', 'AC2010': '500V',
                                                'AC2512': '500V'}

    def get_package_dimension(self, size_code, power_rating_code):
        size = self.size_code[size_code]
        return self.dimensions[size]

    def get_max_working_voltage(self, size_code, power_rating_code):
        standard_power = {'AC0201': '25V', 'AC0402': '50V', 'AC0603': '75V', 'AC0805': '150V',
                          'AC1206': '200V', 'AC1210': '200V', 'AC1218': '200V', 'AC2010': '200V', 'AC2512': '200V'}
        dual_power = {'AC0201': None, 'AC0402': '75V', 'AC0603': '75V', 'AC0805': '150V',
                      'AC1206': '200V', 'AC1210': '200V', 'AC1218': '200V', 'AC2010': '200V', 'AC2512': '200V'}
        if power_rating_code in self.dual_power_taping_reel_codes:
            return dual_power[size_code]
        else:
            return standard_power[size_code]

    def get_dielectric_withstanding_voltage(self, size_code, power_rating_code):
        return self.dielectric_withstanding_voltage[size_code]

    def __tcr_range_standard(self, tolerance_code, tcr_code):
        if tolerance_code == 'J':  # 5%
            if tcr_code == '200':
                return {'ranges': [[e24, '[1, 10]']]}
            elif tcr_code == '100':
                return {'ranges': [[e24, '(10, 10000000]']]}
            elif tcr_code == '200':
                return {'ranges': [[e24, '(10000000, 22000000]']]}
        elif tolerance_code in ['F', 'D']:  # 1%, 0.5%
            if tcr_code == '200':
                return {'ranges': [[e24_e96, '[1, 10]']]}
            elif tcr_code == '100':
                return {'ranges': [[e24_e96, '(10, 10000000]']]}

    def __tcr_range_dual(self, tolerance_code, tcr_code):
        if tolerance_code == 'J':  # 5%
            if tcr_code == '200':
                return {'ranges': [[e24, '[1, 10]']]}
            elif tcr_code == '100':
                return {'ranges': [[e24, '(10, 10000000]']]}
        elif tolerance_code in ['F', 'D']:  # 1%, 0.5%
            if tcr_code == '200':
                return {'ranges': [[e24_e96, '[1, 10]']]}
            elif tcr_code == '100':
                return {'ranges': [[e24_e96, '(10, 10000000]']]}

    def get_resistance_range(self, size_code, tolerance_code, tcr_code, power_rating_code, special_feature):
        if size_code == 'AC0201' and power_rating_code == '1/20W':
            if tolerance_code == 'J':  # 5%
                if tcr_code == '-100+350':
                    return {'ranges': [[e24, '[1, 10]']]}
                elif tcr_code == '200':
                    return {'ranges': [[e24, '(10, 10000000]']]}
            elif tolerance_code == 'F':  # 1%
                if tcr_code == '-100+350':
                    return {'ranges': [[e24_e96, '[1, 10]']]}
                elif tcr_code == '200':
                    return {'ranges': [[e24_e96, '(10, 10000000]']]}
            elif tolerance_code == 'D':  # 0.5%
                if tcr_code == '-100+350':
                    return {'ranges': [[e24_e96, '[10, 10]']]}
                elif tcr_code == '200':
                    return {'ranges': [[e24_e96, '(10, 10000000]']]}
        elif size_code == 'AC0402':
            if power_rating_code == '1/16W':
                return self.__tcr_range_standard(tolerance_code, tcr_code)
            elif power_rating_code == '1/8D':
                return self.__tcr_range_dual(tolerance_code, tcr_code)
        elif size_code == 'AC0603':
            if power_rating_code == '1/10W':
                return self.__tcr_range_standard(tolerance_code, tcr_code)
            elif power_rating_code == '1/5D':
                return self.__tcr_range_dual(tolerance_code, tcr_code)
        elif size_code == 'AC0805':
            if power_rating_code == '1/8W':
                return self.__tcr_range_standard(tolerance_code, tcr_code)
            elif power_rating_code == '1/4D':
                return self.__tcr_range_dual(tolerance_code, tcr_code)
        elif size_code == 'AC1206':
            if power_rating_code == '1/4W':
                return self.__tcr_range_standard(tolerance_code, tcr_code)
            elif power_rating_code == '1/2D':
                return self.__tcr_range_dual(tolerance_code, tcr_code)
        elif size_code == 'AC1210':
            if power_rating_code == '1/2W':
                return self.__tcr_range_standard(tolerance_code, tcr_code)
            elif power_rating_code == '1D':
                return self.__tcr_range_dual(tolerance_code, tcr_code)
        elif size_code == 'AC1218':
            if power_rating_code in ['1W', '1.5D']:
                if tolerance_code == 'J':  # 5%
                    if tcr_code == '200':
                        return {'ranges': [[e24, '[1, 10]']]}
                    elif tcr_code == '100':
                        return {'ranges': [[e24, '(10, 1000000]']]}
                elif tolerance_code in ['F', 'D']:  # 1%, 0.5%
                    if tcr_code == '200':
                        return {'ranges': [[e24_e96, '[1, 10]']]}
                    elif tcr_code == '100':
                        return {'ranges': [[e24_e96, '(10, 1000000]']]}
        elif size_code == 'AC2010':
            if power_rating_code == '3/4W':
                return self.__tcr_range_standard(tolerance_code, tcr_code)
            elif power_rating_code == '1.25D':
                return self.__tcr_range_dual(tolerance_code, tcr_code)
        elif size_code == 'AC2512':
            if power_rating_code == '1W':
                return self.__tcr_range_standard(tolerance_code, tcr_code)
            elif power_rating_code == '2D':
                return self.__tcr_range_dual(tolerance_code, tcr_code)

    def packaging_data(self, size_code, power_rating_code, packaging_code):
        packaging_type, taping_reel = packaging_code.split('_')
        return self.get_packaging_detail(size_code, packaging_type, taping_reel)

    def get_files(self, partnumber, ordernumber):
        return {
            'datasheet': 'https://www.yageo.com/upload/media/product/productsearch/datasheet/rchip/PYu-AC_51_RoHS_L_8.pdf'}
