#!/usr/bin/env bash
set -xeuo pipefail

cat ./05_create_convert_command.py.txt | xargs -I{} -P ${PARALLEL_COUNT} bash -x -c "{}" 2>&1 | tee $0.log
