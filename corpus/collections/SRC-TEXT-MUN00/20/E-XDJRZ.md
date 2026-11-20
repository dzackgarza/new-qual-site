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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the same three parts. The question taken up was whether the
    Cauchy--Schwarz step is proved or merely cited: it is cited from Exercise 9(b) of the same section,
    printed p. 128, which is what the exercise's own hint directs the reader to for part (a), and the card
    now says so at the step instead of leaving the reference implicit. What the earlier prose did not
    justify is the use of the inequality for the infinite sums of part (c): that is now derived by passing
    to the limit of the partial-sum inequalities, which needs the convergence of the series of products
    from part (a) and the boundedness of a limit by its bound. Nothing else was changed. Checked against
    Munkres, Topology (2000), Section 20 Exercise 10, printed p. 128.
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

All three parts are **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 20.10, PDF p. 22** (`tmp/sources/munkres-solutions-positron-ch2.pdf`). The Cauchy--Schwarz inequality is not proved here and is not silent either: it is Exercise 9(b) of the same section, which the exercise's own hint directs the reader to for part (a), and its use for the *infinite* sums of part (c) is derived from the finite case by passing to limits, which the earlier prose passed over.

The statement was checked against Munkres, *Topology* (2000), §20 Exercise 10, with Exercise 9 on the same page. Throughout, $X$ is the set of sequences $\mathbf{x}=(x_{1},x_{2},\dots)$ of real numbers for which $\sum_{i\geq1}x_{i}^{2}$ converges, $\mathbf{x}_{n}\coloneqq(x_{1},\dots,x_{n})\in\RR^{n}$, $\norm{\mathbf{x}_{n}}\coloneqq\big(\sum_{i=1}^{n}x_{i}^{2}\big)^{1/2}$, and $\mathbf{x}\cdot\mathbf{y}$ is the dot product of $\RR^{n}$ for the truncated vectors. The standard facts about series used are that a series of nonnegative terms with bounded partial sums converges, and that a limit of converging sequences is the limit of their limits.

::: pf

::: {.pf-step #part-a}

(a) If $\mathbf{x},\mathbf{y}\in X$, then $\sum\abs{x_{i}y_{i}}$ converges.

:::: pf-proof

The bound comes from Cauchy--Schwarz on the truncated vectors.

::: {.pf-step #cs-finite}

For $\mathbf{x},\mathbf{y}\in X$ and every $n$, $\sum_{i=1}^{n}\abs{x_{i}y_{i}}\leq\big(\sum_{i\geq1}x_{i}^{2}\big)^{1/2}\big(\sum_{i\geq1}y_{i}^{2}\big)^{1/2}$.

::: pf-proof

For vectors of $\RR^{n}$ the Cauchy--Schwarz inequality reads $\abs{\mathbf{x}_{n}\cdot\mathbf{y}_{n}}\leq\norm{\mathbf{x}_{n}}\norm{\mathbf{y}_{n}}$ (Exercise 9(b)), so
$$
\sum_{i=1}^{n}\abs{x_{i}y_{i}}\leq\norm{\mathbf{x}_{n}}\norm{\mathbf{y}_{n}}=\Big(\sum_{i=1}^{n}x_{i}^{2}\Big)^{1/2}\Big(\sum_{i=1}^{n}y_{i}^{2}\Big)^{1/2}\leq\Big(\sum_{i\geq1}x_{i}^{2}\Big)^{1/2}\Big(\sum_{i\geq1}y_{i}^{2}\Big)^{1/2},
$$
the last inequality because the partial sums of a series of nonnegative terms increase to its sum.

:::

:::

::: {.pf-step #a}

(a) $\sum_{i\geq1}\abs{x_{i}y_{i}}$ converges.

::: pf-proof

The partial sums of the series of nonnegative terms $\abs{x_{i}y_{i}}$ are increasing, and by step [](#cs-finite){.pf-ref} they are bounded by the number $\big(\sum x_{i}^{2}\big)^{1/2}\big(\sum y_{i}^{2}\big)^{1/2}$. An increasing sequence of real numbers that is bounded above converges; so the series converges.

:::

:::

::::

:::

::: {.pf-step #part-b}

(b) If $\mathbf{x},\mathbf{y}\in X$ and $c\in\RR$, then $\mathbf{x}+\mathbf{y}\in X$ and $c\mathbf{x}\in X$; so $X$ is a vector space under coordinatewise operations.

:::: pf-proof

Closure under sums and scalar multiples is what makes $X$ a vector space.

::: {.pf-step #sum}

$\mathbf{x}+\mathbf{y}\in X$.

::: pf-proof

For each $n$ one has $(a+b)^{2}\leq2a^{2}+2b^{2}$, so
$$
\sum_{i=1}^{n}(x_{i}+y_{i})^{2}\leq2\sum_{i=1}^{n}x_{i}^{2}+2\sum_{i=1}^{n}y_{i}^{2}\leq2\sum_{i\geq1}x_{i}^{2}+2\sum_{i\geq1}y_{i}^{2},
$$
and the partial sums of the series $\sum(x_{i}+y_{i})^{2}$ are therefore increasing and bounded, hence convergent.

:::

:::

::: {.pf-step #scalar}

$c\mathbf{x}\in X$.

::: pf-proof

$\sum_{i=1}^{n}(cx_{i})^{2}=c^{2}\sum_{i=1}^{n}x_{i}^{2}\leq c^{2}\sum_{i\geq1}x_{i}^{2}$ for every $n$, so the partial sums are increasing and bounded, hence convergent.

:::

:::

::: {.pf-step #vector-space}

The coordinatewise operations make $X$ a real vector space.

::: pf-proof

The two closure properties of steps [](#sum){.pf-ref} and [](#scalar){.pf-ref}, together with the fact that the coordinatewise operations on sequences satisfy the vector space axioms because each coordinate does, make $X$ a real vector space; the zero sequence lies in $X$.

:::

:::

::::

:::

::: {.pf-step #part-c}

(c) The formula $d(\mathbf{x},\mathbf{y})\coloneqq\big(\sum_{i\geq1}(x_{i}-y_{i})^{2}\big)^{1/2}$ defines a metric on $X$.

:::: pf-proof

The metric axioms are checked in order; the only substantive one is the triangle inequality.

::: {.pf-step #well-defined}

$d(\mathbf{x},\mathbf{y})$ is a well-defined nonnegative real, vanishing exactly when $\mathbf{x}=\mathbf{y}$, and $d$ is symmetric.

::: pf-proof

$\mathbf{x}-\mathbf{y}\in X$ by step [](#part-b){.pf-ref}, so the series $\sum(x_{i}-y_{i})^{2}$ converges with nonnegative terms and its sum has a real square root; the sum is $0$ exactly when every term is $0$, that is exactly when $x_{i}=y_{i}$ for all $i$. Symmetry is clear from $(x_{i}-y_{i})^{2}=(y_{i}-x_{i})^{2}$.

:::

:::

::: {.pf-step #cs-infinite}

For $\mathbf{a},\mathbf{b}\in X$ one has $\abs{\sum_{i\geq1}a_{i}b_{i}}\leq\big(\sum_{i\geq1}a_{i}^{2}\big)^{1/2}\big(\sum_{i\geq1}b_{i}^{2}\big)^{1/2}$.

::: pf-proof

By step [](#cs-finite){.pf-ref} applied to the truncated vectors, $\abs{\sum_{i=1}^{n}a_{i}b_{i}}\leq\big(\sum_{i=1}^{n}a_{i}^{2}\big)^{1/2}\big(\sum_{i=1}^{n}b_{i}^{2}\big)^{1/2}\leq\big(\sum_{i\geq1}a_{i}^{2}\big)^{1/2}\big(\sum_{i\geq1}b_{i}^{2}\big)^{1/2}$ for every $n$. The series $\sum a_{i}b_{i}$ converges by step [](#part-a){.pf-ref} applied to $\mathbf{a},\mathbf{b}$, so its sum is the limit of its partial sums; a limit of real numbers all bounded in absolute value by a constant is bounded by that constant, which gives the inequality.

:::

:::

::: {.pf-step #triangle}

The triangle inequality holds.

::: pf-proof

Let $\mathbf{x},\mathbf{y},\mathbf{z}\in X$ and put $\mathbf{a}\coloneqq\mathbf{x}-\mathbf{z}$, $\mathbf{b}\coloneqq\mathbf{z}-\mathbf{y}$, which lie in $X$ by step [](#part-b){.pf-ref}; then $\mathbf{a}+\mathbf{b}=\mathbf{x}-\mathbf{y}$. Writing $\norm{\mathbf{a}}\coloneqq d(\mathbf{0},\mathbf{a})$,
$$
d(\mathbf{x},\mathbf{y})^{2}=\sum_{i}(a_{i}+b_{i})^{2}=\sum_{i}a_{i}^{2}+2\sum_{i}a_{i}b_{i}+\sum_{i}b_{i}^{2}\leq\norm{\mathbf{a}}^{2}+2\norm{\mathbf{a}}\norm{\mathbf{b}}+\norm{\mathbf{b}}^{2}=\big(d(\mathbf{x},\mathbf{z})+d(\mathbf{z},\mathbf{y})\big)^{2},
$$
the inequality by step [](#cs-infinite){.pf-ref} and the identity by the convergence of the three series involved. Both sides are nonnegative, so taking square roots gives $d(\mathbf{x},\mathbf{y})\leq d(\mathbf{x},\mathbf{z})+d(\mathbf{z},\mathbf{y})$.

:::

:::

::: pf-step

$d$ is a metric on $X$.

::: pf-proof

Steps [](#well-defined){.pf-ref} and [](#triangle){.pf-ref} give positivity with definiteness, symmetry, and the triangle inequality, which are the three axioms of a metric.

:::

:::

::::

:::

::: pf-step

Therefore $X=\ell^{2}$ is a real vector space and $d$ is a metric on it.

::: pf-proof

Part [](#part-b){.pf-ref} gives the vector space structure and part [](#part-c){.pf-ref} the metric, which is the assertion of the exercise.

:::

:::

:::

:::
