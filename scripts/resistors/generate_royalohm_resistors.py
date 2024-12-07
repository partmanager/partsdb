from .royalohm.royalohm_CFR_generator import RoyalohmCFRGenerator
from .royalohm.royalohm_CQ_generator import RoyalohmCQGenerator
from .royalohm.royalohm_HP_generator import RoyalohmHPGenerator
from .royalohm.royalohm_KNP_generator import RoyalohmKNPGenerator
from .royalohm.royalohm_MF_generator import RoyalohmMFGenerator
from .royalohm.royalohm_PRW_generator import RoyalohmPRWGenerator
from .royalohm.royalohm_general_purpose_thick_film_chip_resistor_generator import RoyalohmGeneralPurposeThickFilmChipResistorGenerator


def generate_royalohm_resistors(dest_dir, data_sources):
    dest_dir = dest_dir.joinpath("royalohm")

    cfr = RoyalohmCFRGenerator()
    cfr.generate_resistor(dest_dir.joinpath('royalohm_cfr_generated.json'))

    cq = RoyalohmCQGenerator()
    cq.generate_resistor(dest_dir.joinpath('royalohm_cq_generated.json'))

    hp = RoyalohmHPGenerator()
    hp.generate_resistor(dest_dir.joinpath('royalohm_hp_generated.json'))

    knp = RoyalohmKNPGenerator()
    knp.generate_resistor(dest_dir.joinpath('royalohm_knp_generated.json'))

    mf = RoyalohmMFGenerator()
    mf.generate_resistor(dest_dir.joinpath('royalohm_mf_generated.json'))

    pwr = RoyalohmPRWGenerator()
    pwr.generate_resistor(dest_dir.joinpath('royalohm_prw_generated.json'))

    generic = RoyalohmGeneralPurposeThickFilmChipResistorGenerator()
    generic.generate_resistor(dest_dir.joinpath('royalohm_general_purpose_thick_film_chip_resistor_generated.json'))
