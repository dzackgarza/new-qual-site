---
schema: qual/card@1
id: E-XDJRZ
kind: problem
title: $\ell^2$ is a vector space with the $\ell^2$ metric
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §20 Exercise 10, printed p. 128; the three parts
    are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 20.10, PDF p. 22. The Cauchy-Schwarz bound on the
    partial sums gives absolute convergence of the series of products, the two-square
    inequality gives closure under sums and scalar multiples, and the metric axioms follow
    from the same bound, which makes the triangle inequality the one in the Cauchy-Schwarz
    form. (tmp/sources/munkres-solutions-positron-ch2.pdf).
---

::: {.exercise}

Let $X$ denote the subset of $\RR^\omega$ consisting of all sequences $(x_1, x_2, \ldots)$ such that $\sum x_i^2$ converges.
(You may assume the standard facts about infinite series.
In case they are not familiar to you, we shall give them in Exercise 11 of the next section.)

(a) Show that if $\mathbf{x}, \mathbf{y} \in X$, then $\sum \abs{x_i y_i}$ converges.
[Hint: Use (b) of Exercise 9 to show that the partial sums are bounded.]

(b) Let $c \in \RR$.
Show that if $\mathbf{x}, \mathbf{y} \in X$, then so are $\mathbf{x} + \mathbf{y}$ and $c\mathbf{x}$.

(c) Show that

$$
d(\mathbf{x}, \mathbf{y}) = \left[ \sum_{i=1}^{\infty} (x_i - y_i)^2 \right]^{1/2}
$$

is a well-defined metric on $X$.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 20.10, PDF p. 22** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); all three parts are theirs.

(a) Let $\mathbf{x},\mathbf{y}\in X$, so $\sum x_{i}^{2}$ and $\sum y_{i}^{2}$ converge. For $n\in\ZZ_{+}$ let $\mathbf{x}_{n}=(x_{1},\dots,x_{n})$ and $\mathbf{y}_{n}=(y_{1},\dots,y_{n})$. By the Cauchy--Schwarz inequality in $\RR^{n}$ (Exercise 20.9(b)),
$$
\sum_{i=1}^{n}\abs{x_{i}y_{i}}=\abs{\mathbf{x}_{n}\cdot\mathbf{y}_{n}}\le\norm{\mathbf{x}_{n}}\norm{\mathbf{y}_{n}}\le\Big(\sum_{i\ge1}x_{i}^{2}\Big)^{1/2}\Big(\sum_{i\ge1}y_{i}^{2}\Big)^{1/2}.
$$
The partial sums of $\sum\abs{x_{i}y_{i}}$ are increasing and bounded, so the series converges.

(b) For every $n$, $\sum_{i=1}^{n}(x_{i}+y_{i})^{2}\le2\sum_{i=1}^{n}x_{i}^{2}+2\sum_{i=1}^{n}y_{i}^{2}\le2\sum_{i\ge1}x_{i}^{2}+2\sum_{i\ge1}y_{i}^{2}$, since $(a+b)^{2}\le2a^{2}+2b^{2}$; so the partial sums of $\sum(x_{i}+y_{i})^{2}$ are bounded and the series converges: $\mathbf{x}+\mathbf{y}\in X$. Similarly $\sum(cx_{i})^{2}=c^{2}\sum x_{i}^{2}$ converges, so $c\mathbf{x}\in X$.

(c) For $\mathbf{x},\mathbf{y}\in X$, part (b) gives $\mathbf{x}-\mathbf{y}\in X$, so the series $\sum(x_{i}-y_{i})^{2}$ converges and $d(\mathbf{x},\mathbf{y})=\big(\sum_{i}(x_{i}-y_{i})^{2}\big)^{1/2}$ is a well-defined nonnegative real number, vanishing exactly when $x_{i}=y_{i}$ for all $i$. Symmetry is clear. For the triangle inequality put $\mathbf{a}=\mathbf{x}-\mathbf{z}$ and $\mathbf{b}=\mathbf{z}-\mathbf{y}$, which lie in $X$ by (b). By (a) applied to $\mathbf{a},\mathbf{b}$ and the Cauchy--Schwarz inequality of Exercise 20.9(b),
$$
\abs{\sum_{i}a_{i}b_{i}}\le\sum_{i}\abs{a_{i}b_{i}}\le\Big(\sum_{i}a_{i}^{2}\Big)^{1/2}\Big(\sum_{i}b_{i}^{2}\Big)^{1/2}.
$$
Since $\mathbf{a}+\mathbf{b}=\mathbf{x}-\mathbf{y}$,
$$
d(\mathbf{x},\mathbf{y})^{2}=\sum_{i}(a_{i}+b_{i})^{2}=\sum_{i}a_{i}^{2}+2\sum_{i}a_{i}b_{i}+\sum_{i}b_{i}^{2}
\le\norm{\mathbf{a}}^{2}+2\norm{\mathbf{a}}\norm{\mathbf{b}}+\norm{\mathbf{b}}^{2}=\big(d(\mathbf{x},\mathbf{z})+d(\mathbf{z},\mathbf{y})\big)^{2},
$$
where $\norm{\mathbf{a}}=d(\mathbf{0},\mathbf{a})$; taking square roots gives the triangle inequality, so $d$ is a metric on $X$.
:::
