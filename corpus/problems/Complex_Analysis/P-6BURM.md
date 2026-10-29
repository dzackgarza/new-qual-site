---
schema: qual/card@1
id: P-6BURM
kind: problem
title: Number of solutions of $e^z=az^n$ in the unit disc when $\abs{a}>e$ and when $\abs{a}<1/e$
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
relations: []
review: draft
---

::: {.problem}
Let $n\in \ZZ^{\geq 0}$ and show that the equation
$$
e^z = az^n
$$
has $n$ solutions in the open unit disc if $\abs{a} > e$, and no solutions if $\abs{a} < \frac{1}{e}$.
:::

::: {.solution}
Solutions are the zeros of $f(z) \coloneqq e^z-az^n$ in $\DD$, counted with multiplicity.
On $\abs{z}=1$, $\abs{e^z} = e^{\Re z}\in[e^{-1},e]$.

::: pf

::: pf-step
If $\abs{a}>e$, then $f$ has exactly $n$ zeros in $\DD$.

::: pf-proof
On $\abs{z}=1$, $\abs{e^z}\le e<\abs{a}=\abs{az^n}$.
By Rouché's theorem, $f$ has as many zeros in $\DD$ as $az^n$, which has a zero of order $n$ at $0$ and no others.
:::

:::

::: pf-step
If $\abs{a}<1/e$, then $f$ has no zeros in $\DD$.

::: pf-proof
On $\abs{z}=1$, $\abs{az^n}=\abs{a}<e^{-1}\le\abs{e^z}$.
By Rouché's theorem, $f$ has as many zeros in $\DD$ as $e^z$, which has none.
:::

:::

:::

:::
