from os.path import splitext, basename
from sys import argv
import json


with open('01_get_all_files.sh.txt') as f:
    result = set([splitext(x)[1] for x in f.read().split("\n") if x])

with open(f'{basename(argv[0])}.json', 'w') as f:
    json.dump(sorted(result), f, indent=2, ensure_ascii=False)

