---
schema: qual/card@1
id: P-KNIPC
kind: problem
title: $P_n(z)=\sum_{k=1}^n kz^{k-1}$ has no zeros in $\abs{z}<r<1$ for large $n$
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
  - Polynomials
  - Uniform Convergence
relations: []
review: draft
---

::: {.problem}
Let $0<r<1$. Show that polynomials
$P_n(z)  = 1 + 2z + 3 z^2 + \cdots + n z^{n-1}$ have no zeros in $\abs{z}<r$
for all sufficiently large $n$'s.
:::

::: {.solution}
Put $P(z)=(1-z)^{-2}$.

::: pf

::: {.pf-step #unif}
$P_n\to P$ uniformly on $\abs{z}\le r$.

::: pf-proof
For $\abs{z}<1$, $\sum_{k\ge0}z^k=(1-z)^{-1}$, and termwise differentiation of this power series inside its disk of convergence gives $\sum_{k\ge1}kz^{k-1}=(1-z)^{-2}$. So $P_n$ is the $n$th partial sum of the power series of $P$, whose radius of convergence is $1$. A power series converges uniformly on each closed disk of smaller radius.
:::

:::

::: {.pf-step #lower}
$\abs{P(z)}>\frac14$ for $\abs{z}\le r$.

::: pf-proof
$\abs{1-z}\le1+\abs{z}\le1+r<2$.
:::

:::

::: pf-step
For all sufficiently large $n$, $P_n$ has no zeros in $\abs{z}<r$.

::: pf-proof
By step [](#unif){.pf-ref} there is $N$ with $\abs{P_n(z)-P(z)}<\frac14$ on $\abs{z}\le r$ for $n\ge N$. By step [](#lower){.pf-ref}, then $\abs{P_n(z)}\ge\abs{P(z)}-\abs{P_n(z)-P(z)}>0$ on $\abs{z}\le r$.
:::

:::

:::

:::
