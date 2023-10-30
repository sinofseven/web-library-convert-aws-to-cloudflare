#!/usr/bin/env bash
set -xeuo pipefail

cp ./08_create_raw_shelf.py.json raw/shelf.json
mv raw "$TITLE_SERIES"
zip -r "$TITLE_SERIES.zip" "$TITLE_SERIES"
mv "$TITLE_SERIES" raw
