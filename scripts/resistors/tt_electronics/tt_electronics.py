from common.value_series import e24_e96
from resistors.common import resistance_to_str, resistance_to_str_v3
from resistors.resistor_generator_base import ResistorGeneratorBase


class TTResistorGenerator(ResistorGeneratorBase):
    def __init__(self):
        super().__init__("TT Electronics",
                         "Resistor Thin Film",
                         "PCF",
                         "Precision Thin Film Nichrome Chip Resistors",
                         operating_temp_range='-55°C ~ 125°C',
                         storage_temp_range='-55°C ~ 125°C',
                         size_code={'0201': '0201', '0402': '0402', '0603': '0603', '0805': '0805', '1206': '1206',
                                    '1210': '1210', '2010': '2010', '2512': '2512'},
                         package={'0201': 'Chip 0201', '0402': 'Chip 0402', '0603': 'Chip 0603', '0805': 'Chip 0805',
                                  '1206': 'Chip 1206', '1210': 'Chip 1210', '2010': 'Chip 2010', '2512': 'Chip 2512'},
                         tolerance={'L': '±0.01%', 'W': '±0.05%', 'B': '±0.1%', 'C': '±0.25%', 'D': '±0.5%',
                                    'F': '±1%'},
                         tcr={'-21': '±1ppm/°C', '-20': '±2ppm/°C', '-19': '±3ppm/°C', '-13': '±5ppm/°C',
                              '-12': '±10ppm/°C', '-11': '±15ppm/°C', 'R': '±25ppm/°C', '-02': '±50ppm/°C'},
                         packaging=['A', 'I', 'A1', 'T1', 'PB', 'LT'],
                         power_rating_codes={'0201': '0.031W', '0402': '0.063W', '0603': '0.063W', '0805': '0.1W'},
                         product_url='https://www.ttelectronics.com/products/categories/resistors/resistors/pcf0603/',
                         notes='')

        self.max_working_voltage = {'0201': '15V', '0402': '25V', '0603': '50V', '0805': '100V',
                                    '1206': '150V', '1210': '150V', '2010': '150V', '2512': '150V'}
        self.max_overload_voltage = None

        self.dimensions = {'0201': {'Length': '0.58mm ±0.05mm', 'Width': '0.29mm ±0.05mm',
                                    'Height': 'max. 0.26mm', 't1': '0.15mm±0.05', 't2': '0.12±0.05mm'},
                           '0402': {'Length': '1.0mm ±0.1mm', 'Width': '0.5mm ±0.05mm',
                                    'Height': 'max. 0.55mm', 't1': '0.25mm ±0.15mm', 't2': '0.2mm ±0.15mm'},
                           '0603': {'Length': '1.6mm ±0.2mm', 'Width': '0.8mm ±0.2mm',
                                    'Height': 'max. 0.65mm', 't1': '0.35mm ±0.25mm', 't2': '0.3mm ±0.2mm'},
                           '0805': {'Length': '2mm ±0.2mm', 'Width': '1.25mm ±0.2mm',
                                    'Height': 'max. 0.65mm', 't1': '0.4mm ±0.25mm', 't2': '0.3mm ±0.2mm'}
                           }

    def get_package_dimension(self, size_code, power_rating_code):
        size = self.size_code[size_code]
        return self.dimensions[size]

    def generate_partnumber(self, size, resistance, power, tcr, tolerance, packaging):
        resistance_str = resistance_to_str(resistance)
        partnumber = f"PCF{size}{tcr}-{resistance_str}{tolerance}#"

        if packaging == 'LT':
            termination = 'LF'
            tcr_converted = {'-13': '13', '-12': '12', '-11': '11', 'R': '03', '-02': '02'}
            tape = 'E' if size in ['2010', '2512'] else 'P'
            if tcr not in tcr_converted.keys():
                return None, None
            resistance_str = resistance_to_str_v3(resistance)
            resistance_str = resistance_str + '0' * (4 - len(resistance_str))
            ordernumber = f"PCF-W{size}{termination}-{tcr_converted[tcr]}-{resistance_str}-{tolerance}-{tape}-{packaging}"
            assert len(ordernumber) == 26, ordernumber + ' ' + str(resistance_str)
        else:
            ordernumber = f"PCF{size}{tcr}-{resistance_str}{tolerance}{packaging}"
        return partnumber, ordernumber

    def get_part_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type, taping_reel):
        partnumber, ordernumber = self.generate_partnumber(size_code, value, power_rating_code, tcr_code,
                                                           tolerance_code, packing_type)
        return partnumber

    def get_order_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type,
                         taping_reel):
        partnumber, ordernumber = self.generate_partnumber(size_code, value, power_rating_code, tcr_code,
                                                           tolerance_code, packing_type)
        return ordernumber

    def get_resistance_range(self, size, tolerance, tcr, power_rating_code, special_feature):
        if size == power_rating_code:
            if size == '0201':
                if tolerance in ['D', 'F']:
                    if tcr == '-02':
                        return {'ranges': [[e24_e96, '[49.9, 33000]']]}
                    elif tcr == 'R':
                        return {'ranges': [[e24_e96, '[49.9, 5000]']]}
            if size == '0402':
                if tolerance in ['F', 'D', 'C']:
                    if tcr in ['-02', 'R']:
                        return {'ranges': [[e24_e96, '[10, 205000]']]}
                elif tolerance == 'B':
                    if tcr in ['-02', 'R']:
                        return {'ranges': [[e24_e96, '[10, 205000]']]}
                    elif tcr == '-11':
                        return {'ranges': [[e24_e96, '[49.9, 70000]']]}
                    elif tcr == '-12':
                        return {'ranges': [[e24_e96, '[49.9, 12000]']]}
                    elif tcr == '-13':
                        return {'ranges': [[e24_e96, '[49.9, 5000]']]}
                    elif tcr in ['-19', '-20']:
                        return {'ranges': [[e24_e96, '[49.9, 4990]']]}
                    elif tcr == '-21':
                        return {'ranges': [[e24_e96, '[49.9, 20000]']]}
                elif tolerance in ['W', 'L']:
                    if tcr in ['-11', '-12']:
                        return {'ranges': [[e24_e96, '[49.9, 12000]']]}
                    elif tcr == '-13':
                        return {'ranges': [[e24_e96, '[49.9, 3000]']]}
                    elif tcr in ['-19', '-20']:
                        return {'ranges': [[e24_e96, '[49.9, 4990]']]}
                    elif tcr == '-21':
                        return {'ranges': [[e24_e96, '[49.9, 20000]']]}
            if size == '0603':
                if tolerance in ['C', 'D', 'F'] and tcr in ['R', '-02']:
                    return {'ranges': [[e24_e96, '[2, 1000000]']]}
                elif tolerance in ['B', 'W', 'L'] and tcr in ['-19', '-20', '-21']:
                    return {'ranges': [[e24_e96, '[24.9, 15000]']]}
                elif tolerance == 'B':
                    if tcr in ['-02', 'R']:
                        return {'ranges': [[e24_e96, '[4.7, 2000000]']]}
                    elif tcr in ['-12', '-11']:
                        return {'ranges': [[e24_e96, '[2, 332000]']]}
                    elif tcr == '-13':
                        return {'ranges': [[e24_e96, '[24.9, 15000]']]}
                elif tolerance == 'W':
                    if tcr in ['-02', 'R', '-12', '-11']:
                        return {'ranges': [[e24_e96, '[4.7, 332000]']]}
                    elif tcr == '-13':
                        return {'ranges': [[e24_e96, '[24.9, 100000]']]}
            if size == '0805':
                if tolerance in ['C', 'D', 'F'] and tcr in ['R', '-02']:
                    return {'ranges': [[e24_e96, '[1, 2000000]']]}
                elif tolerance in ['B', 'W', 'L'] and tcr in ['-19', '-20', '-13']:
                    return {'ranges': [[e24_e96, '[24.9, 49900]']]}
                elif tolerance in ['B', 'W', 'L'] and tcr == '-21':
                    return {'ranges': [[e24_e96, '[24.9, 30000]']]}
                elif tolerance == 'B':
                    if tcr in ['-02', 'R']:
                        return {'ranges': [[e24_e96, '[4.7, 2500000]']]}
                    elif tcr in ['-12', '-11']:
                        return {'ranges': [[e24_e96, '[4.7, 1000000]']]}
                elif tolerance == 'W':
                    if tcr in ['-02', 'R', '-12', '-11']:
                        return {'ranges': [[e24_e96, '[4.7, 1000000]']]}
                elif tolerance == 'L':
                    if tcr in ['-12', '-11']:
                        return {'ranges': [[e24_e96, '[24.9, 500000]']]}

    def packaging_data(self, size, power_rating_code, code):
        if code == 'I' or code == 'LT':
            if size == '0201':
                packaging = {
                    'Packaging Code': 'I', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 10000,
                    'Packaging Data': {
                        'Reel Diameter': '', 'Reel Width': '',
                        'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '', 'Tape F': '', 'Tape SO': '',
                        'Tape P0': '', 'Tape P1': '', 'Tape P2': '', 'Tape D': '', 'Tape D1': '', 'Tape A0': '',
                        'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
                return packaging
            elif size == '0402':
                packaging = {
                    'Packaging Code': 'I', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 10000,
                    'Packaging Data': {
                        'Reel Diameter': '', 'Reel Width': '',
                        'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '', 'Tape F': '', 'Tape SO': '',
                        'Tape P0': '', 'Tape P1': '', 'Tape P2': '', 'Tape D': '', 'Tape D1': '', 'Tape A0': '',
                        'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
                return packaging
            elif size == '0603':
                packaging = {
                    'Packaging Code': 'I', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 5000,
                    'Packaging Data': {
                        'Reel Diameter': '', 'Reel Width': '',
                        'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '', 'Tape F': '', 'Tape SO': '',
                        'Tape P0': '', 'Tape P1': '', 'Tape P2': '', 'Tape D': '', 'Tape D1': '', 'Tape A0': '',
                        'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
                return packaging
            elif size == '0805':
                packaging = {
                    'Packaging Code': 'I', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 5000,
                    'Packaging Data': {
                        'Reel Diameter': '', 'Reel Width': '',
                        'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '', 'Tape F': '', 'Tape SO': '',
                        'Tape P0': '', 'Tape P1': '', 'Tape P2': '', 'Tape D': '', 'Tape D1': '', 'Tape A0': '',
                        'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
                return packaging

    def get_files(self, partnumber, ordernumber):
        return {}

    def pre_save_validate(self):
        assert 'PCF0603-11-1K54B#' in self.parts
        part = self.parts['PCF0603-11-1K54B#']
        assert part['manufacturer'] == 'TT Electronics'
        assert part['partNumber'] == 'PCF0603-11-1K54B#'
        assert part['partType'] == 'Resistor Thin Film', part['partType']
        assert part['series']['name'] == 'PCF', part['series']['name']
        assert part['series']['description'] == 'Precision Thin Film Nichrome Chip Resistors', part['series']['description']
        parameters = part['parameters']
        assert parameters['Resistance']['value'] == "1540.00R \u00b10.1%", parameters['Resistance']
        assert parameters['TCR']['value'] == "\u00b115ppm/\u00b0C", parameters['TCR']
        assert parameters['Rated Power']['value'] == "max. 0.063W", parameters['Max Power']
        assert parameters['Working Voltage']['value'] == 'max. 50V', parameters['Working Voltage']
        assert 'Overload Voltage' not in parameters, parameters['Overload Voltage']
        assert part['package']['type'] == 'Chip 0603', part['package']['type']
        assert part['symbol&footprint']['symbolName'] == 'resistor'

        assert 'PCF0603-11-1K54BI' in part['orderNumbers']
        order_number = part['orderNumbers']['PCF0603-11-1K54BI']
        assert 'I' == order_number['Packaging Code']
        assert 'Paper Tape / Reel' == order_number['Packaging Type']
        assert 5000 == order_number['Packaging Qty']
        return True
