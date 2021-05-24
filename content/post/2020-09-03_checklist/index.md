---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Beyond Accuracy: Behavioral Testing of NLP Models with CheckList (Ribeiro, et al., ACL 2020 Best Paper)"
subtitle: ""
summary: "It is difficult to predict how well a model will work in the real world. Carefully curated test sets provide some signal, but only if they are large, representative, and have not been overfit to. This paper builds on two ideas for this problem: constructing challenge datasets and breaking performance down into subcategories. Together, these become a process of designing specific tests that measure how well a model handles certain types of variation in data."
authors: []
tags: ["paper", "analysis", "data"]
categories: []
date: 2020-09-03T14:44:29-05:00
lastmod: 2020-09-03T14:44:29-05:00
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

It is difficult to predict how well a model will work in the real world.
Carefully curated test sets provide some signal, but only if they are large, representative, and have not been overfit to.
This paper builds on two ideas for this problem: constructing challenge datasets and breaking performance down into subcategories.
Together, these become a process of designing specific tests that measure how well a model handles certain types of variation in data.

The paper organises these tests along two axes.
One is the type of test:

- Invariance: Giving the same answer when changes are made that should not impact the model prediction.
- Directional: Giving an answer that differs in a way that matches the intended impact of a change.
- Minimum Function Tests: A range of other tests that consider specific cases.

The other axis is the linguistic property being varied:

- Vocabulary Change
- Named Entity Variation
- Temporal Shift
- Negation
- Semantic Role Swap
- Various Other Changes

For example, an invariance test on vocabulary would be that replacing words with their synonyms should not change the result.

The paper tests the idea on (1) sentiment analysis on SST-2, (2) identifying matching questions on QQP, and (3) machien comprehension on SQuAD.
Researchers / developers using the method are more effective at finding issues than those asked to write tests without this framework to approach the problem.

Understanding system errors has been an interest of mine for a long time now (back to my 2012 parsing paper) and from my experience with startups it is definitely challenging to develop effective tests for NLP models.
I'm curious to see how this approach works out when used iteratively.
When users modify their model or data to address the problems do they actually fix them or just overfit to the new set of tests?
Another open question is how to apply these to problems with more structured output (e.g. text-to-SQL).
Some would easily apply, e.g. invariance tests, while others would be more difficult.

## Citation

[Paper](https://aclanthology.org/2020.acl-main.442/)

```bibtex
@inproceedings{ribeiro-etal-2020-beyond,
    title = "Beyond Accuracy: Behavioral Testing of {NLP} Models with {C}heck{L}ist",
    author = "Ribeiro, Marco Tulio  and
      Wu, Tongshuang  and
      Guestrin, Carlos  and
      Singh, Sameer",
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics",
    month = "jul",
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.acl-main.442",
    doi = "10.18653/v1/2020.acl-main.442",
    pages = "4902--4912",
    abstract = "Although measuring held-out accuracy has been the primary approach to evaluate generalization, it often overestimates the performance of NLP models, while alternative approaches for evaluating models either focus on individual tasks or on specific behaviors. Inspired by principles of behavioral testing in software engineering, we introduce CheckList, a task-agnostic methodology for testing NLP models. CheckList includes a matrix of general linguistic capabilities and test types that facilitate comprehensive test ideation, as well as a software tool to generate a large and diverse number of test cases quickly. We illustrate the utility of CheckList with tests for three tasks, identifying critical failures in both commercial and state-of-art models. In a user study, a team responsible for a commercial sentiment analysis model found new and actionable bugs in an extensively tested model. In another user study, NLP practitioners with CheckList created twice as many tests, and found almost three times as many bugs as users without it.",
}
```

