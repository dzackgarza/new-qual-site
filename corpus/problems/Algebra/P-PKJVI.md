---
schema: qual/card@1
id: P-PKJVI
kind: problem
title: Groups of order $pq$ with $p>q$ have a proper nontrivial normal subgroup
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $G$ be a group of order $\abs{G} = p q$, where $p$ and $q$ are distinct primes with $p > q$.
Prove that $G$ possesses a unique (and hence normal) Sylow $p$-subgroup of order $p$.
:::

::: {.solution}
Let $n_p$ be the number of Sylow $p$-subgroups of $G$.

::: pf

::: {.pf-step #sylow}
$n_p\in\{1,q\}$ and $n_p\equiv1\pmod p$.

::: pf-proof
By the Sylow theorems, $n_p$ divides $q$ and $n_p\equiv1\pmod p$; since $q$ is prime, $n_p\in\{1,q\}$.
:::

:::

::: pf-step
$n_p=1$, so the Sylow $p$-subgroup $P$ is unique and normal, and it is proper and nontrivial.

::: pf-proof
Since $1<q<p$, $q\not\equiv1\pmod p$, so step [](#sylow){.pf-ref} leaves $n_p=1$. Every conjugate of $P$ is a Sylow $p$-subgroup, hence equals $P$, so $P$ is normal. Its order $p$ satisfies $1<p<pq$.
:::

:::

:::

:::
