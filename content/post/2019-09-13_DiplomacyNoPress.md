+++
title = "No-Press Diplomacy: Modeling Multi-Agent Gameplay (Paquette et al., 2019)"
date = 2019-09-13T13:00:23-04:00
draft = false

summary = "Games have been a focus of AI research for decades, from Samuel's checkers program in the 1950s, to Deep Blue playing Chess in the 1990s, and AlphaGo playing Go in the 2010s. All of those are two-player..."

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["paper", 'neurips']
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

Games have been a focus of AI research for decades, from Samuel's checkers program in the 1950s, to Deep Blue playing Chess in the 1990s, and AlphaGo playing Go in the 2010s.
All of those are two-player sequential games.
In this paper (to appear at NeurIPS), we looked at Diplomacy, a seven player game with simultaneous turns.

The paper makes three main contributions:

- A neural model that plays the game.
- Software to play the game (determining the outcomes of player actions is a non-trivial problem).
- Experiments with supervised learning and reinforcement learning.

Our paper only considers the version of the game where players can not talk to each other (No Press).
Engaging in conversation in the game is a fascinating challenge that will involve a lot more work.

How well does the bot play the game?
It convincingly beats prior systems designed for the game.
Playing against it, I saw an impressive improvement over the course of the project.
Early on I won trivially with mostly conservative moves.
Later I had to carefully consider my moves, and was unable to win as certain powers (e.g. Austria).
Eventually I was unable to beat the bot without playing several times, using observations from one game to inform my strategy in subsequent games.
I am not an expert player, but I doubt a human playing one power in the game with no prior knowledge can win against the bot.
However, I think a single bot playing against six skilled humans would almost definitely lose (we did not test this setting).

## Citation

[Paper](https://arxiv.org/abs/1909.02128)

```bibtex
@InProceedings{neurips19diplomacy,
  author    = {Philip Paquette, Yuchen Lu, Steven Bocco, Max O. Smith, Satya Ortiz-Gagn{\'e}, Jonathan K. Kummerfeld, Joelle Pineau, Satinder Singh, Aaron Courville},
  title     = {No-Press Diplomacy: Modeling Multi-Agent Gameplay},
  booktitle = {Advances in Neural Information Processing Systems 32},
  year      = {2019},
  month     = {December},
  pages     = {},
  url       = {},
  arxiv     = {https://arxiv.org/abs/1909.02128},
}
```
