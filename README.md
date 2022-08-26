# IMGrep

Want to find that one meme with the funny punchline?
Looking for a picture of a PowerPoint presentation on a specific topic, that you took 5 years ago?
IMGrep might help.

It works like `grep`, but for images, and with a lot less features
... and it's also much slower ... and not suuuper accurate ;D

IMGrep is built on the [Tesseract-OCR-Engine](https://github.com/tesseract-ocr/tesseract)
and uses [pytesseract](https://pypi.org/project/pytesseract/) for the bindings.

# Install

You can install imgrep from [PyPI](pypi.org) with `pip`

    pip install imgrep

# Usage

Get the usage with `imgrep -h`.

    usage: imgrep [-h] [-i] [-r] [-f] [-0] pattern file

    Grep for text in images.
    
    positional arguments:
      pattern               A Python regex, to search for.
      file                  Path of the image(s) to search through. (Or folder(s), if `--recursive' is specified).
    
    options:
      -h, --help            show this help message and exit
      -i, --ignore-case     Ignore case distinctions in patterns and input data.
      -r, --recursive       Grep through every file under a given directory.
      -f, --filenames-only  Only print the file names, not the contents. Makes no sense without `--recursive', and will be ignored if `--recursive' is not specified.
      -0, --null            Print the output seperated by null characters, this is useful for badly named files. Makes no sense without `--filenames-only', but will be done regardless, if specified!
    
    Be patient. It uses multiple cores, but this just takes a while. Searching for a specific string in my ca. 2000 image strong memes folder took about 8 minutes and 30 seconds.

# Performance

Is abysmal. You've been warned.

Neither accuracy, nor execution time are that great, but it works for my use case.
And it is still much faster, than combing through my photos one by one, when I'm looking for something specific.

# TODO

- Having `-a` and `-b` flags to include N lines of output after, and before the match would be nice.
- Also coloring the output on smart terminals would be cool.
  - That opens a whole can of worms with determining whether the terminal supports it or not.
  - Or whether the user wants color (NOCOLOR, or TERM=dumb etc.?).
