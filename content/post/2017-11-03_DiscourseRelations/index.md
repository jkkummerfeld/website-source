+++
title = "Joint Modeling of Content and Discourse Relations in Dialogues (Qin et al., 2017)"
date = 2017-11-03T15:40:32-04:00
draft = false

summary = "Identifying the key phrases in a dialogue at the same time as identifying the type of relations between pairs of utterances leads to substantial improvements on both tasks."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "dialogue", "acl"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

Automatically generating high quality meeting notes and summaries would be awesome, but involves solving many challenges.
Here, they assume speech recognition is already done and we also know the structure over utterances indicating which previous utterance each is a response to.
The task is to label each of those utterance-utterance pairs with a type (e.g. elaboration) and to select the key phrase of each utterance.

Two datasets are used, the AMI and ICSO meeting corpora, which have all of the required information.
The new idea here is to jointly model the choice of link label and the key phrase, which is intuitive.
To show the value of joint modeling they run a version of the system with the same linear model, but with independent inference, which performs quite a bit worse.

One neat follow up is that by combining the key phrases into a list you get a form of summary.
According to automatic metrics it is quite a bit better than running the summarisation system they compare to, though it's still a long way from a human summary.

## Citation

[Paper](https://aclanthology.org/P17-1090)

```bibtex
@InProceedings{qin-wang-kim:2017:Long,
  author    = {Qin, Kechen  and  Wang, Lu  and  Kim, Joseph},
  title     = {Joint Modeling of Content and Discourse Relations in Dialogues},
  booktitle = {Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  month     = {July},
  year      = {2017},
  address   = {Vancouver, Canada},
  publisher = {Association for Computational Linguistics},
  pages     = {974--984},
  url       = {https://aclanthology.org/P17-1090}
}
```
