#!/usr/bin/env bash
set -xeuo pipefail

rm -rf ./raw/
rm -rf ./converted/
rm -f *.txt
rm -f *.json
rm -f *.log
rm -f *.zip

echo "[]" > 07_titles.json
