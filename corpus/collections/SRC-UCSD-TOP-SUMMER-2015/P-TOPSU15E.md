---
schema: qual/card@1
id: P-TOPSU15E
kind: problem
title: "Z3 action on a genus-3 surface has at least two fixed points"
classification:
  areas:
  - topology
  topics:
  - Group Actions
  - Surfaces
  - Fixed Point Theory
relations: []
review: draft
---

::: {.problem}
Let $\Sigma_3$ be the closed orientable surface of genus $3$.
Suppose $\mathbb{Z}_3$ acts on $\Sigma_3$; show that there must be at least two fixed points.
:::

::: {.solution}

::: pf

::: pf-step
Any action of $\mathbb Z/3$ on the orientable surface $\Sigma_3$ is orientation-preserving.

::: pf-proof
The orientation character of the action is a homomorphism $\mathbb Z/3\to\mathbb Z/2$, which must be trivial.
:::

:::

::: pf-step
Let $r$ be the number of fixed points and let the underlying quotient surface have genus $h$.

::: pf-proof
Since the group has prime order, every nonfree orbit has stabilizer equal to the whole group and hence is a fixed point.
:::

:::

::: {.pf-step #riemann-hurwitz-equation}
The Riemann--Hurwitz formula gives
$$
2-2\cdot3=3(2-2h)-2r.
$$

::: pf-proof
Away from the $r$ fixed points the quotient map has degree $3$. Each fixed point is a branch point of order $3$, contributing ramification defect $3-1=2$.
:::

:::

::: pf-step
Thus
$$
-4=6-6h-2r,
\qquad\text{so}\qquad r=5-3h.
$$

::: pf-proof
Rearrange the equation in step [](#riemann-hurwitz-equation){.pf-ref}.
:::

:::

::: {.pf-step #possible-h-r-values}
Since $r\ge0$ and $h\ge0$, the only possibilities are
$$
(h,r)=(0,5)\quad\text{or}\quad(1,2).
$$

::: pf-proof
If $h\ge2$, then $5-3h<0$.
:::

:::

::: pf-step
Therefore
$$
\boxed{r\ge2}.
$$

::: pf-proof
Both possible values of $r$ in step [](#possible-h-r-values){.pf-ref} are at least two.
:::

:::

:::

:::
