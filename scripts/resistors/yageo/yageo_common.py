import decimal
from resistors.common import *
from resistors.resistor_generator_base import ResistorGeneratorBase


class YageoResistorBase(ResistorGeneratorBase):
    def __init__(self, part_type, series, series_description, operating_temp_range, storage_temp_range, size_code,
                 package, packaging, power_rating_codes, product_url, notes):
        super().__init__(manufacturer="Yageo",
                         part_type=part_type,
                         series=series,
                         series_description=series_description,
                         operating_temp_range=operating_temp_range,
                         storage_temp_range=storage_temp_range,
                         size_code=size_code,
                         package=package,
                         tolerance={'W': '±0.05%', 'B': '±0.1%', 'C': '±0.25%', 'D': '±0.5%', 'F': '±1%', 'J': '±5%'},
                         tcr={'R': '±10ppm/°C', 'P': '±15ppm/°C', 'D': '±25ppm/°C', 'E': '±50ppm/°C',
                              '100': '±100ppm/°C',
                              '200': '±200ppm/°C', '300': '±300ppm/°C',
                              '-100+350': '-100 ~ +350ppm/°C', '-100+600': '-100 ~ +600ppm/°C',
                              '-400+150': '-400 ~ +150ppm/°C'},
                         packaging=packaging,
                         power_rating_codes=power_rating_codes,
                         product_url=product_url,
                         notes=notes)
        self.dual_power_taping_reel_codes = ['R_7W', 'R_3W', 'E_7W', 'E_3W'],
        self.reel_size = {'07': '7', '10': '10', '13': '13', '7W': '7', '7N': '7', '3W': '13'}
        self.default_code = 'L'

    def get_packaging_detail(self, size, packaging_type, taping_reel):
        packaging_code = self.get_packaging_code(packaging_type, taping_reel)
        quantity = self.get_packaging_quantity(size, packaging_type, taping_reel)
        if quantity:
            if packaging_type == 'R':
                if taping_reel in ['07', '7W', '7N']:
                    packaging = {
                        'Code': packaging_code,
                        'Type': 'Paper Tape / Reel',
                        'Qty': quantity,
                        'PackagingData': {
                            'reel': {
                                "Diameter": '178mm',
                                'Width': '12.5mm'},
                            'tape': {
                                'Pin 1 Quadrant': 'Q1',
                                'W': '8mm', 'E': '1.75mm±0.1mm',
                                'F': '3.50mm±0.05mm',
                                'P0': '4mm±0.10mm',
                                'P1': '2mm',
                                'P2': '2mm±0.05mm'
                            }
                        }
                    }
                    return packaging
                elif taping_reel in ['10']:
                    packaging = {
                        'Code': packaging_code,
                        'Type': 'Paper Tape / Reel',
                        'Qty': quantity,
                        'PackagingData': {
                            'reel': {
                                'Diameter': '254mm',
                                'Width': '12.5mm'
                            },
                            'tape': {
                                'Pin 1 Quadrant': 'Q1',
                                'W': '8mm',
                                'E': '1.75mm±0.1mm',
                                'F': '3.50mm±0.05mm',
                                'P0': '4mm±0.10mm',
                                'P1': '2mm',
                                'P2': '2mm±0.05mm'
                            }
                        }
                    }
                    return packaging
                elif taping_reel in ['13', '3W']:
                    packaging = {
                        'Code': packaging_code,
                        'Type': 'Paper Tape / Reel',
                        'Qty': quantity,
                        'PackagingData': {
                            'reel': {
                                'Diameter': '330mm',
                                'Width': '12.5mm'
                            },
                            'tape': {
                                'Pin 1 Quadrant': 'Q1',
                                'W': '8mm',
                                'E': '1.75mm±0.1mm',
                                'F': '3.50mm±0.05mm',
                                'P0': '4mm±0.10mm',
                                'P1': '2mm',
                                'P2': '2mm±0.05mm'
                            }
                        }
                    }
                    return packaging
            elif packaging_type == 'K':
                if taping_reel in ['07', '7W', '7N']:
                    packaging = {
                        'Code': packaging_code,
                        'Type': 'Embossed Tape / Reel',
                        'Qty': quantity,
                        'PackagingData': {
                            'reel': {
                                'Diameter': '178mm',
                                'Width': '12.5mm'
                            },
                            'tape': {
                                'Pin 1 Quadrant': 'Q1',
                                'W': '8mm',
                                'E': '1.75mm±0.1mm',
                                'F': '3.50mm±0.05mm',
                                'P0': '4mm±0.10mm',
                                'P1': '2mm',
                                'P2': '2mm±0.05mm'
                            }
                        }
                    }
                    return packaging

    def get_packaging_code(self, packaging_type, taping_reel):
        return f"{packaging_type}-{taping_reel}"

    def get_packaging_quantity(self, size_code, packaging_type, taping_reel):
        qty = {'0075': {'7_R': None, '10_R': None, '13_R': None, '7_S': 20000, '7_K': None},
               '0100': {'7_R': 20000, '10_R': None, '13_R': 80000, '7_S': 40000, '7_K': None},
               '0201': {'7_R': 10000, '10_R': 20000, '13_R': 50000, '7_S': None, '7_K': None},
               '0402': {'7_R': 10000, '10_R': 20000, '13_R': 50000, '7_S': None, '7_K': None},
               '0603': {'7_R': 5000, '10_R': 10000, '13_R': 20000, '7_S': None, '7_K': None},
               '0805': {'7_R': 5000, '10_R': 10000, '13_R': 20000, '7_S': None, '7_K': None},
               '1206': {'7_R': 5000, '10_R': 10000, '13_R': 20000, '7_S': None, '7_K': None},
               '1210': {'7_R': 5000, '10_R': 10000, '13_R': 20000, '7_S': None, '7_K': None},
               '1218': {'7_R': None, '10_R': None, '13_R': None, '7_S': None, '7_K': 4000},
               '2010': {'7_R': None, '10_R': None, '13_R': None, '7_S': None, '7_K': 4000},
               '2512': {'7_R': None, '10_R': None, '13_R': None, '7_S': None, '7_K': 4000},
               }
        key = self.reel_size[taping_reel] + '_' + packaging_type
        size = self.size_code[size_code]
        return qty[size][key] if key in qty[size] else None

    def get_part_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type, special_feature):
        if 'D' not in power_rating_code or ('D' in power_rating_code and packing_type in self.dual_power_taping_reel_codes):
            packing_type, taping_reel = packing_type.split('_')
            packing_type = '#'
            resistance_str = resistance_to_str(value)
            return f"{size_code}{tolerance_code}{packing_type}-{taping_reel}{resistance_str}{self.default_code}"

    def get_order_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type, special_feature):
        packing_type, taping_reel = packing_type.split('_')
        resistance_str = resistance_to_str(value)
        return f"{size_code}{tolerance_code}{packing_type}-{taping_reel}{resistance_str}{self.default_code}"


resistor_taping_reel = {'07': '7 inch dia. Reel',
                        '10': '10 inch dia. Reel',
                        '13': '13 inch dia. Reel',
                        '7W': '7 inch dia. Reel',  #  2 x standard power
                        '7N': '7 inch dia. Reel, ESD safe reel', #  (0075/0100 only)
                        '3W': '13 inch dia. Reel'}  #  2 x standard power


def value_to_ohm(value_str):
    if 'R' in value_str:
        return decimal.Decimal(value_str.replace('R', '.'))
    if 'K' in value_str:
        return decimal.Decimal(value_str.replace('K', '.')) * 1000
    if 'M' in value_str:
        return decimal.Decimal(value_str.replace('M', '.')) * 1000000


def rated_power(size, taping_reel, power_rating):
    if taping_reel in ['7W', '3W']:
        return power_rating[size][1]
    else:
        return power_rating[size][0]


def packing_quantity(size, taping_reel):
    quantity_map = {'0075': {'7N': 20000},
                    '0100': {'07': 20000, '13': 80000, '7N': 40000},
                    '0201': {'07': 10000, '10': 20000, '13': 50000},
                    '0402': {'07': 10000, '7W': 10000, '10': 20000, '13': 50000, '3W': 50000},
                    '0603': {'07': 5000, '7W': 5000, '10': 10000, '13': 20000, '3W': 20000},
                    '0805': {'07': 5000, '7W': 5000, '10': 10000, '13': 20000, '3W': 20000},
                    '1206': {'07': 5000, '7W': 5000, '10': 10000, '13': 20000, '3W': 20000},
                    '1210': {'07': 5000, '10': 10000, '13': 20000},
                    '1218': {'07': '4000'},
                    '2010': {'07': '4000'},
                    '2512': {'07': '4000', '7W': 4000}}
    return quantity_map[size][taping_reel]
