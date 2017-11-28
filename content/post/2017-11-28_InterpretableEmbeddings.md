+++
title = "SPINE: SParse Interpretable Neural Embeddings (Subramanian et al., 2017)"
date = 2017-11-28T16:51:09-05:00
draft = false

summary = "By introducing a new loss that encourages sparsity, an auto-encoder can be used to go from existing word vectors to new ones that are sparser and more interpretable, though the impact on downstream tasks is mixed."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "arxiv", "word-vectors"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

The first step in almost any neural network model for language is to look up a vector for each token in the input.
These vectors express relations between the words, but it is difficult to know exactly what relations.
This work proposes a way to modify a vector space of words to have more interpretable dimensions.

The core idea is actually more general, it is a new loss that encourages sparsity in an auto-encoder.
In this case the model is very simple: input a word vector, apply an affine transformation and a pointwise nonlinearity, producing a hidden vector, then apply another affine transformation to get the output.
The loss is a combination of how well the input and output match (reconstruction loss), plus a function that is minimised when the average activation is below a threshold (average sparsity loss), and the new idea, a loss that is minimised at either 0 or 1 for each hidden value.
To get the hidden values to be bounded between 1 and 0, the nonlinearity used is a modified ReLU that stops increasing after reaching 1.
After training, the hidden values become the new word vectors.

To evaluate interpretability they consider the top 4 words along each dimension, add a random word, and ask a person to identify the odd word out.
Using either word2vec or GloVe as the initial vectors and applying this method, the results shown a dramatic difference (~25 vs. ~70).
On downstream tasks the story is more mixed.
With 1,000 dimensional vectors, there is usually an improvement for GloVe, but not for word2vec, and the differences are generally small.
Apparently going up to 2,000 further improves interpretability scores, but 'at a severe cost' for the downstream tasks.
Going the other direction, to 500, hurts interpretability, and probably doesn't improve downstream performance (it isn't mentioned).

I would be curious to see if taking these new word vectors and applying them to a downstream task like parsing, but letting them change during training, would be beneficial.
The general idea of a sparse auto-encoder also seems cool and may have other applications.

## Citation

[ArXiv Paper](https://arxiv.org/abs/1711.08792)

```bibtex
@ARTICLE{2017arXiv171108792S,
  author        = {{Subramanian}, A. and {Pruthi}, D. and {Jhamtani}, H. and {Berg-Kirkpatrick}, T. and {Hovy}, E.},
  title         = {SPINE: SParse Interpretable Neural Embeddings},
  journal       = {ArXiv e-prints},
  archivePrefix = {arXiv},
  eprint        = {1711.08792},
  primaryClass  = {cs.CL},
  year          = {2017},
  month         = {November},
  url           = {https://arxiv.org/abs/1711.08792},
}
```
