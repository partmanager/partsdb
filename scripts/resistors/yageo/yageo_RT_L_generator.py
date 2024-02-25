from .yageo_common import *
from common.value_series import e24, e24_e96


class YageoRTLResistorGenerator(YageoResistorBase):
    def __init__(self):
        super().__init__(part_type="Resistor Thin Film",
                         series="RT_L",
                         series_description="Thin Film Chip Resistors, High precision - high stability",
                         operating_temp_range='-55°C ~ 155°C',
                         storage_temp_range='5°C ~ 35°C',
                         size_code={'RT0201': '0201', 'RT0402': '0402', 'RT0603': '0603', 'RT0805': '0805',
                                    'RT1206': '1206', 'RT1210': '1210', 'RT2010': '2010', 'RT2512': '2512'},
                         package={'RT0201': 'Chip 0201', 'RT0402': 'Chip 0402', 'RT0603': 'Chip 0603',
                                  'RT0805': 'Chip 0805', 'RT1206': 'Chip 1206', 'RT1210': 'Chip 1210',
                                  'RT2010': 'Chip 2010', 'RT2512': 'Chip 2512'},
                         packaging=['R_07', 'R_10', 'R_13', 'R_7W', 'R_3W', 'K_07', 'K_10', 'K_13', 'K_7W', 'K_3W',
                                    'S_7N'],
                         power_rating_codes={'1/20W': '50mW', '1/16W': '62.5mW', '1/8W': '125mW', '1/10W': '0.1W',
                                             '1/5W': '0.2W', '1/4W': '0.25W', '1/2W': '0.5W', '1W': '1W', '1.5W': '1.5W',
                                             '3/4W': '0.75W', '1.25W': '1.25W', '2W': '2W',
                                             '1/20D': '50mW', '1/16D': '62.5mW', '1/8D': '125mW', '1/10D': '0.1W',
                                             '1/5D': '0.2W', '1/4D': '0.25W', '1/2D': '0.5W', '1D': '1W', '1.5D': '1.5W',
                                             '3/4D': '0.75W', '1.25D': '1.25W', '2D': '2W'},  # D indicates dual power
                         product_url='',
                         notes="Generated based on data from datasheet: Revision: 201304")
        self.max_working_voltage = {'RT0201': '25V', 'RT0402': '50V', 'RT0603': '75V', 'RT0805': '150V',
                                    'RT1206': '200V', 'RT1210': '200V', 'RT2010': '200V', 'RT2512': '200V'}
        self.max_overload_voltage = {'RT0201': '50V', 'RT0402': '100V', 'RT0603': '150V', 'RT0805': '300V',
                                     'RT1206': '400V', 'RT1210': '400V', 'RT2010': '400V', 'RT2512': '400V'}
        self.dielectric_withstanding_voltage = {'RT0201': '50V', 'RT0402': '75V', 'RT0603': '100V', 'RT0805': '200V',
                                                'RT1206': '300V', 'RT1210': '400V', 'RT2010': '400V', 'RT2512': '400V'}
        self.max_temperature = {'RT0201': '125', 'RT0402': '155', 'RT0603': '155', 'RT0805': '155', 'RT1206': '155',
                                'RT1210': '125', 'RT2010': '125', 'RT2512': '125'}
        self.dimensions = {
            '0201': {'Length': '0.60mm ±0.03', 'Width': '0.30mm ±0.03', 'Height': '0.23mm ±0.03', 'l1': '0.10mm ±0.05',
                     'l2': '0.15±0.05mm'},
            '0402': {'Length': '1.00mm ±0.10', 'Width': '0.50mm ±0.05', 'Height': '0.30mm ±0.05', 'l1': '0.20mm ±0.10',
                     'l2': '0.25±0.10mm'},
            '0603': {'Length': '1.60mm ±0.10', 'Width': '0.80mm ±0.10', 'Height': '0.45mm ±0.10', 'l1': '0.25mm ±0.15',
                     'l2': '0.25mm±0.15'},
            '0805': {'Length': '2.00mm ±0.10', 'Width': '1.25mm ±0.10', 'Height': '0.50mm ±0.10', 'l1': '0.35mm ±0.20',
                     'l2': '0.35mm±0.20'},
            '1206': {'Length': '3.10mm ±0.10', 'Width': '1.60mm ±0.10', 'Height': '0.55mm ±0.10', 'l1': '0.45mm ±0.20',
                     'l2': '0.40mm±0.20'},
            '1210': {'Length': '3.10mm ±0.10', 'Width': '2.60mm ±0.15', 'Height': '0.55mm ±0.10', 'l1': '0.50mm ±0.20',
                     'l2': '0.50mm ±0.20'},
            '2010': {'Length': '5.00mm ±0.10', 'Width': '2.50mm ±0.15', 'Height': '0.55mm ±0.10', 'l1': '0.60mm ±0.20',
                     'l2': '0.50mm ±0.20'},
            '2512': {'Length': '6.35mm ±0.10', 'Width': '3.20mm ±0.15', 'Height': '0.55mm ±0.10', 'l1': '0.60mm ±0.20',
                     'l2': '0.50mm ±0.20'}}

    def get_part_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type, special_feature):
        if 'D' not in power_rating_code or ('D' in power_rating_code and packing_type in self.dual_power_taping_reel_codes):
            packing_type, taping_reel = packing_type.split('_')
            packing_type = '#'
            resistance_str = resistance_to_str(value)
            return f"{size_code}{tolerance_code}{packing_type}{tcr_code}{taping_reel}{resistance_str}{self.default_code}"

    def get_order_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type, special_feature):
        packing_type, taping_reel = packing_type.split('_')
        resistance_str = resistance_to_str(value)
        return f"{size_code}{tolerance_code}{packing_type}{tcr_code}{taping_reel}{resistance_str}{self.default_code}"

    def get_operating_temperature_range(self, size_code, power_rating_code, partnumber):
        return '-55°C ~ {}°C'.format(self.max_temperature[size_code])

    def get_resistance_range(self, size_code, tolerance_code, tcr_code, power_rating_code, special_feature):
        if tolerance_code in ['L', 'P', 'W', 'B', 'C', 'D', 'F']:
            if size_code == 'RT0201' and power_rating_code == '1/20W':
                if tcr_code == 'A':  # 5 ppm
                    return None
                elif tcr_code in ['B', 'C']:  # 10, 15 ppm
                    resistance_range = {'L': None, 'P': None, 'W': None,
                                        'B': {'ranges': [[e24_e96, '[22, 5000]']]},
                                        'C': {'ranges': [[e24_e96, '[22, 5000]']]}, 'D': None, 'F': None}
                    return resistance_range[tolerance_code]
                elif tcr_code in ['D', 'E']:  # 25, 50 ppm
                    resistance_range = {'L': None, 'P': None, 'W': None,
                                        'B': {'ranges': [[e24_e96, '[22, 75000]']]},
                                        'C': {'ranges': [[e24_e96, '[22, 75000]']]},
                                        'D': {'ranges': [[e24_e96, '[22, 75000]']]},
                                        'F': {'ranges': [[e24_e96, '[22, 75000]']]}}
                    return resistance_range[tolerance_code]
            if size_code == 'RT0402' and power_rating_code == '1/16W':
                if tcr_code == 'A':
                    resistance_range = {'L': {'ranges': [[e24_e96, '[20, 10000]']]},
                                        'P': {'ranges': [[e24_e96, '[20, 10000]']]},
                                        'W': {'ranges': [[e24_e96, '[20, 10000]']]},
                                        'B': {'ranges': [[e24_e96, '[20, 10000]']]},
                                        'C': {'ranges': [[e24_e96, '[20, 10000]']]}, 'D': None, 'F': None}
                    return resistance_range[tolerance_code]
                elif tcr_code in ['B', 'C']:  # 10, 15 ppm
                    resistance_range = {'L': {'ranges': [[e24_e96, '[20, 12000]']]},
                                        'P': {'ranges': [[e24_e96, '[20, 12000]']]},
                                        'W': {'ranges': [[e24_e96, '[20, 12000]']]},
                                        'B': {'ranges': [[e24_e96, '[20, 200000]']]},
                                        'C': {'ranges': [[e24_e96, '[20, 200000]']]}, 'D': None, 'F': None}
                    return resistance_range[tolerance_code]
                elif tcr_code in ['D', 'E']:  # 25, 50 ppm
                    resistance_range = {'L': {'ranges': [[e24_e96, '[50.1, 12000]']]},
                                        'P': {'ranges': [[e24_e96, '[50.1, 12000]']]},
                                        'W': {'ranges': [[e24_e96, '[20, 12000]']]},
                                        'B': {'ranges': [[e24_e96, '[4.7, 240000]']]},
                                        'C': {'ranges': [[e24_e96, '[4.7, 240000]']]},
                                        'D': {'ranges': [[e24_e96, '[4.7, 240000]']]},
                                        'F': {'ranges': [[e24_e96, '[4.7, 240000]']]}}
                    return resistance_range[tolerance_code]
            if size_code == 'RT0603' and power_rating_code == '1/10W':
                if tcr_code == 'A':
                    resistance_range = {'L': {'ranges': [[e24_e96, '[20, 30000]']]},
                                        'P': {'ranges': [[e24_e96, '[20, 30000]']]},
                                        'W': {'ranges': [[e24_e96, '[20, 30000]']]},
                                        'B': {'ranges': [[e24_e96, '[20, 30000]']]},
                                        'C': {'ranges': [[e24_e96, '[20, 30000]']]}, 'D': None, 'F': None}
                    return resistance_range[tolerance_code]
                elif tcr_code in ['B', 'C']:
                    resistance_range = {'L': {'ranges': [[e24_e96, '[50.1, 100000]']]},
                                        'P': {'ranges': [[e24_e96, '[50.1, 100000]']]},
                                        'W': {'ranges': [[e24_e96, '[4.7, 100000]']]},
                                        'B': {'ranges': [[e24_e96, '[4.7, 680000]']]},
                                        'C': {'ranges': [[e24_e96, '[4.7, 680000]']]}, 'D': None, 'F': None}
                    return resistance_range[tolerance_code]
                elif tcr_code in ['D', 'E']:  # 25, 50 ppm
                    resistance_range = {'L': {'ranges': [[e24_e96, '[50.1, 30000]']]},
                                        'P': {'ranges': [[e24_e96, '[50.1, 30000]']]},
                                        'W': {'ranges': [[e24_e96, '[4.7, 100000]']]},
                                        'B': {'ranges': [[e24_e96, '[1, 1000000]']]},
                                        'C': {'ranges': [[e24_e96, '[1, 1000000]']]},
                                        'D': {'ranges': [[e24_e96, '[1, 1000000]']]},
                                        'F': {'ranges': [[e24_e96, '[1, 1000000]']]}}
                    return resistance_range[tolerance_code]
            if size_code == 'RT0805' and power_rating_code == '1/8W':
                if tcr_code == 'A':
                    resistance_range = {'L': {'ranges': [[e24_e96, '[20, 50000]']]},
                                        'P': {'ranges': [[e24_e96, '[20, 50000]']]},
                                        'W': {'ranges': [[e24_e96, '[20, 50000]']]},
                                        'B': {'ranges': [[e24_e96, '[20, 50000]']]},
                                        'C': {'ranges': [[e24_e96, '[20, 50000]']]}, 'D': None, 'F': None}
                    return resistance_range[tolerance_code]
                elif tcr_code in ['B', 'C']:
                    resistance_range = {'L': {'ranges': [[e24_e96, '[50.1, 200000]']]},
                                        'P': {'ranges': [[e24_e96, '[50.1, 200000]']]},
                                        'W': {'ranges': [[e24_e96, '[4.7, 200000]']]},
                                        'B': {'ranges': [[e24_e96, '[4.7, 1000000]']]},
                                        'C': {'ranges': [[e24_e96, '[4.7, 1000000]']]}, 'D': None, 'F': None}
                    return resistance_range[tolerance_code]
                elif tcr_code in ['D', 'E']:  # 25, 50 ppm
                    resistance_range = {'L': {'ranges': [[e24_e96, '[50.1, 30000]']]},
                                        'P': {'ranges': [[e24_e96, '[50.1, 30000]']]},
                                        'W': {'ranges': [[e24_e96, '[4.7, 200000]']]},
                                        'B': {'ranges': [[e24_e96, '[1, 1500000]']]},
                                        'C': {'ranges': [[e24_e96, '[1, 1500000]']]},
                                        'D': {'ranges': [[e24_e96, '[1, 1500000]']]},
                                        'F': {'ranges': [[e24_e96, '[1, 1500000]']]}}
                    return resistance_range[tolerance_code]
            if size_code == '1206':
                if tcr_code == 'A':
                    resistance_range = {'L': {'ranges': [[e24_e96, '[20, 50000]']]},
                                        'P': {'ranges': [[e24_e96, '[20, 50000]']]},
                                        'W': {'ranges': [[e24_e96, '[20, 50000]']]},
                                        'B': {'ranges': [[e24_e96, '[20, 50000]']]},
                                        'C': {'ranges': [[e24_e96, '[20, 50000]']]}, 'D': None, 'F': None}
                    return resistance_range[tolerance_code]
                elif tcr_code in ['B', 'C']:
                    resistance_range = {'L': {'ranges': [[e24_e96, '[50.1, 200000]']]},
                                        'P': {'ranges': [[e24_e96, '[50.1, 200000]']]},
                                        'W': {'ranges': [[e24_e96, '[4.7, 200000]']]},
                                        'B': {'ranges': [[e24_e96, '[4.7, 1000000]']]},
                                        'C': {'ranges': [[e24_e96, '[4.7, 1000000]']]}, 'D': None, 'F': None}
                    return resistance_range[tolerance_code]
                elif tcr_code in ['D', 'E']:  # 25, 50 ppm
                    resistance_range = {'L': {'ranges': [[e24_e96, '[50.1, 30000]']]},
                                        'P': {'ranges': [[e24_e96, '[50.1, 30000]']]},
                                        'W': {'ranges': [[e24_e96, '[4.7, 200000]']]},
                                        'B': {'ranges': [[e24_e96, '[1, 1500000]']]},
                                        'C': {'ranges': [[e24_e96, '[1, 1500000]']]},
                                        'D': {'ranges': [[e24_e96, '[1, 1500000]']]},
                                        'F': {'ranges': [[e24_e96, '[1, 1500000]']]}}
                    return resistance_range[tolerance_code]
            if (size_code, power_rating_code) in [('RT1210', '1/4W'), ('RT2010', '1/2W'), ('RT2512', '3/4W')]:
                if tcr_code == 'A':
                    return None
                elif tcr_code in ['B', 'C']:
                    resistance_range = {'L': None, 'P': None,
                                        'W': {'ranges': [[e24_e96, '[100, 100000]']]},
                                        'B': {'ranges': [[e24_e96, '[4.7, 100000]']]},
                                        'C': {'ranges': [[e24_e96, '[4.7, 100000]']]},
                                        'D': None, 'F': None}
                    return resistance_range[tolerance_code]
                elif tcr_code in ['D', 'E']:  # 25, 50 ppm
                    resistance_range = {'L': None, 'P': None,
                                        'W': {'ranges': [[e24_e96, '[4.7, 1000000]']]},
                                        'B': {'ranges': [[e24_e96, '[4.7, 1000000]']]},
                                        'C': {'ranges': [[e24_e96, '[4.7, 1000000]']]},
                                        'D': {'ranges': [[e24_e96, '[4.7, 1000000]']]},
                                        'F': {'ranges': [[e24_e96, '[4.7, 1000000]']]}}
                    return resistance_range[tolerance_code]
            elif size_code == 'RT2512' and power_rating_code == '1D':
                if tcr_code in ['A', 'B', 'C']:  # 5, 10, 15 ppm
                    return None
                else:
                    resistance_range = {'L': None, 'P': None,
                                        'W': {'ranges': [[e24_e96, '[10, 1000000]']]},
                                        'B': {'ranges': [[e24_e96, '[10, 1000000]']]},
                                        'C': {'ranges': [[e24_e96, '[10, 1000000]']]},
                                        'D': {'ranges': [[e24_e96, '[10, 1000000]']]},
                                        'F': {'ranges': [[e24_e96, '[10, 1000000]']]}}
                    return resistance_range[tolerance_code]

    def packaging_data(self, size_code, power_rating_code, packaging_code):
        packaging_type, taping_reel = packaging_code.split('_')
        return self.get_packaging_detail(size_code, packaging_type, taping_reel)

    def get_files(self, partnumber, ordernumber):
        return {}
