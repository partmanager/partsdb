from .vishay.vishay_MMU_MMA_MMB_generator import VishayMMU


def generate_vishay_resistors(dest_dir, data_sources):
    dest_dir = dest_dir.joinpath("vishay")

    mmu = VishayMMU()
    mmu.generate_resistor(dest_dir.joinpath('vishay_mmu_generated.json'))
