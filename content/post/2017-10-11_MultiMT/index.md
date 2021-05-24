+++
title = "Google's Multilingual Neural Machine Translation System: Enabling Zero-Shot Translation (Johnson et al., TACL 2017)"
date = 2017-10-11T17:29:04-04:00
draft = false

summary = "A translation model trained on sentence pairs from a mixture of languages can do very well across all of the languages, and even generalise somewhat to new pairs of the languages. That's useful as one model can do the work of $O(n^2)$ models, and with a fraction of the parameters."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "tacl", "mt"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

This paper is a detailed analysis of a surprisingly effective simple idea: train a machine translation system with sentence pairs from multiple languages, adjusting the input to have an extra token at the end that says what the target language is.
To deal with class imbalance, data is oversampled to have all language pairs be equally represented (though even without that, it works fairly well).

The biggest advantage of this approach is that a single model can handle translation between many pairs, rather than needing $O(n^2)$ models for $n$ languages.
The performance is slightly lower on average, but the single model can manage with far fewer parameters.
In one example, twelve models are combined into a single model with as many parameters as one of the twelve, and the results are lower by just 0.76 BLEU on average.
Another advantage of the model is the ability to handle code-switched language, though they didn't have evaluation datasets to get an quantitative measure of accuracy.

Having this model also opens up the possibility of translating between pairs of languages with no parallel training data (A -> B).
As long as there is data (A -> C) and (D -> B), sentences from A can be fed in with B as the target language.
For closely related languages this works very well, and in particular, better than going via another language such that there is data for the two language pairs.
For example, going from Portuguese to Spanish with the multilingual model scores 24.75, whereas going via English scores 21.62 and a model with explicit training data gets 31.50.
Going between less related languages is less successful, with direct Spanish to Japanese scoring 9.14, and going via English scoring 18.00.
One thing I wish the paper had is more exploration of this result - what does it get right when scoring 9.14?
For the time being at least, going via a third language still seems necessary, and presumably the best language to use is whichever one the performance is highest on.

## Citation

[Paper](https://aclanthology.org/Q/Q17/Q17-1024.pdf)

[ArXiv version](https://arxiv.org/pdf/1611.04558.pdf) which appears to be the same aside from one extra figure of the model architecture.

As an aside, it is interesting to see the timeline for this paper:

- November 2016, Submission to ArXiv and in the TACL submission batch
- March 2017, TACL revision batch
- October 2017, TACL published

```bibtex
@article{TACL1081,
	author    = {Johnson, Melvin  and Schuster, Mike  and Le, Quoc  and Krikun, Maxim  and Wu, Yonghui  and Chen, Zhifeng  and Thorat, Nikhil  and Viégas, Fernanda  and Wattenberg, Martin  and Corrado, Greg  and Hughes, Macduff  and Dean, Jeffrey},
	title     = {Google's Multilingual Neural Machine Translation System: Enabling Zero-Shot Translation},
	journal   = {Transactions of the Association for Computational Linguistics},
	volume    = {5},
	year      = {2017},
	issn      = {2307-387X},
	url       = {https://www.transacl.org/ojs/index.php/tacl/article/view/1081},
	pages     = {339--351}
}
```

