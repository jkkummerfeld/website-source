+++
title = "Shift-Reduce Constituency Parsing with Dynamic Programming and POS Tag Lattice (Mi and Huang, 2015)"
date = 2017-10-25T14:44:13-04:00
draft = false

summary = "An implementation of the transition-parsing as a dynamic program idea, leading to fast parsing and strong performance."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "syntax"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

This paper is a follow-up to yesterday's, where the approach is implemented and evaluated on English and Chinese, with very strong results.
The novel contribution is the idea of introducing alternating steps in the dynamic program to do unary steps (not a novel idea in general, but novel in its application to the dynamic programming version of shift-reduce parsing).

What I found interesting here were the clear benefits of the dynamic program (DP) version.
One way of viewing this is that the DP gives a more intelligent type of beam, avoiding the issue where the beam is filled with minor variations on a theme.
Results are given for various beam sizes in both approaches, but it would be interesting to see a graph where the x-axis is number of items built.
I suspect in that situation, the gap would be smaller.
On speed, there is the nice theoretical bound of $O(n)$ for this approach, but that obscures a grammar constant related to the item structure.

## Citation

[Paper](https://aclanthology.org/N15-1108)

```bibtex
@InProceedings{mi-huang:2015:NAACL-HLT,
  author    = {Mi, Haitao  and  Huang, Liang},
  title     = {Shift-Reduce Constituency Parsing with Dynamic Programming and POS Tag Lattice},
  booktitle = {Proceedings of the 2015 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},
  month     = {May--June},
  year      = {2015},
  address   = {Denver, Colorado},
  publisher = {Association for Computational Linguistics},
  pages     = {1030--1035},
  url       = {https://aclanthology.org/N15-1108}
}
```
