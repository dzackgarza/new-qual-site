---
schema: qual/card@1
id: P-IT7OC
kind: problem
title: A subgroup that meets every conjugacy class is the whole group
classification:
  areas:
  - algebra
  topics:
  - Conjugacy
  - Cosets and Lagrange
  - Subgroups
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
Let $G$ be a finite group and let $H \le G$ be a subgroup.
Prove that if $H$ meets every conjugacy class of $G$ (i.e. $\bigcup_{g \in G} g H g^{-1} = G$), then $H = G$ (Jordan's Theorem on permutation groups).
:::

::: {.solution}
We prove the contrapositive. Suppose $H<G$ is proper and put $n=[G:H]\ge2$.

::: pf

::: {.pf-step #count}

$H$ has at most $n$ distinct conjugates.

::: pf-proof

The number of conjugates of $H$ is $[G:N_G(H)]$, and $H\le N_G(H)$ gives $[G:N_G(H)]\le[G:H]=n$.

:::

:::

::: pf-step

$\bigcup_{g\in G}gHg^{-1}\ne G$, so $H$ misses some conjugacy class of $G$.

::: pf-proof

Every conjugate of $H$ has $\abs{H}$ elements and contains the identity. By step [](#count){.pf-ref},
$$
\abs{\bigcup_{g\in G}gHg^{-1}}\le 1+n(\abs{H}-1)=\abs{G}-(n-1)<\abs{G},
$$
using $n\abs{H}=\abs{G}$ and $n\ge2$. An element of $G$ outside the union lies in a conjugacy class that $H$ does not meet, since $H$ meets the class of $x$ exactly when $x$ lies in some conjugate of $H$.

:::

:::

:::

:::
