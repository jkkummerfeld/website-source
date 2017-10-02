+++
date = 2017-09-27
draft = false
tags = ["misc"]
title = "Ordering Pizza for an Event with Vegetarians"
math = true
summary = """
A simple model to help determine how much of each pizza type to order for an event.
"""
+++

## How much vegetarian pizza should I order?

This question frequently comes up in the world of free food at university events. In my experience (as someone who does not eat meat pizzas), often not enough is ordered. Let's try to come up with a model to tell us how much to order. Set it up like this:

* There are $N$ people.
* There are $P$ pizzas.
* The fraction of people who are vegetarian is $V$.
* Assume everyone eats the same amount of pizza, and all the pizza is eaten (ie. each person eats $\frac{P}{N}$).
* Assume people randomly sample from the available pizzas, subject to the constraint that some eat only vegetarian pizzas.

Now, let the fraction of vegetarian pizzas we get be $k$, and we can write down the number of vegetarian pizzas in two ways:

* How many we order: $P * k$
* How many are eaten: (pizzas eaten by vegetarians) + (vegetarian pizzas eaten by others) = $\frac{P}{N} * (N * V) + \frac{P}{N} * (N * (1 - V)) * k$

Since all the pizza we order is eaten, these are equal.
$N$ and $P$ are both positive numbers, so we can safely cancel the $N$s and divide through by $P$, giving:

$V + (1 - V) * k = k$

To satisfy this equation, $k = 1$. Therefore all the pizza should be vegetarian :)

Of course, these assumptions aren't quite right (for example, not everyone samples randomly from the available pizza), so here are some more useful suggestions too:

* Do order more than the proportion of vegetarians.
* Place the vegetarian pizza at the end of the line of pizzas, or in a separate location with clear signage discouraging non-vegetarians from eating it.
* Order a diverse set of popular meat pizzas (people tend to want variety, so this encourages them to try more meat pizzas).

For other peoples' thoughts on this question see
[Serious Eats](http://www.seriouseats.com/2014/07/etiquette-ordering-pizza-for-a-group-manner-matters.html) and
[Quora](https://www.quora.com/What-are-the-best-pizza-toppings-to-get-for-a-big-group)
