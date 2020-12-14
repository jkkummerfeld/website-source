+++
title = "A Two-Stage Parsing Method for Text-Level Discourse Analysis (Wang et al., 2017)"
date = 2017-11-17T18:40:20-05:00
draft = false

summary = "Breaking discourse parsing into separate relation identification and labeling tasks can boost performance (by dealing with limited training data)."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "acl", "discourse"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

Discourse parsing for Rhetorical Structure Theory is difficult partly because it involves a range of relation types at different scales (within and between sentences) and partly because there is relatively little annotated data available.
To deal with the limited data, this paper breaks the task into two parts: (1) identify relations, (2) assign labels.
Their system is state-of-the-art, and an ablation shows that the division of tasks helps performance.
They also divide up the labeling step to have different classifiers for within sentences, between sentences in the same paragraph, and between paragraphs, which also helps a little.

I find the second improvement surprising, since an expanded feature set for a single classifier would be able to emulate their multi-classifier model, while having the advantage of sharing information between classes.
The first improvement is more intuitive (a denser space makes for an easier problem), though I wonder whether this will be one point on the back-and-forth that usually occurs between sequential and joint models (with joint models usually winning in the end).
This paper also continues the trend of transition-based inference applying effectively to tasks, which makes sense if our models are getting good enough that search errors are not a major issue.

## Citation

[Paper](http://aclweb.org/anthology/P17-2029)

```bibtex
@InProceedings{wang-li-wang:2017:Short,
  author    = {Wang, Yizhong  and  Li, Sujian  and  Wang, Houfeng},
  title     = {A Two-Stage Parsing Method for Text-Level Discourse Analysis},
  booktitle = {Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},
  month     = {July},
  year      = {2017},
  address   = {Vancouver, Canada},
  publisher = {Association for Computational Linguistics},
  pages     = {184--188},
  url       = {http://aclweb.org/anthology/P17-2029}
}
```
