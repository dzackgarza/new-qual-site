---
schema: qual/card@1
id: P-WESTOP05-01
kind: problem
title: Cardinalities of power sets, intervals, and sequence spaces
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Determine the cardinalities of the following sets:
$$
\mathcal P(\NN),
\qquad
\{0,1\},
\qquad
[0,1],
\qquad
(0,1),
$$
and
$$
\{f:\NN\to[0,1]\}.
$$
Here $\mathcal P$ denotes power set.
:::

::: {.solution}

Let
$$
\mathfrak c
=
|\RR|
=
2^{\aleph_0}
$$
denote the cardinality of the continuum.

::: pf

::: {.pf-step #s1-1}

One has
$$
\boxed{
|\mathcal P(\NN)|
=
2^{\aleph_0}
=
\mathfrak c}.
$$


::: pf-proof

By definition,
$$
2^{\aleph_0}
$$
is the cardinality of the set of all functions
$$
\NN\to\{0,1\}.
$$
Each subset $A\subseteq\NN$ corresponds uniquely to its
characteristic function
$$
\mathbf 1_A:\NN\to\{0,1\}.
$$
Thus
$$
\mathcal P(\NN)
$$
is in bijection with $\{0,1\}^{\NN}$.

:::

:::

::: {.pf-step #s1-2}

One has
$$
\boxed{
|\{0,1\}|=2}.
$$


::: pf-proof

The set has exactly two elements.

:::

:::

::: {.pf-step #s1-3}

One has
$$
\boxed{
|[0,1]|=\mathfrak c}.
$$


::: pf-proof

The interval $[0,1]$ is a nondegenerate interval in $\RR$, and
every nondegenerate real interval has the same cardinality as $\RR$.
For example, the map
$$
x\longmapsto \frac12+\frac1\pi\arctan x
$$
is a bijection
$$
\RR\to(0,1).
$$
Since
$$
(0,1)\subseteq[0,1]\subseteq\RR,
$$
the Cantor--Bernstein theorem gives
$$
|[0,1]|=|\RR|=\mathfrak c.
$$

:::

:::

::: {.pf-step #s1-4}

One has
$$
\boxed{
|(0,1)|=\mathfrak c}.
$$


::: pf-proof

The explicit map
$$
x\longmapsto
\frac12+\frac1\pi\arctan x
$$
is a bijection
$$
\RR\to(0,1).
$$
Hence the cardinalities are equal.

:::

:::

::: pf-step

Let
$$
S
=
\{f:\NN\to[0,1]\}
=
[0,1]^{\NN}.
$$
Then
$$
\boxed{|S|\ge\mathfrak c}.
$$


::: pf-proof

Every $x\in[0,1]$ determines the constant sequence
$$
f_x(n)=x.
$$
The map
$$
x\longmapsto f_x
$$
is injective. By step [](#s1-3){.pf-ref},
$$
|[0,1]|=\mathfrak c.
$$

:::

:::

::: {.pf-step #s1-6}

Since
$$
|[0,1]|=\mathfrak c=2^{\aleph_0},
$$
one has
$$
|S|
=
\mathfrak c^{\aleph_0}.
$$


::: pf-proof

The set of all functions from a set of cardinality $\aleph_0$ into a set
of cardinality $\mathfrak c$ has cardinality
$$
\mathfrak c^{\aleph_0}.
$$

:::

:::

::: {.pf-step #s1-7}

Cardinal exponentiation gives
$$
\boxed{
\mathfrak c^{\aleph_0}
=
(2^{\aleph_0})^{\aleph_0}
=
2^{\aleph_0\cdot\aleph_0}
=
2^{\aleph_0}
=
\mathfrak c}.
$$


::: pf-proof

Use
$$
(\kappa^\lambda)^\mu
=
\kappa^{\lambda\mu}
$$
for cardinals, together with
$$
\aleph_0\cdot\aleph_0=\aleph_0.
$$

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
\boxed{
\left|
\{f:\NN\to[0,1]\}
\right|
=
\mathfrak c}.
$$


::: pf-proof

Combine steps [](#s1-6){.pf-ref} through [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

Collecting the results,
$$
\boxed{
|\mathcal P(\NN)|
=
|[0,1]|
=
|(0,1)|
=
\left|
\{f:\NN\to[0,1]\}
\right|
=
\mathfrak c}
$$
and
$$
\boxed{
|\{0,1\}|=2}.
$$


::: pf-proof

Use steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref} and [](#s1-8){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} gives all requested cardinalities.

:::

:::

:::
