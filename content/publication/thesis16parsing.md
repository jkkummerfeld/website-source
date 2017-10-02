+++
bibkey = "thesis16parsing"
bibtex = """@PhDThesis{thesis16parsing,
  title     = {Algorithms for Identifying Syntactic Errors and Parsing with Graph Structured Output},
  author    = {Jonathan K. Kummerfeld},
  year      = {2016},
  month     = {Aug},
  address   = {Berkeley, CA, USA},
  school    = {EECS Department, University of California, Berkeley},
  number    = {UCB/EECS-2016-138},
  url       = {https://www2.eecs.berkeley.edu/Pubs/TechRpts/2016/EECS-2016-138.html},
  abstract  = {Representation of syntactic structure is a core area of research in Computational Linguistics, disambiguating distinctions in meaning that are crucial for correct interpretation of language. Development of algorithms and statistical models over the past three decades has led to systems that are accurate enough to be deployed in industry, playing a key role in products such as Google Search and Apple Siri. However, syntactic parsers today are usually constrained to tree representations of language, and performance is interpreted through a single metric that conveys no linguistic information regarding remaining errors.

  In this dissertation, we present new algorithms for error analysis and parsing. The heart of our approach to error analysis is the use of structural transformations to identify more meaningful classes of errors, and to enable comparisons across formalisms. For parsing, we combine a novel dynamic program with careful choices in syntactic representation to create an efficient parser that produces graph structured output. Together, these developments allowed us to evaluate the outstanding challenges in parsing and to address a key weakness in current work.

  First, we present a search algorithm that, given two structures, finds a sequence of modifications leading from one structure to the other. We applied this algorithm to syntactic error analysis, where one structure is the output of a parser, the other is the correct parse, and each modification corresponds to fixing one error. We constructed a tool based on the algorithm and analyzed variations in behavior between parsers, types of text, and languages. Our observations shine light on several assumptions about syntactic errors, showing some to be true and others to be false. For example, prepositional phrase attachment errors are indeed a major issue, while coordination scope errors do not hurt performance as much as expected.

  Next, we describe an algorithm that builds a parse in one syntactic representation to match a parse in another representation. Specifically, we build phrase structure parses from Combinatory Categorial Grammar derivations. Our approach follows the philosophy of CCG, defining specific phrase structures for each lexical category and generic rules for combinatory steps. The new parse is built by following the CCG derivation bottom-up, gradually building the corresponding phrase structure parse. This produced significantly more accurate parses than past work, and enabled us to compare performance of several parsers across formalisms.

  Finally, we address a weakness we observed in phrase structure parsers: the exclusion of syntactic trace structures for computational convenience. We present an efficient dynamic programming algorithm that constructs the graph structure that has the highest score under an edge-factored scoring function. We define a parse representation compatible with the algorithm, and show how certain linguistic distinctions dramatically impact coverage. We also show various ways to modify the algorithm to improve performance by exploiting properties of observed linguistic structure. This approach to syntactic parsing is the first to cover virtually all structure encoded in the Penn Treebank.},
}
"""
title = "Algorithms for Identifying Syntactic Errors and Parsing with Graph Structured Output"
date = "2016-01-01"
draft = false
authors = ["Jonathan K. Kummerfeld"]
publication_types = ["4"]
publication = "EECS Department, University of California, Berkeley"
publication_short = "EECS Department, University of California, Berkeley"
abstract = """Representation of syntactic structure is a core area of research in Computational Linguistics, disambiguating distinctions in meaning that are crucial for correct interpretation of language. Development of algorithms and statistical models over the past three decades has led to systems that are accurate enough to be deployed in industry, playing a key role in products such as Google Search and Apple Siri. However, syntactic parsers today are usually constrained to tree representations of language, and performance is interpreted through a single metric that conveys no linguistic information regarding remaining errors.

In this dissertation, we present new algorithms for error analysis and parsing. The heart of our approach to error analysis is the use of structural transformations to identify more meaningful classes of errors, and to enable comparisons across formalisms. For parsing, we combine a novel dynamic program with careful choices in syntactic representation to create an efficient parser that produces graph structured output. Together, these developments allowed us to evaluate the outstanding challenges in parsing and to address a key weakness in current work.

First, we present a search algorithm that, given two structures, finds a sequence of modifications leading from one structure to the other. We applied this algorithm to syntactic error analysis, where one structure is the output of a parser, the other is the correct parse, and each modification corresponds to fixing one error. We constructed a tool based on the algorithm and analyzed variations in behavior between parsers, types of text, and languages. Our observations shine light on several assumptions about syntactic errors, showing some to be true and others to be false. For example, prepositional phrase attachment errors are indeed a major issue, while coordination scope errors do not hurt performance as much as expected.

Next, we describe an algorithm that builds a parse in one syntactic representation to match a parse in another representation. Specifically, we build phrase structure parses from Combinatory Categorial Grammar derivations. Our approach follows the philosophy of CCG, defining specific phrase structures for each lexical category and generic rules for combinatory steps. The new parse is built by following the CCG derivation bottom-up, gradually building the corresponding phrase structure parse. This produced significantly more accurate parses than past work, and enabled us to compare performance of several parsers across formalisms.

Finally, we address a weakness we observed in phrase structure parsers: the exclusion of syntactic trace structures for computational convenience. We present an efficient dynamic programming algorithm that constructs the graph structure that has the highest score under an edge-factored scoring function. We define a parse representation compatible with the algorithm, and show how certain linguistic distinctions dramatically impact coverage. We also show various ways to modify the algorithm to improve performance by exploiting properties of observed linguistic structure. This approach to syntactic parsing is the first to cover virtually all structure encoded in the Penn Treebank."""
abstract_short = """Representation of syntactic structure is a core area of research in Computational Linguistics, disambiguating distinctions in meaning that are crucial for correct interpretation of language. Development of algorithms and statistical models over the past three decades has led to systems that are accurate enough to be deployed in industry, playing a key role in products such as Google Search and Apple Siri. However, syntactic parsers today are usually constrained to tree representations of language, and performance is interpreted through a single metric that conveys no linguistic information regarding remaining errors.

In this dissertation, we present new algorithms for error analysis and parsing. The heart of our approach to error analysis is the use of structural transformations to identify more meaningful classes of errors, and to enable comparisons across formalisms. For parsing, we combine a novel dynamic program with careful choices in syntactic representation to create an efficient parser that produces graph structured output. Together, these developments allowed us to evaluate the outstanding challenges in parsing and to address a key weakness in current work.

First, we present a search algorithm that, given two structures, finds a sequence of modifications leading from one structure to the other. We applied this algorithm to syntactic error analysis, where one structure is the output of a parser, the other is the correct parse, and each modification corresponds to fixing one error. We constructed a tool based on the algorithm and analyzed variations in behavior between parsers, types of text, and languages. Our observations shine light on several assumptions about syntactic errors, showing some to be true and others to be false. For example, prepositional phrase attachment errors are indeed a major issue, while coordination scope errors do not hurt performance as much as expected.

Next, we describe an algorithm that builds a parse in one syntactic representation to match a parse in another representation. Specifically, we build phrase structure parses from Combinatory Categorial Grammar derivations. Our approach follows the philosophy of CCG, defining specific phrase structures for each lexical category and generic rules for combinatory steps. The new parse is built by following the CCG derivation bottom-up, gradually building the corresponding phrase structure parse. This produced significantly more accurate parses than past work, and enabled us to compare performance of several parsers across formalisms.

Finally, we address a weakness we observed in phrase structure parsers: the exclusion of syntactic trace structures for computational convenience. We present an efficient dynamic programming algorithm that constructs the graph structure that has the highest score under an edge-factored scoring function. We define a parse representation compatible with the algorithm, and show how certain linguistic distinctions dramatically impact coverage. We also show various ways to modify the algorithm to improve performance by exploiting properties of observed linguistic structure. This approach to syntactic parsing is the first to cover virtually all structure encoded in the Penn Treebank."""
address = "Berkeley, CA, USA"
doi = ""
issue = ""
number = "UCB/EECS-2016-138"
pages = ""
publisher = ""
volume = ""
math = true
highlight = false
image_preview = ""
selected = false
url_pdf = "https://www2.eecs.berkeley.edu/Pubs/TechRpts/2016/EECS-2016-138.html"
url_poster = ""
url_code = ""
url_dataset = ""
url_project = ""
url_slides = ""
url_video = ""



+++