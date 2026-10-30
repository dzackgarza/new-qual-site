---
schema: qual/card@1
id: P-NLMMW
kind: problem
title: Groups of order $pq$ need not be nilpotent
classification:
  areas:
  - algebra
  topics:
  - Nilpotent Groups
  - Classification
  - Centralizers and Normalizers
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
If $\cardinality{G} = pq$ (distinct primes), is $G$ necessarily nilpotent?
:::

::: {.solution}
::: pf

::: pf-step
$\boxed{\text{No}}$: $S_3$ has order $6=2\cdot3$ and is not nilpotent.

::: pf-proof
A nontrivial nilpotent group has nontrivial center, and $Z(S_3)=1$: a transposition commutes only with $e$ and itself, and a $3$-cycle commutes only with its powers.
:::

:::

:::

:::

::: {.remark}
A finite group is nilpotent exactly when all its Sylow subgroups are normal.
If $\abs{G}=pq$ with primes $p<q$, the Sylow $q$-subgroup is normal, and $G$ is nonabelian exactly when it is a semidirect product $C_q\rtimes C_p$ with nontrivial action, which exists exactly when $p\mid q-1$; then the Sylow $p$-subgroups are not normal and $G$ is not nilpotent.
The case $p=2$, $q=3$ is $S_3$.
:::
