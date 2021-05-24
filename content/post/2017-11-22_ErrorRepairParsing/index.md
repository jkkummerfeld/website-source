+++
title = "Error-repair Dependency Parsing for Ungrammatical Texts (Sakaguchi et al., 2017)"
date = 2017-11-22T15:48:53-05:00
draft = false

summary = "Grammatical error correction can be improved by jointly parsing the sentence being corrected."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "acl", "error-correction"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

This work presents a system that parses sentences and identifies grammatical errors simultaneously.
It's an intuitive combination - a syntactic model should assign higher probability to a parse for a fixed version of a sentence than the one with a mistake.

They build on an incremental 'easy-first' dependency parsing approach.
Easy-First parsing starts with the set of words in the sentence and allows an edge to be created between any adjacent pair of words.
Once an edge is created, the child is hidden beneath its parent, so now the parent is effectively adjacent to a word slightly further away.
Then the process repeats, until there is only one word left (the root of the sentence).
In a way it is like following a dynamic program, but with only a single state that ties together multiple cells.

The change in this paper is the addition of actions that insert a word, delete a word, or alter a word.
To make it work, there are constraints to avoid cycles of repeated actions (e.g. insert-delete-insert-delete...), and on the sets of allowed word substitutions.
To produce additional training data, a tool is used to inject errors into grammatical text.
On error detection, this approach does lead to improvements, though it changes a relatively small number of the sentences.
On dependency parsing it is (unsurprisingly) worse than a baseline system on grammatical text.
It does perform better on ungrammatical text, though the data is generated using the same process as the training data, creating a bias in the system's favour.

## Citation

[Paper](https://aclanthology.org/P17-2030)

```bibtex
@InProceedings{sakaguchi-post-vandurme:2017:Short,
  author    = {Sakaguchi, Keisuke  and  Post, Matt  and  Van Durme, Benjamin},
  title     = {Error-repair Dependency Parsing for Ungrammatical Texts},
  booktitle = {Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},
  month     = {July},
  year      = {2017},
  address   = {Vancouver, Canada},
  publisher = {Association for Computational Linguistics},
  pages     = {189--195},
  url       = {https://aclanthology.org/P17-2030}
}
```
