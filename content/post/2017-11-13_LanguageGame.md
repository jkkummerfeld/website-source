+++
title = "Natural Language Does Not Emerge 'Naturally' in Multi-Agent Dialog (Kottur et al., 2017)"
date = 2017-11-13T09:47:08-05:00
draft = false

summary = "Constraining the language of a dialogue agent can improve performance by encouraging the use of more compositional language."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "emnlp", "grounded-language"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

In reference games, two players communicate in a shared world with the goal of one learning what the other is referring to.
Their small scale and clear success criteria make them a convenient testbed for dialogue agents, going back decades, with recent work focusing on neural approaches.
This paper considers a simple game and constrains models in various ways to improve performance and see how their communication varies, a line of work also appearing in recent papers by Jacob Andreas ([ACL 2017](https://www.aclweb.org/anthology/P17-1022.pdf), [EMNLP 2017](https://www.aclweb.org/anthology/D17-1311.pdf)).

The game in this case is to find out two properties of an object, where there are three possible properties, each with four possible values.
Given enough flexibility, models will explicitly encode every possible structure of the world as a separate symbol, which does not generalise well.
Limiting the vocabulary to one symbol per property and one per value helps, but in this particular game there are only 3 possible questions, and over two turns of dialogue the 12 value words are sufficient to encode the space.
Limiting even further, to 4 words for values and providing each turn in isolation to the answerer does lead to some compositionality, but clearly not full compositionality as they still make errors on unseen combinations of the inputs.

It's a short paper, so they can only do so much, but some experiments I am curious about are:

- Decrease the questioner vocabulary to 2. This avoids the problem that the questioner can express the task in one step by saying what is not needed. It's still doable, by defining an order for questions, e.g. ask about attribute A vs. B first, then in the second step ask about either C or the other option from the first step. This is a little weird as symbols need to mean different things at different time steps, but would be interesting.
- Increase the number of attributes to 4. This also avoids the task expression problem, by forcing there to be compositionality on the questioner side (watching the video of the talk, someone asked this in the question time, and they didn't know).

## Citation

[Paper](https://www.aclweb.org/anthology/D17-1320)

```bibtex
@InProceedings{kottur-EtAl:2017:EMNLP2017,
  author    = {Kottur, Satwik  and  Moura, Jos\'{e}  and  Lee, Stefan  and  Batra, Dhruv},
  title     = {Natural Language Does Not Emerge 'Naturally' in Multi-Agent Dialog},
  booktitle = {Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing},
  month     = {September},
  year      = {2017},
  address   = {Copenhagen, Denmark},
  publisher = {Association for Computational Linguistics},
  pages     = {2952--2957},
  url       = {https://www.aclweb.org/anthology/D17-1320}
}
```
