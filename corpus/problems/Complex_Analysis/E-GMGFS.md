---
schema: qual/card@1
id: E-GMGFS
kind: problem
title: Laurent series and residue of $\cos(1-1/z)$ at $0$
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Essential Singularities
  - Residues
  - Trigonometry
relations: []
review: draft
---

::: {.exercise}
Find a Laurent expansion about $z=0$ of
$$
f(z) \coloneqq \cos\qty{1- {1\over z}}
,$$
and compute the "residue" coefficient $c_{-1}$.
:::

::: {.solution}

::: pf

::: {.pf-step #laurent}
For $z\neq0$,
$$
\boxed{f(z)=\sum_{k\ge0}{(-i)^ke^i+i^ke^{-i}\over 2\,k!}\,z^{-k}}
.$$

::: pf-proof
Let $g(w)\coloneqq\cos(1-w)$, so $f(z)=g(1/z)$.
For every $w\in\CC$,
$$
\begin{aligned}
g(w) &= {1\over 2}\qty{e^{i(1-w)} + e^{-i(1-w)}} = {1\over 2}\qty{e^i e^{-iw} + e^{-i} e^{iw}} \\
&= {1\over 2}\sum_{k\geq 0} \qty{ (-i)^k e^i + i^k e^{-i} } {w^k \over k!}
.\end{aligned}
$$
Substituting $w=1/z$ gives a series converging for all $z\neq0$, which is the Laurent expansion by uniqueness.
:::

:::

::: pf-step
$c_{-1}=\boxed{\sin 1}$.

::: pf-proof
The term $k=1$ of step [](#laurent){.pf-ref} gives
$$
c_{-1} = {-ie^i + ie^{-i} \over 2} = -i\cdot {e^i - e^{-i}\over 2} = {e^i - e^{-i}\over 2i} = \sin 1
.$$
:::

:::

:::

:::
