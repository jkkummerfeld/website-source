+++
title = "Paper Reading"
date = 2020-01-26T16:09:06-05:00
draft = false

summary = ""

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["advice"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

Keeping up with research is hard.
I've previously made lists of papers I wanted to read, and then only gotten to a small fraction of them.
Simply resolving to read more papers hasn't worked for me.

I'm trying out a new approach.
The goals are (1) read less of more papers, and (2) read more papers that are critical to my work.
Sometimes just the introduction or abstract is enough for me to get the ideas I need from the paper.
I want to read the whole paper only if it is really relevant to me.
The problem is that it's easy to start reading a paper and then just keep going, and without a process it can be easy to put off starting at all.
This is the process I've worked out (in Chrome) to do this:

1. Go through the proceedings for a conference on the ACL anthology and read every title. Based on the title, decide whether to read the abstract. Based on the abstract, decide whether to read the introduction, in which case open the paper in a tab.
2. Bookmark all tabs. Either use `Shift+Command+D` or Bookmarks -> Bookmark All Tabs.
3. Export the folder of bookmarks to a file. To do this, go to `chrome://bookmarks`, select the new folder then use the menu on the far right of the blue bar to select Export Bookmarks.
4. Run the code below, with `bookmarks_DATE.html` as input (note, requires `PyPDF2`). This produces a pdf with only the introduction of each paper (approximately).
5. Read through the pdf this produces and flag the papers to read all of.

This will hopefully produce a list that is short enough to read all of (and maybe write blog posts about!).

```Python
# Get the paper URLs
import sys
papers = {}
for line in sys.stdin:
    if 'www.aclweb.org' in line:
        content = line.strip()
        url = content.split()[1].split('"')[1][:-1] + ".pdf"
        name = content.split(" - ACL Anthology")[0].split(">")[-1]
        papers[name] = url

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
        # Try to find the start of section 2
        if part.startswith('2') and len(part) > 1:
            if part[1] in string.ascii_letters:
                done = True
    if not done:
        page1 = pdf.getPage(1)
        start = page1.extractText().split('\n')[0]
        # Try to find the start of section 2
        if start.startswith('2') and len(start) > 1:
            if start[1] in string.ascii_letters:
                done = True
        if not done:
            pdf_writer.addPage(page1)

with open('example.pdf', 'wb') as out:
    pdf_writer.write(out)
```
