---
schema: qual/card@1
id: P-LG4RJ
kind: problem
title: Every $p$-group is solvable
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Solvable Groups
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
Show that every finite $p$-group is solvable.
:::

::: {.solution}
We argue by induction on $\abs{G}$; the trivial group is solvable. Let $G$ be a nontrivial finite $p$-group.

::: pf

::: {.pf-step #central}
$G$ has a normal subgroup $C$ of order $p$.

::: pf-proof
The center $Z(G)$ is nontrivial by the class equation, so by Cauchy's theorem it contains a subgroup $C$ of order $p$. Every subgroup of the center is normal.
:::

:::

::: pf-step
$G$ is solvable.

::: pf-proof
By step [](#central){.pf-ref}, $G/C$ is a finite $p$-group of smaller order, hence solvable by induction. Pulling back a subnormal series of $G/C$ with abelian factors and prepending $\{e\}\trianglelefteq C$ gives a subnormal series of $G$ whose factors are those of $G/C$ together with $C\cong\ZZ/p\ZZ$, all abelian.
:::

:::

:::

:::
