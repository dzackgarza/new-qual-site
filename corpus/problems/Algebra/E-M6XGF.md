---
schema: qual/card@1
id: E-M6XGF
kind: problem
title: Poincaré's theorem on finite-index subgroups
classification:
  areas:
  - algebra
  topics:
  - Cosets and Lagrange
  - Normal Subgroups
  - Group Actions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used the coset action and the normal core directly.
---

::: {.exercise}
Prove Poincaré's theorem: if $H\le G$ has finite index $n$, then there is $N\trianglelefteq G$ with $N\subseteq H$ and
$$
[G:N]\mid n!.
$$
:::

::: {.solution}
Let $G$ act by left multiplication on the $n$ left cosets $G/H$, let $\rho\colon G\to S_n$ be the resulting homomorphism, and let $N=\ker\rho$.

::: pf

::: {.pf-step #core}
$N\trianglelefteq G$ and $N=\bigcap_{x\in G}xHx^{-1}\subseteq H$.

::: pf-proof
A kernel is normal. Moreover,
$$
g\in N
\iff gxH=xH\text{ for every }x\in G
\iff x^{-1}gx\in H\text{ for every }x\in G,
$$
and taking $x=1$ gives $N\subseteq H$.
:::

:::

::: pf-step
$[G:N]\mid n!$.

::: pf-proof
By the first isomorphism theorem $G/N\cong\im\rho\le S_n$, so by Lagrange's theorem $[G:N]=\abs{G/N}$ divides $\abs{S_n}=n!$. Together with step [](#core){.pf-ref}, $N$ is the required normal subgroup.
:::

:::

:::

:::
