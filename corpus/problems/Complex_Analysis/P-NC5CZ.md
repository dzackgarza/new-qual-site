---
schema: qual/card@1
id: P-NC5CZ
kind: problem
title: Compactly uniform limits of holomorphic functions are holomorphic
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Series of Functions
  - Holomorphic Functions
  - Morera
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
- Show that if each $f_n$ is holomorphic on $\Omega$ and $F \definedas \sum f_n$ converges uniformly on every compact subset of $\Omega$, then $F$ is holomorphic.
:::

::: {.solution}
**Goal:** If each $f_n$ is holomorphic on $\Omega$ and $F \definedas \sum_n f_n$ converges uniformly on every compact subset of $\Omega$, show $F$ is holomorphic on $\Omega$.

::: pf

::: {.pf-step #s1}

$F$ is continuous on $\Omega$.

::: pf-proof

Uniform convergence on compact subsets: fix $z_0 \in \Omega$ and a compact neighborhood $K$ of $z_0$ inside $\Omega$; the partial sums $S_N = \sum_{n \leq N} f_n$ are continuous, and $S_N \rightrightarrows F$ on $K$, so $F$ is continuous on $K$, hence at $z_0$.

:::

:::

::: {.pf-step #s2}

For every closed triangle $\Delta \subseteq \Omega$, $\int_\Delta F = 0$.

::: pf-proof

Since $S_N \rightrightarrows F$ on the compact set $\Delta$, $\int_\Delta F = \lim_N \int_\Delta S_N = \lim_N \sum_{n\leq N}\int_\Delta f_n = \lim_N \sum_{n \leq N} 0 = 0$; each $\int_\Delta f_n = 0$ by the Cauchy–Goursat theorem applied to the holomorphic $f_n$.

:::

:::

::: {.pf-step #s3}

$F$ is holomorphic on $\Omega$.

::: pf-proof

By Morera's theorem, a continuous function on an open set with vanishing integrals over all closed triangles is holomorphic; step [](#s1){.pf-ref} gives continuity and step [](#s2){.pf-ref} gives the vanishing integrals.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the claim.

:::

:::

:::
