+++
title = "Pushing the Limits of Paraphrastic Sentence Embeddings with Millions of Machine Translations (Wieting et al., 2017)"
date = 2018-01-31T19:25:36-05:00
draft = false

summary = "With enough training data, the best vector representation of a sentence is to concatenate an average over word vectors and an average over character trigram vectors."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "arxiv", "semantics"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

It would be convenient to have a way to represent sentences in a vector space, similar to the way vectors are frequently used to represent input words for a task.
Quite a few sentence embeddings methods have been proposed, but none have really caught on.
Building on prior work by the same authors, the approach here is to define a neural network that maps a sentence to a vector, then train it with a loss function that measures similarity between the vectors for paraphrases.

This paper scales up the approach, using millions of paraphrases, and explores a range of models.
To get the paraphrases they use translation (start with a sentence, translate it to another language and back, then assume the translation is a paraphrase).
For negative examples they use the sentence that the model currently thinks is most similar other than the correct one (choosing this from a large enough set is key).

The best model is very simple - concatenate together the average of word vectors and the average of character trigram vectors.
That consistently beats prior work, including convolutional models, and LSTMs.
In a way, this is nice as it is a simple way to get a sentence representation!
On the other hand, this can't possibly capture the semantics of a sentence fully since it doesn't take word order into consideration at all.

## Citation

[ArXiv Paper](https://arxiv.org/abs/1711.05732)

```bibtex
@ARTICLE{2017arXiv171105732W,
  author        = {{Wieting}, J. and {Gimpel}, K.},
  title         = {Pushing the Limits of Paraphrastic Sentence Embeddings with Millions of Machine Translations},
  journal       = {ArXiv e-prints},
  archivePrefix = {arXiv},
  eprint        = {1711.05732},
  primaryClass  = {cs.CL},
  year          = {2017},
  month         = {November},
  url           = {https://arxiv.org/abs/1711.05732},
}
```
