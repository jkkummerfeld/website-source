+++
title = "High-risk learning: acquiring new word vectors from tiny data (Herbelot et al., 2017)"
date = 2017-12-07T20:45:39-05:00
draft = false

summary = "The simplest way to learn word vectors for rare words is to average their context. Tweaking word2vec to make greater use of the context may do slightly better, but it's unclear."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "emnlp", "word-embeddings"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

Word vectors are great for common words, but what about rare words?
People can have a fairly good understanding of a word given only a few instances, but it's fairly standard to turn all words with a frequency of less than 5 into UNK when learning word vectors.

One simple approach is to add up word vectors from the context of the rare word and use that as the representation.
This paper proposes using a tweaked version of word2vec: keep vectors for frequent words fixed, increase the learning rate, use a fixed width context window, initialise with the additive approach, and only subsample by discarding frequent words.
All of those make sense, though I am curious whether it would be better to just decrease subsampling or disable it entirely.

The results are mixed, with the improvement over the additive approach data dependent.
That might partly reflect the tasks though - something downstream like POS tagging would have been interesting, particularly since the LSTM may already be capturing contextual information that covers what the additive approach has, but not what this adds.
Ultimately this is not a solution to this problem, but it's an idea to keep in mind.

## Citation

[Paper](https://www.aclweb.org/anthology/D17-1030)

```bibtex
@InProceedings{herbelot-baroni:2017:EMNLP2017,
  author    = {Herbelot, Aur\'{e}lie  and  Baroni, Marco},
  title     = {High-risk learning: acquiring new word vectors from tiny data},
  booktitle = {Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing},
  month     = {September},
  year      = {2017},
  address   = {Copenhagen, Denmark},
  publisher = {Association for Computational Linguistics},
  pages     = {304--309},
  url       = {https://www.aclweb.org/anthology/D17-1030}
}
```
