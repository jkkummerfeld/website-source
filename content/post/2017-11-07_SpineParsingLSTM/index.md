+++
title = "Arc-Standard Spinal Parsing with Stack-LSTMs (Ballesteros et al., 2017)"
date = 2017-11-07T20:42:45-05:00
draft = false

summary = "Stack-LSTM models for dependency parsing can be adapted to constituency parsing by considering spinal version of the parse and adding a single 'create-node' operation to the transition-based parsing scheme, giving an elegant algorithm and competitive results."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "iwpt", "syntax"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

This paper brings together work on neural dependency parsing with the idea of non-terminal spines as a way to represent constituency structure.
Within the transition parsing inference process they can naturally fit the generation of a new spines by gradually building up the spine, which makes for a very elegant inference process.

Surprisingly, it doesn't seem to matter what head choices are used to generate the spines (they tried leftmost word, rightmost word, and two standard schemes).
This contrasts with my own observations that the choice of head had a big impact (0.5 F) on accuracy.
I think the incrementally-built spines are the key difference.
Decisions about higher up in the spine are difficult to make when looking at a single word, but with the incremental construction there is information about a larger context.

## Citation

[Paper](https://aclanthology.org/W17-6316)

```bibtex
@InProceedings{ballesteros-carreras:2017:IWPT,
  author    = {Ballesteros, Miguel  and  Carreras, Xavier},
  title     = {Arc-Standard Spinal Parsing with Stack-LSTMs},
  booktitle = {Proceedings of the 15th International Conference on Parsing Technologies},
  month     = {September},
  year      = {2017},
  address   = {Pisa, Italy},
  publisher = {Association for Computational Linguistics},
  pages     = {115--121},
  url       = {https://aclanthology.org/W17-6316}
}
```
