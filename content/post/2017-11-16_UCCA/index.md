+++
title = "A Transition-Based Directed Acyclic Graph Parser for UCCA (Hershcovich et al., 2017)"
date = 2017-11-16T17:24:59-05:00
draft = false

summary = "Parsing performance on the semantic structures of UCCA can be boosted by using a transition system that combines ideas from discontinuous and constituent transition systems, covering the full space of structures."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "acl", "syntax"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

Over the last few years interest has risen in parsing structures other than projective trees (including my dissertation!).
There are now a range of different datasets with annotations for syntactic and/or semantic structure that include discontinuous constituents and graphs.
This paper looks at UCCA, a proposed formalism that is somewhat similar to SRL, with non-terminals included to allow for easier handling of cases like coordination.

The parser is a transition based, with a transition system that covers all the structural phenomena in UCCA: non-terminals, discontinuous spans, and multiple parents.
The key to consistent multiple parents is distinguishing the addition of edges that are the primary parent (to prevent multiple being added).
To get discontinuity, they use a swap operation.
They consider a range of models, including both linear and neural network examples.

The dataset is relatively small, with only 4,268 training sentences, and the task is hard, so performance is relatively low (50 - 75 for primary edges, 20-50 for others).
The neural model consistently beats the linear ones, particularly for the non-primary edges.
Comparing to other standard parsers (retrained on this data), the ability to generate the full space of structures makes a big difference.

It would be interesting to see coverage of this data for one-endpoint crossing graphs.
If it is high, then my own parser could be applied fairly directly!

## Citation

[Paper](https://aclanthology.org/P17-1104)

```bibtex
@InProceedings{hershcovich-abend-rappoport:2017:Long,
  author    = {Hershcovich, Daniel  and  Abend, Omri  and  Rappoport, Ari},
  title     = {A Transition-Based Directed Acyclic Graph Parser for UCCA},
  booktitle = {Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  month     = {July},
  year      = {2017},
  address   = {Vancouver, Canada},
  publisher = {Association for Computational Linguistics},
  pages     = {1127--1138},
  url       = {https://aclanthology.org/P17-1104}
}
```
