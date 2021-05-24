+++
title = "Learning Whom to Trust with MACE (Hovy et al., NAACL 2013)"
date = 2017-10-19T17:08:50-04:00
draft = false

summary = "By using a generative model to explain worker annotations, we can more effectively predict the correct label, and which workers are spamming."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "naacl", "crowdsourcing"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

The standard way to get high quality annotations is to get labels from multiple people and take a majority vote.
Getting multiple annotations costs more, and the quality of annotators can vary considerably (with spamming at one extreme).
One way to avoid the quality issue is to restrict who can do the task (must have done X previous tasks with an accept rate of Y), but that limits the pool of available workers.
Another approach is to try to estimate the quality of annotator work using a statistical model.

Here a generative model is used, with the following structure:

- $T_i$, the true label, sampled with a uniform prior over labels
- $S_{ij}$, a binary variable indicating if the person is spamming or not, sampled as a Bernoulli variable with a Beta prior
- $A_{ij}$, the annotator's decision, if they are spamming it is sampled from a multinomial with parameters specific to them (with a Dirichlet prior), otherwise it is the true label

$A$ is observed, but $T$ and $S$ are not, so they use expectation maximization to get both model parameters and variable values.
To deal with nonconvexity they use 100 random restarts, deciding which is best based on how well the model describes the data.
Note - this model (and the code) was the basis of the error detection paper I [wrote about]({{< ref "2017-10-13_ErrorDetection.md" >}}) recently.

For predicting annotator quality the model is consistently effective across three datasets, though the Beta and Dirichlet priors are key for one (where annotator agreement was high on average).
For determining the correct answer it is slightly better than majority vote, though the gains are small.
The real advantage comes in deciding whether to discard data, where the choice of what to discard can be guided by the estimate of quality (this is what the error detection paper was doing).
A range of synthetic experiments also show positive results, though their design shares the assumptions about behaviour that are baked into the model.

I found a few results particularly interesting:

- As the number of annotators is decreased, the benefit of this approach over majority vote grows to be quite substantial (the main experiments are for data with 10 annotators).
- If you do use majority vote, use an odd number of annotators. Switching to an even number mainly seems to create ties. The right number is also very data dependent.
- Providing gold information as supervision within EM doesn't help much unless it is quite substantial (20%+ of the data)

## Citation

[Paper](https://aclanthology.org/N13-1132.pdf)

```bibtex
@InProceedings{hovy-EtAl:2013:NAACL-HLT,
  author    = {Hovy, Dirk  and  Berg-Kirkpatrick, Taylor  and  Vaswani, Ashish  and  Hovy, Eduard},
  title     = {Learning Whom to Trust with MACE},
  booktitle = {Proceedings of the 2013 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},
  month     = {June},
  year      = {2013},
  address   = {Atlanta, Georgia},
  publisher = {Association for Computational Linguistics},
  pages     = {1120--1130},
  url       = {https://aclanthology.org/N13-1132}
}
```

