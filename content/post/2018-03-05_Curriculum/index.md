+++
title = "Learning the Curriculum with Bayesian Optimization for Task-Specific Word Representation Learning (Tsvetkov et al., 2016)"
date = 2018-03-05T21:09:58-05:00
draft = false

summary = "Reordering training sentences for word vectors may impact their usefulness for downstream tasks."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "acl", "word-vectors"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

Usually when we learn, we have a curriculum designed to incrementally build understanding.
It seems reasonable that the same idea could be useful for machine learning, and indeed there is a large body of work on the topic.
This paper explores the specific question of whether a curriculum can help develop task-specific word vectors, and whether we can determine an effective curriculum automatically.

They define a linear model with a range of features that characterise a paragraph of text, such as the number of distinct words, the number of prepositional phrases, and the average number of syllables per word.
Paragraphs are sorted by the model and used to train word vectors with word2vec.
These word vectors are then used as part of a model for a target task, giving a score that indicates the quality of the curriculum.
Based on this score the weights for the model are updated, using a form of Bayesian optimisation.

One really nice aspect of this paper is the range of tasks considered: sentiment analysis, NER, POS tagging, and parsing.
Learning a curriculum does improve performance slightly, and which features are important varies across the tasks (indicating the importance of task-specific curriculums).
However, the models are somewhat restricted (as shown by the low absolute performance) because they do not change the word vectors during training.
For most of this paper that's a reasonable decision, as it allows a clearer learning signal, but it would have been interesting to also see the impact on the normal training scenario and a state-of-the-art model.
In my experience (and in our soon-to-appear NAACL paper) we find that variations in word vectors can disappear during training for a downstream task.

## Citation

[Paper](http://www.aclweb.org/anthology/P16-1013)

```bibtex
@InProceedings{tsvetkov-EtAl:2016:P16-1,
  author    = {Tsvetkov, Yulia  and  Faruqui, Manaal  and  Ling, Wang  and  MacWhinney, Brian  and  Dyer, Chris},
  title     = {Learning the Curriculum with Bayesian Optimization for Task-Specific Word Representation Learning},
  booktitle = {Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  month     = {August},
  year      = {2016},
  address   = {Berlin, Germany},
  publisher = {Association for Computational Linguistics},
  pages     = {130--139},
  url       = {http://www.aclweb.org/anthology/P16-1013}
}
```
