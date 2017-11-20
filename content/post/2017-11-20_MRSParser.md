+++
title = "Robust Incremental Neural Semantic Graph Parsing (Buys et al., 2017)"
date = 2017-11-20T10:13:12-05:00
draft = false

summary = "A neural transition based parser with actions to create non-local links can perform well on Minimal Recursion Semantics parsing."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "acl", "semantic-parsing"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

Like the [UCCA parser]({{< ref "2017-11-16_UCCA.md" >}}), this paper explores a transition-based neural model for semantic parsing, but for Minimal Recursion Semantics instead of Universal Conceptual Cognitive Annotation.
Comparing MRS and UCCA, every word gets a non-terminal symbol in MRS, plus additional non-terminals for phenomena like quantification, while UCCA only introduces them for special cases like linking to a coordination.
Both have discontinuous graph structures, creating a challenge for most parsers.

The UCCA and MRS parsers extend the basic shift-reduce transitions in different ways.
Here, crossing edges can be added with a transition that forms edges between the front of the buffer and a word anywhere in the stack, while the UCCA parser used swapping and a additional reduce actions for graph edges.
The models are similar, both using a form of stack-RNN, but with different structures (partly as a result of the different transition schemes).
The results in this case are not state-of-the-art, though this task has received more attention, and the data is slightly biased (the parser that does better, ACE, is based on the grammar that was used to determine which sentences to include).
However, the system can also be applied to AMR, and does fairly well, better than other neural AMR parsers at the time (and more recent ideas for improvements are large orthogonal).

## Citation

[Paper](http://aclweb.org/anthology/P17-1112)

```bibtex
@InProceedings{buys-blunsom:2017:Long,
  author    = {Buys, Jan  and  Blunsom, Phil},
  title     = {Robust Incremental Neural Semantic Graph Parsing},
  booktitle = {Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  month     = {July},
  year      = {2017},
  address   = {Vancouver, Canada},
  publisher = {Association for Computational Linguistics},
  pages     = {1215--1226},
  url       = {http://aclweb.org/anthology/P17-1112}
}
```
