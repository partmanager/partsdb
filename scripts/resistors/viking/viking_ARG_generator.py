from common.value_series import e24, e24_e96
from resistors.common import resistance_to_str, resistance_to_str_v3, resistance_to_str_v2
from resistors.resistor_generator_base import ResistorGeneratorBase


class VikingARGResistorGenerator(ResistorGeneratorBase):
    def __init__(self):
        super().__init__(manufacturer="Viking",
                         part_type="Resistor Thin Film",
                         series="ARG",
                         series_description="Thin Film Chip Resistor",
                         operating_temp_range='-55°C ~ 155°C',
                         storage_temp_range='15°C ~ 28°C',
                         size_code={'ARG02': '0402', 'ARG03': '0603', 'ARG05': '0805', 'ARG06': '1206'},
                         package={'ARG02': 'Chip 0402', 'ARG03': 'Chip 0603', 'ARG05': 'Chip 0805', 'ARG06': 'Chip 1206'},
                         tolerance={'B': '±0.1%', 'C': '±0.25%', 'D': '±0.5%', 'F': '±1%'},
                         tcr={'C': '±25ppm/°C', 'D': '±50ppm/°C'},
                         packaging=['T', 'B'],
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
                                             'S': '2W',
                                             'LL': '1/16W'},
                         product_url='https://www.viking.com.tw/en/category/General-Purpose-Thin-Film-Resistor-ARG-Series/Resistor-ARG.html',
                         notes="Generated based on data from datasheet, Edition : REV.A5, Revision: 22-May-2019")
        self.max_working_voltage = {'ARG02': '50V', 'ARG03': '75V', 'ARG05': '150V', 'ARG06': '200V'}
        self.max_overload_voltage = {'ARG02': '100V', 'ARG03': '150V', 'ARG05': '300V', 'ARG06': '400V'}
        self.dimensions = {
            '0402': {'Length': '1.00mm ±0.05', 'Width': '0.50mm ±0.05', 'Height': '0.30mm±0.10',
                     't1': '0.20mm±0.10', 't2': '0.20±0.10mm'},
            '0603': {'Length': '1.60mm ±0.10', 'Width': '0.80mm ±0.10', 'Height': '0.45mm±0.10',
                     't1': '0.3mm±0.20', 't2': '0.3mm±0.20'},
            '0805': {'Length': '2.00mm ±0.15', 'Width': '1.25mm ±0.15', 'Height': '0.50mm±0.10',
                     't1': '0.30mm±0.20', 't2': '0.4mm±0.20'},
            '1206': {'Length': '3.10mm ±0.15', 'Width': '1.55mm ±0.15', 'Height': '0.55mm±0.10',
                     't1': '0.42mm±0.20', 't2': '0.35mm±0.25'}}

    def get_part_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type, taping_reel):
        standard_power = {'ARG02': 'LL', 'ARG03': 'X', 'ARG05': 'W', 'ARG06': 'V'}
        if standard_power[size_code] == power_rating_code:
            value_str = resistance_to_str_v2(value)
            value_str = '0' * (4 - len(value_str)) + value_str
            assert len(value_str) == 4, value_str
            packing_type = '#'
            return f"{size_code}{tolerance_code}{packing_type}{tcr_code}{value_str}"

    def get_order_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type, taping_reel):
        standard_power = {'ARG02': 'LL', 'ARG03': 'X', 'ARG05': 'W', 'ARG06': 'V'}
        if standard_power[size_code] == power_rating_code:
            value_str = resistance_to_str_v2(value)
            value_str = '0' * (4 - len(value_str)) + value_str
            assert len(value_str) == 4, value_str
            return f"{size_code}{tolerance_code}{packing_type}{tcr_code}{value_str}"

    def get_resistance_range(self, size_code, tolerance_code, tcr_code, power_rating_code, special_feature):
        if size_code == 'ARG02' and tolerance_code in ['B', 'C', 'D', 'F'] and tcr_code in ['C', 'D']:
            return {'ranges': [[e24_e96, '[4.7, 255000]']]}
        elif size_code == 'ARG03' and tolerance_code in ['B', 'C', 'D', 'F'] and tcr_code in ['C', 'D']:
            return {'ranges': [[e24_e96, '[1, 1000000]']]}
        elif size_code == 'ARG05' and tolerance_code in ['B', 'C', 'D', 'F'] and tcr_code in ['C', 'D']:
            return {'ranges': [[e24_e96, '[1, 2000000]']]}
        elif size_code == 'ARG06' and tolerance_code in ['B', 'C', 'D', 'F'] and tcr_code in ['C', 'D']:
            return {'ranges': [[e24_e96, '[1, 2490000]']]}

    def packaging_data(self, size_code, power_rating_code, code):
        size = self.size_code[size_code]
        if code == 'T':
            if size == '0402':
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
            elif size == '0603':
                packaging = {
                    'Packaging Code': 'T', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 5000,
                    'Packaging Data': {
                        'Reel Diameter': '178.5mm', 'Reel Width': '12.5mm',
                        'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '1.75mm±0.1mm',
                        'Tape F': '3.50mm±0.05mm', 'Tape SO': '',
                        'Tape P0': '4mm±0.10mm', 'Tape P1': '4mm±0.05mm', 'Tape P2': '2mm±0.05mm', 'Tape D': '',
                        'Tape D1': '', 'Tape A0': '',
                        'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            elif size == '0805':
                packaging = {
                    'Packaging Code': 'T', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 5000,
                    'Packaging Data': {
                        'Reel Diameter': '178.5mm', 'Reel Width': '12.5mm',
                        'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '1.75mm±0.1mm',
                        'Tape F': '3.50mm±0.05mm', 'Tape SO': '',
                        'Tape P0': '4mm±0.10mm', 'Tape P1': '4mm±0.05mm', 'Tape P2': '2mm±0.05mm', 'Tape D': '',
                        'Tape D1': '', 'Tape A0': '',
                        'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            elif size == '1206':
                packaging = {
                    'Packaging Code': 'T', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 5000,
                    'Packaging Data': {
                        'Reel Diameter': '178.5mm', 'Reel Width': '12.5mm',
                        'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '1.75mm±0.1mm',
                        'Tape F': '3.50mm±0.05mm', 'Tape SO': '',
                        'Tape P0': '4mm±0.10mm', 'Tape P1': '4mm±0.05mm', 'Tape P2': '2mm±0.05mm', 'Tape D': '',
                        'Tape D1': '', 'Tape A0': '',
                        'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            elif size == '1210':
                packaging = {
                    'Packaging Code': 'T', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 5000,
                    'Packaging Data': {
                        'Reel Diameter': '178.5mm', 'Reel Width': '12.5mm',
                        'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '1.75mm±0.1mm',
                        'Tape F': '3.50mm±0.05mm', 'Tape SO': '',
                        'Tape P0': '4mm±0.10mm', 'Tape P1': '4mm±0.05mm', 'Tape P2': '2mm±0.05mm', 'Tape D': '',
                        'Tape D1': '', 'Tape A0': '',
                        'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            elif size == '2010':
                packaging = {
                    'Packaging Code': 'T', 'Packaging Type': 'Embossed Tape / Reel', 'Packaging Qty': 4000,
                    'Packaging Data': {
                        'Reel Diameter': '178.5mm', 'Reel Width': '15.5mm',
                        'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '12mm', 'Tape E': '1.75mm±0.1mm',
                        'Tape F': '5.50mm±0.05mm', 'Tape SO': '',
                        'Tape P0': '4mm±0.10mm', 'Tape P1': '4mm±0.10mm', 'Tape P2': '2mm±0.05mm', 'Tape D': '',
                        'Tape D1': '', 'Tape A0': '',
                        'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            elif size == '2512':
                packaging = {
                    'Packaging Code': 'T', 'Packaging Type': 'Embossed Tape / Reel', 'Packaging Qty': 4000,
                    'Packaging Data': {
                        'Reel Diameter': '178.5mm', 'Reel Width': '15.5mm',
                        'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '12mm', 'Tape E': '1.75mm±0.1mm',
                        'Tape F': '5.50mm±0.05mm', 'Tape SO': '',
                        'Tape P0': '4mm±0.10mm', 'Tape P1': '4mm±0.10mm', 'Tape P2': '2mm±0.05mm', 'Tape D': '',
                        'Tape D1': '', 'Tape A0': '',
                        'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
        elif code == 'B':
            packaging = {}
        return packaging

    def get_files(self, partnumber, ordernumber):
        return {}

    def pre_save_validate(self):
        assert 'ARG03F#C1001' in self.parts
        part = self.parts['ARG03F#C1001']
        assert part['manufacturer'] == 'Viking'
        assert part['partNumber'] == 'ARG03F#C1001'
        assert part['partType'] == 'Resistor Thin Film'
        assert part['series']['name'] == 'ARG'
        assert part['series']['description'] == 'Thin Film Chip Resistor'
        parameters = part['parameters']
        assert parameters['Resistance']['value'] == "1000.00R \u00b11%"
        assert parameters['TCR']['value'] == "\u00b125ppm/\u00b0C"
        assert parameters['Rated Power']['value'] == "max. 0.1W"
        assert parameters['Working Voltage']['value'] == 'max. 75V'
        assert parameters['Overload Voltage']['value'] == 'max. 150V'
        assert part['package']['type'] == 'Chip 0603'
        assert part['symbol&footprint']['symbolName'] == 'resistor'

        assert 'ARG03FTC1001' in part['orderNumbers']
        return True
