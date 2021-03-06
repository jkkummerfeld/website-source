+++
title = "A Factored Neural Network Model for Characterizing Online Discussions in Vector Space (Cheng et al., EMNLP 2017)"
date = 2017-10-16T20:55:07-04:00
draft = false

summary = "A proposal for how to improve vector representations of sentences by using attention over (1) fixed vectors, and (2) a context sentence."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "emnlp", "word-vectors"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

Attention - a weighted average over a set of vectors representing context - has consistently produced positive results.
Here we see an example of how it can be applied in the case of modeling a threaded discussion.

Attention is applied in two ways.
First, over a fixed set of vectors.
This is intended to provide a mechanism to choose between several different sub-models contained within a single model.
Put differently, the vectors provide a set of latent representations that capture each of the different types of posts in the subreddit.
Second, attention over the current utterance is used in the process of predicting responses (at training time only).
This provides an additional source of input to the model, by forcing it to explain the response utterances using the same representations as a source of information.

The application is a new task, using values assigned to posts = upvotes - downvotes (i.e. Reddit karma).
Predicting the specific value is hard, so the task is split into 7 binary decisions about whether a post has a score higher or lower than some value.
On this task the new approach provides consistent gains, though overall performance remains low (53 - 56%).
Confusingly though, one of the figures (number 4) seems to suggest that it was a single multi-way decision, not a set of binary decisions.
I'm also curious about the data, in particular what the distribution of scores is.
The paper mentions it is Zipfian, but surely it would be something double-sided with a massive peak at 0 and a rapid drop in either direction?

Overall, this is further evidence of the versatility of the idea of attention!

## Citation

[Paper](https://aclanthology.org/D17-1242.pdf)

```bibtex
@InProceedings{cheng-fang-ostendorf:2017:EMNLP2017,
  author    = {Cheng, Hao  and  Fang, Hao  and  Ostendorf, Mari},
  title     = {A Factored Neural Network Model for Characterizing Online Discussions in Vector Space},
  booktitle = {Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing},
  month     = {September},
  year      = {2017},
  address   = {Copenhagen, Denmark},
  publisher = {Association for Computational Linguistics},
  pages     = {2286--2296},
  url       = {https://aclanthology.org/D17-1242}
}
```
