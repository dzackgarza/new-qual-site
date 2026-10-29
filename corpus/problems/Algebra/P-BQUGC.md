---
schema: qual/card@1
id: P-BQUGC
kind: problem
title: $\QQ$ is not a finitely generated group
classification:
  areas:
  - algebra
  topics:
  - Abelian Groups
  - Counterexamples
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
Show that $\QQ$ is not finitely generated as a group.
:::

::: {.solution}
Let $q_1,\ldots,q_r\in\QQ$, write $q_i=a_i/b_i$ with $a_i\in\ZZ$ and $b_i\ge1$, and let $B=\lcm(b_1,\ldots,b_r)$.

::: pf

::: {.pf-step #contained}

The subgroup $\langle q_1,\ldots,q_r\rangle$ is contained in $\frac1B\ZZ$.

::: pf-proof

Each $q_i=a_i(B/b_i)/B\in\frac1B\ZZ$, and $\frac1B\ZZ$ is a subgroup of $\QQ$.

:::

:::

::: pf-step

$\langle q_1,\ldots,q_r\rangle\ne\QQ$, so $(\QQ,+)$ is not finitely generated.

::: pf-proof

If $\frac1{2B}=\frac mB$ with $m\in\ZZ$, then $m=\frac12$, which is impossible. Hence $\frac1{2B}\notin\frac1B\ZZ$, and by step [](#contained){.pf-ref} it is not in $\langle q_1,\ldots,q_r\rangle$. Since $q_1,\ldots,q_r$ were arbitrary, no finite subset generates $\QQ$.

:::

:::

:::

:::
