---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Iterative Feature Mining for Constraint-Based Data Collection to Increase Data Diversity and Model Robustness (Larson, et al., EMNLP 2020)"
subtitle: ""
summary: "When we crowdsource data for tasks like SRL and sentiment analysis we only care about accuracy.  For tasks where workers write new content, such as paraphrasing and creating questions, we also care about data diversity.  If our data is not diverse then models trained on it will not be robust in the real world.  The core idea of this paper is to encourage creativity by constraining workers."
authors: []
tags: ["crowdsourcing", "dialogue"]
categories: []
date: 2020-10-12T10:28:13-05:00
lastmod: 2020-10-12T10:28:13-05:00
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

When we crowdsource data for tasks like SRL and sentiment analysis we only care about accuracy.
For tasks where workers write new content, such as paraphrasing and creating questions, we also care about data diversity.
If our data is not diverse then models trained on it will not be robust in the real world.
The core idea of this paper is to encourage creativity by constraining workers.

We use three steps:

1. Collect some data.
2. Create a taboo list of words / phrases based on the data collected.
3. Return to step 1, but tell workers they can't use things in the taboo list.

We explored this idea for task-oriented dialogue.
We identified taboo words using an SVM with a bag-of-words to identify common words associated with specific intents or slot values.
Depending on the taboo word, we got quite different paraphrases.
For example, for the sentence "What is the capital of Florida?" we collected paraphrases with various taboo words:

| Taboo Word | Paraphrases                                     |
|------------|-------------------------------------------------|
|            | what city is the state capital of florida       |
| florida    | what is the capital of the sunshine state       |
| capital    | where is the seat of government in florida      |
| what       | tell me the name of florida's capital           |

These examples show interesting variations, but to see if the variations are significant we tried collecting new test sets for five intent classification datasets and four slot filling datasets.
With just two taboo words, a BERT based model trained on the original dataset did considerably worse on our new data.
The drop varied from 2 to 33 points, with a median of 9.
This indicates that we are capturing ways of expressing these intents that are not well covered by the original data.

Addressing this issue is simple - train on data collected with our method!
Interestingly, this approach is complementary to the outlier-based approach from [our NAACL 2019 paper](http://jkk.name/publication/naacl19outliers/).
Examples collected using one approach are hard for models trained on data from the other.
Fortunately, training with data from a mix of the two leads to strong results on both.

I'm particularly excited about this work because the general idea could be applied in so many ways:

- Change the task.
- Vary the type of taboo item (e.g. phrases instead of words).
- Try other ways of selecting taboo items.
- Use a different mapping from taboo items to tasks.

In fact, more specific versions of this idea have already been used.
[Luis von Ahn's ESP game](https://dl.acm.org/doi/10.1145/985692.985733) for image captioning used a taboo list.
Each image had a list of complete labels previously assigned to the image.
New labels could not match an existing label.
That work predates this paper by 16 years, but hasn't had much traction in the NLP community, possibly because of the limitation of requiring complete matches on labels (making it impractical for sentences or even phrases).
I'm hopeful that our more general version will be useful in a range of crowdsourcing efforts.

## Citation

[Paper](http://www.jkk.name/pub/emnlp20taboo.pdf)

```bibtex
@InProceedings{emnlp20taboo,
  title     = {Iterative Feature Mining for Constraint-Based Data Collection to Increase Data Diversity and Model Robustness},
  author    = {Larson, Stefan and Zheng, Anthony and Mahendran, Anish and Tekriwal, Rishi and Cheung, Adrian and Guldan, Eric and Leach, Kevin and Kummerfeld, Jonathan K.},
  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},
  month     = {November},
  year      = {2020},
  location  = {Online},
  url       = {http://www.jkk.name/pub/emnlp20taboo.pdf},
}
```
