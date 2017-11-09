+++
title = "Learning Symmetric Collaborative Dialogue Agents with Dynamic Knowledge Graph Embeddings (He et al., 2017)"
date = 2017-11-08T18:46:04-05:00
draft = false

summary = "During task-oriented dialogue generation, to take into consideration a table of information about entities, represent it as a graph, run message passing to get vector representations of each entity, and use attention."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "acl", "dialogue"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

Task-oriented dialogue systems are often focused on a very narrow task, to the point where the state can be described completely with a tuple (e.g. preferences for a restaurant).
This paper sets up a more challenging task with more complex language use, while still having a specific goal and directly relevant structured information.
They collected 11,000 dialogues, where two people have private lists of friends and are trying to identify which friend they have in common.
While this is a lot of data, the mechanical turk workers are clearly moving fast, with dialogues taking 1.5 minutes on average, and in 18% of cases they get the friend wrong.

The algorithmic contribution is that the lists of people are represented as a graph, where nodes are properties like company and hobby.
The graph is used to generate vectors for each person by running a form of message passing over its structure.
During generation, the LSTM uses attention over these vectors to inform the output choice.

A few interesting things in the output:

- There are cases where the output is incorrect, as in, says a fact about the structured information / knowledge base that is false.
- Evaluation is tricky, and over the metrics they consider sometimes this wins, but sometimes the baseline system (rules) does better. In particular, success on bot-bot evaluation doesn't seem to clearly transfer to bot-human experiments.
- The utterances are very fluent, but that may be because it's essentially copying from the training data. It looks like there is diversity in the dataset, but a lot of utterances do fit a template of "I have X who Y"

## Citation

[Paper](http://aclweb.org/anthology/P17-1162)

```bibtex
@InProceedings{he-EtAl:2017:Long4,
  author    = {He, He  and  Balakrishnan, Anusha  and  Eric, Mihail  and  Liang, Percy},
  title     = {Learning Symmetric Collaborative Dialogue Agents with Dynamic Knowledge Graph Embeddings},
  booktitle = {Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  month     = {July},
  year      = {2017},
  address   = {Vancouver, Canada},
  publisher = {Association for Computational Linguistics},
  pages     = {1766--1776},
  abstract  = {We study a \emph{symmetric collaborative dialogue} setting
	in which two agents, each with private knowledge,
	must strategically communicate to achieve a common goal.
	The open-ended dialogue state in this setting poses new challenges for existing
	dialogue systems.
	We collected a dataset of 11K human-human dialogues,
	which exhibits interesting lexical, semantic, and strategic elements.
	To model
	both structured knowledge and unstructured language,
	we propose a neural model with dynamic knowledge graph embeddings
	that evolve as the dialogue progresses.
	Automatic and human evaluations show that our model is both more effective
	at achieving the goal and more human-like than baseline neural and rule-based
	models.},
  url       = {http://aclweb.org/anthology/P17-1162}
}
```
