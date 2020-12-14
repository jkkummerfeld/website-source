+++
title = "The strange geometry of skip-gram with negative sampling (Mimno et al., 2017)"
date = 2017-12-12T20:15:34-05:00
draft = false

summary = "Surprisingly, word2vec (negative skipgram sampling) produces vectors that point in a consistent direction, a pattern not seen in GloVe (but also one that doesn't seem to cause a problem for downstream tasks)."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "emnlp", "word-vectors"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

It turns out that if the vectors learned by word2vec are projected into a plane they all point in the same direction.
Also, the context vectors (which are part of the algorithm, but not retained afterwards) point the other way.
When visualising with t-SNE this effect is not visible because of the way the space is warped to optimise the t-SNE objective.

This is surprising, and may seem problematic since it doesn't fit our goals for what these vectors should be capturing.
However, it doesn't seem to impact downstream tasks, for example, GloVe does not have this property, and doesn't seem to derive a great benefit from it.

## Citation

[Paper](https://www.aclweb.org/anthology/D17-1308)

```bibtex
@InProceedings{mimno-thompson:2017:EMNLP2017,
  author    = {Mimno, David  and  Thompson, Laure},
  title     = {The strange geometry of skip-gram with negative sampling},
  booktitle = {Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing},
  month     = {September},
  year      = {2017},
  address   = {Copenhagen, Denmark},
  publisher = {Association for Computational Linguistics},
  pages     = {2873--2878},
  url       = {https://www.aclweb.org/anthology/D17-1308}
}
```
