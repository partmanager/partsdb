from common.value_encoder import digits_multiplier_encoder
from resistors.resistor_generator_base import ResistorGeneratorBase


class RoyalohmResistorBase(ResistorGeneratorBase):
    def get_package_dimension(self, size_code, power_rating_code):
        size = self.size_code[size_code]
        return self.dimensions[size]

    def get_part_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type,
                        special_feature):
        if tolerance_code in self.short_value_code_tolerance_list:
            resistance_str = '0' + digits_multiplier_encoder(value, digits=2, multiplier_str=self.multiplier_str)
        else:
            resistance_str = digits_multiplier_encoder(value, multiplier_str=self.multiplier_str)
        partnumber = f"{size_code}{power_rating_code}{tolerance_code}{resistance_str}##"
        if special_feature:
            partnumber = partnumber + str(special_feature)
        assert len(partnumber) == 14, partnumber
        return partnumber

    def get_order_number(self, size_code, value, tolerance_code, tcr_code, power_rating_code, packing_type,
                         special_feature):
        if tolerance_code in self.short_value_code_tolerance_list:
            resistance_str = '0' + digits_multiplier_encoder(value, digits=2, multiplier_str=self.multiplier_str)
        else:
            resistance_str = digits_multiplier_encoder(value, multiplier_str=self.multiplier_str)
        ordernumber = f"{size_code}{power_rating_code}{tolerance_code}{resistance_str}{packing_type}{special_feature}"
        assert len(ordernumber) == 14
        return ordernumber

    def packaging_data(self, size_code, power_rating_code, packing_type_code):
        size = self.size_code[size_code]
        if size == '0201' and packing_type_code == 'TC':
            packaging = {
                'Packaging Code': 'TC', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 10000,
                'Packaging Data': {
                    'Reel Diameter': '', 'Reel Width': '',
                    'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '', 'Tape F': '', 'Tape SO': '',
                    'Tape P0': '', 'Tape P1': '', 'Tape P2': '', 'Tape D': '', 'Tape D1': '', 'Tape A0': '',
                    'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            return packaging
        elif size == '0402' and packing_type_code == 'TC':
            packaging = {
                'Packaging Code': 'TC', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 10000,
                'Packaging Data': {
                    'Reel Diameter': '', 'Reel Width': '',
                    'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '', 'Tape F': '', 'Tape SO': '',
                    'Tape P0': '', 'Tape P1': '', 'Tape P2': '', 'Tape D': '', 'Tape D1': '', 'Tape A0': '',
                    'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            return packaging
        elif size == '0603' and packing_type_code == 'T5':
            packaging = {
                'Packaging Code': 'T5', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 5000,
                'Packaging Data': {
                    'Reel Diameter': '', 'Reel Width': '',
                    'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '', 'Tape F': '', 'Tape SO': '',
                    'Tape P0': '', 'Tape P1': '', 'Tape P2': '', 'Tape D': '', 'Tape D1': '', 'Tape A0': '',
                    'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            return packaging
        elif size == '0805' and packing_type_code == 'T5':
            packaging = {
                'Packaging Code': 'T5', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 5000,
                'Packaging Data': {
                    'Reel Diameter': '', 'Reel Width': '',
                    'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '', 'Tape F': '', 'Tape SO': '',
                    'Tape P0': '', 'Tape P1': '', 'Tape P2': '', 'Tape D': '', 'Tape D1': '', 'Tape A0': '',
                    'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            return packaging
        elif size == '1206' and packing_type_code == 'T5':
            packaging = {
                'Packaging Code': 'T5', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 5000,
                'Packaging Data': {
                    'Reel Diameter': '', 'Reel Width': '',
                    'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '', 'Tape F': '', 'Tape SO': '',
                    'Tape P0': '', 'Tape P1': '', 'Tape P2': '', 'Tape D': '', 'Tape D1': '', 'Tape A0': '',
                    'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            return packaging
        elif size == '1210' and packing_type_code == 'T5':
            packaging = {
                'Packaging Code': 'T5', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 5000,
                'Packaging Data': {
                    'Reel Diameter': '', 'Reel Width': '',
                    'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '', 'Tape F': '', 'Tape SO': '',
                    'Tape P0': '', 'Tape P1': '', 'Tape P2': '', 'Tape D': '', 'Tape D1': '', 'Tape A0': '',
                    'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            return packaging
        elif size == '2010' and packing_type_code == 'T4':
            packaging = {
                'Packaging Code': 'T4', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 4000,
                'Packaging Data': {
                    'Reel Diameter': '', 'Reel Width': '',
                    'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '', 'Tape F': '', 'Tape SO': '',
                    'Tape P0': '', 'Tape P1': '', 'Tape P2': '', 'Tape D': '', 'Tape D1': '', 'Tape A0': '',
                    'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            return packaging
        elif size == '2512' and packing_type_code == 'T4':
            packaging = {
                'Packaging Code': 'T4', 'Packaging Type': 'Paper Tape / Reel', 'Packaging Qty': 4000,
                'Packaging Data': {
                    'Reel Diameter': '', 'Reel Width': '',
                    'Tape Pin 1 Quadrant': 'Q1', 'Tape W': '8mm', 'Tape E': '', 'Tape F': '', 'Tape SO': '',
                    'Tape P0': '', 'Tape P1': '', 'Tape P2': '', 'Tape D': '', 'Tape D1': '', 'Tape A0': '',
                    'Tape A1': '', 'Tape B0': '', 'Tape B1': '', 'Tape T': '', 'Tape K': ''}}
            return packaging
