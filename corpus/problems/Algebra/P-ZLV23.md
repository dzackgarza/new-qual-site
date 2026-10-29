---
schema: qual/card@1
id: P-ZLV23
kind: problem
title: No simple group of order $160$, and the structure of groups of that order
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Simple Groups
  - Classification
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
Prove that there is no simple group of order 160. What can you say about the structure of groups of that order?
:::

::: {.solution}
Let $\abs{G}=160=2^5\cdot5$, and let $P$ be a Sylow $2$-subgroup, so $[G:P]=5$.

::: pf

::: pf-step

No group of order $160$ is simple.

::: pf-proof

The action of $G$ on the five left cosets of $P$ is a homomorphism $\rho\colon G\to S_5$. It is nontrivial because the action is transitive on five points, so $\ker\rho\ne G$. If $G$ were simple, $\ker\rho$ would be trivial and $G$ would embed in $S_5$, but $\abs{G}=160>120=\abs{S_5}$.

:::

:::

::: pf-step

Every group of order $160$ is solvable.

::: pf-proof

This is Burnside's $p^aq^b$ theorem.

:::

:::

::: pf-step

The number of Sylow $5$-subgroups is $n_5\in\{1,16\}$, and if $n_5=1$ then $G\cong C_5\rtimes P$ with $P$ of order $32$ acting through $\Aut(C_5)\cong C_4$.

::: pf-proof

By the Sylow theorems, $n_5\mid 32$ and $n_5\equiv1\pmod 5$; the divisors of $32$ congruent to $1$ are $1$ and $16$. If $n_5=1$, the Sylow $5$-subgroup $C_5$ is normal, $C_5\cap P=1$ by orders, and $\abs{C_5P}=160$, so $G=C_5\rtimes P$ with $P$ acting by conjugation, that is, through a homomorphism $P\to\Aut(C_5)\cong C_4$.

:::

:::

:::

:::
