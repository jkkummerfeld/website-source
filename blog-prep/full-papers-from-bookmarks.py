#!/usr/bin/env python3

import sys

# Get the paper URLs
papers = {}
for line in sys.stdin:
    if 'www.aclweb.org' in line:
        content = line.strip()
        url = content.split()[1].split('"')[1][:-1] + ".pdf"
        name = content.split(" - ACL Anthology")[0].split(">")[-1]
        papers[name] = url

# Download the papers
import io, requests
from PyPDF2 import PdfFileReader, PdfFileMerger

for name, url in papers.items():
    key = url.split("/")[-1]
    r = requests.get(url, auth=('usrname', 'password'), verify=False,stream=True)
    assert 200 <= r.status_code < 400
    r.raw.decode_content = True

    raw_pdf = io.BytesIO(r.content)
    pdf = PdfFileReader(raw_pdf)
    merger = PdfFileMerger()
    merger.append(pdf)
    merger.write(key)

