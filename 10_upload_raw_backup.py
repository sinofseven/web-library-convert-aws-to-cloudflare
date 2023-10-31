#!/usr/bin/env python3

from os import getenv

import boto3

title = getenv("TITLE_SERIES")
with open(f"{title}.zip", "rb") as f:
    resp = boto3.client("s3").put_object(
        Bucket="raw.backup.library.luciferous.link",
        Key=f"{title}.zip",
        Body=f,
        StorageClass="GLACIER",
    )
print(resp)
