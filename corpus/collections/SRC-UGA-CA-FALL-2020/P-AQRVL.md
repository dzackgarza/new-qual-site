---
schema: qual/card@1
id: P-AQRVL
kind: problem
title: Laurent expansions of $\frac{1}{1-z^2}+\frac{1}{z-3}$ in $\abs{z}<1$, $1<\abs{z}<3$, and $\abs{z}>3$
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Poles
  - Power Series
relations: []
review: draft
---

::: {.problem}
Expand $\frac{1}{1-z^{2}}+\frac{1}{z-3}$ in a series of the form $\sum_{-\infty}^{\infty} a_{n} z^{n}$ so it converges for

- $\abs{z}<1$,

- $1<\abs{z}<3$,

- $\abs{z}>3$.

:::

::: {.remark title="Variations"}
The same problem is also asked with $\frac{1}{3-z}$ in place of $\frac{1}{z-3}$, together with the question of how many Laurent expansions about $0$ the function has. The singularities $\pm1$ and $3$ split the plane into the three annuli above, so there are exactly three, and replacing $\frac{1}{z-3}$ by $\frac{1}{3-z}$ only changes the sign of its series.
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
