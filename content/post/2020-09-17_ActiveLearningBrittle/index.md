---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Practical Obstacles to Deploying Active Learning (Lowell, et al., EMNLP 2019)"
subtitle: ""
summary: "Training models requires massive amounts of labeled data.  We usually sample data iid from the target domain (e.g. newspapers), but it seems intuitive that this means we wast effort labeling samples that are obvious or easy and so not informative during training.  Active Learning follows that intuition, labeling data incrementally, selecting the next example(s) to label based on what a model considers uncertain.  Lots of work has shown this can be effective for that model, but if the labeled dataset is then used to train another model will it also do well?"
authors: []
tags: ["paper", "annotation"]
categories: []
date: 2020-09-17T15:08:35-05:00
lastmod: 2020-09-17T15:08:35-05:00
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

Training models requires massive amounts of labeled data.
We usually sample data iid from the target domain (e.g. newspapers), but it seems intuitive that this means we wast effort labeling samples that are obvious or easy and so not informative during training.
Active Learning follows that intuition, labeling data incrementally, selecting the next example(s) to label based on what a model considers uncertain.
Lots of work has shown this can be effective for that model, but if the labeled dataset is then used to train another model will it also do well?

For text classification this paper finds the answer is no: training model X on iid samples is as good or better than training on samples collected while active learning with model Y.
They show this through experiments with four datasets and three models, training on up to 25% of the available data.
For named entity recognition the story is different in my opinion - iid is consistently slightly worse, though the gains from active learning are small in all cases (0 to 0.6 point gain for the better model, 0.4 to 1.7 for the weaker model).
One caveat is that these models are not state-of-the-art.
For CoNLL 2003 NER, many models score [around 93](https://nlpprogress.com/english/named_entity_recognition.html), but these models are getting 70-90.
On OntoNotes, the best results are close to 90, but these models get 74-85.
This is still an interesting result, but I'm left with a few questions:

- This work focused on a low data scenario. What if I have a lot of data? It may be that sampling iid and active learning based samples were similar here because either way the data was capturing the core phenomena. The challenge here is that you can't run this experiment easily with an existing dataset (unless it is truly massive).
- How does the sampled data differ from iid data? Is there a significant shift in the distribution of class types?
- What about using a hybrid approach, with some data sampled iid and other data sampled randomly?

Overall, what I take away from this work is that active learning may not be the right choice for building a small dataset in NLP.
For large datasets, building models, or other tasks and domains the conclusions are less clear, though it is certainly worth being aware of the risk that a dataset made with active learning may not be equally useful to all models.

## Citation

[Paper](https://www.aclweb.org/anthology/D19-1003.pdf)

Twitter discussion in [2018](https://twitter.com/zacharylipton/status/1019222882482905088)) and [2019](https://twitter.com/zacharylipton/status/1165692913290043398?s=20).

```bibtex
@inproceedings{lowell-etal-2019-practical,
    title = "Practical Obstacles to Deploying Active Learning",
    author = "Lowell, David  and
      Lipton, Zachary C.  and
      Wallace, Byron C.",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)",
    month = "nov",
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/D19-1003",
    doi = "10.18653/v1/D19-1003",
    pages = "21--30",
    abstract = "Active learning (AL) is a widely-used training strategy for maximizing predictive performance subject to a fixed annotation budget. In AL, one iteratively selects training examples for annotation, often those for which the current model is most uncertain (by some measure). The hope is that active sampling leads to better performance than would be achieved under independent and identically distributed (i.i.d.) random samples. While AL has shown promise in retrospective evaluations, these studies often ignore practical obstacles to its use. In this paper, we show that while AL may provide benefits when used with specific models and for particular domains, the benefits of current approaches do not generalize reliably across models and tasks. This is problematic because in practice, one does not have the opportunity to explore and compare alternative AL strategies. Moreover, AL couples the training dataset with the model used to guide its acquisition. We find that subsequently training a successor model with an actively-acquired dataset does not consistently outperform training on i.i.d. sampled data. Our findings raise the question of whether the downsides inherent to AL are worth the modest and inconsistent performance gains it tends to afford.",
}
```
