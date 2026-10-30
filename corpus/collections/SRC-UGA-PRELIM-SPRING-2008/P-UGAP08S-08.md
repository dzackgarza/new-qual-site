---
schema: qual/card@1
id: P-UGAP08S-08
kind: problem
title: 'Examples: $\forall$ not distributing over $\lor$, a power series converging exactly on $[0,4)$, and pointwise but nonuniform convergence'
classification:
  areas: [prelim]
  topics:
  - Logic and Quantifiers
  - Power Series
  - Uniform Convergence
  - Counterexamples
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Give examples of the following. No proofs are required.

(a) Open sentences $P(x)$ and $Q(x)$ such that
$$
\forall x\,[P(x)\lor Q(x)]
$$
is true, but
$$
[\forall x\,P(x)]\lor[\forall x\,Q(x)]
$$
is false.

(b) A real power series whose domain of convergence is the half-open interval $[0,4)$.

(c) A sequence $(f_n)$ of real-valued functions $\RR\to\RR$ which converges pointwise but not uniformly.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For part (a), take the universe to be
$$
\RR
$$
and define
$$
P(x):
x\ge0,
\qquad
Q(x):
x\le0.
$$


::: pf-proof

Every real number satisfies at least one of
$$
x\ge0
\quad\text{or}\quad
x\le0,
$$
so
$$
\forall x,[P(x)\lor Q(x)]
$$
is true.

But
$$
P(-1)
$$
is false, so
$$
\forall x,P(x)
$$
is false.
Likewise
$$
Q(1)
$$
is false, so
$$
\forall x,Q(x)
$$
is false.
Hence
$$
[\forall x,P(x)]
\lor
[\forall x,Q(x)]
$$
is false.

:::

:::

::: {.pf-step #s1-2}

For part (b), take
$$
\boxed{
\sum_{n=1}^{\infty}
\frac{(x-2)^n}{n,2^n}.
}
$$


::: pf-proof

The coefficients relative to the center
$$
2
$$
are
$$
a_n
=
\frac1{n2^n}.
$$
Since
$$
\limsup_{n\to\infty}
\abs{a_n}^{1/n}
=
\frac12,
$$
the radius of convergence is
$$
R=2.
$$
Thus the series converges absolutely for
$$
0<x<4
$$
and diverges for
$$
x<0
\quad\text{or}\quad
x>4.
$$

At
$$
x=0,
$$
the series is
$$
\sum_{n=1}^{\infty}
\frac{(-2)^n}{n2^n}
=
\sum_{n=1}^{\infty}
\frac{(-1)^n}{n},
$$
which converges.

At
$$
x=4,
$$
the series is
$$
\sum_{n=1}^{\infty}
\frac{2^n}{n2^n}
=
\sum_{n=1}^{\infty}
\frac1n,
$$
which diverges.
Hence the domain of convergence is exactly
$$
[0,4).
$$

:::

:::

::: {.pf-step #s1-3}

For part (c), define
$$
\boxed{
f_n(x)=\frac{x}{n}
\qquad
(x\in\RR).
}
$$


::: pf-proof

For every fixed
$$
x\in\RR,
$$
$$
f_n(x)
=
\frac{x}{n}
\longrightarrow
0.
$$
Thus
$$
f_n\to0
$$
pointwise.

The convergence is not uniform on
$$
\RR.
$$
Indeed, for every
$$
n,
$$
$$
\sup_{x\in\RR}
\abs{f_n(x)}
=
\sup_{x\in\RR}
\frac{\abs{x}}{n}
=
+\infty.
$$
In particular the supremum does not tend to $0$.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} provide the three requested examples and verify their
properties.

:::

:::

:::
