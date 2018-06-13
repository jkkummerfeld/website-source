+++
title = "Extending a Parser to Distant Domains Using a Few Dozen Partially Annotated Examples (Vidur Joshi et al., 2018)"
date = 2018-06-12T20:33:00-04:00
draft = false

summary = "Virtually all systems trained using data have trouble when applied to datasets that differ even slightly - even switching from Wall Street..."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper"]
categories = ["acl", "domain-adaptation", "syntax"]

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

Virtually all systems trained using data have trouble when applied to datasets that differ even slightly - even switching from Wall Street Journal text to New York Times text can hurt parsing performance slightly.
Extensive work has explored how to adapt to new domains (including [one of my own](http://jkk.name/publication/acl10adapt/)), but generally these approaches only made up a fraction of the gap in performance.

This paper shows two interesting new approaches to this issue:

- Use [ELMo](https://allennlp.org/elmo), a type of word representation trained on massive amounts of text.
- Train a span-based parser with partial annotations.

The first is straightforward, and further demonstrates the effectiveness of ELMo.
To give a sense of how much this helps, the Charniak parser goes from 92 on the WSJ to 85 on the Brown corpus, while this model goes from 94 to 90.
The second idea takes advantage of [a recent parsing model](https://aclanthology.info/papers/P17-1076/p17-1076) with a simple approach:

1. Independently assign a score to every span of a sentence, indicating whether it is part of the parse.
2. Find the maximum scoring set of spans using a dynamic program.

The structure of the scoring step allows for a convenient form of partial annotations.
Simply label the tricky spans in a sentence (e.g. to indicate where a prepositional phrase attaches / does not attach).
During training on partially annotated sentences, only the labeled spans are used to update the model.
This gives dramatic gains across multiple datasets.

## Citation

[Paper](https://arxiv.org/abs/1805.06556)

```bibtex
@InProceedings{Joshi:2018:ACL,
  author    = {Vidur Joshi, Matthew Peters, Mark Hopkins},
  title     = {Extending a Parser to Distant Domains Using a Few Dozen Partially Annotated Examples},
  booktitle = {ACL},
  year      = {2018},
  url       = {https://arxiv.org/abs/1805.06556},
}
```
