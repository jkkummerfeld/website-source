+++
title = "Sequence Effects in Crowdsourced Annotations (Mathur et al., 2017)"
date = 2017-12-08T19:49:09-05:00
draft = false

summary = "Annotator sequence bias, where the label for one item affects the label for the next, occurs across a range of datasets. Avoid it by separately randomise the order of items for each annotator."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "emnlp", "annotation"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

Getting high quality annotations from crowdsourcing requires careful design.
This paper looks at how one annotation a worker does can influence their next annotation, for example:

- When scoring translations, a good example may make the next one look worse in comparison
- For labeling tasks, we may expect a long sequence of the same label to be rare (the gambler's fallacy)

To investigate this they fit a linear model with inputs (previous label, gold label, random noise) and see what the coefficients are.
Across multiple tasks, there is a non-zero correlation with the previous label.
Interestingly, there also seems to be a learning effect for good workers, where over time they become calibrated and show less sequence bias.
Fortunately, there is a simple solution - for each worker, give every annotator their documents in a different random order!
With that change, averaging over annotations should avoid this bias.

## Citation

[Paper](https://aclanthology.org/D17-1306)

```bibtex
@InProceedings{mathur-baldwin-cohn:2017:EMNLP2017,
  author    = {Mathur, Nitika  and  Baldwin, Timothy  and  Cohn, Trevor},
  title     = {Sequence Effects in Crowdsourced Annotations},
  booktitle = {Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing},
  month     = {September},
  year      = {2017},
  address   = {Copenhagen, Denmark},
  publisher = {Association for Computational Linguistics},
  pages     = {2860--2865},
  url       = {https://aclanthology.org/D17-1306}
}
```
