+++
title = "Getting the Most out of AMR Parsing (Wang and Xue, EMNLP 2017)"
date = 2017-10-12T19:52:34-04:00
draft = false

summary = "Two ideas for improving AMR parsing: (1) take graph distance into consideration when generating alignments, (2) during parsing, for concept generation, generate individual concepts in some cases and frequently occurring subgraphs in other cases."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "emnlp", "amr"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

Abstract Meaning Representation (AMR) structures represent sentence meaning with labeled nodes (concepts) that are related to the words in the sentence, but not explicitly linked to them.
This is a problem for most parsing algorithms, which need a way to efficiently decompose the structure in order to learn how to generate it.
In dependency parsing there are no abstract nodes to generate, in constituency parsing there is a very small set of node types, and for CCG, TAG, etc the labels come from a constrained space.
The solution for many AMR parsers is to have a process for generating the concepts as a first step towards parsing, and to automatically align the training data to guide this concept generation stage.

The first idea in this paper is about the set of AMR concepts.
Some concepts are easy to link, as the concept clearly maps to a single word in the sentence.
Around a quarter of concepts have a more complex relation, where a set of concepts link to a set of words, for example, named entities.
The idea for these is to identify common subgraphs by abstracting some lexical items.
For example, a teacher and a worker both get mapped to a person concept that is the ARG0 of the lexical item (teach, or work in this case).
This can allow for the generation of entirely novel concepts (e.g. "concept"-er), giving a 0.6 boost to recall for CAMR simply by making these additional concepts available.
Using a bidirectional LSTM with a character CNN to generate features on likely concepts, there is a gain of 1.0 F1 for the parser.

The second idea is to improve the alignments used to train concept generation by taking into consideration the graph structure.
To use an aligner developed for machine translation the graph needs to be turned into a linear sequence, but that can lead to strange jumps.
The idea here is to take that into consideration by modifying the calculation of the cost of distortion (i.e. jumping) to be reshaped based on the graph structure.
For optimal alignment quality they consider aligning in either direction, directly changing the distance metric in the English-AMR direction, and just rescaling it to be less sensitive when appropriate for AMR-English.
This is definitely higher precision than prior approaches, but lower recall.
It's hard to tell whether this helps, since the evaluation doesn't separate it out from the first idea (results in section 5.3 are not on the same dataset as 5.1).

Given how separate this is from CAMR, it would be interesting to see if it helps other systems similarly.
With concept identification at 83 F there is still plenty of scope for improvement, though there is no analysis of which types of concepts remain the most problematic.

## Citation

[Paper](http://aclweb.org/anthology/D/D17/D17-1130.pdf)

```bibtex
@InProceedings{wang-xue:2017:EMNLP2017,
  author    = {Wang, Chuan  and  Xue, Nianwen},
  title     = {Getting the Most out of AMR Parsing},
  booktitle = {Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing},
  month     = {September},
  year      = {2017},
  address   = {Copenhagen, Denmark},
  publisher = {Association for Computational Linguistics},
  pages     = {1268--1279},
  url       = {https://www.aclweb.org/anthology/D17-1130},
}
```

