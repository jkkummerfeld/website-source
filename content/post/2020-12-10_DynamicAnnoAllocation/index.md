---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Improving Human-Labeled Data through Dynamic Automatic Conflict Resolution (Sun, et al., CoLing 2020)"
subtitle: ""
summary: ""
authors: []
tags: []
categories: []
date: 2021-01-01T01:26:35-06:00
lastmod: 2021-01-01T09:26:35-06:00
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

The standard approach in crowdsourcing is to have a fixed number of workers annotate each instance and then aggregate annotations in some way (possibly with experts resolving disagreements).
This paper proposes a way to dynamically allocate workers.

The process is as follows:

1. Get two workers to annotate an example. If they agree, assign the label.
2. For disagreements, ask additional annotators to label it until a simple majority annotation is reached or a limit is reached.
3. For cases where the limit is reached, use some aggregation approach / experts.

I really like this idea - it's simple to apply and the intuition for why it should work is clear.
Unfortunately, the experiments in the paper do not do the comparison I am most interested in: real data, with multiple annotation strategies applied.
The simulated study supports the effectiveness, but that means buying a range of assumptions about annotator behaviour (e.g. that all errors are equally likely and all workers have the same pattern of behaviour).
There is a large-scale experiment with real data in which the approach collects 3.74 labels per instance on average (with a mimimum of 3) and only 5% of cases not reaching a consensus.
That seems very good!

## Citation

[Paper](https://www.aclweb.org/anthology/2020.coling-main.316)

```bibtex
@inproceedings{sun-etal-2020-improving,
    title = "Improving Human-Labeled Data through Dynamic Automatic Conflict Resolution",
    author = "Sun, David Q.  and
      Kotek, Hadas  and
      Klein, Christopher  and
      Gupta, Mayank  and
      Li, William  and
      Williams, Jason D.",
    booktitle = "Proceedings of the 28th International Conference on Computational Linguistics",
    month = "dec",
    year = "2020",
    address = "Barcelona, Spain (Online)",
    publisher = "International Committee on Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.coling-main.316",
    pages = "3547--3557",
    abstract = "This paper develops and implements a scalable methodology for (a) estimating the noisiness of labels produced by a typical crowdsourcing semantic annotation task, and (b) reducing the resulting error of the labeling process by as much as 20-30{\%} in comparison to other common labeling strategies. Importantly, this new approach to the labeling process, which we name Dynamic Automatic Conflict Resolution (DACR), does not require a ground truth dataset and is instead based on inter-project annotation inconsistencies. This makes DACR not only more accurate but also available to a broad range of labeling tasks. In what follows we present results from a text classification task performed at scale for a commercial personal assistant, and evaluate the inherent ambiguity uncovered by this annotation strategy as compared to other common labeling strategies.",
}
```
