+++
title = "Provenance for Natural Language Queries (Deutch et al., 2017)"
date = 2018-03-08T20:11:48-05:00
draft = false

summary = "Being able to query a database in natural language could help make data accessible ..."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "vldb", "sql"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

Being able to query a database in natural language could help make data accessible to more people.
Systems that do this have to solve two challenges: (1) understanding the query and (2) expressing the response in a way the user will understand.
Recently there have been papers in the NLP community on the first challenge, but this paper comes from the DB community and considers the second.

The approach assumes we have a syntactic parse of the query and an alignment between the parse and the SQL query it corresponds to (they rely on prior work for this query interpretation piece).
Given that, the new idea in this paper is to take the database results and use the alignment to insert values for each field into the original parse, and from there into the original question.
To avoid extremely long sentences (when there are multiple result rows) they define a procedure to identify ways to summarise results.

However, I'm not convinced by the evaluation.
The dataset they use was collected by (1) enumerating the 196 types of queries people could ask using the Microsoft Academic Search service, and (2) a person manually writing a question for each query.
As a result, the questions feel very formulaic and also only cover cases that we already have a user-friendly interface for, making it unclear how well this will generalise to more natural data.
Still, this work explores an interesting problem and it's cool to see a direct use of syntactic parsing!

## Citation

[Paper](http://www.vldb.org/pvldb/vol10/p577-deutch.pdf)

```bibtex
@Article{Deutch:2017,
  author = {Deutch, Daniel and Frost, Nave and Gilad, Amir},
  title = {Provenance for Natural Language Queries},
  journal = {Proceedings of the VLDB Endowment},
  volume = {10},
  number = {5},
  month = {Jan},
  year = {2017},
  issn = {2150-8097},
  pages = {577--588},
  doi = {10.14778/3055540.3055550},
  url = {http://www.vldb.org/pvldb/vol10/p577-deutch.pdf},
}
```
