+++
title = "Learning Distributed Representations of Texts and Entities from Knowledge Base (Yamada et al., 2017)"
date = 2017-11-15T18:01:27-05:00
draft = false

summary = "Vectors for words and entities can be learned by trying to model the text written about the entities. This leads to word vectors that score well on similarity tasks and entity vectors that produce excellent results on entity linking and question answering."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

Since word2vec was released there have been a series of X2vec papers, though none have had the success of word vectors.
In this case the idea is to represent entities and chunks of text (words, sentences, paragraphs).

Entities are represented with vectors.
To get the vector for a chunk of text, they:

1. Sum word vectors for the text.
2. Rescale to be of unit length.
3. Multiply by a weight matrix and add a bias.

Then to learn these, negative log likelihood is used, where the probability is defined as a softmax over the dot product between entity and text vectors.
The data is a portion of Wikipedia annotated with entities as indicated by links (plus they say the entity the page is about is implicitly part of every sentence).

With these new vectors in hand, they try textual similarity, with strong results.
They also build a very simple entity linking system, a feed-forward network with these representations plus a few other features, and beat all prior work.
Similarly
They apply the same modeling approach to Quizball QA, also with strong results.

The simplicity and effectiveness of the model really is impressive.
Some qualitative examples are included, but hard to find trends in.
It does seem like a more reasonable vector learning approach than skip-thought and other similar approaches that rely only on text context - the entities provide something different, but clearly closely related.
That said, I feel like more ablation is needed to see what role each of these pieces is playing (are they learning better vectors, or using them in a way that is more effective? Or both?).

## Citation

[Paper](https://www.transacl.org/ojs/index.php/tacl/article/view/1065)

```bibtex
@article{TACL1065,
	author = {Yamada, Ikuya  and Shindo, Hiroyuki  and Takeda, Hideaki  and Takefuji, Yoshiyasu },
	title = {Learning Distributed Representations of Texts and Entities from Knowledge Base},
	journal = {Transactions of the Association for Computational Linguistics},
	volume = {5},
	year = {2017},
	issn = {2307-387X},
	url = {https://www.transacl.org/ojs/index.php/tacl/article/view/1065},
	pages = {397--411}
}
```
