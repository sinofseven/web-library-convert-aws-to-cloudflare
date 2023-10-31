#!/usr/bin/env bash
set -xeuo pipefail

aws s3 --profile cloudflare-r2 cp --recursive converted/ s3://web-library-v3-data/
