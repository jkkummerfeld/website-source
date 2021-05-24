+++
title = "Mr. Bennet, his coachman, and the Archbishop walk into a bar but only one of them gets recognized: On The Difficulty of Detecting Characters in Literary Texts (Vala et al., 2015)"
date = 2017-11-06T20:16:28-05:00
draft = false

summary = "With some tweaks (domain-specific heuristics), coreference systems can be used to identify the set of characters in a novel, which in turn can be used to do large scale tests of hypotheses from literary analysis."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "emnlp"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

NLP tools seem like a natural fit for literary analysis, but the domain shift from news text is large enough to degrade performance to the point where tools are not useful.
Here the specific question is how many characters are there in novels?
NER + coreference would seem to be enough, but an off-the-shelf system fares poorly (and I doubt improvements in the last few years would change that story).

The solution is to craft a kind of coreference system focused on getting all of the characters, but not necessarily every mention.
The most interesting new piece is how they identify rare characters: identify arguments of verbs that usually take people.
With this tool in hand they analyse patterns of character use over time to test hypotheses from literary analysis.

Another key piece of this work was a tool to annotate a collection of books with character occurrences.
CHARLES, their tool, is built on top of [brat](http://brat.nlplab.org/), adding features to help multiple annotators coordinate labels (specifically handling the case of new character identification, which modifies the set of linkable entities).

Finally, they released the character lists identified for the novels considered ([here](https://aclanthology.org/attachments/D/D15/D15-1088.Attachment.zip)).
It would be interesting to modify a coreference resolution system to process these books, taking advantage of that information!

## Citation

[Paper](https://aclanthology.org/D15-1088)

[Annotation Tool Paper](http://www.lrec-conf.org/proceedings/lrec2016/pdf/1130_Paper.pdf)

```bibtex
@InProceedings{vala-EtAl:2015:EMNLP,
  author    = {Vala, Hardik  and  Jurgens, David  and  Piper, Andrew  and  Ruths, Derek},
  title     = {Mr. Bennet, his coachman, and the Archbishop walk into a bar but only one of them gets recognized: On The Difficulty of Detecting Characters in Literary Texts},
  booktitle = {Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing},
  month     = {September},
  year      = {2015},
  address   = {Lisbon, Portugal},
  publisher = {Association for Computational Linguistics},
  pages     = {769--774},
  url       = {https://aclanthology.org/D15-1088}
}
```
