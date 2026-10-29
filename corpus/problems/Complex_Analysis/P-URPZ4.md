---
schema: qual/card@1
id: P-URPZ4
kind: problem
title: The number of solutions of $6z^3+1=-e^z$ in $\abs{z}<1$
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
Find the number of solutions to the following equation on $\abs{z} < 1$:
$$
6z^3 + 1 = -e^z.
$$
:::

::: {.solution}
The solutions are the zeros of $f(z) \coloneqq 6z^3 + 1 + e^z$. Write $f = M + m$ with $M(z) = 6z^3$ and $m(z) = e^z + 1$.

::: pf

::: {.pf-step #estimate}

$\abs{m(z)} < \abs{M(z)}$ on $\abs{z} = 1$.

::: pf-proof

For $\abs{z} = 1$,
$$
\abs{e^z + 1} \leq e^{\Re(z)} + 1 \leq e + 1 < 6 = \abs{6z^3}.
$$

:::

:::

::: pf-step

The equation has $\boxed{3}$ solutions in $\abs{z} < 1$, counted with multiplicity.

::: pf-proof

By step [](#estimate){.pf-ref} and Rouché's theorem, $f$ and $M$ have the same number of zeros in $\abs{z} < 1$, and $M(z) = 6z^3$ has a zero of order $3$ at $0$.

:::

:::

:::

:::
