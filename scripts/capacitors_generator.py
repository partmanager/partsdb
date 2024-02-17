from capacitors.generate_aishi import generate_aishi_capacitors
from capacitors.generate_jb_capacitors import generate_jb_capacitors
from capacitors.generate_kemet import generate_kemet_capacitors
from capacitors.generate_nichicon import generate_nichicon_capacitors
from capacitors.generate_tayo_yuden import generate_taiyo_yuden_capacitors
from capacitors.generate_vishay import generate_vishay_capacitors
from capacitors.generate_yageo import generate_yageo_capacitors


def generate_capacitors(dest_dir, data_sources):
    generate_yageo_capacitors(dest_dir, data_sources + "/capacitors/")
    generate_jb_capacitors(dest_dir, data_sources + "/capacitors/")
    generate_kemet_capacitors(dest_dir, data_sources + "/capacitors/")
    generate_nichicon_capacitors(dest_dir, data_sources + "/capacitors/")
    generate_vishay_capacitors(dest_dir, data_sources + "/capacitors/")
    generate_aishi_capacitors(dest_dir, data_sources + "/capacitors/")
    generate_taiyo_yuden_capacitors(dest_dir, data_sources + "/capacitors/")
