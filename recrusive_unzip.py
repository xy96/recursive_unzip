#!/usr/bin/env python3
import os
import glob
import logging
from pathlib import Path
from shutil import unpack_archive
from pathlib import Path



directory=input(r"Enter directory: ")
zip_files = Path(directory).rglob("*.zip")
while True:
    try:
        path = next(zip_files)
    except StopIteration:
        break # no more files
    except PermissionError:
        logging.exception("permission error")
    else:
         extract_dir = path.with_name(path.stem)
         unpack_archive(str(path), str(extract_dir), 'zip')



for f in Path(directory).rglob('*.zip'):
    try:
        f.unlink()
    except OSError as e:
        print("Error: %s : %s" % (f, e.strerror))
