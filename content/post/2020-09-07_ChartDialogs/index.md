---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "ChartDialogs: Plotting from Natural Language Instructions (Shao and Nakashole, ACL 2020)"
subtitle: ""
summary: "Natural language interfaces to computer systems are an exciting area with new workshops ([WNLI](https://aclanthology.org/volumes/2020.nli-1/) at ACL and [IntEx-SemPar](https://intex-sempar.github.io/) at EMNLP), a range of datasets (including my own work on [text-to-SQL](/publication/acl18sql/)), and many papers. Most work focuses on either (1) commands for simple APIs, (2) generating a database query, or (3) generating general purpose code. This paper considers an interesting application: interaction with data visualisation tools."
authors: []
tags: ["paper", "dialogue", "data", "grounded-language", "nli"]
categories: []
date: 2020-09-07T14:41:34-05:00
lastmod: 2020-09-07T14:41:34-05:00
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

Natural language interfaces to computer systems are an exciting area with new workshops ([WNLI](https://aclanthology.org/volumes/2020.nli-1/) at ACL and [IntEx-SemPar](https://intex-sempar.github.io/) at EMNLP), a range of datasets (including my own work on [text-to-SQL](/publication/acl18sql/)), and many papers.
Most work focuses on either (1) commands for simple APIs, (2) generating a database query, or (3) generating general purpose code.
This paper considers an interesting application: interaction with data visualisation tools.

Using the full flexibility of these tools is a tall order, so this work focuses on commands to modify style parameters of a figure.
For that setting, the problem can be framed as task-oriented dialogue in which each style parameter (e.g. x-axis font size) is a slot that needs to be defined.
Using this framing of the problem, the paper presents a new dataset of 3,200 conversations in which a person modifies the style of a plot.
These were collected on Mechanical Turk by having one worker describe a target plot and another worker manipulating values for parameters to match it.
There are 12 plot types with 3-13 properties, with the target plot randomly generated.
Baseline approaches do fairly well, but far short of a human (either another worker or one of the authors).

It's a large resource with high agreement between annotators and the paper presents detailed analysis and helpful examples.
One experiment I'd be curious to see is results with a fixed number of training examples per plot type (or per slot type).
Histograms and scatter plots appear particularly difficult in the breakdown of results by plot type, but they are also the types with the fewest examples (a tenth as many as the type with the most).

I find this general topic exciting because it brings together several areas of NLP and it seems feasible to create a useful system in the near future.
Hopefully there will be progress on models for this dataset and development of additional resources.
In particular, there was a decision here to limit generation to slot-values, which is powerful, but does not capture the full flexibility of matplotlib (at least not without further work on representing more features this way).
Arbitrary code generation would be a fantastic extension, though creating the data would require some creativity as the approach used here wouldn't directly work.


## Citation

[Paper](https://aclanthology.org/2020.acl-main.328.pdf)

```bibtex
@inproceedings{shao-nakashole-2020-chartdialogs,
    title = "{C}hart{D}ialogs: {P}lotting from {N}atural {L}anguage {I}nstructions",
    author = "Shao, Yutong  and
      Nakashole, Ndapa",
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics",
    month = "jul",
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.acl-main.328",
    doi = "10.18653/v1/2020.acl-main.328",
    pages = "3559--3574",
    abstract = "This paper presents the problem of conversational plotting agents that carry out plotting actions from natural language instructions. To facilitate the development of such agents, we introduce ChartDialogs, a new multi-turn dialog dataset, covering a popular plotting library, matplotlib. The dataset contains over 15,000 dialog turns from 3,200 dialogs covering the majority of matplotlib plot types. Extensive experiments show the best-performing method achieving 61{\%} plotting accuracy, demonstrating that the dataset presents a non-trivial challenge for future research on this task.",
}
```
