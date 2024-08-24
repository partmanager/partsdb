from capacitors.capacitor_generator_base import CapacitorGeneratorBase
from common.csv_utils import load_csv_data

voltage_code = {'6.3V': '9', '10V': '8', '16V': '4', '25V': '3', '50V': '5', '100V': '1', '200V': '2', '250V': 'A'}
tolerance = {'B': '±0.10pF', 'C': '±0.25pF', 'D': '±0.50pF', 'F': '±1%', 'G': '±2%', 'J': '±5%', 'K': '±10%', 'M': '±20%'}
packing = {'AUTO': '7" reel',
           'AUTO7411': '13" reel',
           'AUTO7210': '13" reel tape',
           '3190': '7" reel tape',
           '3191': '13" reel tape',
           'TU': '7" reel'}


thickness = {'AB': {'case size': '0201', 'thickness': '0.30mm ±0.03mm', 'Paper quantity': [15000, None]},
             'BB': {'case size': '0402', 'thickness': '0.50mm ±0.05mm', 'Paper quantity': [10000, 50000]},
             'BD': {'case size': '0402', 'thickness': '0.55mm ±0.05mm', 'Paper quantity': [10000, 50000]},
             'CF': {'case size': '0603', 'thickness': '0.80mm ±0.07mm', 'Paper quantity': [4000, 15000]},
             'CH': {'case size': '0603', 'thickness': '0.85mm ±0.07mm', 'Paper quantity': [4000, 10000]},
             'CJ': {'case size': '0603', 'thickness': '0.80mm ±0.15mm', 'Paper quantity': [10000, 50000]},
             'DM': {'case size': '0805', 'thickness': '0.70mm ±0.20mm', 'Paper quantity': [4000, 15000]},
             'DN': {'case size': '0805', 'thickness': '0.78mm ±0.10mm', 'Paper quantity': [10000, 50000]},
             'DP': {'case size': '0805', 'thickness': '0.90mm ±0.10mm', 'Paper quantity': [10000, 50000]},
             'DE': {'case size': '0805', 'thickness': '1.00mm ±0.10mm', 'Plastic quantity': [2500, 10000]},
             'DF': {'case size': '0805', 'thickness': '1.10mm ±0.10mm', 'Plastic quantity': [2500, 10000]},
             'DG': {'case size': '0805', 'thickness': '1.25mm ±0.15mm', 'Plastic quantity': [2500, 10000]},
             'DH': {'case size': '0805', 'thickness': '1.25mm ±0.20mm', 'Plastic quantity': [2500, 10000]},
             'EB': {'case size': '1206', 'thickness': '0.78mm ±0.10mm', 'Plastic quantity': [4000, 10000]},
             'EC': {'case size': '1206', 'thickness': '0.90mm ±0.10mm', 'Plastic quantity': [4000, 10000]},
             'EN': {'case size': '1206', 'thickness': '0.95mm ±0.10mm', 'Plastic quantity': [4000, 10000]},
             'ED': {'case size': '1206', 'thickness': '1.00mm ±0.10mm', 'Plastic quantity': [2500, 10000]},
             'EE': {'case size': '1206', 'thickness': '1.10mm ±0.10mm', 'Plastic quantity': [2500, 10000]},
             'EF': {'case size': '1206', 'thickness': '1.20mm ±0.15mm', 'Plastic quantity': [2500, 10000]},
             'EM': {'case size': '1206', 'thickness': '1.25mm ±0.15mm', 'Plastic quantity': [2500, 10000]},
             'EG': {'case size': '1206', 'thickness': '1.60mm ±0.15mm', 'Plastic quantity': [2000, 8000]},
             'EH': {'case size': '1206', 'thickness': '1.60mm ±0.20mm', 'Plastic quantity': [2000, 8000]},
             'FB': {'case size': '1210', 'thickness': '0.78mm ±0.10mm', 'Plastic quantity': [4000, 10000]},
             'FC': {'case size': '1210', 'thickness': '0.90mm ±0.10mm', 'Plastic quantity': [4000, 10000]},
             'FD': {'case size': '1210', 'thickness': '0.95mm ±0.10mm', 'Plastic quantity': [4000, 10000]},
             'FE': {'case size': '1210', 'thickness': '1.0mm ±0.10mm', 'Plastic quantity': [2500, 10000]},
             'FF': {'case size': '1210', 'thickness': '1.10mm ±0.10mm', 'Plastic quantity': [2500, 10000]},
             'FG': {'case size': '1210', 'thickness': '1.25mm ±0.15mm', 'Plastic quantity': [2500, 10000]},
             'FL': {'case size': '1210', 'thickness': '1.40mm ±0.15mm', 'Plastic quantity': [2000, 8000]},
             'FH': {'case size': '1210', 'thickness': '1.55mm ±0.15mm', 'Plastic quantity': [2000, 8000]},
             'FP': {'case size': '1210', 'thickness': '1.60mm ±0.20mm', 'Plastic quantity': [2000, 8000]},
             'FM': {'case size': '1210', 'thickness': '1.70mm ±0.20mm', 'Plastic quantity': [2000, 8000]},
             'FJ': {'case size': '1210', 'thickness': '1.85mm ±0.20mm', 'Plastic quantity': [2000, 8000]},
             'FK': {'case size': '1210', 'thickness': '2.10mm ±0.20mm', 'Plastic quantity': [2000, 8000]},
             'FS': {'case size': '1210', 'thickness': '2.50mm ±0.30mm', 'Plastic quantity': [1000, 4000]}}


def get_package_size(case_code, thickness_code):
    thickness_and_packaging = thickness[thickness_code]
    if case_code == '0201':
        assert (thickness_and_packaging['case size'] == case_code)
        size = {"Length": '0.60mm ±0.03mm', "Width": '0.30mm ±0.05mm', 'e': '0.15mm ±0.05mm', 's': 'min. 0.30mm'}
        size['Height'] = thickness_and_packaging['thickness']
        return size
    if case_code == '0402':
        assert (thickness_and_packaging['case size'] == case_code)
        size = {"Length": '1.00mm ±0.05mm', "Width": '0.50mm ±0.05mm', 'e': '0.30mm ±0.05mm', 's': 'min. 0.30mm'}
        size['Height'] = thickness_and_packaging['thickness']
        return size
    if case_code == '0603':
        assert (thickness_and_packaging['case size'] == case_code)
        size = {"Length": '1.60mm ±0.15mm', "Width": '0.80mm ±0.15mm', 'e': '0.35mm ±0.15mm', 's': 'min. 0.70mm'}
        size['Height'] = thickness_and_packaging['thickness']
        return size
    if case_code == '0805':
        assert (thickness_and_packaging['case size'] == case_code)
        size = {"Length": '2.00mm ±0.20mm', "Width": '1.25mm ±0.05mm', 'e': '0.50mm ±0.25mm', 's': 'min. 0.75mm'}
        size['Height'] = thickness_and_packaging['thickness']
        return size
    if case_code == '1206':
        assert (thickness_and_packaging['case size'] == case_code)
        size = {"Length": '3.20mm ±0.20mm', "Width": '1.60mm ±0.20mm', 'e': '0.50mm ±0.25mm'}
        size['Height'] = thickness_and_packaging['thickness']
        return size
    if case_code == '1210':
        assert (thickness_and_packaging['case size'] == case_code)
        size = {"Length": '3.20mm ±0.20mm', "Width": '1.50mm ±0.20mm', 'e': '0.50mm ±0.25mm'}
        size['Height'] = thickness_and_packaging['thickness']
        return size
    if case_code == '1812':
        assert (thickness_and_packaging['case size'] == case_code)
        size = {"Length": '4.50mm ±0.30mm', "Width": '3.20mm ±0.30mm', 'e': '0.60mm ±0.35mm'}
        size['Height'] = thickness_and_packaging['thickness']
        return size
    if case_code == '2220':
        assert (thickness_and_packaging['case size'] == case_code)
        size = {"Length": '5.70mm ±0.40mm', "Width": '5.00mm ±0.40mm', 'e': '0.60mm ±0.35mm'}
        size['Height'] = thickness_and_packaging['thickness']
        return size


def generate_packaging_info(thickness_code, packaging_code):
    thickness_and_packaging = thickness[thickness_code]
    seven_inch_or_13_inch = 0 if packaging_code in ["AUTO", "TU"] else 1
    if 'Paper quantity' in thickness_and_packaging:
        return {'Packaging Code': packaging_code,
                'Packaging Type': 'Paper Tape / Reel',
                'Packaging Qty': thickness_and_packaging['Paper quantity'][seven_inch_or_13_inch],
                'Packaging Data': {
                    'Reel Diameter': '7"' if seven_inch_or_13_inch == 0 else '13"'}
                }
    elif 'Plastic quantity' in thickness_and_packaging:
        return {'Packaging Code': packaging_code,
                'Packaging Type': 'Embossed Tape / Reel',
                'Packaging Qty': thickness_and_packaging['Plastic quantity'][seven_inch_or_13_inch],
                'Packaging Data': {
                    'Reel Diameter': '7"' if seven_inch_or_13_inch == 0 else '13"'}
                }


class KemetCapacitorConverter(CapacitorGeneratorBase):
    def __init__(self, src_filename, parameters):
        super().__init__(manufacturer='Kemet')
        self.capacitor_data = load_csv_data(src_filename)
        self.parameters = parameters

    def generate_capacitor(self):
        for capacitor in self.capacitor_data:
            for case_size_key in capacitor:
                if case_size_key not in ['Capacitance Code', 'Capacitance', 'Tolerance']:
                    case_height = capacitor[case_size_key]
                    if case_height:
                        case_code, voltage = case_size_key.split(' ')
                        capacitance = capacitor['Capacitance']
                        capacitance_code = capacitor['Capacitance Code']
                        dielectric_code = {'C0G': 'G', 'X7R': 'R'}[self.parameters['Dielectric Type']]
                        if len(case_height) > 2:
                            allowed_tolerance = self.parameters['tolerance exception'][case_height[-1]]
                            case_height = case_height[:-1]
                        else:
                            allowed_tolerance = ['B', 'C', 'D', 'F', 'G', 'J', 'K', 'M']
                        for capacitance_tolerance_code in capacitor['Tolerance'].split(', '): #['J', 'K', 'M']:
                            if capacitance_tolerance_code in allowed_tolerance:
                                partnumber = f"C{case_code}C{capacitance_code}{capacitance_tolerance_code}{voltage_code[voltage]}{dielectric_code}AC#"

                                parameters = {
                                    'Working Temp Range': '-55°C ~ 125°C',
                                    'Capacitance': self.encode_parameter(value=capacitance, tolerance=tolerance[capacitance_tolerance_code]),
                                    'Dielectric Type': self.parameters['Dielectric Type'],
                                    'Rated Voltage': self.encode_parameter(value='max. {}'.format(voltage))
                                    }

                                for packing_code in self.parameters['packaging codes']:
                                    ordernumber = partnumber.replace('#', packing_code)
                                    part = {
                                        'manufacturer': self.manufacturer,
                                        'partNumber': partnumber,
                                        'productionStatus': None,
                                        'markingCode': None,
                                        'partType': 'MLCC',
                                        'series': {'name': None, 'description': None},
                                        'description': None,
                                        'productUrl': None,
                                        'notes': '',
                                        'tags': [],
                                        'storageConditions': {'temperature': '-40°C ~ 105°C'},
                                        'parameters': parameters,
                                        'files': self.get_files(partnumber, ordernumber),
                                        'package': {'type': 'Chip ' + case_code,
                                                    'dimensions': get_package_size(case_code, case_height)},
                                        'symbol&footprint': {'symbolName': 'capacitor',
                                                             'pinmap': {},
                                                             'footprints': []},
                                        'orderNumbers': {ordernumber: generate_packaging_info(case_height, packing_code)}
                                    }
                                    self.validate_part(part)
                                    self.create_or_update_part(part)
