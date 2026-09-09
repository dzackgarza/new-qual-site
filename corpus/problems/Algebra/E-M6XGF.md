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
\[
[G:N]\mid n!.
\]
:::

::: {.solution}
Let $G$ act by left multiplication on the $n$ left cosets $G/H$. This gives a homomorphism
\[
\rho:G\longrightarrow S_n.
\]
Let
\[
N=\ker\rho.
\]
Then $N\trianglelefteq G$. Moreover,
\[
g\in N
\iff gxH=xH\text{ for every }x\in G
\iff x^{-1}gx\in H\text{ for every }x\in G,
\]
so
\[
N=\bigcap_{x\in G}xHx^{-1}\subseteq H.
\]
By the first isomorphism theorem,
\[
G/N\cong\operatorname{im}\rho\le S_n.
\]
Hence, by Lagrange,
\[
[G:N]=|G/N|\mid |S_n|=n!.
\]
:::
