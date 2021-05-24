+++
title = "Frames: a corpus for adding memory to goal-oriented dialogue systems (El Asri et al., 2017)"
date = 2017-11-09T19:47:08-05:00
draft = false

summary = "A new dialogue dataset that has annotations of multiple plans (frames) and dialogue acts that indicate modifications to them."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "sigdial", "dialogue", "data"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

Another paper about a dataset of dialogues, but this time with structure.
Like the paper from yesterday, the aim is a dataset of task-oriented conversations, but with more complexity than prior work.
The difference is that this work includes a structured representation of the state of the conversation: frames.

A frame is essentially a tuple describing a query, e.g. (Destination: Sydney, Origin: Ann Arbor, price: 1500 USD).
There are multiple frames in a dialogue (a departure from DSTC tasks), and utterances are labeled with dialogue acts that capture modifications to the frames as well as references to them.
This structure sounds fairly general, though the focus here was on vacation planning, where the user is buying a package.
The setup doesn't maximise the potential complexity though, as there are a small number of set packages available, rather than the complex tradeoffs of flight+hotel combinations that exist in practise.
Looking at the example dialogues in the paper, it has complete sentences of some complexity.
One thing I'm still curious about is disagreements between annotators, as for the complete task the score was 0.62 +/- 5 (with dialogue acts being trickier than slot values, and no scores for frame references on their own).

Comparing to the Stanford dataset this is smaller (11k vs. 1.4k), but has more turns per dialogue (11 vs. 15) and probably longer turns too, judging by the examples.
The tasks are completely different, but both come with small tables of information that are private to the two participants and required for almost every turn in the conversation.
Evaluating on both could be a great way to show the flexibility of a dialogue system, but the lack of frames for the Stanford data and the difficulty of running a human evaluation for this data limits the feasible types of multi-domain experiments.

## Citation

[Paper](https://aclanthology.org/W17-5526)

```bibtex
@InProceedings{elasri-EtAl:2017:W17-55,
  author    = {El Asri, Layla  and  Schulz, Hannes  and  Sharma, Shikhar  and  Zumer, Jeremie  and  Harris, Justin  and  Fine, Emery  and  Mehrotra, Rahul  and  Suleman, Kaheer},
  title     = {Frames: a corpus for adding memory to goal-oriented dialogue systems},
  booktitle = {Proceedings of the 18th Annual SIGdial Meeting on Discourse and Dialogue},
  month     = {August},
  year      = {2017},
  address   = {Saarbrucken, Germany},
  publisher = {Association for Computational Linguistics},
  pages     = {207--219},
  url       = {https://aclanthology.org/W17-5526}
}
```
