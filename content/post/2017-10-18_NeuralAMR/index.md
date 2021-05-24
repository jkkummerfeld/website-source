+++
title = "Addressing the Data Sparsity Issue in Neural AMR Parsing (Peng et al., EACL 2017)"
date = 2017-10-18T21:31:05-04:00
draft = false

summary = "Another paper looking at the issue of output symbol sparsity in AMR parsing, though here the solution is to group the consistent but rare symbols (rather than graph fragments like the paper last week). This drastically increases neural model performance, but does not reach the level of hybrid systems."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "eacl", "amr"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

This is another paper concerned with the challenge of sparsity in AMR parsing, specifically that there are an enormous number of output symbols in the parse trees and most are seen infrequently.
The system they develop is based on the encoder-decoder with attention approach, which has previously done poorly for AMR, partially because of sparsity.

Their solution is to merge certain types of symbols into groups (dates, named entities, rare verbs, constants, etc) and have a standard way to map from the surface form to the output symbol.
This is an alternative to the approach from the paper I [wrote about]({{< ref "2017-10-12_AMRalignment.md" >}}) last week.
They also introduce a completely separate idea, which is a different way to take an AMR graph and turn it into a linear sequence.
This change is necessary to make the output follow the form their model generates - a sequence (though there has been work on tree based LSTMs on the output side, so AMR could be directly generated, and I believe there has been some work on applying that to AMR).

Together these changes do substantially improve performance over previous encoder-decoder based work for AMR.
However, there is still a substantial gap between the system and state-of-the-art, presumably because of the additional resources that other systems indirectly use by running external systems for NER, dependency parsing, etc.
Given the recent success of multi-task learning with neural nets, it would be interesting to see if those resources could be used here to further boost performance.
It may also be productive to combine these ideas with the graph abstraction ideas from AMR alignment paper.

## Citation

[Paper](https://aclanthology.org/E/E17/E17-1035.pdf)

```bibtex
@InProceedings{peng-EtAl:2017:EACLlong1,
  author    = {Peng, Xiaochang  and  Wang, Chuan  and  Gildea, Daniel  and  Xue, Nianwen},
  title     = {Addressing the Data Sparsity Issue in Neural AMR Parsing},
  booktitle = {Proceedings of the 15th Conference of the European Chapter of the Association for Computational Linguistics: Volume 1, Long Papers},
  month     = {April},
  year      = {2017},
  address   = {Valencia, Spain},
  publisher = {Association for Computational Linguistics},
  pages     = {366--375},
  url       = {https://aclanthology.org/E17-1035}
}
```

