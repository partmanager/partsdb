from .tt_electronics.tt_electronics import TTResistorGenerator


def generate_tt_resistors(dest_dir, data_sources):
    dest_dir = dest_dir + "/tt_electronics/"
    tt_generator = TTResistorGenerator()
    tt_generator.generate_resistor(dest_dir + 'pcf_standard_generated.json')
