![GitHub Workflow Status](https://img.shields.io/github/workflow/status/FynnFreyer/imgrep/PyPI)
![License](https://img.shields.io/pypi/l/imgrep)
![PyPI](https://img.shields.io/pypi/v/imgrep)

# IMGrep

Want to find that one meme with the funny punchline?
Looking for a picture of a PowerPoint presentation on a specific topic, that you took 5 years ago?
IMGrep might help.

It works like `grep`, but for images, and with a lot less features ... and it's also much slower ... and not suuuper
accurate, especially for handwriting, or weird fonts ;D

`imgrep` is built on top of [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract) and uses
the [pytesseract](https://pypi.org/project/pytesseract/) bindings to interface with it.

# Install

You can install `imgrep` from [PyPI](https://pypi.org/project/imgrep/) with `pip`

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
- Fuzzy search
- Preprocessing/Indexing (?)
    - Pro:
        - Done once it heavily improves performance for subsequent searches
    - Con:
        - I don't want to put garbage files into the users' filesystem.  
          This could be done, by having only one index file in XDG_CONFIG_HOME (or similar on other OS's),
          that gets uninstalled with imgrep in the end.
    - Conclusion:
        - Probably worth it

# Alternatives

I noticed, that there is a similar project, even with the same name [imgrep](https://github.com/keeferrourke/imgrep).
I am in no way affiliated with that project, but it looks cool, and it might actually suit you better, because they
already allow for preprocessing and fuzzy search, both of which are not currently implemented in this project.

OTOH for a quick and dirty one off job the convenience of `python -m pip install imgrep; imgrep -rif pattern images` is
probably nice.
