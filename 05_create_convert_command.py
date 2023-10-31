#!/usr/bin/env python3

from os import makedirs
from os.path import basename, dirname, splitext
from sys import argv

with open("04_get_image_list.sh.txt") as f:
    files = [x for x in f.read().split("\n") if x]


dir_names = set()
result = []

for path in files:
    base = splitext(path[4:])[0]
    output = f"converted/{base}.avif"
    dir_names.add(dirname(output))
    result.append(f"cavif -f -s 1 -Q 75 -o {output} {path}")

for path in dir_names:
    makedirs(path, exist_ok=True)

with open(f"{basename(argv[0])}.txt", "w") as f:
    f.write("\n".join(result))
