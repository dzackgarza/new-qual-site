---
schema: qual/card@1
id: P-BQVDL
kind: problem
title: A subgroup of index equal to the smallest prime dividing $\cardinality{G}$ is normal
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
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
Let $G$ be a finite group, and let $H \le G$ be a subgroup of index $[G : H] = p$, where $p$ is the smallest prime dividing $\cardinality{G}$.
Prove that $H$ is a **normal** subgroup of $G$ ($H \trianglelefteq G$).
:::

::: {.solution}
Let $G$ act by left multiplication on the $p$ left cosets of $H$, let $\rho:G\to S_p$ be the resulting homomorphism, and let $K=\ker\rho$.

::: pf

::: {.pf-step #kernel}

$K\trianglelefteq G$, $K\le H$, and $[H:K]$ divides $(p-1)!$.

::: pf-proof

$K$ is a kernel, so it is normal. An element of $K$ fixes the coset $H$, so it lies in $H$. By the first isomorphism theorem, $[G:K]=\abs{\im\rho}$ divides $\abs{S_p}=p!$. Since $[G:K]=[G:H][H:K]=p[H:K]$, $[H:K]$ divides $(p-1)!$.

:::

:::

::: pf-step

$[H:K]=1$, so $H=K\trianglelefteq G$.

::: pf-proof

Suppose $[H:K]>1$ and let $q$ be a prime dividing $[H:K]$. Then $q$ divides $\abs{G}$, so $q\ge p$ by the minimality of $p$. By step [](#kernel){.pf-ref}, $q$ divides $(p-1)!$, so $q<p$, a contradiction.

:::

:::

:::

:::
