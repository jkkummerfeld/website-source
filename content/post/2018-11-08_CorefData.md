+++
title = "PreCo: A Large-scale Dataset in Preschool Vocabulary for Coreference Resolution (Chen et al., 2018)"
date = 2018-11-08T11:29:32-05:00
draft = false

summary = "The OntoNotes dataset, which is the focus of almost all coreference resolution research, had several compromises in its development (as is the case for any dataset).  Some of these are discussed in..."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "data", "coreference"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

The OntoNotes dataset, which is the focus of almost all coreference resolution research, had several compromises in its development (as is the case for any dataset).
Some of these are discussed in my [CoNLL Shared Task submission paper](http://jkk.name/publication/conll11coreference/), the biggest being the choice to not annotate mentions that are not coreferent.
This paper describes a new dataset that has a different set of compromises, specifically:

- A broader definition of coreference (e.g. appositives are coreferent)
- All mentions annotated
- Different annotation methods for different subsets of the data (training data is double annotated and then adjudicated, while the development and test data is triple annotated, all pairs of annotations are adjudicated, then the outcomes are merged by voting)
- A variety of genres, but generally simpler language

The dataset is 10x the size of OntoNotes and freely available, which is fantastic.
The source text is 2/3rds the RACE dataset (English reading comprehension exams from China), and 1/3rd scraped websites.
Measurements of annotator agreement suggest the annotations are not as consistent as OntoNotes, but still good enough to be a useful resource.
I do disagree with one aspect of the paper's analysis - the results show a substantial gain in performance when providing gold mentions, suggesting to me that it remains an important challenge in coreference resolution.
I'm also curious whether my [coreference analysis tool](http://jkk.name/publication/emnlp13analysis/) would find different patterns in errors on this dataset compared to OntoNotes.

## Citation

[Paper](http://aclweb.org/anthology/D18-1016)

[Data](https://preschool-lab.github.io/PreCo/)

```bibtex
@InProceedings{Chen:EMNLP:2018,
  author    = {Chen, Hong and Fan, Zhenhua and Lu, Hao and Yuille, Alan and Rong, Shu},
  title     = {PreCo: A Large-scale Dataset in Preschool Vocabulary for Coreference Resolution},
  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},
  year      = {2018},
  publisher = {Association for Computational Linguistics},
  pages     = {172--181},
  location  = {Brussels, Belgium},
  url       = {http://aclweb.org/anthology/D18-1016},
}
```

