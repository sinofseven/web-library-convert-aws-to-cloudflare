#!/usr/bin/env bash
set -xeuo pipefail

cp -v ./13_update_production_shelf.py.json "$PRODUCTION_SHELF_PATH" 2>&1 | tee $0.log

