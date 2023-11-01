#!/usr/bin/env bash
set -xeuo pipefail

cp -r raw/ "$TITLE_SERIES"
cp ./08_create_raw_shelf.py.json "$TITLE_SERIES/shelf.json"
zip -r "$TITLE_SERIES.zip" "$TITLE_SERIES"
rm -rf "$TITLE_SERIES"
