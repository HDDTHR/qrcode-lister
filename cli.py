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
        '-o', '--output-file', required=True, type=argparse.FileType("w"), default=os.path.curdir, help="The directory containing the images"
    )
    parser.add_argument(
        '-v', '--verbose', help="Be verbose", action="store_const", dest="loglevel", const=logging.INFO, default=logging.CRITICAL
    )
    args_obj = parser.parse_args()
    args = Args(input_directory=args_obj.input_directory,
                loglevel=args_obj.loglevel, output_file=args_obj.output_file)

    print(args)

    run_script(args)


if __name__ == "__main__":
    main()
