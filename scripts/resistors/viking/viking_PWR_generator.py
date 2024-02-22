from common.value_series import e24, e24_e96
from resistors.common import resistance_to_str_v2
from resistors.resistor_generator_base import ResistorGeneratorBase


class VikingPWRResistorGenerator(ResistorGeneratorBase):
    def __init__(self):
        super().__init__(manufacturer="Viking",
                         part_type="Resistor Thin Film",
                         series="PWR",
                         series_description="Pulse Withstanding Chip Resistor",
                         operating_temp_range='-55°C ~ 155°C',
                         storage_temp_range='-55°C ~ 155°C',
                         size_code={'PWR02': '0402', 'PWR03': '0603', 'PWR05': '0805', 'PWR06': '1206', 'PWR13': '1210',
                                    'PWR10': '2010', 'PWR12': '2512'},
                         package={'PWR02': 'Chip 0402', 'PWR03': 'Chip 0603', 'PWR05': 'Chip 0805', 'PWR06': 'Chip 1206', 'PWR13': 'Chip 1210',
                                  'PWR10': 'Chip 2010', 'PWR12': 'Chip 2512'},
                         tolerance={'D': '±0.5%', 'F': '±1%', 'J': '±5%'},
                         tcr={'E': '±100ppm/°C', 'F': '±200ppm/°C', 'G': '±300ppm/°C', '4': '±350ppm/°C'},
                         packaging=['T'],
                         power_rating_codes={'A': '1.5W',
                                             'T': '1W',
                                             'Q': '0.75W',  # '3/4W',
                                             'U': '0.5W',  # '1/2W',
                                             'G': '0.4W',  # '2/5W',
                                             'O': '0.333333333W',  # '1/3W',
                                             'V': '0.25W',  # '1/4W',
                                             'W': '0.125W',  # '1/8W',
                                             'X': '0.1W',  # '1/10W',
                                             'P': '0.2W',  # '1/5W',
                                             'S': '2W'},
                         product_url='',
                         notes="Generated based on data from datasheet, Edition : REV.C6, Revision: 31-Jan-2020")
        self.max_working_voltage = {'PWR02': '50V', 'PWR03': '50V', 'PWR05': '150V',
                                    'PWR06': '200V', 'PWR13': '200V', 'PWR10': '150V', 'PWR12': '150V'}
        self.max_overload_voltage = {'PWR02': '100V', 'PWR03': '100V', 'PWR05': '300V',
                                     'PWR06': '400V', 'PWR13': '400V', 'PWR10': '800V', 'PWR12': '1000V'}
        self.dimensions = {
                              '0402': {'Length': '1.00mm ±0.05', 'Width': '0.50mm ±0.05', 'Height': '0.35mm±0.05',
                                       't1': '0.20mm±0.10', 't2': '0.20±0.10mm'},
                              '0603': {'Length': '1.60mm ±0.10', 'Width': '0.80mm ±0.10', 'Height': '0.45mm±0.10',
                                       't1': '0.3mm±0.20', 't2': '0.3mm±0.20'},
                              '0805': {'Length': '2.00mm ±0.10', 'Width': '1.25mm ±0.10', 'Height': '0.50mm±0.10',
                                       't1': '0.35mm±0.20', 't2': '0.4mm±0.20'},
                              '1206': {'Length': '3.10mm ±0.10', 'Width': '1.55mm ±0.10', 'Height': '0.55mm±0.10',
                                       't1': '0.50mm±0.25', 't2': '0.50mm±0.20'},
                              '1210': {'Length': '3.10mm ±0.10', 'Width': '2.60mm ±0.15mm', 'Height': '0.55mm±0.10',
                                       't1': '0.5mm±0.25', 't2': '0.50mm±0.20'},
                              '2010': {'Length': '5.00mm ±0.10', 'Width': '2.50mm ±0.15', 'Height': '0.55mm±0.10',
                                       't1': '0.6mm±0.25', 't2': '0.5mm±0.20'},
                              '2512': {'Length': '6.35mm ±0.20', 'Width': '3.15mm ±0.15', 'Height': '0.60mm±0.10',
                                       't1': '0.6mm±0.25', 't2': '0.6mm±0.20'}}
        # self.size_code = {'0402': 'PWR02', '0603': 'PWR03', '0805': 'PWR05', '1206': 'PWR06', '1210': 'PWR13',
        #                   '2010': 'PWR10', '2512': 'PWR12'}

    def get_part_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type, taping_reel):
        standard_power = {'PWR02': 'P', 'PWR03': 'X', 'PWR05': 'W', 'PWR06': 'O', 'PWR13': 'U', 'PWR10': 'Q', 'PWR12': 'A'}
        if standard_power[size_code] == power_rating_code:
            value_str = resistance_to_str_v2(value)
            value_str = '0' * (4 - len(value_str)) + value_str
            assert len(value_str) == 4, value_str
            packing_type = '#'
            return f"{size_code}{tolerance_code}{packing_type}{tcr_code}{power_rating_code}{value_str}"

    def get_order_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type, taping_reel):
        standard_power = {'PWR02': 'P', 'PWR03': 'X', 'PWR05': 'W', 'PWR06': 'O', 'PWR13': 'U', 'PWR10': 'Q', 'PWR12': 'A'}
        if standard_power[size_code] == power_rating_code:
            value_str = resistance_to_str_v2(value)
            value_str = '0' * (4 - len(value_str)) + value_str
            assert len(value_str) == 4, value_str
            return f"{size_code}{tolerance_code}{packing_type}{tcr_code}{power_rating_code}{value_str}"

    def package_dimension(self, size):
        return {}

    def get_resistance_range(self, size, tolerance_code, tcr_code, power_rating_code, special_feature):
        if size == 'PWR02':
            if tolerance_code == 'D' and tcr_code == 'E':  # 0.5% 100ppm
                return {'ranges': [[e24_e96, '[100, 1000000]']]}
            elif tolerance_code == 'F':  # 1%
                if tcr_code == 'G':  # 300ppm
                    return {'ranges': [[e24_e96, '[1, 20]']]}
                elif tcr_code == 'E':  # 100ppm
                    return {'ranges': [[e24_e96, '[20.5, 1000000]']]}
            elif tolerance_code == 'J':  # 5%
                if tcr_code == 'G':  # 300ppm
                    return {'ranges': [[e24, '[1, 20]']]}
                elif tcr_code == 'E':  # 100ppm
                    return {'ranges': [[e24, '[20.5, 1000000]']]}
        elif size == 'PWR03':
            if tcr_code == 'E':  # 100ppm
                if tolerance_code in ['D', 'F']:  # 0.5%, 1%
                    return {'ranges': [[e24_e96, '[300, 1000000]']]}
                elif tolerance_code == 'J':  # 5%
                    return {'ranges': [[e24, '[300, 1000000]']]}
            elif tcr_code == 'F':
                if tolerance_code == 'D':
                    return {'ranges': [[e24_e96, '[10, 294]']]}
                elif tolerance_code == 'F':
                    return {'ranges': [[e24_e96, '[1, 294]']]}
                elif tolerance_code == 'J':
                    return {'ranges': [[e24, '[1, 294]']]}
        elif size == 'PWR05':
            if tcr_code == 'E':  # 100ppm
                if tolerance_code in ['D', 'F']:  # 0.5%, 1%
                    return {'ranges': [[e24_e96, '[300, 2000000]']]}
                elif tolerance_code == 'J':  # 5%
                    return {'ranges': [[e24, '[300, 2000000]']]}
            elif tcr_code == 'F':
                if tolerance_code == 'D':
                    return {'ranges': [[e24_e96, '[10, 294]']]}
                elif tolerance_code == 'F':
                    return {'ranges': [[e24_e96, '[1, 294]']]}
                elif tolerance_code == 'J':
                    return {'ranges': [[e24, '[1, 294]']]}
        elif size in ['PWR06', 'PWR13', 'PWR10', 'PWR12']:
            if tcr_code == 'E':  # 100ppm
                if tolerance_code in ['D', 'F']:  # 0.5%, 1%
                    return {'ranges': [[e24_e96, '[20.5, 2000000]']]}
                elif tolerance_code == 'J':  # 5%
                    return {'ranges': [[e24, '[20.5, 2000000]']]}
            elif tcr_code == 'F':  # 200ppm
                if tolerance_code == 'D':
                    return {'ranges': [[e24_e96, '[10, 20]']]}
                elif tolerance_code == 'F':
                    return {'ranges': [[e24_e96, '[1, 20]']]}
                elif tolerance_code == 'J':
                    return {'ranges': [[e24, '[1, 20]']]}

    def packaging_data(self, size, power_rating_code, code):
        if code == 'T':
            if size == 'PWR02':
                packaging = {
                    'Packaging Code': 'T', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 10000,
                    'Packaging Data': {
                        'Reel Diameter': '178.5mm', 'Reel Width': '12.5mm',
                        'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '1.75mm±0.1mm',
                        'Tape F': '3.50mm±0.05mm',
                        'Tape SO': '',
                        'Tape P0': '4mm±0.10mm', 'Tape P1': '2mm±0.05mm', 'Tape P2': '2mm±0.05mm', 'Tape D': '',
                        'Tape D1': '',
                        'Tape A0': '', 'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            elif size == 'PWR03':
                packaging = {
                    'Packaging Code': 'T', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 5000,
                    'Packaging Data': {
                        'Reel Diameter': '178.5mm', 'Reel Width': '12.5mm',
                        'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '1.75mm±0.1mm',
                        'Tape F': '3.50mm±0.05mm', 'Tape SO': '',
                        'Tape P0': '4mm±0.10mm', 'Tape P1': '4mm±0.05mm', 'Tape P2': '2mm±0.05mm', 'Tape D': '',
                        'Tape D1': '', 'Tape A0': '',
                        'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            elif size == 'PWR05':
                packaging = {
                    'Packaging Code': 'T', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 5000,
                    'Packaging Data': {
                        'Reel Diameter': '178.5mm', 'Reel Width': '12.5mm',
                        'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '1.75mm±0.1mm',
                        'Tape F': '3.50mm±0.05mm', 'Tape SO': '',
                        'Tape P0': '4mm±0.10mm', 'Tape P1': '4mm±0.05mm', 'Tape P2': '2mm±0.05mm', 'Tape D': '',
                        'Tape D1': '', 'Tape A0': '',
                        'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            elif size == 'PWR06':
                packaging = {
                    'Packaging Code': 'T', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 5000,
                    'Packaging Data': {
                        'Reel Diameter': '178.5mm', 'Reel Width': '12.5mm',
                        'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '1.75mm±0.1mm',
                        'Tape F': '3.50mm±0.05mm', 'Tape SO': '',
                        'Tape P0': '4mm±0.10mm', 'Tape P1': '4mm±0.05mm', 'Tape P2': '2mm±0.05mm', 'Tape D': '',
                        'Tape D1': '', 'Tape A0': '',
                        'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            elif size == 'PWR13':
                packaging = {
                    'Packaging Code': 'T', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 5000,
                    'Packaging Data': {
                        'Reel Diameter': '178.5mm', 'Reel Width': '12.5mm',
                        'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '1.75mm±0.1mm',
                        'Tape F': '3.50mm±0.05mm', 'Tape SO': '',
                        'Tape P0': '4mm±0.10mm', 'Tape P1': '4mm±0.05mm', 'Tape P2': '2mm±0.05mm', 'Tape D': '',
                        'Tape D1': '', 'Tape A0': '',
                        'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            elif size == 'PWR10':
                packaging = {
                    'Packaging Code': 'T', 'Packaging Type': 'Embossed Tape / Reel', 'Packaging Qty': 4000,
                    'Packaging Data': {
                        'Reel Diameter': '178.5mm', 'Reel Width': '15.5mm',
                        'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '12mm', 'Tape E': '1.75mm±0.1mm',
                        'Tape F': '5.50mm±0.05mm', 'Tape SO': '',
                        'Tape P0': '4mm±0.10mm', 'Tape P1': '4mm±0.10mm', 'Tape P2': '2mm±0.05mm', 'Tape D': '',
                        'Tape D1': '', 'Tape A0': '',
                        'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            elif size == 'PWR12':
                packaging = {
                    'Packaging Code': 'T', 'Packaging Type': 'Embossed Tape / Reel', 'Packaging Qty': 4000,
                    'Packaging Data': {
                        'Reel Diameter': '178.5mm', 'Reel Width': '15.5mm',
                        'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '12mm', 'Tape E': '1.75mm±0.1mm',
                        'Tape F': '5.50mm±0.05mm', 'Tape SO': '',
                        'Tape P0': '4mm±0.10mm', 'Tape P1': '4mm±0.10mm', 'Tape P2': '2mm±0.05mm', 'Tape D': '',
                        'Tape D1': '', 'Tape A0': '',
                        'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
        return packaging

    def get_files(self, partnumber, ordernumber):
        return {}
