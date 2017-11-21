+++
title = "Attention Strategies for Multi-Source Sequence-to-Sequence Learning (Libovicky et al., 2017)"
date = 2017-11-21T16:42:19-05:00
draft = false

summary = "To apply attention across multiple input sources, it is best to apply attention independently and then have a second phase of attention over the summary vectors for each source."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "acl", "neural-network"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

Attention, a weighted average over vectors with weights determined based on context (usually decoder state), has proven effective in many NLP tasks.
There are several variants, and this paper adds new types that address the question of how to apply attention to different sources at the same time, such as text and an image.

They consider three general versions:

- Concatenation, just do attention separately then concatenate the vectors from the input sources
- Flat, do the weighted average over all of the inputs
- Hierarchical, do attention separately, but then combine the vectors with another phase of attention

They also explore two variations that are orthogonal to the list above:

- The first step and the last step in attention both involve the input vectors being multiplied by a weight matrix. Should that matrix be shared for the two steps, or different? (the first informs the decision of what to give high weight in the average, the second determines what is being averaged over)
- _sentinel gates_, a modification to the way the inputs and context vector are combined that allow one or the other to be ignored.

They consider two tasks, (1) translation when both an image and source sentence are given, (2) post-editing a translated sentence with the original source given.
The results show fairly clear trends, though the systems are not great compared to baselines (worse than a text only baseline for the first, and only slightly better than a direct MT system for the second).
The trends are that hierarchical is best, the sentinel doesn't help, and it is better to not share weights (though I wonder if that would be true when controlling for the total number of parameters).

## Citation

[Paper](http://aclweb.org/anthology/P17-2031)

```bibtex
@InProceedings{libovicky-helcl:2017:Short,
  author    = {Libovick\'{y}, Jind\v{r}ich  and  Helcl, Jind\v{r}ich},
  title     = {Attention Strategies for Multi-Source Sequence-to-Sequence Learning},
  booktitle = {Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},
  month     = {July},
  year      = {2017},
  address   = {Vancouver, Canada},
  publisher = {Association for Computational Linguistics},
  pages     = {196--202},
  url       = {http://aclweb.org/anthology/P17-2031}
}
```
