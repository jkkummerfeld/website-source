+++
title = "Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer (Shazeer et al., 2017)"
date = 2017-11-01T21:57:27-04:00
draft = false

summary = "Neural networks for language can be scaled up by using a form of selective computation, where a noisy single-layer model chooses among feed-forward networks (experts) that sit between LSTM layers."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "neural-network"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

Mixture of experts can be seen as an ensemble approach in which we assume that each of our models is effective under different circumstances and so we combine them by switching between which we use to make our decision.
From this perspective the idea can be applied to any set of models, but here the idea is to train (1) the expert models, (2) our method of choosing between them, and (3) a set of common model components, all at the same time.

The particular set up here is that they modify a series of LSTM layers, adding a new layer in between each pair of LSTMs.
The new layer has a set of small feed-forward networks (the experts) and an even simpler network that chooses which expert to use.
One big benefit of this is that a lot of computation can be avoided when we know some of the small feed-forward components are going to be ignored.
As a result, they can scale up to massive networks while still having reasonable runtimes.

Some key things to make this all work:

- Enough machines to train it! Also, there is a careful mixture of data and model parallelism during training.
- Some noise in the expert selection process
- A loss that directly encourages the use of multiple experts

One thing mentioned in passing is how this relates to a form of dropout (which can be viewed as training a set of overlapping experts, kind of).

## Citation

[Paper](https://openreview.net/pdf?id=B1ckMDqlg)

```bibtex
@inproceedings{45929,
	title = {Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer},
  author    = {Shazeer, Noam and Mirhoseini, Azalia and Maziarz, Krzysztof and Davis, Andy and Le, Quoc and Hinton, Geoffrey and Dean, Jeff},
	year  = {2017},
  booktitle = {ICLR},
	URL = {https://openreview.net/pdf?id=B1ckMDqlg},
}
```
