---
schema: qual/card@1
id: E-1SW9Q
kind: exercise
title: The Prufer manifold
classification:
  areas:
  - topology
  topics:
  - Manifolds
relations: []
review: draft
solved: false
---

::: {.exercise title="Munkres §50 Supplementary"}


There is a space that is locally 2-euclidean and satisfies (v) but not (iv) of Exercise 2. It is constructed as follows. Let $A$ be the following subspace of $\mathbb{R}^3$:

$$
A = \ts{(x, y, 0) \mid x > 0}.
$$

Given $c$ real, let $B_c$ be the following subspace of $\mathbb{R}^3$:

$$
B_c = \ts{(x, y, c) \mid x \leq 0}.
$$

Let $X$ be the set that is the union of $A$ and all the spaces $B_c$, for $c$ real. Topologize $X$ by taking as a basis all sets of the following three types:

(i) $U$, where $U$ is open in $A$.

(ii) $V$, where $V$ is open in the subspace of $B_c$ consisting of points with $x < 0$.

(iii) For each open interval $I = (a, b)$ of $\mathbb{R}$, each real number $c$, and each $\epsilon > 0$, the set $A_c(I, \epsilon) \cup B_c(I, \epsilon)$, where

$$
A_c(I, \epsilon) = \ts{(x, y, 0) \mid 0 < x < \epsilon \text{ and } c + ax < y < c + bx},
$$

$$
B_c(I, \epsilon) = \ts{(x, y, c) \mid -\epsilon < x \leq 0 \text{ and } a < y < b}.
$$

The space $X$ is called the "Prüfer manifold."

(a) Sketch the sets $A_c(I, \epsilon)$ and $B_c(I, \epsilon)$.

(b) Show the sets of types (i)-(iii) form a basis for a topology on $X$.

(c) Show the map $f_c: \mathbb{R}^2 \to X$ given by

$$
f_c(x, y) =
\begin{cases}
(x, c + xy, 0) & \text{for } x > 0, \\
(x, y, c) & \text{for } x \leq 0
\end{cases}
$$

defines a homeomorphism of $\mathbb{R}^2$ with the subspace $A \cup B_c$ of $X$.

(d) Show that $A \cup B_c$ is open in $X$; conclude that $X$ is 2-euclidean.

(e) Show that $X$ is Hausdorff.

(f) Show that $X$ is not normal. [Hint: The subspace

$$
L = \ts{(0, 0, c) \mid c \in \mathbb{R}}
$$

of $X$ is closed and discrete. Compare Example 3 of §31.]
:::
