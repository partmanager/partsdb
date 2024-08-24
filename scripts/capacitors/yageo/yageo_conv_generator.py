from capacitors.common import *
from capacitors.yageo.yageo_common import *

from capacitors.capacitor_generator_base import CapacitorGeneratorBase
from common.csv_utils import load_csv_data


def package_dimensions(size, capacitance):
    dimensions = {
        '0201': {'Length': '0.60mm ±0.03', 'Width': '0.30mm ±0.03', 'e': '0.15mm ±0.05'},
        '0402': {'Length': '1.00mm ±0.05', 'Width': '0.50mm ±0.05', 'e': '0.25mm ±0.05'},
        '0603': {'Length': '1.60mm ±0.10', 'Width': '0.80mm ±0.10', 'e': '0.40mm ±0.20'},
        '0805_lc': {'Length': '2.00mm ±0.10', 'Width': '1.25mm ±0.10', 'e': '0.50mm ±0.25'},
        '0805_hc': {'Length': '2.00mm ±0.20', 'Width': '1.25mm ±0.20', 'e': '0.50mm ±0.25'},
        '1206_lc': {'Length': '3.20mm ±0.15', 'Width': '1.60mm ±0.15', 'e': '0.50mm ±0.25'},
        '1206_hc': {'Length': '3.20mm ±0.30', 'Width': '1.60mm ±0.20', 'e': '0.50mm ±0.25'},
        '1210': {'Length': '3.20mm ±0.20', 'Width': '2.50mm ±0.20', 'e': '0.50mm ±0.25'},
        '1812': {'Length': '4.50mm ±0.20', 'Width': '3.20mm ±0.20', 'e': '0.50mm ±0.25'}}
    if size in ['0805', '1206']:
        if capacitance < 1000000:
            return dimensions[size + '_lc']
        else:
            return dimensions[size + '_hc']
    return dimensions[size]


def allowed_packing_styles(size, thickness):
    thickness = thickness.replace(' ', '')
    if size == '0201' and thickness == '0.3±0.03':
        return {'R': 15000, 'P': 50000}
    if size == '0402' and thickness == '0.5±0.05':
        return {'R': 10000, 'P': 50000, 'C': 50000}
    if size == '0603':
        if thickness == '0.8±0.1':
            return {'R': 4000, 'P': 15000, 'C': 15000}
    if size == '0805':
        if thickness == '0.6±0.1':
            return {'R': 4000, 'P': 20000, 'C': 10000}
        if thickness == '0.85±0.1':
            return {'R': 4000, 'P': 15000, 'C': 8000}
        if thickness == '1.25±0.2':
            return {'K': 3000, 'F': 10000, 'C': 5000}
    if size == '1206':
        if thickness == '0.6±0.1':
            return {'R': 4000, 'P': 20000}
        if thickness == '0.85±0.1':
            return {'R': 4000, 'P': 15000}
        if thickness in ['1.00±0.10', '1.00±0.1'] or thickness == '1.15±0.1':
            return {'K': 3000, 'F': 10000}
        if thickness == '1.25±0.2':
            return {'K': 3000, 'F': 10000}
        if thickness == '1.6+-0.15':
            return {'K': 2500, 'F': 10000}
        if thickness == '1.60±0.2' or thickness == '1.6±0.2':
            return {'K': 2000, 'F': 10000}
        if thickness == '1.60±0.30':
            return {'K': 2000, 'F': 10000}
    if size == '1210':
        if thickness == '0.6' or thickness == '0.7':
            return {'K': 4000, 'F': 15000}
        if thickness in ['0.85±0.10', '0.85±0.1']:
            return {'K': 4000, 'F': 10000}
        if thickness == '1.15±0.10':
            return {'K': 3000, 'F': 10000}
        if thickness == '1.25±0.2':
            return {'K': 3000}
        if thickness == '1.5±0.1':
            return {'K': 2000}
        if thickness == '1.50±0.30':
            return {'K': 2000}
        if thickness == '1.60±0.2' or thickness == '1.6±0.2' or thickness == '1.90±0.20':
            return {'K': 2000}
        if thickness == '2.0±0.2':
            return {'K': 2000}
        if thickness in ['2.50±0.20', '2.5±0.2']:
            return {'K': 1000}
        if thickness == '2.5 ±0.30':
            return {'K': 1000}
    if size == '1808':
        if thickness == '1.15':
            return {'K': 3000}
        elif thickness == '1.25':
            return {'K': 3000}
        else:
            return {'K': 2000}
    if size == '1812':
        if thickness == '0.6' or thickness == '0.85':
            return {'K': 2000}
        elif thickness == '2.5':
            return {'K': 500}
        else:
            return {'K': 1000}


class YageoCapacitorConverter(CapacitorGeneratorBase):
    def __init__(self, src_filename, parameters, allowed_tolerance):
        super().__init__(manufacturer='Yageo')
        self.capacitor_data = load_csv_data(src_filename)
        self.parameters = parameters
        self.allowed_tolerance = allowed_tolerance

    def generate_capacitor(self):
        series_code = self.parameters['Series code']
        for capacitor in self.capacitor_data:
            capacitance = str_capacitance_to_capacitance_in_pF(capacitor['Capacitance'])
            for case_and_voltage in capacitor:
                if case_and_voltage.strip() not in ["Capacitance", "12NC"]:
                    thickness = capacitor[case_and_voltage].strip()
                    if thickness:
                        for tolerance in self.allowed_tolerance(capacitance):
                            case, voltage = decode_case_and_volgage(case_and_voltage)
                            partnumber = f"{self.parameters['Partname header']}{case}{tolerance_code[tolerance]}#{self.parameters['Dielectric Type']}{voltage_code[str(voltage)]}{series_code}{capacitance_to_str(capacitance).replace('.', 'R')}"
                            package_dimension = package_dimensions(case, capacitance)

                            parameters = {
                                'Working Temp Range': self.parameters['Working Temp Range'],
                                'Capacitance': self.encode_parameter(value=str(capacitance) + 'pF ',
                                                                     tolerance=tolerance),
                                'Dielectric Type': self.parameters['Dielectric Type'],
                                'Rated Voltage': self.encode_parameter(value='max. {}V'.format(voltage))
                            }

                            order_codes = allowed_packing_styles(case, thickness)
                            for order_code in order_codes:
                                ordernumber = partnumber.replace('#', order_code)

                                part = {
                                    'manufacturer': self.manufacturer,
                                    'partNumber': partnumber,
                                    'productionStatus': None,
                                    'markingCode': None,
                                    'partType': 'MLCC',
                                    'series': {'name': self.parameters['Series'],
                                               'description': self.parameters['Series Description']},
                                    'description': None,
                                    'productUrl': None,
                                    'notes': None,
                                    'tags': [],
                                    'storageConditions': {'temperature': '-40°C ~ 105°C'},
                                    'parameters': parameters,
                                    'files': self.get_files(partnumber, ordernumber),
                                    'package': {'type': 'Chip ' + case,
                                                'dimensions': {**package_dimension, 'Height': thickness}
                                                },
                                    'symbol&footprint': {'symbolName': 'capacitor_nonpolar',
                                                         'pinmap': {},
                                                         'footprints': []},
                                    'orderNumbers': {ordernumber: {**packing_style[order_code],
                                                                   'Packaging Qty': order_codes[order_code]
                                                                   }
                                                     }
                                }
                                self.validate_part(part)
                                self.create_or_update_part(part)
