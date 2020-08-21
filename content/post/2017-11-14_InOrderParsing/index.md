+++
title = "In-Order Transition-based Constituent Parsing (Liu et al., 2017)"
date = 2017-11-14T14:10:39-05:00
draft = false

summary = "Using in-order traversal for transition based parsing (put the non-terminal on the stack after its first child but before the rest) is consistently better than pre-order / top-down or post-order / bottom-up traversal."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "tacl", "syntax"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

Shift-reduce constituency parsing incrementally builds the parse either bottom-up or top-down.
The difference is whether a non-terminal is placed on the stack before or after the words that it spans.
This corresponds to two forms of depth-first traversal of the tree: pre-order or post-order.

The idea in this paper is to do an in-order traversal, which in a binary tree means traversing the left child of a node, then the node, then its right child.
In this context that means putting the non-terminal symbol on the stack after the first word it spans, but before the rest.
The model follows the stack-LSTM approach of Dyer et al., with non-terminals always fed into the LSTM first during composition, regardless of where it was inserted into the stack.

This leads to a 0.5 F1 gain on standard parsing metrics, with no hyperparameter tuning.
High-level error analysis seems to show it just does better everywhere.
I wonder whether further gains could be realised with a label-sensitive ordering.

## Citation

[Paper](https://www.transacl.org/ojs/index.php/tacl/article/view/1199)

```bibtex
@article{TACL1199,
	author = {Liu, Jiangming  and Zhang, Yue },
	title = {In-Order Transition-based Constituent Parsing},
	journal = {Transactions of the Association for Computational Linguistics},
	volume = {5},
	year = {2017},
	issn = {2307-387X},
	url = {https://www.transacl.org/ojs/index.php/tacl/article/view/1199},
	pages = {413--424}
}
```
