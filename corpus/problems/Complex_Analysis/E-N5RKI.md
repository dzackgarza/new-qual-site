---
schema: qual/card@1
id: E-N5RKI
kind: problem
title: Constant boundary modulus implies constancy or an interior zero
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
  - Zeros
relations: []
review: draft
---

::: {.exercise}
Let $G\subset\CC$ be a bounded region, and suppose $f$ is continuous on
$\overline G$ and holomorphic on $G$. Assume that there is a constant $c\ge0$
such that
$$
\abs{f(z)}=c
\qquad(z\in\partial G).
$$
Show that either $f$ is constant or $f$ has a zero in $G$.
:::

::: {.solution}
::: pf

::: pf-step
If $c=0$, then $f\equiv0$.

::: pf-proof
$\overline G$ is compact, so the maximum modulus principle gives $\abs f\le\max_{\partial G}\abs f=0$ on $G$.
:::

:::

::: {.pf-step #modulus-constant}
If $c>0$ and $f$ has no zero in $G$, then $\abs f\equiv c$ on $G$.

::: pf-proof
The maximum modulus principle gives $\abs f\le c$ on $G$. As $f\neq0$ on $\partial G$ too, $1/f$ is holomorphic on $G$ and continuous on $\overline G$ with $\abs{1/f}=1/c$ on $\partial G$, so $\abs{1/f}\le1/c$ on $G$, that is, $\abs f\ge c$.
:::

:::

::: pf-step
If $c>0$ and $f$ has no zero in $G$, then $f$ is constant.

::: pf-proof
By step [](#modulus-constant){.pf-ref}, $f(G)$ lies in the circle $\theset{\abs w=c}$, which contains no nonempty open set. Since $G$ is connected, the open mapping theorem forces $f$ to be constant.
:::

:::

:::

:::
