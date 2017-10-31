+++
title = "Real-time Captioning by Groups of Non-experts (Lasecki et al., 2012)"
date = 2017-10-31T13:23:13-04:00
draft = false

summary = "By dividing a task up among multiple annotators carefully we can achieve high-quality real-time annotation of data, in this case transcription of audio."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "crowdsourcing"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

For any given task, automatic systems are fast, while annotation is accurate.
This work is about bridging that gap to provide a way for a team of annotators to produce real-time high quality labels.
The specific application is speech transcription, in which automatic systems are not accurate, while average people are slow (experts can transcribe in real time, but are very expensive).

The solution is to carefully break up the task and combine annotations back together.
To get it to work well there are a range of subtle design decisions:

- People hear the entire audio stream, but with their section at normal volume and the rest quieter. This allows them to focus their effort while still understanding the context.
- The alignment process combines annotations with guidance from a language model and a model of typos based on keyboard layout.
- Words are locked in shortly after being typed, to encourage workers to go on rather than revising their own errors.

Follow up work added several more ideas to improve performance:

- Time warping, slowing down to half speed for their section, then going to 1.5x for the rest.
- Use ASR as well, either as another worker (with very uncorrelated errors), or as a starting point for human editing (or vice versa).
- Use A\* search rather than a greedy algorithm for the alignment.

Performance does not reach the level of a professional, but is far better than ASR.
From the paper it's tricky to see a final cost, but it is certainly far lower than the professional.

## Citation

[Paper](http://doi.acm.org/10.1145/2380116.2380122)

```bibtex
@inproceedings{Lasecki:2012:RCG:2380116.2380122,
 author = {Lasecki, Walter and Miller, Christopher and Sadilek, Adam and Abumoussa, Andrew and Borrello, Donato and Kushalnagar, Raja and Bigham, Jeffrey},
 title = {Real-time Captioning by Groups of Non-experts},
 booktitle = {Proceedings of the 25th Annual ACM Symposium on User Interface Software and Technology},
 series = {UIST '12},
 year = {2012},
 isbn = {978-1-4503-1580-7},
 location = {Cambridge, Massachusetts, USA},
 pages = {23--34},
 numpages = {12},
 url = {http://doi.acm.org/10.1145/2380116.2380122},
 doi = {10.1145/2380116.2380122},
 acmid = {2380122},
 publisher = {ACM},
 address = {New York, NY, USA},
 keywords = {captioning, crowdsourcing, deaf, hard of hearing, real-time, text alignment, transcription},
}
```
