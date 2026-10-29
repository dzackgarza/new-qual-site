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

::: {.problem}
Show that if $G$ is an infinite simple group, then $G$ cannot have a proper subgroup of finite index.
:::

::: {.solution}
Suppose, for contradiction, that $H<G$ is a proper subgroup of finite index $n$.

::: pf

::: {.pf-step #core}
The action of $G$ on the left cosets $G/H$ gives a homomorphism $\rho:G\to S_n$ whose kernel $\bigcap_{g\in G}gHg^{-1}$ is a normal subgroup of $G$ contained in $H$.

::: pf-proof
The kernel consists of the $g$ with $gxH=xH$ for all $x$, that is, $g\in xHx^{-1}$ for all $x$. Kernels are normal, and taking $x=e$ gives $\ker\rho\subseteq H$.
:::

:::

::: pf-step
This contradicts the infiniteness of $G$.

::: pf-proof
Since $G$ is simple, $\ker\rho$ is $1$ or $G$. By step [](#core){.pf-ref}, $\ker\rho\subseteq H\ne G$, so $\ker\rho=1$. Then $\rho$ embeds $G$ into the finite group $S_n$, so $G$ is finite.
:::

:::

:::

:::
