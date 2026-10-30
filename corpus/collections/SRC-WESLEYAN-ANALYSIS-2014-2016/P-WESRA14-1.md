---
schema: qual/card@1
id: P-WESRA14-1
kind: problem
title: 'Littlewood’s three principles'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 1 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md.
---

::: {.problem}
State one of Littlewood's three principles:

(a) in words;

(b) in a precise mathematical formulation.
:::

::: {.solution}

One of Littlewood's principles is the principle that **pointwise convergence
is nearly uniform convergence**.

::: pf

::: {.pf-step #s1-1}

In words:

> On a set of finite measure, if a sequence of measurable functions
> converges pointwise almost everywhere, then after discarding a set of
> arbitrarily small measure, the convergence becomes uniform.


::: pf-proof

This is the informal content of Egorov's theorem, one of the standard
precise forms of Littlewood's principles.

:::

:::

::: {.pf-step #s1-2}

Precisely, let
$$
(X,\mathcal M,\mu)
$$
be a measure space with
$$
\mu(X)<\infty.
$$
Let
$$
f_n:X\to\RR
$$
and
$$
f:X\to\RR
$$
be measurable, and suppose
$$
f_n(x)\to f(x)
$$
for almost every
$$
x\in X.
$$
Then for every
$$
\varepsilon>0
$$
there exists a measurable set
$$
E\subseteq X
$$
such that
$$
\mu(E)<\varepsilon
$$
and
$$
f_n\to f
$$
uniformly on
$$
X\setminus E.
$$


::: pf-proof

This is Egorov's theorem.
It is the exact mathematical statement corresponding to the phrase
“pointwise convergence is nearly uniform.”

:::

:::

::: pf-step

Equivalently, the exceptional set can be made arbitrarily small:
for every
$$
\varepsilon>0
$$
there exists
$$
E
$$
with
$$
\mu(E)<\varepsilon
$$
such that
$$
\forall\eta>0+\exists N+\forall n\ge N+\forall x\in X\setminus E,
\quad
\abs{f_n(x)-f(x)}<\eta.
$$


::: pf-proof

This is simply the definition of uniform convergence written with all
quantifiers displayed.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} gives the requested verbal form and step [](#s1-2){.pf-ref} gives the precise
mathematical formulation.

:::

:::

:::
