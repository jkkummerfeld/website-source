+++
title = "Detecting annotation noise in automatically labelled data (Rehbein and Ruppenhofer, ACL 2017)"
date = 2017-10-13T13:32:19-04:00
draft = false

summary = "When labeling a dataset automatically there are going to be errors, but we can use a generative model and active learning to guide effort to checking the examples most likely to be incorrect."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "acl", "annotation"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

Active learning doesn't seem to get much attention in NLP, probably because of fear that developing data based on the errors of one model will introduce a particular sampling bias.
This paper is a nice example of a problem it can be applied to that doesn't raise that issue: detecting all the errors in a system's output.

The scenario is that you have a bunch of models for doing a task (e.g. POS tagging) and a new dataset with no labeled data, which you would like to label.
Having a person label the data would take a long time and doesn't take advantage of these systems.
At the same time, we can't just run the systems and use their output because they aren't perfect, particularly out of domain.
We could run the systems and check their output, which could be faster than annotating directly, but would still take a long time.
If we don't mind having some errors, we can check just some output, but how do we decide what to check?

This paper applies the generative model from [MACE](https://aclanthology.org/N13-1132) to build a generative model of system outputs.
The model is:

- For each example, sample the true label with a uniform prior 
- Then, for each classifier, sample from a Bernoulli distribution to decide if they are good or not
- A good classifier returns the true label, a not good classifier samples from a multinomial over the options

Since we don't know the parameters of the model, or the true labels, use expectation maximisation to learn.

This work takes that model, trains it and uses it to identify the sample that is most uncertain.
A person annotates it, the correct label replaces one of the system predictions, and EM is run again.
This is repeated until either there appear to be no more errors, or annotators run out of time.

How well does it work?
The main metric is precision: how many of the instances asked for annotation actually have errors.
For POS tagging on WSJ text, the taggers initially get 2.5% of words wrong.
To get that down to 1.1% the precision is 33%, and to get it to 0.65% precision is 17.6%.
On an out of domain dataset, the error rate is 10% initially, and is down to 5% with a precision of 50%.
Put differently, in a dataset of 25,000 tokens, with 2,500 errors, after checking 2,500 tokens, there are only 1,250 errors (another 2,500 checks brings it down to 730).
It also works well for NER, and consistently does better than the alternative they compare to (consider the taggers a committee and find the examples with highest entropy, i.e. greatest disagreement).

This seems like a natural fit for [prodigy](https://prodi.gy/) and something that could be broadly useful.

## Citation

[Paper](https://aclanthology.org/P/P17/P17-1107.pdf)

```bibtex
@InProceedings{rehbein-ruppenhofer:2017:Long,
  author    = {Rehbein, Ines  and  Ruppenhofer, Josef},
  title     = {Detecting annotation noise in automatically labelled data},
  booktitle = {Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  month     = {July},
  year      = {2017},
  address   = {Vancouver, Canada},
  publisher = {Association for Computational Linguistics},
  pages     = {1160--1170},
  url       = {https://aclanthology.org/P17-1107}
}
```
