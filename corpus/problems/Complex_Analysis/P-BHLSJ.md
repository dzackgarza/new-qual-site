---
schema: qual/card@1
id: P-BHLSJ
kind: problem
title: Laurent expansions of $e^{1/z}$ and $\cos(1/z)$ about $0$
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Essential Singularities
  - Principal Parts
relations: []
review: draft
---

::: {.problem}
Find the Laurent expansions about $z=0$ of the following functions:
$$
e^{1\over z}, \qquad \cos \qty{1\over z}.
$$
:::

::: {.solution}

::: pf

::: pf-step
$e^{1/z}=\sum_{n=0}^\infty \frac{1}{n!\,z^n}=1+\frac1z+\frac1{2!\,z^2}+\frac1{3!\,z^3}+\cdots$ for $z\neq0$.

::: pf-proof
Substitute $w=1/z$ in $e^w=\sum_{n\ge0}w^n/n!$, which converges for every $w\in\CC$.
:::

:::

::: pf-step
$\cos(1/z)=\sum_{n=0}^\infty \frac{(-1)^n}{(2n)!\,z^{2n}}=1-\frac1{2!\,z^2}+\frac1{4!\,z^4}-\frac1{6!\,z^6}+\cdots$ for $z\neq0$.

::: pf-proof
Substitute $w=1/z$ in $\cos w=\sum_{n\ge0}(-1)^nw^{2n}/(2n)!$, which converges for every $w\in\CC$.
Both series converge on the annulus $0<\abs{z}<\infty$, so they are the Laurent expansions there.
:::

:::

:::

:::
