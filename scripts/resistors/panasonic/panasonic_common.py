from common.value_series import in_e24
from resistors.resistor_generator_base import ResistorGeneratorBase
from resistors.common import resistance_to_str_multiplier, resistance_to_str_multiplier_coma


class PanasonicResistorBase(ResistorGeneratorBase):
    def __init__(self, part_type, series, series_description, operating_temp_range, storage_temp_range, size_code,
                 package, packaging, power_rating_codes, product_url, notes):
        super().__init__(manufacturer="Panasonic",
                         part_type=part_type,
                         series=series,
                         series_description=series_description,
                         operating_temp_range=operating_temp_range,
                         storage_temp_range=storage_temp_range,
                         size_code=size_code,
                         package=package,
                         tolerance={'W': '±0.05%', 'B': '±0.1%', 'C': '±0.25%', 'D': '±0.5%', 'F': '±1%', 'J': '±5%'},
                         tcr={'R': '±10ppm/°C', 'P': '±15ppm/°C', 'E': '±25ppm/°C', 'H': '±50ppm/°C',
                              'K': '±100ppm/°C',
                              '200': '±200ppm/°C', '300': '±300ppm/°C',
                              '-100+600': '-100 ~ +600ppm/°C', '-400+150': '-400 ~ +150ppm/°C'},
                         packaging=packaging,
                         power_rating_codes=power_rating_codes,
                         product_url=product_url,
                         notes=notes)
        #tolerance = {'W': '±0.05%', 'B': '±0.1%', 'C': '±0.25%', 'D': '±0.5%', 'F': '±1%', 'J': '±5%'},
        #tolerance = {'W': '±0.05%', 'B': '±0.1%', 'C': '±0.25%', 'D': '±0.5%', 'F': '±1%', 'J': '±5%'},
        #tcr = {'R': '±10ppm/°C', 'P': '±15ppm/°C', 'E': '±25ppm/°C', 'H': '±50ppm/°C', 'K': '±100ppm/°C',
        #       '200': '±200ppm/°C', '300': '±300ppm/°C', '-100+600': '-100 ~ +600ppm/°C'},
        #tcr = {'R': '±10ppm/°C', 'P': '±15ppm/°C', 'E': '±25ppm/°C', 'H': '±50ppm/°C', 'K': '±100ppm/°C',
        #       '200': '±200ppm/°C', '300': '±300ppm/°C', '-100+600': '-100 ~ +600ppm/°C'},

        #tolerance = {'D': '±0.5%', 'F': '±1%'},
        #tcr = {'R': '±10ppm/°C', 'P': '±15ppm/°C', 'E': '±25ppm/°C', 'H': '±50ppm/°C', 'K': '±100ppm/°C',
        #       '200': '±200ppm/°C', '300': '±300ppm/°C', '-100+600': '-100 ~ +600ppm/°C'},

        #tolerance = {'W': '±0.05%', 'B': '±0.1%', 'C': '±0.25%', 'D': '±0.5%', 'F': '±1%'},
        #tcr = {'R': '±10ppm/°C', 'P': '±15ppm/°C', 'E': '±25ppm/°C', 'H': '±50ppm/°C',
        #       'K': '±100ppm/°C'},

    def generate_part_number_in_e24(self, size, value, tolerance_code, tcr_code, power_rating_code, packing_type, taping_reel):
        if size == "ERA" + power_rating_code:
            if in_e24(value):
                value_str = resistance_to_str_multiplier_coma(value, digits=2)
                assert len(value_str) == 3, f"{value} -> {value_str}"
            else:
                value_str = resistance_to_str_multiplier_coma(value)
                assert len(value_str) == 4, value_str
            return f"{size}{tcr_code}{tolerance_code}{value_str}{packing_type}"

    def generate_part_number_no_tcr(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type, taping_reel):
        value_str = resistance_to_str_multiplier_coma(value)
        assert len(value_str) == 4, value_str
        return f"{size_code}{tolerance_code}{value_str}{packing_type}"

    def generate_part_number_no_tcr_with_marking(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type, taping_reel):
        value_str = resistance_to_str_multiplier_coma(value, digits=2)
        assert len(value_str) == 3, value_str
        value_marking = '' if power_rating_code in ['XGN', '1GN', '2GE'] else 'Y'
        return f"{size_code}{value_marking}{tolerance_code}{value_str}{packing_type}"