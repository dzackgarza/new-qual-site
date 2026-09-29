---
schema: qual/card@1
id: P-3PD4W
kind: problem
title: The center of a $p$-group is nontrivial
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Centralizers and Normalizers
  - Class Equation
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
Prove that the centre of a group of order $p^r$ ($p$ prime) is not trivial.
:::

::: {.solution}
Let $|G|=p^r$. Under conjugation, the class equation is
\[
|G|=|Z(G)|+\sum_i [G:C_G(x_i)],
\]
where the $x_i$ represent the noncentral conjugacy classes.

::: pf

::: {.pf-step #s1}

Every noncentral conjugacy-class size is divisible by $p$.

::: pf-proof

For noncentral $x_i$, the centralizer $C_G(x_i)$ is a proper subgroup of the $p$-group $G$. Hence
\[
[G:C_G(x_i)]>1
\]
and, being a divisor of $|G|=p^r$, it is a positive power of $p$. Therefore it is divisible by $p$.

:::

:::

::: pf-step

The order $|Z(G)|$ is divisible by $p$.

::: pf-proof

Reducing the class equation modulo $p$ and using step [](#s1){.pf-ref} gives
\[
0\equiv |G|\equiv |Z(G)|\pmod p.
\]
Thus $p\mid |Z(G)|$.

:::

:::

::: pf-step

Therefore $Z(G)$ is nontrivial.

::: pf-proof

Since $p\mid |Z(G)|$, one has $|Z(G)|\ge p>1$. Hence $Z(G)\ne\{e\}$.

:::

:::

:::

:::
