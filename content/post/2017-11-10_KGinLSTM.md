+++
title = "Leveraging Knowledge Bases in LSTMs for Improving Machine Reading (Yang et al., 2017)"
date = 2017-11-10T15:37:15-05:00
draft = false

summary = "Incorporating vector representations of entities from structured resources like NELL and WordNet into the output of an LSTM can improve entity and event extraction."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "acl", "knowledge-graph"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

Structured information sources have been effectively used for entity detection and typing in linear models with the information encoded as binary features.
This paper looks at how to integrate vector representations of structured information into an LSTM.
The solution is an additional processing step during output generation, in which the vectors for relevant entities in the structured data are combined with the standard LSTM output (note, they do not affect the cell itself, so the information is not passed on through the recurrence).

In this case the structured information is a set of tuples forming a graph of relations between entities, from either NELL or WordNet.
The actual encoding of entities is an application of prior work; vectors representing tuples are trained with the objective that the score for any tuple is higher than made-up tuples (where the score is $v_a M_r v_b$ for entities $a$ and $b$ in relation $r$).
The set of relevant entities for a particular word in the sentence is obtained by string matching, and then attention is used to combine them.
There is also a kind of gating mechanism to choose how big a role the entities play in the prediction, using a combination of the input, hidden state, and cell state.

The results are interesting not only because this method helps, but because of how well the standard LSTM does on this task, matching or exceeding prior results.
This is even more impressive given how small ACE is (if I remember correctly).
The other key observations are that having a sequence level loss (using a CRF) helps, and NELL and WordNet seem to be providing different types of information (as using both leads to further improvements).

## Citation

[Paper](http://aclweb.org/anthology/P17-1132)

```bibtex
@InProceedings{yang-mitchell:2017:Long,
  author    = {Yang, Bishan  and  Mitchell, Tom},
  title     = {Leveraging Knowledge Bases in LSTMs for Improving Machine Reading},
  booktitle = {Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  month     = {July},
  year      = {2017},
  address   = {Vancouver, Canada},
  publisher = {Association for Computational Linguistics},
  pages     = {1436--1446},
  url       = {http://aclweb.org/anthology/P17-1132}
}
```
