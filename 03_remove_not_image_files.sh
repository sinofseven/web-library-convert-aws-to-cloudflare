#!/usr/bin/env bash
set -xeuo pipefail

find raw -type f | grep -v "jpg$" | grep -v "png$" | xargs rm -rf 
find raw -type f -name ".*" | xargs rm -rf

