#!/usr/bin/env python3

import json
from os import getenv, listdir
from os.path import basename
from sys import argv
from typing import List

with open("07_titles.json") as f:
    titles: List[str] = json.load(f)

id_series = getenv("DIR_SERIES")
dir_raw = "converted"

series = {"id": id_series, "name": getenv("TITLE_SERIES"), "books": []}

all_books = []

for dir_individual, title in zip(sorted(listdir(f"{dir_raw}/{id_series}")), titles):
    book = {
        "id": f"{id_series}_{dir_individual}",
        "name": title,
        "pages": [
            f"{id_series}/{dir_individual}/{x}"
            for x in sorted(listdir(f"{dir_raw}/{id_series}/{dir_individual}"))
        ],
    }
    all_books.append(book)
    series["books"].append(book["id"])

shelf = {"series": [series], "books": all_books}

with open(f"{basename(argv[0])}.json", "w") as f:
    json.dump(shelf, f, indent=2, ensure_ascii=False)
