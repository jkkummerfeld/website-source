---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "A Novel Workflow for Accurately and Efficiently Crowdsourcing Predicate Senses and Argument Labels (Jiang, et al., Findings of EMNLP 2020)"
subtitle: ""
summary: "My [previous post](http://jkk.name/post/2020-09-25_crowdqasrl/) discussed work on crowdsourcing QA-SRL, a way of capturing semantic roles in text by asking workers to answer questions. This post covers a paper I contributed to that also considers crowdsourcing SRL, but collects the more traditional form of annotation used in resources like Propbank."
authors: []
tags: ["paper", "annotation", "crowdsourcing", "srl"]
categories: []
date: 2020-10-04T15:10:12-05:00
lastmod: 2020-10-04T15:10:12-05:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

My [previous post](http://jkk.name/post/2020-09-25_crowdqasrl/) discussed work on crowdsourcing QA-SRL, a way of capturing semantic roles in text by asking workers to answer questions.
This post covers a paper I contributed to that also considers crowdsourcing SRL, but collects the more traditional form of annotation used in resources like Propbank.

The core new idea is a filtering process in which workers identify *incorrect* answers for a task.
This is the first step of a three stage process:

1. Five workers iteratively filter the options for a label (either for a predicate or argument) until there are only three.
2. Five workers select the correct answer.
3. If the workers disagree or any of them indicates uncertainty, ask an expert to annotate the example.

To make this work, we use an automatic system for identifying spans for predicates and arguments.
This is better than going straight to the second step because it makes the set of labels less overwhelming, focusing effort on the subtle distinctions between the options.

This mixture of crowd and expert effort achieves high accuracy (94%) while only having 12% of examples annotated by experts.
The cost is about 52 cents per label for crowd work plus the cost of the expert.

It's a little tricky to compare the cost with prior work.
Comparing to other work on SRL, we spend more on the crowd, but less on experts.
Whether that trade-off is worth it will depend on the cost of experts.
In practise, our experts are often members of the research team and so their time is a stronger constraint than the crowdsourcing budget.
In that case, our approach comes out ahead as we can get more data annotated per unit of expert effort (by a factor of four).
The QA-SRL work is quite a bit cheaper, at 54 cents per predicate with 2.9 roles on average (which would be ~$2 + expert effort for our approach), but the type of annotations collected are quite different, with ours providing labels from the sense inventory in Propbank.

I see a range of interesting potential improvements for future work.
First, bringing in methods of worker training in order to improve their accuracy and so reduce the need for duplicate effort.
Second, combining with ideas from other work, such as having a model deciding whether examples are easy or hard and changing how they are processed accordingly, or using QA-SRL annotation to inform the process.

## Citation

[Paper](http://www.jkk.name/pub/emnlp-findings20srl.pdf)

```bibtex
@InProceedings{emnlp-findings20srl,
  title     = {A Novel Workflow for Accurately and Efficiently Crowdsourcing Predicate Senses and Argument Labels},
  author    = {Youxuan Jiang and Huaiyu Zhu and Jonathan K. Kummerfeld and Yunyao Li and Walter Lasecki},
  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},
  shortvenue = {Findings of EMNLP},
  month     = {November},
  year      = {2020},
  location  = {Online},
  url       = {http://www.jkk.name/pub/emnlp-findings20srl.pdf},
  abstract  = {Resources for Semantic Role Labeling (SRL) are typically annotated by experts at great expense. Prior attempts to develop crowdsourcing methods have either had low accuracy or required substantial expert annotation. We propose a new multi-stage crowd workflow that substantially reduces expert involvement without sacrificing accuracy. In particular, we introduce a unique filter stage based on the key observation that crowd workers are able to almost perfectly filter out incorrect options for labels. Our three-stage workflow produces annotations with 95\% accuracy for predicate labels and 93\% for argument labels, which is comparable to expert agreement. Compared to prior work on crowdsourcing for SRL, we decrease expert effort by 4x, from 56\% to 14\% of cases. Our approach enables more scalable annotation of SRL, and could enable annotation of NLP tasks that have previously been considered too complex to effectively crowdsource.},
}
```
