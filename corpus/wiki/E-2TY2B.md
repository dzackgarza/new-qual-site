---
schema: qual/card@1
id: E-2TY2B
kind: exercise
title: Completion via Cauchy sequences
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
relations: []
review: draft
---

::: {.exercise title="Munkres §43.9"}

Let $(X, d)$ be a metric space.
Show that there is an isometric imbedding $h$ of $X$ into a complete metric space $(Y, D)$, as follows.
Let $\tilde{X}$ denote the set of all Cauchy sequences

$$
\mathbf{x} = (x_1, x_2, \dots)
$$

of points of $X$.
Define $\mathbf{x} \sim \mathbf{y}$ if

$$
d(x_n, y_n) \to 0.
$$

Let $[\mathbf{x}]$ denote the equivalence class of $\mathbf{x}$; and let $Y$ denote the set of these equivalence classes.
Define a metric $D$ on $Y$ by the equation

$$
D([\mathbf{x}], [\mathbf{y}]) = \lim_{n \to \infty} d(x_n, y_n).
$$

(a) Show that $\sim$ is an equivalence relation, and show that $D$ is a well-defined metric.

(b) Define $h: X \to Y$ by letting $h(x)$ be the equivalence class of the constant sequence $(x, x, \ldots)$:

$$
h(x) = [(x, x, \dots)].
$$

Show that $h$ is an isometric imbedding.

(c) Show that $h(X)$ is dense in $Y$; indeed, given $\mathbf{x} = (x_1, x_2, \ldots) \in \tilde{X}$, show the sequence $h(x_n)$ of points of $Y$ converges to the point $[\mathbf{x}]$ of $Y$.

(d) Show that if $A$ is a dense subset of a metric space $(Z, \rho)$, and if every Cauchy sequence in $A$ converges in $Z$, then $Z$ is complete.

(e) Show that $(Y, D)$ is complete.
:::
