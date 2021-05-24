+++
title = "Revisiting Selectional Preferences for Coreference Resolution (Heinzerling et al., 2017)"
date = 2017-12-06T19:05:20-05:00
draft = false

summary = "It seems intuitive that a coreference system could benefit from information about what nouns a verb selects for, but experiments on explicitly adding a representation of it to a neural system does not lead to gains, implying it is already learning them or they are not useful."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "emnlp", "coreference"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

Selectional preferences in this context are about how some verbs are more likely to take certain types of arguments (e.g. people laugh, computers do not).
Many papers have added features or structures to coreference systems aiming to get at this kind of information.
This paper presents another way of doing it and experiments that probe how useful it is (punchline: not very).

Their approach is to parse a large amount of text, producing noun-verb pairs.
They learn vector representations of the relations and try to create a single space containing both entities and relations (e.g. Michigan gets a vector, as does attended@dobj).
The goal is that entities end up in locations similar to the locations of relations they are selected for.

For results, first it seems like these vector similarities do not correlate particularly strongly with being coreferent.
It could be that the feature on its own isn't enough, or this representation might not be capturing it effectively.
Adding this to the Stanford coreference system they are able to get slight gains, though the improvement might not be statistically significant.

I'm not sure exactly how to do this, but it would be neat if a vector at some point of the model could be modified to remove any correlation with these features, and see what that does to performance.
If performance remains high, then this actually is an uninformative feature, but if it drops that suggests the model is already learning it.

## Citation

[Paper](https://aclanthology.org/D17-1138)

```bibtex
@InProceedings{heinzerling-moosavi-strube:2017:EMNLP2017,
  author    = {Heinzerling, Benjamin  and  Moosavi, Nafise Sadat  and  Strube, Michael},
  title     = {Revisiting Selectional Preferences for Coreference Resolution},
  booktitle = {Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing},
  month     = {September},
  year      = {2017},
  address   = {Copenhagen, Denmark},
  publisher = {Association for Computational Linguistics},
  pages     = {1332--1339},
  url       = {https://aclanthology.org/D17-1138}
}
```
