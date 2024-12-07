from .murata.murata_converter import MurataCapacitorConverter


def generate_murata_capacitors(dest_dir, data_sources):
    dest_dir = dest_dir + '/murata/'

    grm_parameters = {'series': 'GRM'}
    #grm_converter = MurataCapacitorConverter(data_sources + "/murata/GRM/0402/grm_1.csv", grm_parameters)
    #grm_converter.generate(dest_dir + 'murata_grm_1_generated.json')
    grm_converter = MurataCapacitorConverter(data_sources + "/murata/GRM/0402/grm_2.csv", grm_parameters)
    grm_converter.generate(dest_dir + 'murata_grm_1_generated.json')
    grm_converter = MurataCapacitorConverter(data_sources + "/murata/GRM/0402/grm_3.csv", grm_parameters)
    grm_converter.generate(dest_dir + 'murata_grm_2_generated.json')
    grm_converter = MurataCapacitorConverter(data_sources + "/murata/GRM/0402/grm_4.csv", grm_parameters)
    grm_converter.generate(dest_dir + 'murata_grm_3_generated.json')
    grm_converter = MurataCapacitorConverter(data_sources + "/murata/GRM/0402/grm_5.csv", grm_parameters)
    grm_converter.generate(dest_dir + 'murata_grm_4_generated.json')
    grm_converter = MurataCapacitorConverter(data_sources + "/murata/GRM/0402/grm_6.csv", grm_parameters)
    grm_converter.generate(dest_dir + 'murata_grm_5_generated.json')
    #grm_converter = MurataCapacitorConverter(data_sources + "/murata/GRM/0402/grm_7.csv", grm_parameters)
    #grm_converter.generate(dest_dir + 'murata_grm_6_generated.json')

    grm_converter = MurataCapacitorConverter(data_sources + "/murata/GRM/0805/pref_20230826055946.csv", grm_parameters)
    grm_converter.generate(dest_dir + 'murata_grm_6_generated.json')
    grm_converter = MurataCapacitorConverter(data_sources + "/murata/GRM/0805/pref_20230826060028.csv", grm_parameters)
    grm_converter.generate(dest_dir + 'murata_grm_7_generated.json')
    grm_converter = MurataCapacitorConverter(data_sources + "/murata/GRM/0805/pref_20230826060129.csv", grm_parameters)
    grm_converter.generate(dest_dir + 'murata_grm_8_generated.json')
    grm_converter = MurataCapacitorConverter(data_sources + "/murata/GRM/0805/pref_20230826060254.csv", grm_parameters)
    grm_converter.generate(dest_dir + 'murata_grm_9_generated.json')

    grt_parameters = {'series': 'GRT'}
    grt_converter = MurataCapacitorConverter(data_sources + "/murata/GRT.csv", grt_parameters)
    grt_converter.generate(dest_dir + 'murata_grt_generated.json')
