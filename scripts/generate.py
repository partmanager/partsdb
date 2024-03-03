from capacitors_generator import generate_capacitors
from resistors_generator import generate_resistors

generate_capacitors("../components/capacitors", "../script_data_sources/capacitors")
generate_resistors("../components/resistors", "../script_data_sources")
