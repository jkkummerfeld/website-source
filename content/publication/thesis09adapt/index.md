---

bibkey: thesis09adapt

title: Adaptive Supertagging for Faster Parsing

date: "2009-01-01"

year: 2009

draft: false

preprint: false

archival: true

authors: 
- admin

publication_types: ["7"]

publication: The University of Sydney

publication_short: The University of Sydney

abstract: Statistical parsers are crucial for tackling the grand challenges of Natural Language Processing. The most effective approaches to these tasks are data driven, but parsers are too slow to be effectively used on large data sets. State-of-the-art parsers generally cannot process more than one sentence a second, and the fastest cannot process more than fifty sentences a second. The situation is even worse when they are applied outside of the domain of their training data. The fastest systems have two components, a parser, which has time complexity O(n3) and a supertagger, which has linear time complexity. By shifting work from the parser to the supertagger we dramatically improve speed.\n\nThis work demonstrates several major novel ideas that improve parsing efficiency. The core idea is that the tags chosen by the parser are gold standard data for its supertagger. This leads to the second surprising conceptual development, that decreasing tagging accuracy can improve parsing performance. To demonstrate these ideas required extensive development of the C&C supertagger, including imple- mentation of more efficient estimation algorithms and parallelisation of the training process. This was particularly challenging as the C&C supertagger is a state-of-the-art high performance system designed with a focus on speed rather than flexibility.\n\nI was able to significantly improve performance on the standard evaluation corpus by using the parser to generate extremely large new resources for supertagger training. I have also shown that these methods provide significant benefits on another domain, Wikipedia text, without the cost of generating human annotated data sets. These parsing performance gains occur while supertagging accuracy decreases.\n\nDespite extensive use of supertaggers to improve parsing efficiency there has been no comprehensive study of the interaction between a supertagger and a parser. I present the first systematic exploration of the relationship, show the potential benefits of understanding it, and demonstrate a novel algorithm for optimising the parameters that define it.\n\nI have constructed models that process newspaper text 86% faster than previously, and Wikipedia text 30% faster, without any loss in accuracy and without the aid of extra gold standard resources in either domain. This work will lead directly to improvements in a range of Natural Language Processing tasks by enabling the use of far more parsed data.

abstract_short: Statistical parsers are crucial for tackling the grand challenges of Natural Language Processing. The most effective approaches to these tasks are data driven, but parsers are too slow to be effectively used on large data sets. State-of-the-art parsers generally cannot process more than one sentence a second, and the fastest cannot process more than fifty sentences a second. The situation is even worse when they are applied outside of the domain of their training data. The fastest systems have two components, a parser, which has time complexity O(n3) and a supertagger, which has linear time complexity. By shifting work from the parser to the supertagger we dramatically improve speed.\n\nThis work demonstrates several major novel ideas that improve parsing efficiency. The core idea is that the tags chosen by the parser are gold standard data for its supertagger. This leads to the second surprising conceptual development, that decreasing tagging accuracy can improve parsing performance. To demonstrate these ideas required extensive development of the C&C supertagger, including imple- mentation of more efficient estimation algorithms and parallelisation of the training process. This was particularly challenging as the C&C supertagger is a state-of-the-art high performance system designed with a focus on speed rather than flexibility.\n\nI was able to significantly improve performance on the standard evaluation corpus by using the parser to generate extremely large new resources for supertagger training. I have also shown that these methods provide significant benefits on another domain, Wikipedia text, without the cost of generating human annotated data sets. These parsing performance gains occur while supertagging accuracy decreases.\n\nDespite extensive use of supertaggers to improve parsing efficiency there has been no comprehensive study of the interaction between a supertagger and a parser. I present the first systematic exploration of the relationship, show the potential benefits of understanding it, and demonstrate a novel algorithm for optimising the parameters that define it.\n\nI have constructed models that process newspaper text 86% faster than previously, and Wikipedia text 30% faster, without any loss in accuracy and without the aid of extra gold standard resources in either domain. This work will lead directly to improvements in a range of Natural Language Processing tasks by enabling the use of far more parsed data.

address: 

doi: 

issue: 

number: 

pages: 

publisher: 

volume: 

math: true

highlight: false

image_preview: 

selected: false

url_pdf: "http://www.jkk.name/pub/thesis09adapt_thesis.pdf"

url_poster: "http://www.jkk.name/pub/thesis09adapt_poster.pdf"

url_interview: 

url_arxiv: 

url_code: 

url_dataset: 

url_project: 

url_slides: 

url_video: 

url_blog: 

links: 
- name: PDF Slides
  url: http://www.jkk.name/pub/thesis09adapt_slides.pdf

citation_count: 0
citations:


---