import json
from os import getenv
from os.path import basename
from sys import argv

with open(getenv("PRODUCTION_SHELF_PATH")) as f:
    shelf_prd = json.load(f)

with open("11_create_converted_shelf.py.json") as f:
    shelf_converted = json.load(f)

for k in ["series", "books"]:
    shelf_prd[k] += shelf_converted[k]

with open(f"{basename(argv[0])}.json", "w") as f:
    json.dump(shelf_prd, f, ensure_ascii=False)
