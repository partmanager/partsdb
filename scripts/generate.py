import argparse
import pathlib

from capacitors_generator import generate_capacitors
from resistors_generator import generate_resistors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--prefix', type=pathlib.Path, default='../components')
    args = parser.parse_args()

    generate_capacitors(args.prefix.joinpath("capacitors"), "../script_data_sources/capacitors")
    generate_resistors(args.prefix.joinpath("resistors"), "../script_data_sources")


if __name__ == "__main__":
    main()