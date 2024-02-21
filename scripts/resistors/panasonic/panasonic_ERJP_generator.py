from common.value_series import e24, e24_e96
from resistors.common import resistance_to_str_multiplier_coma
from .panasonic_common import PanasonicResistorBase


class PanasonicERJPResistorGenerator(PanasonicResistorBase):
    def __init__(self):
        super().__init__(part_type="Resistor Thick Film",
                         series="ERJP",
                         series_description="Anti-Surge Thick Film Chip Resistors",
                         operating_temp_range='-55°C ~ 175°C',
                         storage_temp_range='5°C ~ 35°C',
                         size_code={'ERJPA2': '0402', 'ERJP03': '0603', 'ERJPA3': '0603', 'ERJP06': '0805',
                                    'ERJP08': '1206', 'ERJPM8': '1206', 'ERJP14': '1210'},
                         package={'ERJPA2': 'Chip 0402', 'ERJP03': 'Chip 0603', 'ERJPA3': 'Chip 0603',
                                  'ERJP06': 'Chip 0805', 'ERJP08': 'Chip 1206', 'ERJPM8': 'Chip 1206',
                                  'ERJP14': 'Chip 1210'},
                         packaging=['X', 'V', 'U'],
                         power_rating_codes={'PA2': '0.2W', 'P03': '0.2W', 'PA3': '0.25W', 'P06': '0.5W',
                                             'P08': '0.66W', 'PM8': '0.66W', 'P14': '0.5W'},
                         product_url='',
                         notes="Generated based on data from datasheet: 27-Jul-21")
        self.max_working_voltage = {'ERJPA2': '50V', 'ERJP03': '150V', 'ERJPA3': '150V', 'ERJP06': '400V',
                                    'ERJP08': '500V', 'ERJPM8': '500', 'ERJP14': '200V'}
        self.max_overload_voltage = {'ERJPA2': '100V', 'ERJP03': '200V', 'ERJPA3': '200V', 'ERJP06': '600V',
                                     'ERJP08': '1000V', 'ERJPM8': '1000', 'ERJP14': '400V'}
        self.dimensions = {
            'ERJPA2': {'Length': '1.00mm ±0.05', 'Width': '0.50mm ±0.05', 'Height': '0.35mm±0.05',
                       't1': '0.20mm±0.15', 't2': '0.25±0.05mm'},
            'ERJP03': {'Length': '1.60mm ±0.15', 'Width': '0.80mm +0.8/-0.05', 'Height': '0.45mm±0.10',
                       't1': '0.15mm +0.15-0.1', 't2': '0.3mm±0.15'},
            'ERJPA3': {'Length': '1.60mm ±0.15', 'Width': '0.80mm +0.8/-0.05', 'Height': '0.45mm±0.10',
                       't1': '0.15mm +0.15-0.1', 't2': '0.25mm±0.10'},
            'ERJP06': {'Length': '2.00mm ±0.20', 'Width': '1.25mm ±0.10', 'Height': '0.60mm±0.10',
                       't1': '0.25mm±0.20', 't2': '0.40mm±0.20'},
            'ERJP08_PM8': {'Length': '3.20mm +0.05/-0.2', 'Width': '1.60mm +0.05mm/-0.15mm', 'Height': '0.60mm±0.10',
                           't1': '0.40mm±0.20', 't2': '0.50mm±0.20'},
            'ERJP14': {'Length': '3.20mm ±0.20', 'Width': '2.50mm ±0.20', 'Height': '0.60mm±0.10',
                       't1': '0.35mm±0.20', 't2': '0.50mm±0.20'}
        }

    def get_package_dimension(self, size_code, power_rating_code):
        dimensions = {'ERJPA2': self.dimensions['ERJPA2'],
                      'ERJP03': self.dimensions['ERJP03'],
                      'ERJPA3': self.dimensions['ERJPA3'],
                      'ERJP06': self.dimensions['ERJP06'],
                      'ERJP08': self.dimensions['ERJP08_PM8'],
                      'ERJPM8': self.dimensions['ERJP08_PM8'],
                      'ERJP14': self.dimensions['ERJP14']}
        return dimensions[size_code]

    def get_part_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type, taping_reel):
        if size_code == "ERJ" + power_rating_code:
            if tolerance_code == 'J':
                value_str = resistance_to_str_multiplier_coma(value, digits=2)
                assert len(value_str) == 3, f"{value} -> {value_str}"
            else:
                value_str = resistance_to_str_multiplier_coma(value)
                assert len(value_str) == 4, value_str
            packing_type = '#'
            return f"{size_code}{tolerance_code}{value_str}{packing_type}"

    def get_order_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type,
                         taping_reel):
        if size_code == "ERJ" + power_rating_code:
            if tolerance_code == 'J':
                value_str = resistance_to_str_multiplier_coma(value, digits=2)
                assert len(value_str) == 3, f"{value} -> {value_str}"
            else:
                value_str = resistance_to_str_multiplier_coma(value)
                assert len(value_str) == 4, value_str
            return f"{size_code}{tolerance_code}{value_str}{packing_type}"

    def get_resistance_range(self, size_code, tolerance_code, tcr_code, power_rating_code, special_feature):
        if size_code == 'ERJPA2':
            if tolerance_code in ['D', 'F'] and tcr_code == 'K':
                return {'ranges': [[e24_e96, '[10, 1000000]']]}
            elif tolerance_code == 'J' and tcr_code == '200':  # 25ppm
                return {'ranges': [[e24, '[10, 1000000]']]}
        elif size_code == 'ERJP03':
            if tolerance_code == 'D' and tcr_code == '150':
                return {'ranges': [[e24_e96, '[10, 1000000]']]}
            elif tolerance_code == 'F' and tcr_code == '200':
                return {'ranges': [[e24_e96, '[10, 1000000]']]}
            elif tolerance_code == 'J':
                if tcr_code == '-150+400':
                    return {'ranges': [[e24, '[1, 10)']]}
                elif tcr_code == '200':
                    return {'ranges': [[e24, '[10, 1000000]']]}
        elif size_code == 'ERJPA3':
            if tolerance_code in ['D', 'F'] and tcr_code == 'K':
                return {'ranges': [[e24_e96, '[10, 1000000]']]}
            elif tolerance_code == 'J' and tcr_code == '200':
                return {'ranges': [[e24, '[1, 1500000]']]}
        elif size_code == 'ERJP06':
            if tolerance_code in ['D', 'F']:
                if tcr_code == '300':
                    return {'ranges': [[e24_e96, '[10, 33)']]}
                elif tcr_code == 'K':
                    return {'ranges': [[e24_e96, '[33, 1000000]']]}
            elif tolerance_code == 'J':
                if tcr_code == '-100+600':
                    return {'ranges': [[e24, '[1, 10)']]}
                elif tcr_code == '300':
                    return {'ranges': [[e24, '[10, 33)']]}
                elif tcr_code == '200':
                    return {'ranges': [[e24, '[33, 3300000]']]}
        elif size_code == 'ERJP08':
            if tolerance_code in ['D', 'F'] and tcr_code == 'K':
                return {'ranges': [[e24_e96, '[10, 1000000]']]}
            elif tolerance_code == 'J':
                if tcr_code == '-100+600':
                    return {'ranges': [[e24, '[1, 10)']]}
                elif tcr_code == '200':
                    return {'ranges': [[e24, '[10, 10000000]']]}
        elif size_code == 'ERJPM8' and tolerance_code == 'F' and tcr_code == 'K':
            return {'ranges': [[e24_e96, '[1000000, 10000000]']]}
        elif size_code == 'ERJP14':
            if tolerance_code in ['D', 'F'] and tcr_code == 'K':
                return {'ranges': [[e24_e96, '[10, 1000000]']]}
            elif tolerance_code == 'J':
                if tcr_code == '-100+600':
                    return {'ranges': [[e24, '[1, 10)']]}
                elif tcr_code == '200':
                    return {'ranges': [[e24, '[10, 1000000]']]}

    def packaging_data(self, size_code, power_rating_code, code):
        if code == 'X' and size_code in ['ERJPA2']:
            packaging = {
                'Packaging Code': 'X', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 10000,
                'Packaging Data': {
                    'Reel Diameter': '178.5mm', 'Reel Width': '12.5mm',
                    'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '1.75mm±0.1mm', 'Tape F': '3.50mm±0.05mm',
                    'Tape SO': '',
                    'Tape P0': '4mm±0.10mm', 'Tape P1': '2mm', 'Tape P2': '2mm±0.05mm', 'Tape D': '', 'Tape D1': '',
                    'Tape A0': '',
                    'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            return packaging
        elif code == 'V' and size_code in ['ERJP03', 'ERJPA3', 'ERJP06', 'ERJP08', 'ERJPM8']:
            packaging = {
                'Packaging Code': 'V', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 5000,
                'Packaging Data': {
                    'Reel Diameter': '178.5mm', 'Reel Width': '12.5mm',
                    'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '1.75mm±0.1mm', 'Tape F': '3.50mm±0.05mm',
                    'Tape SO': '',
                    'Tape P0': '4mm±0.10mm', 'Tape P1': '4mm', 'Tape P2': '2mm±0.05mm', 'Tape D': '', 'Tape D1': '',
                    'Tape A0': '',
                    'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            return packaging
        elif code == 'U' and size_code in ['ERJP14']:
            packaging = {
                'Packaging Code': 'U', 'Packaging Type': 'Embossed Tape / Reel', 'Packaging Qty': 5000,
                'Packaging Data': {
                    'Reel Diameter': '178.5mm', 'Reel Width': '12.5mm',
                    'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '1.75mm±0.1mm', 'Tape F': '3.50mm±0.05mm',
                    'Tape SO': '',
                    'Tape P0': '4mm±0.10mm', 'Tape P1': '4mm', 'Tape P2': '2mm±0.05mm', 'Tape D': '', 'Tape D1': '',
                    'Tape A0': '',
                    'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            return packaging

    def get_files(self, partnumber, ordernumber):
        return {}

    def pre_save_validate(self):
        assert 'ERJP06D1002#' in self.parts
        part = self.parts['ERJP06D1002#']
        assert part['manufacturer'] == 'Panasonic'
        assert part['partNumber'] == 'ERJP06D1002#'
        assert part['partType'] == 'Resistor Thick Film', part['partType']
        assert part['series']['name'] == 'ERJP', part['series']['name']
        assert part['series']['description'] == 'Anti-Surge Thick Film Chip Resistors', part['series']['description']
        parameters = part['parameters']
        assert parameters['Resistance']['value'] == "10000.00R \u00b10.5%", parameters['Resistance']
        assert parameters['TCR']['value'] == "\u00b1100ppm/\u00b0C", parameters['TCR']
        assert parameters['Rated Power']['value'] == "max. 0.5W"
        assert parameters['Working Voltage']['value'] == 'max. 400V'
        assert parameters['Overload Voltage']['value'] == 'max. 600V'
        assert part['package']['type'] == 'Chip 0805'
        assert part['symbol&footprint']['symbolName'] == 'resistor'

        assert 'ERJP06D1002V' in part['orderNumbers']
        order_number = part['orderNumbers']['ERJP06D1002V']
        assert 'V' == order_number['Packaging Code']
        assert 'Paper Tape / Reel' == order_number['Packaging Type']
        assert 5000 == order_number['Packaging Qty']
        return True
