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

::: problem
If $|G| = pq$ (distinct primes), is $G$ necessarily nilpotent?
:::

::: solution
No. For example, $S_3$ has order $6=2\cdot3$ but is not nilpotent: its center is trivial, so its upper central series cannot reach $S_3$.

More generally, for a finite group, nilpotence is equivalent to normality of every Sylow subgroup. If $|G|=pq$ with primes $p<q$, the Sylow $q$-subgroup is always normal. A nonabelian group of order $pq$ exists exactly when $p\mid(q-1)$; it is a semidirect product
\[
C_q\rtimes C_p
\]
with nontrivial action, and its Sylow $p$-subgroups are not normal. Hence such a group is not nilpotent. The case $p=2,q=3$ is $S_3$.
:::
