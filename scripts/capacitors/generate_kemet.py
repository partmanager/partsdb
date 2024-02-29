from .kemet.kemet_capacitor_converter import KemetCapacitorConverter


def generate_kemet_capacitors(dest_dir, data_sources):
    dest_dir = dest_dir + '/kemet/'
    kemet_capacitor_converter = KemetCapacitorConverter(data_sources + '/kemet/kemet_C0G.csv',
                                                        {'Dielectric Type': 'C0G',
                                                         'tolerance exception': {'¹': ['D', 'J', 'K', 'M'],
                                                                                 '²': ['J', 'K', 'M']},
                                                         'packaging codes': ['TU']})
    kemet_capacitor_converter.generate(dest_dir + 'kemet_C0G_generated.json')

    kemet_capacitor_converter = KemetCapacitorConverter(data_sources + '/kemet/kemet_X7R.csv',
                                                        {'Dielectric Type': 'X7R',
                                                         'tolerance exception': {'¹': ['D', 'J', 'K', 'M'],
                                                                                 '²': ['J', 'K', 'M']},
                                                         'packaging codes': ['TU']})
    kemet_capacitor_converter.generate(dest_dir + 'kemet_X7R_generated.json')
