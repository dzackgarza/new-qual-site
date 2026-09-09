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

::: problem
Let $G$ be a group of order $|G| = p q$, where $p$ and $q$ are distinct primes with $p > q$.
Prove that $G$ possesses a unique (and hence normal) Sylow $p$-subgroup of order $p$.
:::

::: solution
Let $n_p$ be the number of Sylow $p$-subgroups. Sylow's theorem gives
\[
n_p\mid q,\qquad n_p\equiv1\pmod p.
\]
Since $q$ is prime, $n_p$ is either $1$ or $q$. But $p>q$, so $q\not\equiv1\pmod p$. Hence $n_p=1$.

Thus the Sylow $p$-subgroup is unique and therefore normal. Its order is $p$, so it is nontrivial and proper in a group of order $pq$.
:::
