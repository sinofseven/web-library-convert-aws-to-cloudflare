#!/usr/bin/env bash
set -xeuo pipefail

rm -rf ./raw/
rm -rf ./converted/
rm -f *.txt
rm -f *.json
rm -f *.log

echo "[]" > 07_titles.json
