+++
title = "Mastering the game of Go without human knowledge (Silver et al., Nature 2017)"
date = 2017-10-23T21:12:57-04:00
draft = false

summary = "By using a single core model to build a game state representation, which then gives input to both state evaluation and move choice, DeepMind are able to apply reinforcement learning with self-play with no supervision and achieve state-of-the-art performance."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", "rl"]
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

This paper is an extension of the original AlphaGo work on using reinforcement learning to build a Go-player.
Interestingly, the changes have simplified the overall model, as well as enabling it to do even better than the previous model, but now without any supervised training.

One key change is that there is a single core neural network learning to represent the game state.
On top of that there are either a set of layers that produce an evaluation of the quality of a position, or there are a set of layers that place a distribution over moves.
This ties in nicely to a lot of work happening at the moment on multi-task learning in NLP and elsewhere.

Getting into the details, they use monte-carlo tree search to choose actions during training, then update the model to better match the outcomes observed.
Starting from a completely random initialisation, the argument for why this works is that at every point in self-play the MCTS informed outcomes are just slightly better than the current model.
That edge is enough to provide a useful signal, without being such a drastic shift because in self-play the two sides are closely matched.
Interestingly, while the unsupervised model is worse at predicting what expert human players will do in a game, it is still better at predicting which player will win.

## Citation

[Paper](https://www.nature.com/nature/journal/v550/n7676/full/nature24270.html)

```bibtex
@Article{AlphaGoZero,
  author = {Silver, David  and  Schrittwieser, Julian  and  Simonyan, Karen  and  Antonoglou, Ioannis  and  Huang, Aja  and  Guez, Arthur  and  Hubert, Thomas  and  Baker, Lucas  and  Lai, Matthew  and  Bolton, Adrian  and  Chen, Yutian  and  Lillicrap, Timothy  and  Hui, Fan  and  Sifre, Laurent  and  van den Driessche, George  and  Graepel, Thore  and  Hassabis, Demis},
  title = {Mastering the game of Go without human knowledge},
  journal = {Nature},
  year = {2017},
  volume = {550},
  issue = {7676},
  pages = {354-359},
  publisher = {Macmillan Publishers Limited, part of Springer Nature},
  doi = {10.1038/nature24270},
  url = {http://www.nature.com/nature/journal/v550/n7676/abs/nature24270.html#supplementary-information},
}
```
