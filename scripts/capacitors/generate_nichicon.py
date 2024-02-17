from .nichicon.nichicon_converter import NichiconCapacitorConverter


def generate_nichicon_capacitors(dest_dir, data_sources):
    dest_dir = dest_dir + '/nichicon'
    parameters_nichicon_ka = {'Series': 'KA',
                              'Series Description': 'For High Grade Audio Equipment, Wide Temperature Range',
                              'Endurance': '2000h'}
    ka_converter = NichiconCapacitorConverter(data_sources + '/nichicon/nichicon_KA.csv', parameters_nichicon_ka)
    ka_converter.generate(dest_dir + '/nichicon_KA_generated.json')

    parameters_nichicon_vz = {'Series': 'VZ', 'Series Description': 'Wide Temperature Range', 'Endurance': '1000h'}
    vz_generator = NichiconCapacitorConverter(data_sources + '/nichicon/nichicon_VZ.csv', parameters_nichicon_vz)
    vz_generator.generate(dest_dir + '/nichicon_VZ_generated.json')
