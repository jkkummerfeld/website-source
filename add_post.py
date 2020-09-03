#!/usr/bin/env python3

import argparse
import datetime
import subprocess
import sys

import bibtexparser

# Arguments
parser = argparse.ArgumentParser(description='Add a new post, starting from bibtex.')
parser.add_argument('name', help='New post name')
parser.add_argument('bib', help='Bibtex, either a URL or a file path as file:///path/to/file')
args = parser.parse_args()

# Determine name based on current date
now = datetime.datetime.now()
name = "{}-{:>02}-{:>02}_{}".format(now.year, now.month, now.day, args.name)

# Get bib file from online
assert(args.bib.startswith("file:///") or args.bib.startswith("http"))
raw_bibtex = subprocess.run(["curl", "-s", args.bib], stdout=subprocess.PIPE, encoding="ascii").stdout.strip()
bib_data = bibtexparser.loads(raw_bibtex)
current = bib_data.get_entry_list()[0]
title = current['title']
year = current['year']
author = current['author'].split(',')[0]
url = ""
if 'link' in current:
    url = current['link']

# Make 
filename = subprocess.run(["hugo", "new", "post/"+ name +"/index.md"], stdout=subprocess.PIPE, encoding="ascii").stdout
filename = filename.strip().split()[0]
content = open(filename).readlines()

for pos, line in enumerate(content):
    if line.startswith("title = "):
        content[pos] = 'title = "{} ({} et al., {})"\n'.format(title, author, year)

content.append("\n\n## Citation")
content.append("\n\n[Paper]({})".format(url))
content.append("\n\n```bibtex")
content.append("\n"+ raw_bibtex)
content.append("\n```")

out = open(filename, 'w')
print(''.join(content), file=out)
out.close()

print(filename)
