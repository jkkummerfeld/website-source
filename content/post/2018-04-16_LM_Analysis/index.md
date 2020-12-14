+++
title = "An Analysis of Neural Language Modeling at Multiple Scales (Merity et al., 2018)"
date = 2018-04-16T20:55:22-04:00
draft = false

summary = "Assigning a probability distribution over the next word or character in a sequence (language modeling) is a useful component of many systems..."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "language-model", "arxiv"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

Assigning a probability distribution over the next word or character in a sequence (language modeling) is a useful component of many systems, such as speech recognition and translation.
Recently neural networks have come to dominate in performance, with a range of clever innovations in network structure.
This paper is not about new models, but rather explores the current evaluation and how well carefully tuned baseline models can do.

The key observations for me were:

- There are issues with the PTB dataset for character-level evaluation - it removes all punctuation, makes numbers 'N', and removes rare words (i.e. it is a character-level version of the token-level task).
Given that the original Penn Treebank exists, I would have been interested to see a comparison with the PTB without any simplification.
The other dataset, enwik8, makes sense as a testing ground for compression algorithms, but is a little odd for modeling language, since it is the first 100 million bytes of a Wikipedia XML dump.
The paper does have another dataset, WikiText, which sounds good, but then there is no character-level evaluation!
- The LSTM is able to achieve ~SotA results for character-level modeling.
The key seems to be careful design of the softmax that produces the final probability distribution:
(1) rare words are clustered and represented by a single value in the distribution calculation, and
(2) word vectors are shared between input and output.
- Dropout matters more than the network design, and multiple forms of dropout should be tuned jointly.
This comes from analysis of a set of models trained with random variation in hyperparameters.

## Citation

[Paper](https://arxiv.org/abs/1803.08240)

```bibtex
@Article{2018arXiv180308240M,
   author = {{Merity}, S. and {Shirish Keskar}, N. and {Socher}, R.},
    title = {An Analysis of Neural Language Modeling at Multiple Scales},
  journal = {ArXiv e-prints},
     year = {2018},
      url = {https://arxiv.org/abs/1803.08240},
}
```
