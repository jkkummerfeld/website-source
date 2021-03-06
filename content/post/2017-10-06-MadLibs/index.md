+++
title = "Filling the Blanks (hint: plural noun) for Mad Libs Humor (Hossain et al., EMNLP 2017)"
date = 2017-10-06T13:31:43-04:00
draft = false

summary = "A new task and associated evaluation method plus system for Mad Libs - filling in missing words in a story in a funny way. While the system does poorly, using it as a first pass with human rerankers produces funnier stories than people alone."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "emnlp", "humour"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

Humor is an incredibly difficult problem, as this paper makes clear in its background section.
Most work has considered very specific types of jokes (e.g. "that's what she said", or pairs of words that sound similar to form riddles).
This work contributes (1) a new task, (2) an evaluation method, and (3) an example system.

The task is Mad Libs, where a story has some words removed and people choose new words to make the story funny.
If you are familiar with the normal version, one key difference is that here people have access to the complete story when they are choosing their words.
A set of 40 'stories' were written based on Simple Wikipedia articles, and workers on Mechanical Turk wrote words to fill them, with filtering based on judging by other workers.

The evaluation method involved recruiting a set of judges on Mechanical Turk and asking a series of questions to measure humour for a given response.
As well as judging the overall story, they were asked to select which words contributed the most.
By aggregating these selections as votes, each word was scored as funny or not.

The system is a linear classifier with a range of features, including scores from a language model.
On its own, it performs very poorly, but using it as a filter to restrict the space of words a person can choose from actually leads to better performance than people on their own.
Of course, it's difficult to analyse the source of improvement;
The authors theorise that it is because it prevents people from selecting words that only they would see is funny.
Another interpretation is that the constraint gives them a smaller space to think about and so they can find more interesting plays on words.

Finally, as a non-expert in this area, this paper had some nice discussion of the tradeoffs between different ways of generating humour (incongruous vs. coherent content strategies).

## Citation

[Paper](https://aclanthology.org/D17-1068)

```bibtex
@InProceedings{hossain-EtAl:2017:EMNLP2017,
  author    = {Hossain, Nabil  and  Krumm, John  and  Vanderwende, Lucy  and  Horvitz, Eric  and  Kautz, Henry},
  title     = {Filling the Blanks (hint: plural noun) for Mad Libs Humor},
  booktitle = {Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing},
  month     = {September},
  year      = {2017},
  address   = {Copenhagen, Denmark},
  publisher = {Association for Computational Linguistics},
  pages     = {649--658},
  url       = {https://aclanthology.org/D17-1068},
}
```

