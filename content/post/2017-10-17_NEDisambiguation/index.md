+++
title = "Named Entity Disambiguation for Noisy Text (Eshel et al., CoNLL 2017)"
date = 2017-10-17T20:33:58-04:00
draft = false

summary = "The WikiLinks dataset of text mentions that are hyperlinked to wikipedia articles provides a nice testing space for named entity disambiguation, and a neural network using attention over local context does reasonably well."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "conll", "entity-linking"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

Several NLP tasks aim to identify information regarding entities, such as when two sections of text are referring to the same thing, or which thing out of a large set (e.g. things in Wikipedia) a piece of text is about.
This paper focuses on a subset of entity linking, trying to determine which entity out of a set of candidates is the correct one (in a way a kind of reranker for entity linking).

The task is based on a really cool dataset from Google+UMass, which collected text that was hyperlinked to wikipedia articles.
The idea is that the text (_mention_) is probably a reference to the thing the article describes, so it is an easy way to get entity linked data for free.
Here, the data is filtered to mentions that aren't too rare (more than 10 occurrences) and where the mention isn't used to refer to too many different entities (the two most common entities account for over 10% of occurrences).
Then, the set of things that this mention is used to refer to somewhere are treated as a list of candidates, and the task is to choose which one is correct in a given context.

The model is of the common style at the moment:

1. The context is processed using a recurrent neural network to produce a set of vectors
2. Attention is used to produce vectors that combine the context with a candidate entity
3. A feedforward neural network produces a score that is maxed over to get a final decision

On the wikilinks based dataset this performs quite a bit better than other models, but it is behind on the smaller manually curated datasets used elsewhere (YAGO and PPRforNED, which link entities in the CoNLL 2003 shared task).
Interestingly, augmenting the training data for YAGO with data from wikilinks does improve performance.
For future users of the wikilinks data there is also some nice analysis at the end of remaining challenges, which are spit between mistakes in the data (unsurprising given the approximate collection process), answers that are too general or specific, tricky cases, and the long tail (which would be even longer without the filtering used in these experiments).

## Citation

[Paper](https://aclanthology.org/K/K17/K17-1008.pdf)

```bibtex
@InProceedings{eshel-EtAl:2017:CoNLL,
  author    = {Eshel, Yotam  and  Cohen, Noam  and  Radinsky, Kira  and  Markovitch, Shaul  and  Yamada, Ikuya  and  Levy, Omer},
  title     = {Named Entity Disambiguation for Noisy Text},
  booktitle = {Proceedings of the 21st Conference on Computational Natural Language Learning (CoNLL 2017)},
  month     = {August},
  year      = {2017},
  address   = {Vancouver, Canada},
  publisher = {Association for Computational Linguistics},
  pages     = {58--68},
  url       = {https://aclanthology.org/K17-1008}
}
```

