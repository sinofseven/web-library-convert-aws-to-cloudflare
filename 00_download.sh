#!/usr/bin/env bash

set -xeuo pipefail

aws s3 cp --recursive s3://web-library-copy-temp/${DIR_SERIES} raw/${DIR_SERIES} 2>&1 | tee $0.log
