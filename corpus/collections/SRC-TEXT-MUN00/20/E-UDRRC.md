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
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked distributivity of the dot product, the Cauchy-
    Schwarz inequality from the expansion of the norm of cx +/- ey, the triangle inequality
    for the norm by expanding the norm of a sum, and the three metric axioms, against
    Munkres §20 Exercise 9, printed p. 128. positron0802, Exercise 20.9, PDF p. 22,
    following the book's hints. The printed statement needed no repair.
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
The published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 20.9, PDF p. 22** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); all four parts are theirs, following the book's hints.

Write $\mathbf{x}\cdot\mathbf{y}=\sum_{i=1}^{n}x_{i}y_{i}$ and $\norm{\mathbf{x}}=(\mathbf{x}\cdot\mathbf{x})^{1/2}$.

::: pf

::: {.pf-step #part-a}
(a) $\mathbf{x}\cdot(\mathbf{y}+\mathbf{z})=(\mathbf{x}\cdot\mathbf{y})+(\mathbf{x}\cdot\mathbf{z})$.

::: pf-proof
$$
\mathbf{x}\cdot(\mathbf{y}+\mathbf{z})=\sum_{i=1}^{n}x_{i}(y_{i}+z_{i})=\sum_{i=1}^{n}x_{i}y_{i}+\sum_{i=1}^{n}x_{i}z_{i}=\mathbf{x}\cdot\mathbf{y}+\mathbf{x}\cdot\mathbf{z},
$$
where the middle equality is distributivity of the real numbers in each coordinate and the splitting of a finite sum.
:::

:::

::: {.pf-step #part-b}
(b) $\abs{\mathbf{x}\cdot\mathbf{y}}\le\norm{\mathbf{x}}\norm{\mathbf{y}}$.

::: pf-proof
If $\mathbf{x}=\mathbf{0}$ or $\mathbf{y}=\mathbf{0}$ then $\mathbf{x}\cdot\mathbf{y}=0$ and one factor on the right is $0$, so the inequality holds. Otherwise put $c=1/\norm{\mathbf{x}}$ and $e=1/\norm{\mathbf{y}}$, both positive. By step [](#part-a){.pf-ref} and the bilinearity it gives,
$$
0\le\norm{c\mathbf{x}\pm e\mathbf{y}}^{2}=c^{2}(\mathbf{x}\cdot\mathbf{x})+e^{2}(\mathbf{y}\cdot\mathbf{y})\pm2ce(\mathbf{x}\cdot\mathbf{y})=2\pm2ce(\mathbf{x}\cdot\mathbf{y}),
$$
using $c^{2}(\mathbf{x}\cdot\mathbf{x})=1$ and $e^{2}(\mathbf{y}\cdot\mathbf{y})=1$. So $\mp(\mathbf{x}\cdot\mathbf{y})\le 1/(ce)=\norm{\mathbf{x}}\norm{\mathbf{y}}$ for both signs, that is $\abs{\mathbf{x}\cdot\mathbf{y}}\le\norm{\mathbf{x}}\norm{\mathbf{y}}$.
:::

:::

::: {.pf-step #part-c}
(c) $\norm{\mathbf{x}+\mathbf{y}}\le\norm{\mathbf{x}}+\norm{\mathbf{y}}$.

::: pf-proof
$$
\norm{\mathbf{x}+\mathbf{y}}^{2}=(\mathbf{x}+\mathbf{y})\cdot(\mathbf{x}+\mathbf{y})=\norm{\mathbf{x}}^{2}+2(\mathbf{x}\cdot\mathbf{y})+\norm{\mathbf{y}}^{2}\le\norm{\mathbf{x}}^{2}+2\norm{\mathbf{x}}\norm{\mathbf{y}}+\norm{\mathbf{y}}^{2}=(\norm{\mathbf{x}}+\norm{\mathbf{y}})^{2},
$$
by step [](#part-a){.pf-ref} and step [](#part-b){.pf-ref}. Both sides are nonnegative, so taking square roots gives the inequality.
:::

:::

::: {.pf-step #part-d}
(d) $d(\mathbf{x},\mathbf{y})=\norm{\mathbf{x}-\mathbf{y}}$ is a metric on $\RR^{n}$.

::: pf-proof
$d(\mathbf{x},\mathbf{y})\ge0$ because a sum of squares is $\ge0$; $d(\mathbf{x},\mathbf{y})=0$ exactly when $\mathbf{x}-\mathbf{y}=\mathbf{0}$, that is $\mathbf{x}=\mathbf{y}$; and $d(\mathbf{y},\mathbf{x})=\norm{\mathbf{y}-\mathbf{x}}=\norm{\mathbf{x}-\mathbf{y}}=d(\mathbf{x},\mathbf{y})$ because $(-t)^{2}=t^{2}$ in each coordinate. For the triangle inequality, $(\mathbf{x}-\mathbf{z})+(\mathbf{z}-\mathbf{y})=\mathbf{x}-\mathbf{y}$, so by step [](#part-c){.pf-ref}
$$
d(\mathbf{x},\mathbf{y})=\norm{(\mathbf{x}-\mathbf{z})+(\mathbf{z}-\mathbf{y})}\le\norm{\mathbf{x}-\mathbf{z}}+\norm{\mathbf{z}-\mathbf{y}}=d(\mathbf{x},\mathbf{z})+d(\mathbf{z},\mathbf{y}).
$$
So $d$ satisfies the three metric axioms.
:::

:::

::: {.pf-step}
All four parts hold.

::: pf-proof
Steps [](#part-a){.pf-ref}, [](#part-b){.pf-ref}, [](#part-c){.pf-ref} and [](#part-d){.pf-ref} are the four assertions of the exercise.
:::

:::

:::
:::
