---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Compositional Demographic Word Embeddings (Welch et al., EMNLP 2020)"
subtitle: ""
summary: "Most work in NLP uses datasets with a diverse set of speakers. In practise, everyone speaks / writes slightly differently and our models would be better if they accounted for that. This has been the motivation for a line of work by [Charlie Welch](http://cfwelch.com/) that I've been a collaborator on (in [CICLing 2019](http://jkk.name/publication/cicling19personal), [IEEE Intelligent Systems 2019](http://jkk.name/publication/ieee19personal/), [CoLing 2020](http://jkk.name/publication/coling20personal/), and this paper)."
authors: []
tags: ["paper", "word-embeddings", "language-model"]
categories: []
date: 2020-10-10T20:25:11-05:00
lastmod: 2020-10-10T20:25:11-05:00
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

Most work in NLP uses datasets with a diverse set of speakers.
In practise, everyone speaks / writes slightly differently and our models would be better if they accounted for that.
This has been the motivation for a line of work by [Charlie Welch](http://cfwelch.com/) that I've been a collaborator on (in
[CICLing 2019](http://jkk.name/publication/cicling19personal),
[IEEE Intelligent Systems 2019](http://jkk.name/publication/ieee19personal/),
[CoLing 2020](http://jkk.name/publication/coling20personal/),
and this paper).

Here, the question is how to improve language modeling for a new user of a service who voluntarily provided some demographic information, but you have no other data for.
Our solution is a language model that (1) has a separate word embedding space for each individual demographic value, and (2) forms a word embedding for a given user by composing the embeddings for their demographics.
In experiments on Reddit, this leads to improvements in performance for all demographic groups.

In the process, we also developed a way to extract demographics of Reddit users.
Prior work has either inferred demographics or looked at flairs (labels in user profiles).
We use self-reported information in posts, such as "I am a \[blah\]".
We use simple regular expressions, which are enough to get two or more demographic values for 61,000 users.
There is also relatively little overlap with a flair based method (less than 0.5% of ours are in a set based on flairs).

It is important to note that a range of ethical issues exist around the use of demographics in machine learning.
We discuss a range of issues in the paper, but I also wanted to mention a few here.
First, to collect our data, we identified self-reported demographics in Reddit text.
This avoids some of the problems with inferring demographics, but it does mean our sample is biased (it only contains people who wish to publicly share demographics online).
Second, we must consider how our work may be used.
There is a potential positive (improved performance for specific groups), but also the risk that in order to use our ideas developers require users to disclose information or try to infer it automatically.
Third, there is the risk that our work is interpreted as implying that how someone speaks is a consequence of their demographics.
For more detailed discussion of these and other issues see the "Limitations and Ethical Considerations" section of the paper.

## Citation

[Paper](https://arxiv.org/pdf/2010.02986.pdf)

```bibtex
@InProceedings{emnlp20demographics,
  title     = {Compositional Demographic Word Embeddings},
  author    = {Welch, Charles and Kummerfeld, Jonathan K. and P{\'e}rez-Rosas, Ver{\'o}nica and Mihalcea, Rada},
  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},
  month     = {November},
  year      = {2020},
  location  = {Online},
  url       = {https://arxiv.org/pdf/2010.02986.pdf},
  abstract  = {Word embeddings are usually derived from corpora containing text from many individuals, thus leading to general purpose representations rather than individually personalized representations. While personalized embeddings can be useful to improve language model performance and other language processing tasks, they can only be computed for people with a large amount of longitudinal data, which is not the case for new users. We propose a new form of personalized word embeddings that use demographic-specific word representations derived compositionally from full or partial demographic information for a user (i.e., gender, age, location, religion). We show that the resulting demographic-aware word representations outperform generic word representations on two tasks for English: language modeling and word associations. We further explore the trade-off between the number of available attributes and their relative effectiveness and discuss the ethical implications of using them.},
}
```
