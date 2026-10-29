---
schema: qual/card@1
id: P-B2YTD
kind: problem
title: Laurent series of $\frac{1}{1-z^2}+\frac{1}{z-3}$ on $\abs{z}<1$, $1<\abs{z}<3$, and $\abs{z}>3$
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
relations: []
review: draft
---

::: {.problem}
Expand
$$
\frac1{1-z^2}+\frac1{z-3}
$$
as a Laurent series about $0$ on each of the regions $\abs{z}<1$,
$1<\abs{z}<3$, and $\abs{z}>3$.
:::

::: {.solution}

Each expansion comes from the geometric series $\frac1{1-w}=\sum_{k\ge0}w^k$ for $\abs{w}<1$.

::: pf

::: {.pf-step #pieces}
$$
\frac1{1-z^2}=
\begin{cases}
\sum_{k=0}^\infty z^{2k}, & \abs{z}<1,\\
-\sum_{k=1}^\infty z^{-2k}, & \abs{z}>1,
\end{cases}
\qquad
\frac1{z-3}=
\begin{cases}
-\sum_{k=0}^\infty \frac{z^k}{3^{k+1}}, & \abs{z}<3,\\
\sum_{k=0}^\infty 3^kz^{-k-1}, & \abs{z}>3.
\end{cases}
$$

::: pf-proof
Take $w=z^2$, $w=z^{-2}$ in $\frac1{1-z^2}=-z^{-2}\frac1{1-z^{-2}}$, $w=z/3$ in $\frac1{z-3}=-\frac13\frac1{1-z/3}$, and $w=3/z$ in $\frac1{z-3}=\frac1z\frac1{1-3/z}$.
:::

:::

::: pf-step
The expansions are
$$
\frac1{1-z^2}+\frac1{z-3}=
\begin{cases}
\sum_{k=0}^\infty z^{2k}-\sum_{k=0}^\infty\frac{z^k}{3^{k+1}}, & \abs{z}<1,\\
-\sum_{k=1}^\infty z^{-2k}-\sum_{k=0}^\infty\frac{z^k}{3^{k+1}}, & 1<\abs{z}<3,\\
-\sum_{k=1}^\infty z^{-2k}+\sum_{k=0}^\infty 3^kz^{-k-1}, & \abs{z}>3.
\end{cases}
$$

::: pf-proof
Add the expansions of step [](#pieces){.pf-ref} valid in each region.
:::

:::

:::

:::
