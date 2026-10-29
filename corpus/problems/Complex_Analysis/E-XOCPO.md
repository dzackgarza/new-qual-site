---
schema: qual/card@1
id: E-XOCPO
kind: problem
title: Laurent expansion of $1/e^{1-z}$ on $\abs{z}>1$
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Power Series
  - Entire Functions
relations: []
review: draft
---

::: {.exercise}
Find a Laurent expansion that converges for $\abs{z} > 1$ of
$$
f(z) \coloneqq \frac{1}{e^{1-z}}.
$$
:::

::: {.solution}

::: pf

::: pf-step
$$
\boxed{f(z) = \sum_{k\ge0} \frac{z^k}{e\cdot k!}},
$$
and this expansion converges on all of $\CC$, in particular on $\abs{z}>1$.

::: pf-proof
$f(z) = e^{-(1-z)} = e^{-1}e^z$, and the exponential series converges on $\CC$.
By uniqueness of Laurent expansions on the annulus $\abs{z}>1$, this is the Laurent expansion there; its principal part is zero.
:::

:::

:::

:::
