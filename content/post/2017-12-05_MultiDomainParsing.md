+++
title = "Neural Semantic Parsing over Multiple Knowledge-bases (Herzig et al., 2017)"
date = 2017-12-05T19:28:33-05:00
draft = false

summary = "Training a single parser on multiple domains can improve performance, and sharing more parameters (encoder and decoder as opposed to just one) seems to help more."

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

One reason learning for semantic parsing is difficult is that the datasets are generally small.
Assuming some words behave similarly across domains, multi-domain parsing should improve performance by providing more data, which is essentially what this paper finds.
They consider several configurations, all based on a sequence to sequence LSTM:

1. Train a separate model for every domain.
2. Use a single model. They do three subtypes here, (a) that's it, (b) add an LSTM input at each step with the domain, (c) give the domain as a token at the start.
3. Use a single encoder model, but a different decoder for each domain.
4. Combine (1) and (3), have two encoders, one that is domain specific and one that is trained on all domains.

The results show that any of these does better than (1), with (2b) doing best.
There also seems to be three sections: first the independent models (1), then the models with multiple decoders (3 and 4), then the variants of (2).
A natural thing to try would be a version of (4) with a single decoder, in which case the thing that is shared is the output space representation (rather than the input space as the motivation for the paper frames it).
From the paper it sounds like very little hyperparameter tuning was tried, which is a shame because it makes it less clear how definitive the results are.

## Citation

[Paper](http://aclweb.org/anthology/P17-2098)

```bibtex
@InProceedings{herzig-berant:2017:Short,
  author    = {Herzig, Jonathan  and  Berant, Jonathan},
  title     = {Neural Semantic Parsing over Multiple Knowledge-bases},
  booktitle = {Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},
  month     = {July},
  year      = {2017},
  address   = {Vancouver, Canada},
  publisher = {Association for Computational Linguistics},
  pages     = {623--628},
  url       = {http://aclweb.org/anthology/P17-2098}
}
```
