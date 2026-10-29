---
schema: qual/card@1
id: E-ENJAF
kind: problem
title: Laurent series of $e^{1/z}\cos(1/z)$ at its essential singularity $0$
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Essential Singularities
  - Power Series
relations: []
review: draft
---

::: {.exercise}
Find a Laurent expansion at $z=0$ for
$$
f(z) \coloneqq e^{1\over z}\cos\qty{1\over z}.
$$

:::

::: {.solution}
Let $g(z)\coloneqq e^z\cos z$, an entire function with $f(z)=g(1/z)$ for $z\neq0$.

::: pf

::: {.pf-step #taylor}
$g(z)=\frac12\sum_{k\ge0}\qty{(1+i)^k+(1-i)^k}\frac{z^k}{k!}$ for all $z\in\CC$.

::: pf-proof
$g(z)=\frac12e^z\qty(e^{iz}+e^{-iz})=\frac12\qty(e^{(1+i)z}+e^{(1-i)z})$; expand each exponential.
:::

:::

::: pf-step
On $\abs z>0$, $f(z)=\boxed{\frac12\sum_{k\ge0}\qty{(1+i)^k+(1-i)^k}\frac1{k!\,z^k}}$.

::: pf-proof
Substitute $1/z$ for $z$ in step [](#taylor){.pf-ref}; the series converges for every $z\neq0$ and has only nonpositive powers of $z$, so it is the Laurent series of $f$ at $0$.
:::

:::

:::

:::

