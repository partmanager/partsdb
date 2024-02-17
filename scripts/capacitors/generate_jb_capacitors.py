from .jb_capacitors.jb_capacitors_converter import JBCapacitorsConverter


def generate_jb_capacitors(dest_dir, data_sources):
    dest_dir = dest_dir + "/jb_capacitors/"
    parameters = {'Series': 'JRG', 'RippleCurrentCondFreq': '100kHz', 'RippleCurrentCondTemp': '105°C'}
    jb_capacitors_converter = JBCapacitorsConverter(data_sources + '/jb capacitors/jb_capacitors_JRG.csv', parameters)
    jb_capacitors_converter.generate(dest_dir + '/jb_capacitors_JRG_generated.json')
