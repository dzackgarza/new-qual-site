---
schema: qual/card@1
id: E-YTG4V
kind: exercise
title: Continuity of the field operations on R
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
  - Metric Spaces
relations: []
review: draft
solved: false
---

Prove continuity of the algebraic operations on $\mathbb{R}$, as follows. Use the metric $d(a, b) = \abs{a - b}$ on $\mathbb{R}$ and the metric on $\mathbb{R}^2$ given by the equation

$$
\rho((x, y), (x_0, y_0)) = \max\ts{\abs{x - x_0}, \abs{y - y_0}}.
$$

(a) Show that addition is continuous. [Hint: Given $\epsilon$, let $\delta = \epsilon/2$ and note that

$$
d(x + y, x_0 + y_0) \leq \abs{x - x_0} + \abs{y - y_0}.]
$$

(b) Show that multiplication is continuous. [Hint: Given $(x_0, y_0)$ and $0 < \epsilon < 1$, let

$$
3\delta = \epsilon/(\abs{x_0} + \abs{y_0} + 1)
$$

and note that

$$
d(xy, x_0y_0) \leq \abs{x_0}\abs{y - y_0} + \abs{y_0}\abs{x - x_0} + \abs{x - x_0}\abs{y - y_0}.]
$$

(c) Show that the operation of taking reciprocals is a continuous map from $\mathbb{R} - \ts{0}$ to $\mathbb{R}$. [Hint: Show the inverse image of the interval $(a, b)$ is open. Consider five cases, according as $a$ and $b$ are positive, negative, or zero.]

(d) Show that the subtraction and quotient operations are continuous.

::: {.remark}
Munkres, *Topology*, §21 Exercise 12.
:::
