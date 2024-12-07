from .yageo.yageo_conv_generator import YageoCapacitorConverter


def generate_yageo_capacitors(dest_dir, data_sources):
    dest_dir = dest_dir.joinpath("yageo/")
    ############################################
    parameters_npo = {'Dielectric Type': 'NP0',
                      'Working Temp Range': '-55°C ~ 125°C',
                      'Series': 'CC_NPO_BN',
                      'Series Description': 'General purpose Class 1, NP0',
                      'Partname header': 'CC',
                      'Series code': 'BN'
                      }

    def tolerance_npo(capacitance):
        if capacitance >= 10:
            return ['±1%', '±2%', '±5%', '±10%']
        else:
            return ['±0.1pF', '±0.25pF', '±0.5pF']

    cc_np0_bn_generator = YageoCapacitorConverter(data_sources + '/yageo/yageo_CC_NPO_BN.csv', parameters_npo,
                                                  tolerance_npo)
    cc_np0_bn_generator.generate(dest_dir.joinpath('yageo_CC_NPO_BN_generated.json'))
    ############################################
    parameters_y5v = {'Dielectric Type': 'Y5V',
                      'Working Temp Range': '-30°C ~ 85°C',
                      'Series': 'CC_Y5V_BB',
                      'Series Description': 'General purpose & High capacitance Class 2, Y5V',
                      'Partname header': 'CC',
                      'Series code': 'BB'}

    def tolerance_y5v(capacitance):
        return ['±20%', '-20%/+80%']

    cc_y5v_bb_generator = YageoCapacitorConverter(data_sources + '/yageo/yageo_CC_Y5V_BB.csv', parameters_y5v,
                                                  tolerance_y5v)
    cc_y5v_bb_generator.generate(dest_dir.joinpath('yageo_CC_Y5V_BB_generated.json'))
    ############################################
    parameters_np0 = {'Dielectric Type': 'NP0',
                      'Working Temp Range': '-55°C ~ 125°C',
                      'Series': 'AC_B',
                      'Series Description': 'Automotive grade',
                      'Partname header': 'AC',
                      'Series code': 'BN'}

    def tolerance_ac_b_np0(capacitance):
        if capacitance >= 10:
            return ['±1%', '±2%', '±5%']
        else:
            return ['±0.1pF', '±0.25pF', '±0.5pF']

    ac_b_np0_generator = YageoCapacitorConverter(data_sources + '/yageo/yageo_AC_B_NP0.csv', parameters_np0,
                                                 tolerance_ac_b_np0)
    ac_b_np0_generator.generate(dest_dir.joinpath('yageo_AC_B_NP0_generated.json'))

    parameters_x7r = {'Dielectric Type': 'X7R',
                      'Working Temp Range': '-55°C ~ 125°C',
                      'Series': 'AC_B',
                      'Series Description': 'Automotive grade',
                      'Partname header': 'AC',
                      'Series code': 'BB'}

    def tolerance_ac_b_x7r(capacitance):
        return ['±5%', '±10%', '±20%']

    ac_b_x7r_generator = YageoCapacitorConverter(data_sources + '/yageo/yageo_AC_B_X7R.csv', parameters_x7r,
                                                 tolerance_ac_b_x7r)
    ac_b_x7r_generator.generate(dest_dir.joinpath('yageo_AC_B_X7R_generated.json'))
