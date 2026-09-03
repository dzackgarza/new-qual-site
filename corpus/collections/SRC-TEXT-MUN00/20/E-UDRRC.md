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
---

::: {.exercise}

Show that the euclidean metric $d$ on $\mathbb{R}^n$ is a metric, as follows.
If $\mathbf{x}, \mathbf{y} \in \mathbb{R}^n$ and $c \in \mathbb{R}$, define

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
