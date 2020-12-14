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
        print(name)

# Download the papers
import io, requests
PDFs = {}
for name, url in papers.items():
    r = requests.get(url, auth=('usrname', 'password'), verify=False,stream=True)
    assert 200 <= r.status_code < 400
    r.raw.decode_content = True
    PDFs[name] = io.BytesIO(r.content)

# Get the Introductions
from PyPDF2 import PdfFileReader, PdfFileWriter
import string
pdf_writer = PdfFileWriter()
for name, raw_pdf in PDFs.items():
    pdf = PdfFileReader(raw_pdf)
    page0 = pdf.getPage(0)
    pdf_writer.addPage(page0)
    text = page0.extractText().split('\n')
    done = False
    for part in text:
        if part.startswith('2') and len(part) > 1:
            if part[1] in string.ascii_letters:
                done = True
    if not done:
        page1 = pdf.getPage(1)
        start = page1.extractText().split('\n')[0]
        if start.startswith('2') and len(start) > 1:
            if start[1] in string.ascii_letters:
                done = True
        if not done:
            pdf_writer.addPage(page1)

with open('example.pdf', 'wb') as out:
    pdf_writer.write(out)

