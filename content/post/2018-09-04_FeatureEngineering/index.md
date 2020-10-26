+++
title = "Evaluating the Utility of Hand-crafted Features in Sequence Labelling (Minghao Wu et al., 2018)"
date = 2018-09-04T10:37:23-04:00
draft = false

summary = "A common argument in favour of neural networks is that they do not require 'feature engineering', manually defining functions that produce useful representations of the input data (e.g. a function..."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

A common argument in favour of neural networks is that they do not require 'feature engineering', manually defining functions that produce useful representations of the input data (e.g. a function that checks if a word is in a list of cities and returns 1 or 0).
This paper argues that there is in fact still value in such functions.

The task is named entity recognition and the model is a CRF with a bidirectional LSTM using character and word embeddings.
The functions in this case are (1) part of speech tags, (2) word shapes, and (3) gazetteers.
Importantly, as well as receiving these as inputs, the model has to predict them as outputs (in both cases using predictions, not gold values).
The improvement on the test set is substantial, ~0.8 F1.
Ablation indicates that POS tags and word shape are particularly important, and having both the input and output is important.
Interestingly, the shift on the development set is more marginal, ~0.3 F1, and the ablation doesn't show as clear trends.

Overall, my takeaway is that these kinds of features (which are not very hard to define) are worth the effort.
However, there are a few more values I would have liked to see:

- Multi-task learning (they kind of get at this with one ablation, but it is on non-gold output)
- Cross-validation results (given the difference between dev and test)
- ELMo (the paper argues that it is orthogonal, which is reasonable, but I'm still curious)

## Citation

[Paper](https://arxiv.org/abs/1808.09075)

```bibtex
@InProceedings{Wu:2018:EMNLP,
  author    = {Wu, Minghao and Liu, Fei and Cohn, Trevor},
  title     = {Evaluating the Utility of Hand-crafted Features in Sequence Labelling},
  booktitle = {EMNLP},
  year      = {2018},
  url       = {https://arxiv.org/abs/1808.09075},
}
```
