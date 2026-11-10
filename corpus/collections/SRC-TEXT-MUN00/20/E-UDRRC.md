---
schema: qual/card@1
id: E-UDRRC
kind: problem
title: The euclidean metric via the Cauchy-Schwarz inequality
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
    Read against Munkres, Topology (2000), §20 Exercise 9, printed p. 128; the four parts
    and the two hints are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 20.9, PDF p. 22. Distributivity of the dot
    product, the Cauchy-Schwarz inequality from the nonnegativity of |cx +/- dy|^2, the
    triangle inequality by expanding the norm squared, and the metric axioms for the
    euclidean distance. (tmp/sources/munkres-solutions-positron-ch2.pdf).
---

::: {.exercise}

Show that the euclidean metric $d$ on $\RR^n$ is a metric, as follows.
If $\mathbf{x}, \mathbf{y} \in \RR^n$ and $c \in \RR$, define

$$
\begin{array}{c}
\mathbf{x} + \mathbf{y} = (x_1 + y_1, \dots, x_n + y_n), \\
c\mathbf{x} = (cx_1, \dots, cx_n), \\
\mathbf{x} \cdot \mathbf{y} = x_1 y_1 + \dots + x_n y_n.
\end{array}
$$

(a) Show that $\mathbf{x} \cdot (\mathbf{y} + \mathbf{z}) = (\mathbf{x} \cdot \mathbf{y}) + (\mathbf{x} \cdot \mathbf{z})$.

(b) Show that $\abs{\mathbf{x} \cdot \mathbf{y}} \leq \norm{\mathbf{x}} \, \norm{\mathbf{y}}$.
[Hint: If $\mathbf{x}, \mathbf{y} \neq 0$, let $a = 1/\norm{\mathbf{x}}$ and $b = 1/\norm{\mathbf{y}}$, and use the fact that $\norm{a\mathbf{x} \pm b\mathbf{y}} \geq 0$.]

(c) Show that $\norm{\mathbf{x} + \mathbf{y}} \leq \norm{\mathbf{x}} + \norm{\mathbf{y}}$.
[Hint: Compute $(\mathbf{x} + \mathbf{y}) \cdot (\mathbf{x} + \mathbf{y})$ and apply (b).]

(d) Verify that $d$ is a metric.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 20.9, PDF p. 22** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); all four parts are theirs, following the book's hints.

Write $\mathbf{x}\cdot\mathbf{y}=\sum_{i}x_{i}y_{i}$ and $\norm{\mathbf{x}}=(\mathbf{x}\cdot\mathbf{x})^{1/2}$.

(a) $\mathbf{x}\cdot(\mathbf{y}+\mathbf{z})=\sum_{i}x_{i}(y_{i}+z_{i})=\sum_{i}x_{i}y_{i}+\sum_{i}x_{i}z_{i}=\mathbf{x}\cdot\mathbf{y}+\mathbf{x}\cdot\mathbf{z}$.

(b) If $\mathbf{x}=\mathbf{0}$ or $\mathbf{y}=\mathbf{0}$ both sides are $0$; otherwise put $c=1/\norm{\mathbf{x}}$ and $d=1/\norm{\mathbf{y}}$. Then
$$
0\le\norm{c\mathbf{x}\pm d\mathbf{y}}^{2}=c^{2}(\mathbf{x}\cdot\mathbf{x})+d^{2}(\mathbf{y}\cdot\mathbf{y})\pm2cd(\mathbf{x}\cdot\mathbf{y})
=2\pm2cd(\mathbf{x}\cdot\mathbf{y}),
$$
so $\pm(\mathbf{x}\cdot\mathbf{y})\le\norm{\mathbf{x}}\norm{\mathbf{y}}$ and hence $\abs{\mathbf{x}\cdot\mathbf{y}}\le\norm{\mathbf{x}}\norm{\mathbf{y}}$.

(c) $\norm{\mathbf{x}+\mathbf{y}}^{2}=(\mathbf{x}+\mathbf{y})\cdot(\mathbf{x}+\mathbf{y})=\norm{\mathbf{x}}^{2}+2(\mathbf{x}\cdot\mathbf{y})+\norm{\mathbf{y}}^{2}\le\norm{\mathbf{x}}^{2}+2\norm{\mathbf{x}}\norm{\mathbf{y}}+\norm{\mathbf{y}}^{2}=(\norm{\mathbf{x}}+\norm{\mathbf{y}})^{2}$ by (b), and taking square roots gives the triangle inequality.

(d) $d(\mathbf{x},\mathbf{y})=\norm{\mathbf{x}-\mathbf{y}}$ is nonnegative and vanishes exactly when $\mathbf{x}=\mathbf{y}$, and it is symmetric. For the triangle inequality apply (c) to $\mathbf{x}-\mathbf{z}$ and $\mathbf{z}-\mathbf{y}$:
$$
d(\mathbf{x},\mathbf{y})=\norm{(\mathbf{x}-\mathbf{z})+(\mathbf{z}-\mathbf{y})}\le\norm{\mathbf{x}-\mathbf{z}}+\norm{\mathbf{z}-\mathbf{y}}=d(\mathbf{x},\mathbf{z})+d(\mathbf{z},\mathbf{y}),
$$
using $(\mathbf{x}-\mathbf{z})+(\mathbf{z}-\mathbf{y})=\mathbf{x}-\mathbf{y}$. So $d$ is a metric.
:::
