+++
title = "Abstractive Document Summarization with a Graph-Based Attentional Neural Model (Tan et al., 2017)"
date = 2017-11-29T19:14:05-05:00
draft = false

summary = "Neural abstractive summarisation can be dramatically improved with a beam search that favours output that matches the source document, and further improved with attention based on PageRank, with a modification to avoid attending to the same sentence more than once."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "acl", "summarisation"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

Most effective summarisation systems are extractive, selecting the most important sentences in a document and sticking them together.
Clearly that is not how people write summaries, but creating abstractive summaries means generating fluent language.
At the same time, most datasets are based on news text, where the first few sentences are a strong baseline summary (by design, as journalists need to assume that the reader could stop at any point).
This paper introduces several ideas to get state-of-the-art results on summarisation using an abstractive system.

There are three core new ideas, one for decoding and two for the model.
The idea in decoding is a beam search in which the score is increased when adding bigrams that occur in the source but are not in the output.
In the model, they propose a new form of attention based on PageRank, similar to previous methods used for ranking sentences in summarisation.
For every pair of sentences plus the current decoder hidden vector, a similarity score is calculated ($h_1 M h_2$), where $M$ is a matrix of parameters.
This produces a matrix of similarities, which they run PageRank on with initialisation set so that all weight starts on the decoder hidden vector.
That produces a score for each input sentence, which is normalised to get attention values.
The second idea is that they don't want to attend to the same sentence multiple times, so before normalising they subtract the previous score for that sentence (with it capped at 0 to avoid negative values).

Together, these lead to state of the art results, beating both extractive and abstractive systems.
Though in human evaluation using the first three sentences as a summary remains a very strong baseline, only slightly behind this system on informativeness and ahead on coherence and fluency.
Ablation shows that the decoding idea has the biggest impact, but the graph based attention does help.
Interestingly, if the score in decoding is extremely biased to focus on the bigram addition aspect performance only decreases a little.
That may reflect the nature of the metric, which is based on ngram overlap.

There are also a bunch of little details that may be crucial, like adding markers for entities (which seems like a possible space for a more elegant solution).
I'm not sure the beam search scoring idea has applications beyond summarisation, but thee modified attention might!

## Citation

[Paper](https://aclanthology.org/P17-1108)

```bibtex
@InProceedings{tan-wan-xiao:2017:Long,
  author    = {Tan, Jiwei  and  Wan, Xiaojun  and  Xiao, Jianguo},
  title     = {Abstractive Document Summarization with a Graph-Based Attentional Neural Model},
  booktitle = {Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  month     = {July},
  year      = {2017},
  address   = {Vancouver, Canada},
  publisher = {Association for Computational Linguistics},
  pages     = {1171--1181},
  url       = {https://aclanthology.org/P17-1108}
}
```
