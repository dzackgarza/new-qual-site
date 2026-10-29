---
schema: qual/card@1
id: P-BIFDZ
kind: problem
title: Non-isomorphic groups can have isomorphic automorphism groups
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Counterexamples
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Find two groups $G\not\cong H$ where $\Aut G\cong \Aut H$.
:::

::: {.solution}

::: pf

::: pf-step

$G=\boxed{C_3}$ and $H=\boxed{C_4}$ are not isomorphic but have isomorphic automorphism groups.

::: pf-proof

$C_3$ and $C_4$ have different orders, so $G\not\cong H$. For every $n\ge1$, $\Aut(C_n)\cong(\ZZ/n\ZZ)^\times$, because an automorphism of $C_n=\langle g\rangle$ is determined by $g\mapsto g^k$ with $\gcd(k,n)=1$. Hence $\Aut(C_3)\cong(\ZZ/3\ZZ)^\times\cong C_2$ and $\Aut(C_4)\cong(\ZZ/4\ZZ)^\times\cong C_2$.

:::

:::

:::

:::
