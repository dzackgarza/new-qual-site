---
schema: qual/card@1
id: P-KOQPF
kind: problem
title: Infinite simple groups have no finite-index subgroups
classification:
  areas:
  - algebra
  topics:
  - Simple Groups
  - Group Actions
  - Cosets and Lagrange
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Show that if $G$ is an infinite simple group, then $G$ cannot have a proper subgroup of finite index.
:::

::: solution
Suppose $H<G$ has finite index $n$. The action of $G$ on the left cosets $G/H$ gives a homomorphism
\[
\rho:G\to S_n.
\]
Its kernel is the core
\[
\ker\rho=\bigcap_{g\in G}gHg^{-1},
\]
which is a normal subgroup of $G$ contained in $H$.

If $G$ is simple, then $\ker\rho$ is either $1$ or $G$. Since $H$ is proper, $\ker\rho\ne G$, so $\ker\rho=1$. Hence $\rho$ is injective and embeds $G$ into the finite group $S_n$, forcing $G$ to be finite. This contradicts the hypothesis that $G$ is infinite.

Therefore an infinite simple group has no proper subgroup of finite index.
:::
