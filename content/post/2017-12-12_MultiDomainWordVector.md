+++
title = "A Simple Regularization-based Algorithm for Learning Cross-Domain Word Embeddings (Yang et al., 2017)"
date = 2017-12-12T20:25:40-05:00
draft = false

summary = "To leverage out-of-domain data, learn multiple sets of word vectors but with a loss term that encourages them to be similar."

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

To construct word vectors from multi-domain data, use a separate vector for each domain and add a loss term to encourage them to agree.
Here the loss is an l2 norm, weighted by a factor that depends on the frequency of the words in the two domains.
The factor is the harmonic mean of the normalised frequency in each domain (so the lower frequency dominates the factor, pulling it lower).
Across a range of tasks this consistently performs better than other approaches.

## Citation

[Paper](https://www.aclweb.org/anthology/D17-1312)

```bibtex
@InProceedings{yang-lu-zheng:2017:EMNLP2017,
  author    = {Yang, Wei  and  Lu, Wei  and  Zheng, Vincent},
  title     = {A Simple Regularization-based Algorithm for Learning Cross-Domain Word Embeddings},
  booktitle = {Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing},
  month     = {September},
  year      = {2017},
  address   = {Copenhagen, Denmark},
  publisher = {Association for Computational Linguistics},
  pages     = {2898--2904},
  url       = {https://www.aclweb.org/anthology/D17-1312}
}
```
