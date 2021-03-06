+++
title = "Search-based Neural Structured Learning for Sequential Question Answering (Iyyer et al., ACL 2017)"
date = 2017-10-10T13:43:36-04:00
draft = false

summary = "A new dataset containing multi-turn questions about a table, and a model that generates a kind of logical form, but scores actions based on the content of the table."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "acl", "semantic-parsing"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

Semantic parsing datasets generally consist of (question, answer) pairs, where each pair is completely independent of the rest (one exception is ATIS, which has multi-turn conversations, though most work doesn't use them).
In reality, we often ask a series of simple questions that together form a complex one, for example "What flights are available from Detroit to Sydney? And how much is the price if I don't want to leave before 8am?"
This work explores these kinds of sequential questions with a new dataset and algorithm.

The dataset was formed by asking crowd workers to rephrase questions from the WikiTableQuestions dataset into sequences of shorter questions.
This naturally constrains the types of questions (in particular, they reference a single table only), but covers a range of domains.
With 6,066 question sequences, and on average 2.9 questions / sequence, it's a large dataset by semantic parsing standards.
However, there are no logical forms, only the row, column, or cell(s) that contain the answer.

To solve the problem, they treat it as choosing a sequence of actions, where each action generate a part of the execution instructions.
The model follows the recent approach of considering the contents of the database as part of the calculation (e.g. by taking the dot product of the vector for a cell and the vector for the question).

The system has consistently better performance than other QA systems on the new dataset (though no results are shown for the WikiTableQuestions dataset).
At only 12.8% of sequences completely correct, there is plenty of scope for improvement.
Based on the description of the operators there are definitely additional abilities that would be useful, so this model has potential to improve.
That said, it seems difficult to generalise the model to handle more complicated databases with multiple interconnected tables.

## Citation

[Paper](https://aclanthology.org/P/P17/P17-1167.pdf)

```bibtex
@InProceedings{iyyer-yih-chang:2017:Long,
  author    = {Iyyer, Mohit  and  Yih, Wen-tau  and  Chang, Ming-Wei},
  title     = {Search-based Neural Structured Learning for Sequential Question Answering},
  booktitle = {Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  month     = {July},
  year      = {2017},
  address   = {Vancouver, Canada},
  publisher = {Association for Computational Linguistics},
  pages     = {1821--1831},
  url       = {https://aclanthology.org/P17-1167}
}
```

