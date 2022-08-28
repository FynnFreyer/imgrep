import argparse
import re

from typing import List, Union
from pathlib import Path
from multiprocessing import Pool
from os import cpu_count
from functools import partial

import PIL
import pytesseract


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description='Grep for text in images.')

    parser.add_argument('pattern', type=str, help='A Python regex, to search for.')
    parser.add_argument('file', type=Path,
                        help='Path of the image(s) to search through. (Or folder(s), if `--recursive\' is specified).')

    parser.add_argument('-i', '--ignore-case', action='store_true',
                        help='Ignore case distinctions in patterns and input data.')
    parser.add_argument('-r', '--recursive', action='store_true',
                        help='Grep through every file under a given directory.')
    parser.add_argument('-f', '--filenames-only', action='store_true',
                        help='Only print the file names, not the contents.\nMakes no sense without `--recursive\', '
                             'and will be ignored if `--recursive\' is not specified.')
    parser.add_argument('-0', '--null', action='store_true',
                        help='Print the output seperated by null characters, this is useful for badly named files.\n'
                             'Makes no sense without `--filenames-only\', but will be done regardless, if specified!')

    parser.epilog = f'Be patient. It uses multiple cores, but this just takes a while.\n' \
                    f'Searching for a specific string in my ca. 2000 image strong memes folder took about 8 minutes ' \
                    f'and 30 seconds.'

    return parser.parse_args() if argv is None else parser.parse_args(argv)


def imgrep(image: Union[str, Path], needle: re.Pattern) -> List[str]:
    try:
        img = PIL.Image.open(image)
    except PIL.UnidentifiedImageError:
        # skip in case PIL cannot decode the file for any reason
        # (e.g. it might not even be image data)
        return []

    haystack: str = pytesseract.image_to_string(img)
    return [line for line in haystack.splitlines() if needle.search(line)]


def recurse(directory: Union[str, Path], needle: re.Pattern, filenames_only: bool = False) -> List[str]:
    output = []

    dir = Path(directory)
    files = [file for file in dir.glob('**/*') if file.is_file()]

    with Pool() as pool:
        f = partial(imgrep, needle=needle)
        chunksize = len(files) // (cpu_count() * 4) if len(files) > (cpu_count() * 4) else 1
        results = pool.map(f, files, chunksize=chunksize)

    for hits, file in zip(results, files):
        if hits:
            if filenames_only:
                output.append(str(file))
            else:
                output.append(f'{file}: ')
                output.extend(hits)

    return output


def main(argv=None):
    args = parse_args() if argv is None else parse_args(argv)

    recursive: bool = args.recursive
    ignore_case: bool = args.ignore_case
    filenames_only: bool = args.filenames_only
    null: bool = args.null

    pattern: re.Pattern = re.compile(args.pattern) if not ignore_case else re.compile(args.pattern, re.IGNORECASE)
    file: Path = args.file

    if not file.exists():
        print(f'{file} does not exist, or is not readable.')
        exit(1)

    if not recursive:
        if file.is_dir():
            print(f'{file} is a directory. Try again with `--recursive\'')
            exit(2)
    else:
        if not file.is_dir():
            print(f'{file} is not a directory. Try again without `--recursive\'')
            exit(3)

    output = imgrep(file, pattern) if not recursive else recurse(file, pattern, filenames_only)

    for line in output:
        print(line, end='\0' if null else '\n')

    exit(0)

if __name__ == '__main__':
    main()
