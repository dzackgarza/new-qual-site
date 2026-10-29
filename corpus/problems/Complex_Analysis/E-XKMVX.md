---
schema: qual/card@1
id: E-XKMVX
kind: problem
title: Solutions of $f(z)=(2z)^m$ in $\abs{z}<1/2$ for $f:\DD\to\bar\DD$ with $f(0)=0$
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Schwarz Lemma
  - Zeros
relations: []
review: draft
---

::: {.exercise}
Use Rouché's theorem and the Schwarz lemma to prove the following: if $f:\DD\to \bar{\DD}$ is holomorphic with $f(0) = 0$, then there are exactly $m$ solutions (counted with multiplicity) to $f(z) = (2z)^m$ in the disc $\abs{z} < 1/2$.
:::

::: {.solution}

::: pf

::: {.pf-step #schwarz}
$\abs{f(z)} \le \abs{z}$ for all $z\in\DD$.

::: pf-proof
This is the Schwarz lemma, since $f$ is holomorphic on $\DD$ with $\abs{f}\le1$ and $f(0)=0$.
:::

:::

::: {.pf-step #rouche-bound}
On the circle $\abs{z}=1/2$, $\abs{f(z)} < \abs{(2z)^m}$.

::: pf-proof
By step [](#schwarz){.pf-ref}, $\abs{f(z)}\le 1/2 < 1 = \abs{2z}^m$ there.
:::

:::

::: pf-step
$f(z) - (2z)^m$ has exactly $m$ zeros, counted with multiplicity, in $\abs{z}<1/2$.

::: pf-proof
Both $f$ and $(2z)^m$ are holomorphic on a neighbourhood of $\abs{z}\le1/2$.
By step [](#rouche-bound){.pf-ref} and Rouché's theorem, $-(2z)^m + f(z)$ has as many zeros in $\abs{z}<1/2$ as $-(2z)^m$, which has a zero of order $m$ at $0$ and no other zero.
:::

:::

:::

:::
