---

bibkey: emnlp20lm

title: Improving Low Compute Language Modeling with In-Domain Embedding Initialisation

date: "2020-11-01"

year: 2020

draft: false

preprint: false

archival: true

authors: 
- Charles Welch
- Rada Mihalcea
- admin

publication_types: ["1"]

publication: Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing

publication_short: EMNLP (short)

abstract: Many NLP applications, such as biomedical data and technical support, have 10-100 million tokens of in-domain data and limited computational resources for learning from it. How should we train a language model in this scenario? Most language modeling research considers either a small dataset with a closed vocabulary (like the standard 1 million token Penn Treebank), or the whole web with byte-pair encoding. We show that for our target setting in English, initialising and freezing input embeddings using in-domain data can improve language model performance by providing a useful representation of rare words, and this pattern holds across several different domains. In the process, we show that the standard convention of tying input and output embeddings does not improve perplexity when initializing with embeddings trained on in-domain data.

abstract_short: Many NLP applications, such as biomedical data and technical support, have 10-100 million tokens of in-domain data and limited computational resources for learning from it. How should we train a language model in this scenario? Most language modeling research considers either a small dataset with a closed vocabulary (like the standard 1 million token Penn Treebank), or the whole web with byte-pair encoding. We show that for our target setting in English, initialising and freezing input embeddings using in-domain data can improve language model performance by providing a useful representation of rare words, and this pattern holds across several different domains. In the process, we show that the standard convention of tying input and output embeddings does not improve perplexity when initializing with embeddings trained on in-domain data.

address: 

doi: 10.18653/v1/2020.emnlp-main.696

issue: 

number: 

pages: 8625--8634

publisher: 

volume: 

math: true

highlight: false

image_preview: 

selected: false

url_pdf: "https://www.aclweb.org/anthology/2020.emnlp-main.696"

url_poster: 

url_interview: 

url_arxiv: "https://arxiv.org/abs/2009.14109"

url_code: "https://github.com/jkkummerfeld/emnlp20lm"

url_dataset: 

url_project: 

url_slides: 

url_video: 

url_blog: /post/2020-09-29_PretrainingLM/

links: 
- name: Supplementary Material
  url: https://www.aclweb.org/anthology/attachments/2020.emnlp-main.696.OptionalSupplementaryMaterial.zip
- name: ArXiv
  url: https://arxiv.org/abs/2009.14109

citation_count: 0
citations:


---