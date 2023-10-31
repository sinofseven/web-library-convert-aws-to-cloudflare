#!/usr/bin/env python3

import boto3
from os import getenv


title = getenv("TITLE_SERIES")
with open(f"{title}.zip", "rb") as f:
    resp = boto3.client("s3").put_object(
        Bucket="raw.backup.library.luciferous.link",
        Key=f"{title}.zip",
        Body=f,
        StorageClass="GLACIER"
    )
print(resp)

