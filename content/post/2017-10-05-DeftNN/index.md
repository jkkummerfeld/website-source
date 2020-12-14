+++
title = "DeftNN: Addressing Bottlenecks for DNN Execution on GPUs via Synapse Vector Elimination and Near-compute Data Fission (Hill et al., MICRO 2017)"
date = 2017-10-05
publishdate = 2017-10-18
draft = false

summary = "GPU processing can be sped up ~2x by removing low impact rows from weight matrices, and switching to a specialised floating point representation."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "neural-network", "efficiency"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

This paper proposes two techniques for speeding up neural network execution on GPUs:

1. Reduce computation when doing matrix-multiply by removing rows.
2. Reduce communication on the GPU by halving the number of bits used to represent numbers.

Either of these gives a speed up of ~1.5x and together they give ~2x, across a range of different computer vision tasks+models.

## Core ideas in detail

The first idea, reducing work by eliminating parts of the computation, has been considered before.
In the past, however, the focus was on saving memory in models, and so the most common strategy was to move to a sparse matrix where weights close to zero are dropped.
Here the focus is on speed and they show that while the sparse approach saves memory it can end up being slower because of hardware behaviour.
Instead, they eliminate entire rows of the matrix, which means there is less computation, but it remains dense (and therefore fast).
Rows are identified by measuring correlation between outputs and greedily eliminating rows that correlate highly with the rest of the output.

The natural question to ask is whether this hurts performance.
First, they do two things to avoid problems, (1) a scale factor is used to make sure the outputs are of the same range that they would have been with the full matrix, and (2) they restart training to fine-tune the network once pruning is set up.
With high enough pruning accuracy does fall, but speed ups can be gained before that is a problem (the exact point depends on the task).

The second idea relates to numerical representation, and is motivated by measurements of where the bottlenecks are in communication.
Many AI researchers have tried switching to 16 bit representations to save space and time, but here they develop a different floating point encoding that gives more bits to the exponent, and fewer to the mantissa.

## Thoughts

- It would be interesting to see the interaction of this work with the investigation of networks without non-linear functions that can still learn non-linear behaviour because of numerical approximations.
- In the context of language, the weight reduction approach would be interesting to analyse. Specifically, what do we lose in our word vectors depending on the task?
- I've always had some interest in making things faster. It would be interesting to know where the remaining bottlenecks are (after applying these changes).

## Citation

```bibtex
@InProceedings{Hill:MICRO:2017,
  author    = {Hill, Parker and Jain, Animesh and Hill1, Mason and Zamirai, Babak and Hsu, Chang-Hong and Laurenzano, Michael A. and Mahlke, Scott and Tang, Lingjia and Mars, Jason},
  title = {DeftNN: Addressing Bottlenecks for DNN Execution on GPUs via Synapse Vector Elimination and Near-compute Data Fission},
  booktitle = {The 50th Annual IEEE/ACM International Symposium on Microarchitecture},
  year = {2017},
}
```
