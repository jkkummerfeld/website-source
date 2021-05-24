+++
title = "Joint Extraction of Entities and Relations Based on a Novel Tagging Scheme (Zheng et al., 2017)"
date = 2017-11-30T20:01:41-05:00
draft = false

summary = "By encoding the relation type and role of each word in tags, an LSTM can be applied to relation extraction with great success."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "acl", "relation-extraction"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

This paper considers the task of identifying named entities in a sentence and the relations between them.
The contribution is a way of formulating the task as tagging, so a bi-directional LSTM can be applied.

The tags are like in NER (Begin, Inside, End, Single, Outside), but rather than Person, Location, etc, they label each entity with the relation it is participating in, and whether it is in role one or two for the relation.
Applying a two layer bidirectional LSTM to this set up gets to state-of-the-art precision on news data.
To get SotA F-score they modify the loss to place less weight on Outside tags, which raises recall at the cost of precision.

One catch with this approach is handling multiple relations of the same type.
The solution here is to link pairs that are closest together (unclear what they do for nesting).
That doesn't handle overlapping relations, which the authors say is particularly common in the BioInfer data (I'm curious how much it is hurting here too).
It's unclear how this could be addressed without a radical redesign, since extending the tag scheme could lead to sparsity issues.

I was not familiar with this data, so I looked back to the original paper the annotated test data came from: [Hoffman et al., (2011)](https://aclanthology.org/P11-1055).
There is no dev set, only a 395 sentence test set, so the standard practise is to use random 10% samples of the test data for development.
Also, if I understand it correctly, the data was annotated by manually confirming the output of systems, which means it will have recall errors.
If interest in this data grows, going back and annotating more seems worthwhile.

## Citation

[Paper](https://aclanthology.org/P17-1113)

```bibtex
@InProceedings{zheng-EtAl:2017:Long,
  author    = {Zheng, Suncong  and  Wang, Feng  and  Bao, Hongyun  and  Hao, Yuexing  and  Zhou, Peng  and  Xu, Bo},
  title     = {Joint Extraction of Entities and Relations Based on a Novel Tagging Scheme},
  booktitle = {Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  month     = {July},
  year      = {2017},
  address   = {Vancouver, Canada},
  publisher = {Association for Computational Linguistics},
  pages     = {1227--1236},
  url       = {https://aclanthology.org/P17-1113}
}
```
