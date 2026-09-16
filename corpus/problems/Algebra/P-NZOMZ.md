---
schema: qual/card@1
id: P-NZOMZ
kind: problem
title: Groups of prime order are cyclic and simple
classification:
  areas:
  - algebra
  topics:
  - Cyclic Groups
  - Simple Groups
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
Let $p$ be a prime integer, and let $G$ be a group of order $|G| = p$.
Prove that:
(1) $G$ is cyclic ($G \cong \mathbb{Z}_p$).
(2) $G$ is simple (has no non-trivial proper normal subgroups).
:::

::: {.solution}
Choose $g\in G\setminus\{e\}$. By Lagrange,
\[
|\langle g\rangle|\mid |G|=p.
\]
Since $g\neq e$, the subgroup $\langle g\rangle$ is nontrivial, so its order is $p$. Hence $\langle g\rangle=G$, and $G\cong C_p$.

Again by Lagrange, every subgroup $H\le G$ has order dividing $p$, so $H=1$ or $H=G$. Thus $G$ has no nontrivial proper normal subgroup and is simple.
:::
