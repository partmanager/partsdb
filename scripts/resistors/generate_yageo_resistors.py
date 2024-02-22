from .yageo.yageo_AC_generator import YageoACResistorGenerator
from .yageo.yageo_MF0_generator import YageoMF0ResistorGenerator
from .yageo.yageo_RC_L_generator import YageoRCLResistorGenerator
from .yageo.yageo_RT_L_generator import YageoRTLResistorGenerator


def generate_yageo_resistors(dest_dir, data_sources):
    dest_dir = dest_dir + "/yageo/"

    ac = YageoACResistorGenerator()
    ac.generate_resistor(dest_dir + 'yageo_ac_generated.json')

    mf0 = YageoMF0ResistorGenerator()
    mf0.generate_resistor(dest_dir + 'yageo_mf_generated.json')

    rc_l = YageoRCLResistorGenerator()
    rc_l.generate_resistor(dest_dir + 'yageo_rc_l_generated.json')

    rt_l = YageoRTLResistorGenerator()
    rt_l.generate_resistor(dest_dir + 'yageo_rt_l_generated.json')
