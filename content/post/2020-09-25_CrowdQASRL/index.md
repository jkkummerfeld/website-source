---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Controlled Crowdsourcing for High-Quality QA-SRL Annotation (Roit, et al., ACL 2020)"
subtitle: ""
summary: "Semantic Role Labeling captures the content of a sentence by labeling the word sense of the verbs and identifying their arguments.  Over the last few years, [Luke Zettlemoyer's Group](https://www.cs.washington.edu/people/faculty/lsz/) has been exploring using question-answer pairs to represent this structure.  This approach has the big advantage that it is easier to explain than the sense inventory and role types of more traditional SRL resources like PropBank.  However, even with that advantage, crowdsourcing this annotation is difficult, as this paper shows."
authors: []
tags: ["srl", "crowdsourcing", "paper", "data"]
categories: []
date: 2020-09-25T10:17:18-05:00
lastmod: 2020-09-25T10:17:18-05:00
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

Semantic Role Labeling captures the content of a sentence by labeling the word sense of the verbs and identifying their arguments.
Over the last few years, [Luke Zettlemoyer's Group](https://www.cs.washington.edu/people/faculty/lsz/) has been exploring using question-answer pairs to represent this structure.
This approach has the big advantage that it is easier to explain than the sense inventory and role types of more traditional SRL resources like PropBank.
However, even with that advantage, crowdsourcing this annotation is difficult, as this paper shows.

I got three main things out of this paper:

1. It shifted my approach to crowdsourcing to consider workers more like traditional expert annotators.
2. It reinforced the idea that small shifts in crowd workflows can have a major impact on annotation quality.
3. QA-SRL can capture roles not covered by PropBank.

The work also provides a new dataset that will be useful for future work on this problem, and useful benchmarks of systems and measurements of data quality.
Expanding on the three points above:

Crowd workers: The paper argues in favour of putting more time into training workers.
Most of the work I've seen in NLP for crowdsourcing (including my own) focuses on modifying task design or using ML post-processing to improve results.
Here, they run a large-scale qualification task and filter workers based on their performance, then train those workers by paying them to read a set of instructions (23 text-dense slides) and do two small annotation rounds with feedback after each one.
This increases the upfront cost, but reduces the cost of annotation by reducing the need for multiple annotations of each item.
The paper doesn't provide quite enough detail to quantify the cost.
We do know that to get to 11 workers they needed to train 30 workers at a cost of 2 hours each plus 30 minutes of researcher time each.
If we assume 60 workers did the preliminary round, each taking 5 minutes, and that workers cost <span>$</span>12 / hour (<span>$</span>10 to the workers, <span>$</span>2 to Amazon), that's almost <span>$</span>800 plus 15 hours of researcher time.
For a large annotation effort, the savings during annotation will make that worth it (or, as in this case, it will lead to higher quality data).
I am curious which aspect was more important though - filtering the pool of workers, or training workers.

Workflow impact: In previous QA-SRL work, one worker wrote a question and its answers and two workers checked the question and independently added answers.
Here, two workers independently write a question+answer and a third work consolidates the annotations into a final annotation.
The cost for a label is about the same (54c / predicate vs. 51c / predicate), but coverage is considerably higher.
The design space for crowd workflows is huge and this is another example of how important it is to explore.
It's also possible that the changes in recruitment and training were more critical than the workflow shift, but the study didn't include evaluation with only one or the other.

QA-SRL vs. PropBank: This may be less surprising to someone who works more on SRL, but they found their approach captured many implicit roles that PropBank does not.
Specifically, of 100 annotated arguments that were not in PropBank, 68 were valid implicit arguments.
I'm curious about what those implicit arguments are capturing.
Maybe targeted re-annotation could be used to add them to PropBank (identifying relevant sentences by trace parsing).

## Citation

[Paper](https://www.aclweb.org/anthology/2020.acl-main.626/)

[Code](https://github.com/plroit/qasrl-gs)

[My Tweet](https://twitter.com/jkkummerfeld/status/1309592830537543681?s=20)

```bibtex
@inproceedings{roit-etal-2020-controlled,
    title = "Controlled Crowdsourcing for High-Quality {QA}-{SRL} Annotation",
    author = "Roit, Paul  and
      Klein, Ayal  and
      Stepanov, Daniela  and
      Mamou, Jonathan  and
      Michael, Julian  and
      Stanovsky, Gabriel  and
      Zettlemoyer, Luke  and
      Dagan, Ido",
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics",
    month = "jul",
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.acl-main.626",
    doi = "10.18653/v1/2020.acl-main.626",
    pages = "7008--7013",
    abstract = "Question-answer driven Semantic Role Labeling (QA-SRL) was proposed as an attractive open and natural flavour of SRL, potentially attainable from laymen. Recently, a large-scale crowdsourced QA-SRL corpus and a trained parser were released. Trying to replicate the QA-SRL annotation for new texts, we found that the resulting annotations were lacking in quality, particularly in coverage, making them insufficient for further research and evaluation. In this paper, we present an improved crowdsourcing protocol for complex semantic annotation, involving worker selection and training, and a data consolidation phase. Applying this protocol to QA-SRL yielded high-quality annotation with drastically higher coverage, producing a new gold evaluation dataset. We believe that our annotation protocol and gold standard will facilitate future replicable research of natural semantic annotations.",
}
```
