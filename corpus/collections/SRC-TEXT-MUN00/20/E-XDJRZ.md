---
schema: qual/card@1
id: E-XDJRZ
kind: exercise
title: The l2 space is a vector space with the l2 metric
subtitle: Munkres §20.10
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
relations: []
review: draft
---

::: {.exercise}

Let $X$ denote the subset of $\mathbb{R}^\omega$ consisting of all sequences $(x_1, x_2, \ldots)$ such that $\sum x_i^2$ converges.
(You may assume the standard facts about infinite series.
In case they are not familiar to you, we shall give them in Exercise 11 of the next section.)

(a) Show that if $\mathbf{x}, \mathbf{y} \in X$, then $\sum \abs{x_i y_i}$ converges.
[Hint: Use (b) of Exercise 9 to show that the partial sums are bounded.]

(b) Let $c \in \mathbb{R}$.
Show that if $\mathbf{x}, \mathbf{y} \in X$, then so are $\mathbf{x} + \mathbf{y}$ and $c\mathbf{x}$.

(c) Show that

$$
d(\mathbf{x}, \mathbf{y}) = \left[ \sum_{i=1}^{\infty} (x_i - y_i)^2 \right]^{1/2}
$$

is a well-defined metric on $X$.
:::
