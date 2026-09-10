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
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
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

::: {.solution}
(a) By the definition of dot product,
\[
\mathbf x\cdot(\mathbf y+\mathbf z)
=\sum_i x_i(y_i+z_i)
=\sum_i x_iy_i+\sum_i x_iz_i
=\mathbf x\cdot\mathbf y+\mathbf x\cdot\mathbf z.
\]

(b) If either vector is zero the inequality is immediate. Otherwise put
\[
u=\frac{\mathbf x}{\|\mathbf x\|},\qquad v=\frac{\mathbf y}{\|\mathbf y\|}.
\]
Since $\|u\pm v\|^2\ge0$,
\[
0\le 2\pm2(u\cdot v),
\]
so $-1\le u\cdot v\le1$. Multiplying by $\|\mathbf x\|\|\mathbf y\|$ gives
\[
|\mathbf x\cdot\mathbf y|\le\|\mathbf x\|\,\|\mathbf y\|.
\]

(c) Using part (b),
\[
\begin{aligned}
\|\mathbf x+\mathbf y\|^2
&=\|\mathbf x\|^2+2\mathbf x\cdot\mathbf y+\|\mathbf y\|^2\\
&\le \|\mathbf x\|^2+2\|\mathbf x\|\|\mathbf y\|+\|\mathbf y\|^2\\
&=(\|\mathbf x\|+\|\mathbf y\|)^2.
\end{aligned}
\]
Taking nonnegative square roots yields the triangle inequality for the norm.

(d) Define $d(\mathbf x,\mathbf y)=\|\mathbf x-\mathbf y\|$. It is nonnegative and symmetric, and $d(\mathbf x,\mathbf y)=0$ iff every coordinate difference is zero, i.e. $\mathbf x=\mathbf y$. Finally
\[
d(\mathbf x,\mathbf z)=\|(\mathbf x-\mathbf y)+(\mathbf y-\mathbf z)\|
\le d(\mathbf x,\mathbf y)+d(\mathbf y,\mathbf z)
\]
by part (c). Thus $d$ is a metric.
:::
