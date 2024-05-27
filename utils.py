from dataclasses import dataclass
import os
import argparse

from typing import AnyStr, Tuple

@dataclass
class Args:
    input_directory: str

def directory(raw_path) -> AnyStr:
    if not os.path.isdir(raw_path):
        raise argparse.ArgumentTypeError(
            '"{}" is not an existing directory'.format(raw_path))
    return os.path.abspath(raw_path)


def get_absolute_filepaths(directory_path):
    walk_object = next(os.walk(directory_path), (directory_path, [], []))
    directory, _, files = walk_object
    return [os.path.join(directory, filename) for filename in files]
