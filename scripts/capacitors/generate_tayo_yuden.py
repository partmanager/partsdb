from .taiyo_yuden.taiyo_yuden import TaiyoYudenCapacitorConverter


def generate_taiyo_yuden_capacitors(dest_dir, data_sources):
    dest_dir = dest_dir.joinpath('taiyo yuden')
    umk_generator = TaiyoYudenCapacitorConverter(data_sources + '/taiyo yuden/taiyo_yuden_UMK.csv')
    umk_generator.generate(dest_dir.joinpath('taiyo_yuden_UMK_generated.json'))