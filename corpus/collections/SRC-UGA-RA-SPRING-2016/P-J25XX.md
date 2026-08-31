---
schema: qual/card@1
id: P-J25XX
kind: problem
title: A middle-$\lambda$ Cantor set has measure zero
classification:
  areas:
  - real-analysis
  topics:
  - Cantor Set
  - Measure Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: problem
Let $0 < \lambda < 1$ and construct a Cantor set $C_\lambda$ by successively removing middle intervals of length $\lambda$.

Prove that $m(C_\lambda) = 0$.
:::
::: {.solution}
<1>1. Construction: $C_\lambda = \bigcap_n C_n$, where $C_0 = [0,1]$ and $C_{n+1}$ is obtained from $C_n$ by removing, from each of its intervals, the middle open subinterval of relative length $\lambda$ (so each interval of length $\ell$ loses a middle piece of length $\lambda\ell$).
::: {.proof}
"removing middle intervals of length $\lambda$" — relative length $\lambda$ of the current interval; this is the standard fat-Cantor family.
:::

<1>2. Each stage-$n$ interval has length $\ell_n = \left(\frac{1-\lambda}{2}\right)^n$: an interval of length $\ell$ splits into two intervals of length $\frac{1-\lambda}{2}\ell$.
::: {.proof}
each interval keeps two pieces, each of length $\ell \cdot \frac{1-\lambda}{2}$ (the removed middle has length $\lambda\ell$).
:::

<1>3. $C_n$ is a union of $2^n$ closed intervals of length $\ell_n$, so $m(C_n) = 2^n\ell_n = 2^n\left(\frac{1-\lambda}{2}\right)^n = (1-\lambda)^n$.
::: {.proof}
<1>2 and the count of intervals.
:::

<1>4. $m(C_\lambda) = \lim_n m(C_n) = 0$, since $0 < 1 - \lambda < 1$.
::: {.proof}
$C_\lambda \subseteq C_n$ for all $n$ (all $C_n$ measurable, being closed), so $m(C_\lambda) \le m(C_n) = (1-\lambda)^n \to 0$.
:::

<1>5. Q.E.D.
::: {.proof}
<1>4 is the claim.
:::
(The classical middle-thirds Cantor set is the case $\lambda = 1/3$.)
:::
