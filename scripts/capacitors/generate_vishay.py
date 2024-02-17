from .vishay.vishay_capacitor_converter import VishayCapacitorConverter


def generate_vishay_capacitors(dest_dir, data_sources):
    dest_dir = dest_dir + '/vishay'
    #vj_w1bc_generator = VishayCapacitorConverter('data_sources/vishay/vishay_capacitor_VJ_W1BC.csv', {})
    #vj_w1bc_generator.generate('../parts/capacitors/vishay/vishay_VJ_W1BC_generated.json')

    vj_w1bc_x7r_generator = VishayCapacitorConverter(data_sources + '/vishay/vishay_capacitor_VJ_W1BC_X7R.csv',
                                                     {'Dielectric Type': 'X7R',
                                                      'tolerance exception': {'¹': ['K', 'M']},
                                                      'packaging codes': ['AUTO']})
    vj_w1bc_x7r_generator.generate(dest_dir + '/vishay_VJ_W1BC_X7R_generated.json')
