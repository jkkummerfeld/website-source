+++
title = "Dynamic Evaluation of Neural Sequence Models (Krause et al., 2017)"
date = 2017-10-30T13:28:30-04:00
draft = false

summary = "Language model perplexity can be reduced by maintaining a separate model that is updated during application of the model, allowing adaptation to short-term patterns in the text."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "arxiv", "neural-network", "language-model"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

Language is bursty, with rare words occurring in clumps, the simplest example being an unusual name that occurs a lot in one news article, but not in other articles.
This paper is about how to modify a neural language model to take this into consideration, by adapting the model over time.

The main idea is to have one model of overall word usage (global) and a separate model that shifts over time to take into consideration the current text (local).
The idea of adapting is not new (as the paper makes clear), but the key here is an update rule that is a modified form of RMSprop, combining the local and global models.
It also seems like performing the updates after every 5 words is important, balancing frequency with informativeness (though no ablation of frequencies is presented).
Conveniently, this is orthogonal to many other ideas and can essentially be stapled on top of a range of sequential architectures, consistently leading to improvements.

One question left open is how this would work in generation.
The paper describes how it could be applied and could provide improvements, but it also seems likely to risk the repetitive outputs seen in many dialogue systems.


## Citation

[ArXiv Paper](https://arxiv.org/pdf/1709.07432.pdf)

```bibtex
@ARTICLE{2017arXiv170907432K,
   author = {{Krause}, B. and {Kahembwe}, E. and {Murray}, I. and {Renals}, S.},
    title = "{Dynamic Evaluation of Neural Sequence Models}",
  journal = {ArXiv e-prints},
archivePrefix = "arXiv",
   eprint = {1709.07432},
 keywords = {Computer Science - Neural and Evolutionary Computing, Computer Science - Computation and Language},
     year = 2017,
    month = sep,
   adsurl = {http://adsabs.harvard.edu/abs/2017arXiv170907432K},
  adsnote = {Provided by the SAO/NASA Astrophysics Data System},
}
```
