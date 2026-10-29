---
schema: qual/card@1
id: E-SQ4GJ
kind: problem
title: Laurent expansion of $1/(e^z-1)$ at the origin
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Power Series
  - Poles
relations: []
review: draft
audit:
- event: statement-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source asks for "a power series expansion" of $1/(e^z-1)$, which has a pole at $0$ and so has no power series there. The statement now asks for the Laurent expansion at $0$ through the $z$ term, which is what the solution computes.'
---

::: {.exercise}
Find the Laurent expansion of
$$
f(z) = {1\over e^z-1}
$$
about $z=0$, through the term in $z$.
:::

::: {.hint}
Divide $1$ by the power series for $e^z - 1$, or rewrite the reciprocal as a geometric series in that expansion.
:::

::: {.solution}
Put $q(z) \coloneqq \frac12 z + \frac16 z^2 + \frac1{24}z^3+\cdots$, so that $e^z - 1 = z(1+q(z))$ and $q(0)=0$.

::: pf

::: {.pf-step #geometric}
Near $0$, $\frac{1}{1+q(z)} = 1 - \frac12 z + \frac1{12}z^2 + \bigo(z^3)$.

::: pf-proof
For $\abs{q(z)}<1$, $\frac{1}{1+q} = 1 - q + q^2 - \cdots$. Since $q(z) = \frac12 z + \frac16 z^2 + \bigo(z^3)$ and $q(z)^2 = \frac14 z^2 + \bigo(z^3)$, the sum is $1 - \frac12 z + \left(-\frac16+\frac14\right)z^2 + \bigo(z^3)$.
:::

:::

::: pf-step
$\frac{1}{e^z-1} = \boxed{\frac1z - \frac12 + \frac1{12}z + \bigo(z^2)}$.

::: pf-proof
Divide step [](#geometric){.pf-ref} by $z$.
:::

:::

:::

:::

::: {.remark}
The expansion $\frac{1}{1-e^z} = \sum_{k\geq 0} e^{kz}$ is of no use here: it requires $\abs{e^z}<1$, which fails near $0$, and each $e^{kz}$ contributes to the constant term.
:::
