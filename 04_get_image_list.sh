#!/usr/bin/env bash
set -xeuo pipefail

find raw -type f | sort > $0.txt

