+++
title = "Multimodal Word Distributions (Athiwaratkun and Wilson, 2017)"
date = 2017-10-26T20:47:12-04:00
draft = false

summary = "By switching from representing words as points in a vector space to multiple gaussian regions we can get a better model, scoring higher on multiple word similarity metrics than a range of techniques."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "word-vectors"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

Word2Vec and other approaches provide a single vector representing a word's meaning, giving words spatially defined relationships capturing relatedness.
A natural extension is to consider regions in that space and allow some words to take up larger or smaller regions.
Another natural idea is to allow a single word to have multiple representations, to capture the different senses.
This paper considers both of those ideas, using multiple gaussian distributions per word.

Using gaussians has the nice property that there is a closed form for calculating the amount of overlap between them, which is used as a measure of similarity.
Following ideas from word2vec, during learning the aim is to increase similarity between words that occur together and decrease it between random pairs that do not occur together.
Once the word representations are learned, KL divergence is used for similarity, along with the standard approaches that only look at the gaussian centres.

In practise, two spherical distributions per word is sufficient.
Performance is better than word2vec and several other approaches for multi-sense word embeddings.
There was one puzzling line about the model suffering larger variance problems, but it was not quantified.

It would be very interesting to inject some knowledge, such as from WordNet, to guide the number of gaussians per word, rather than giving them all N.
The paper also doesn't get into details about the learned space, for example, are the two senses often far apart or close together? (in the latter case it is learning a slightly non-linear spatial representation).

## Citation

[Paper](https://aclanthology.org/P17-1151)

```bibtex
@InProceedings{athiwaratkun-wilson:2017:Long,
  author    = {Athiwaratkun, Ben  and  Wilson, Andrew},
  title     = {Multimodal Word Distributions},
  booktitle = {Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  month     = {July},
  year      = {2017},
  address   = {Vancouver, Canada},
  publisher = {Association for Computational Linguistics},
  pages     = {1645--1656},
  url       = {https://aclanthology.org/P17-1151}
}
```
