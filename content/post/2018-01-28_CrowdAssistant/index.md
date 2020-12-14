+++
title = "Evorus: A Crowd-powered Conversational Assistant Built to Automate Itself Over Time (Huang et al., 2018)"
date = 2018-01-28T16:01:20-05:00
draft = false

summary = "For a more flexible dialogue system, use the crowd to propose and vote on responses, then introduce agents and a model for voting, gradually learning to replace the crowd."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "chi", "crowdsourcing", "dialogue"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

There is a lot of interest in dialogue agents, but a lot of work sits at one of two extremes: either chit-chat agents that just chat, or task-oriented agents that aim to call a specific API for the user.
This work is about trying to integrate a range of systems from both categories, to get something more general purpose as a result.

The core approach is a hybrid system that switches between different agents behind the scenes (an approach taken by a number of Alexa Prize teams).
The innovation here is that crowd workers will help with the decision (both suggesting things to say and voting on which response to use), and their votes will be used to learn a model to (partially) replace the people over time.

Unfortunately, the improvement from a learned model of votes is only small (saves only 14% of the crowd effort), and the automated responses are rarely chosen (12% of the time).
That said, it seems like an interesting design with a lot of subtle decisions that require more exploration - the sets of agents (4-6 here, mostly narrow types), the voting scheme (only 1 or 2 votes needed here), choosing which agent responses to show (here, the proportion of previously accepted messages from this agent), and so on.
That choice of which responses to show is particularly tricky, as with this scheme a very domain specific agent might get voted down too much initially and never be chosen when the appropriate time comes.
One potentially interesting alternative would be to let the crowd workers choose which agent's response to see, and possibly even post-edit slightly.

Note - This post is the first of a (hopefully) regular series again.
However, rather than keeping it weekday-ly, I plan to do three times a week, at least until the ACL deadline.

## Citation

[Paper](https://www.cs.cmu.edu/~tinghaoh/pdf/2018/2018_chi.pdf)

```bibtex
@InProceedings{blah,
  title = {Evorus: A Crowd-powered Conversational Assistant Built to Automate Itself Over Time},
  author    = {Huang, Ting-Hao (Kenneth) and Chang, Joseph Chee and Bigham, Jeffrey P.},
  booktitle = {CHI},
  year = {2018},
  url = {https://www.cs.cmu.edu/~tinghaoh/pdf/2018/2018_chi.pdf},
}
```
