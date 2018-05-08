+++
title = "The Fine Line between Linguistic Generalization and Failure in Seq2Seq-Attention Models (Weber et al., 2018)"
date = 2018-05-08T09:00:31-04:00
draft = false

summary = "We know that training a neural network involves optimising over a non-convex space, but using standard evaluation methods we see that our models..."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "gen-deep", "analysis", "neural-network"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

We know that training a neural network involves optimising over a non-convex space, but using standard evaluation methods we see that our models usually end up doing reasonably well.
This paper asks an important question - are those metrics measuring generalisability effectively?
In particular, if we sample our test set from a slightly different distribution of data, do models still work well?

As a controlled set up they form a simple dataset as follows for each sentence:

- Go through the sentence left to right
- For each word generate three words in the output, where the output words are randomly sampled from a small vocabulary that is unique to each input word

This is clearly learnable and it seems reasonable that a sequence-to-sequence neural model with attention should be able to learn it.
Experiments show they do, getting close to 100% on a test set sampled the same way as the training set (input length 5-10, no symbol used twice).
However, if the test set is slightly different, with sequences of length 11-15, then results vary from 0% to 98% depending on the random seed in training (other variations also lead to large variations).
What this means is that sometimes the model is not learning to generalise.
They also show that the models that do generalise can only do so in one way (e.g. remain effective when length varies, or remain effective when symbols are used more than once in the input).

A few takeaways:

- Make sure your training and testing data are sampled from the distribution you are interested in
- More study of training data order and weight initialisation is needed (these are the two factors impacted by the random seed)

Incidentally, I am a co-author on an ACL paper that points out a similar issue for mapping text questions to SQL queries.
If we restrict the test set to be novel queries (i.e. the model has to generalise) performance falls through the floor.


## Citation

[Paper](https://arxiv.org/abs/1805.01445)

```bibtex
@Article{Weber:2018:GenDeep,
   author = {Noah Weber, Leena Shekhar, Niranjan Balasubramanian},
    title = {The Fine Line between Linguistic Generalization and Failure in Seq2Seq-Attention Models},
  journal = {Workshop on New Forms of Generalization in Deep Learning and NLP (NAACL 2018)},
     year = {2018},
      url = {https://arxiv.org/abs/1805.01445},
}
```
