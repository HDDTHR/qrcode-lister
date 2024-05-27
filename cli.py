import argparse
from dataclasses import dataclass
import logging
import os

from script import run_script
from utils import Args, directory


def main():
    parser = argparse.ArgumentParser(
        description="A script that reads images with qr codes in a directory, and spits out a bunch of qr text.")
    parser.add_argument(
        '-i', '--input-directory', required=True, type=directory, default=os.path.curdir, help="The directory containing the images"
    )
    parser.add_argument(
        '-v', '--verbose', help="Be verbose", action="store_const", dest="loglevel", const=logging.INFO,
    )
    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel)
    run_script(Args(input_directory=args.input_directory))


if __name__ == "__main__":
    main()
