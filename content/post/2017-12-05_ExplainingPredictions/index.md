+++
title = "A causal framework for explaining the predictions of black-box sequence-to-sequence models (Alvarez-Melis et al., 2017)"
date = 2017-12-05T15:40:45-05:00
draft = false

summary = "To explain structured outputs in terms of which inputs have most impact, treat it as identifying components in a bipartite graph where weights are determined by perturbing the input and observing the impact on outputs."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "emnlp", "analysis"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

Interpreting the behaviour of statistical models in NLP has been hard for a long time, but it has gotten even harder with nonlinear models.
The simplest method so far in NLP has been to look at the attention distributions in sequence to sequence models, but that doesn't provide everything we need and obviously only applies when the model has attention.
For looking at the dynamics of the hidden state in an LSTM the Harvard NLP group built a cool [visualisation](http://lstm.seas.harvard.edu/), but what about structured outputs?

This paper considers sequence to sequence models and determines which parts of the input were most important for determining each part of the output.
The steps are:

1. Use a variational autoencoder to get perturbed versions of the input
2. Use logistic regression to get scores for every output symbol indicating how sensitive it is to variations in parts of the input
3. Create a bipartite graph between inputs and outputs, then find high weight components in the graph

These components serve as the representation of which parts of the input determine which parts of the output.
Experiments show results that match with past observations and intuitions, which is good for supporting the effectiveness of the method, but it's a shame this didn't uncover any exciting new patterns.

## Citation

[Paper](https://www.aclweb.org/anthology/D17-1042)

```bibtex
@InProceedings{alvarezmelis-jaakkola:2017:EMNLP2017,
  author    = {Alvarez-Melis, David  and  Jaakkola, Tommi},
  title     = {A causal framework for explaining the predictions of black-box sequence-to-sequence models},
  booktitle = {Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing},
  month     = {September},
  year      = {2017},
  address   = {Copenhagen, Denmark},
  publisher = {Association for Computational Linguistics},
  pages     = {412--421},
  url       = {https://www.aclweb.org/anthology/D17-1042}
}
```
