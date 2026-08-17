---
schema: qual/card@1
id: P-NC5CZ
kind: problem
title: Compactly uniform limits of holomorphic functions are holomorphic
classification:
  areas:
  - complex-analysis
  topics:
  - uniform-convergence
  - series-of-functions
  - holomorphic-functions
  - morera
relations: []
review: draft
solved: true
---

::: problem
- Show that if each $f_n$ is holomorphic on $\Omega$ and $F \definedas \sum f_n$ converges uniformly on every compact subset of $\Omega$, then $F$ is holomorphic.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** If each $f_n$ is holomorphic on $\Omega$ and $F \definedas \sum_n f_n$ converges uniformly on every compact subset of $\Omega$, show $F$ is holomorphic on $\Omega$.

<1>1. $F$ is continuous on $\Omega$.
Proof: Uniform convergence on compact subsets: fix $z_0 \in \Omega$ and a compact neighborhood $K$ of $z_0$ inside $\Omega$; the partial sums $S_N = \sum_{n \leq N} f_n$ are continuous, and $S_N \rightrightarrows F$ on $K$, so $F$ is continuous on $K$, hence at $z_0$.

<1>2. For every closed triangle $\Delta \subseteq \Omega$, $\int_\Delta F = 0$.
Proof: Since $S_N \rightrightarrows F$ on the compact set $\Delta$, $\int_\Delta F = \lim_N \int_\Delta S_N = \lim_N \sum_{n\leq N}\int_\Delta f_n = \lim_N \sum_{n \leq N} 0 = 0$; each $\int_\Delta f_n = 0$ by the Cauchy–Goursat theorem applied to the holomorphic $f_n$.

<1>3. $F$ is holomorphic on $\Omega$.
Proof: By Morera's theorem, a continuous function on an open set with vanishing integrals over all closed triangles is holomorphic; <1>1 gives continuity and <1>2 gives the vanishing integrals.

<1>4. Q.E.D. Proof: <1>3 is the claim.
:::
