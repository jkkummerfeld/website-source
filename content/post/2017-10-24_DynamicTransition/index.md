+++
title = "Dynamic Programming Algorithms for Transition-Based Dependency Parsers (Kuhlmann et al., ACL 2011)"
date = 2017-10-24T13:06:04-04:00
draft = false

summary = "Transition based algorithms can be transformed into dynamic programs by defining sequences of actions that correspond to the same overall transformation."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "syntax"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

This paper from 2011 explores the relationship between transition based parsing and dynamic programming based parsing.
They show how to convert common dependency parsing systems (Arc-Standard and Arc-Eager) into dynamic programs, and how doing the reverse on a dynamic program gives the Arc-Hybrid approach (which has since been used in many places, and is now joined by additional systems like Arc-Swift).

The benefit of this transformation is that we can find exact answers without massive beams.
The drawback is that the feature set is restricted.
This paper is theoretical, so it doesn't give a direct measure of this tradeoff, though [follow up work](http://www.anthology.aclweb.org/D/D13/D13-1071.pdf) shows that avoiding search errors is indeed beneficial.

With all of the positive results using neural networks for multi-task learning, one thought this work leads to is whether we could treat different inference methods as different tasks.
In other words, have a single model encoding the input, then have multiple inference algorithms with different extensions of that model, all trained simultaneously.
The variation in available context for the different algorithms may force generality in the core representation shared across them.

## Citation

[Paper](http://aclweb.org/anthology/P/P11/P11-1068.pdf)

```bibtex
@InProceedings{kuhlmann-gomezrodriguez-satta:2011:ACL-HLT2011,
  author    = {Kuhlmann, Marco  and  G\'{o}mez-Rodr\'{i}guez, Carlos  and  Satta, Giorgio},
  title     = {Dynamic Programming Algorithms for Transition-Based Dependency Parsers},
  booktitle = {Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies},
  month     = {June},
  year      = {2011},
  address   = {Portland, Oregon, USA},
  publisher = {Association for Computational Linguistics},
  pages     = {673--682},
  url       = {http://www.aclweb.org/anthology/P11-1068}
}
```
