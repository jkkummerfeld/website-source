+++
title = "A Local Detection Approach for Named Entity Recognition and Mention Detection (Xu et al., 2017)"
date = 2017-12-01T15:28:59-05:00
draft = false

summary = "Effective NER can be achieved without sequence prediction using a feedforward network that labels every span with a fixed attention mechanism for getting contextual information."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "acl", "ner"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

The classic NER system is a model that has a lot of curated features, like lists of people, and does inference by choosing the top scoring tag sequence for the whole sentence, using Viterbi decoding.
The neural version swaps the curated features for word vectors, and viterbi inference for an LSTM (maybe with beam search).
This paper makes the argument that in reality people are very good at identifying an entity in isolation, so why do global decoding for the best tag sequence?

Given that perspective, they make a model that scores every span of the sentence independently using a feedforward network.
To get an input representing context, they use a weighted sum of word embeddings, where the weights decay exponentially further from the span (FOFE = Fixed-size Ordinally Forgetting Encoding).
The authors point out that this gives a fixed length encoding that could be reversed to recover the original sequence (assuming arbitrary precision floating point numbers).
Thinking about the calculation though, a word ten positions away is having its vector scaled down by a factor of a thousand, so it probably has negligible impact on the decision.
They also apply this idea to the characters of the span itself in both directions.

One tradeoff with the independent classification idea is that it can select overlapping spans.
This is a benefit in one sense, because it naturally handles nested entities (e.g. "[Member of the Order of [Australia]]"), but for partially overlapping spans we have to decide which to keep.
Their solution is to sort by model score and keep the higher scoring option.

The experiments show this is comparable with previous work using LSTMs.
There were a few things I found interesting in the results:

- The FOFE encoding for characters is far worse than a CNN encoding when on their own, but give similar gains when combined with word level features. Since the FOFE essentially ignores the centre of long spans, this suggests they are both learning some representation of prefixes and suffixes.
- They don't try it, but this model seems very amenable to gazetteers, which may be a way to further boost performance.
- They have an in-house dataset of 10,000 manually labeled documents (!), but it only gives a 3% gain on the KBP evaluation.

## Citation

[Paper](https://aclanthology.org/P17-1114)

```bibtex
@InProceedings{xu-jiang-watcharawittayakul:2017:Long,
  author    = {Xu, Mingbin  and  Jiang, Hui  and  Watcharawittayakul, Sedtawut},
  title     = {A Local Detection Approach for Named Entity Recognition and Mention Detection},
  booktitle = {Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  month     = {July},
  year      = {2017},
  address   = {Vancouver, Canada},
  publisher = {Association for Computational Linguistics},
  pages     = {1237--1247},
  url       = {https://aclanthology.org/P17-1114}
}
```
