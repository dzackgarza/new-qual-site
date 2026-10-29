---
schema: qual/card@1
id: P-QQTBQ
kind: problem
title: Every finitely generated torsion-free abelian group is free abelian
classification:
  areas:
  - algebra
  topics:
  - Free Modules
  - Torsion
  - Abelian Groups
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
Prove that every finitely generated torsion-free abelian group is free abelian.
:::

::: {.solution}
::: pf

::: {.pf-step #structure}
$G\cong\ZZ^r\oplus\ZZ/d_1\ZZ\oplus\cdots\oplus\ZZ/d_s\ZZ$ for some $r,s\ge0$ and integers $d_i\ge2$, and the torsion subgroup of $G$ corresponds to $\ZZ/d_1\ZZ\oplus\cdots\oplus\ZZ/d_s\ZZ$.

::: pf-proof
The decomposition is the structure theorem for finitely generated abelian groups. An element $(v,t)$ with $v\in\ZZ^r$ has finite order exactly when $v=0$, since $\ZZ^r$ is torsion-free and the finite summand is killed by $d_1\cdots d_s$.
:::

:::

::: pf-step
If $G$ is torsion-free, then $G\cong\ZZ^r$ is free abelian.

::: pf-proof
By step [](#structure){.pf-ref}, the torsion subgroup corresponds to the finite summand, which is $0$; since each $d_i\ge2$, this forces $s=0$.
:::

:::

:::
:::
