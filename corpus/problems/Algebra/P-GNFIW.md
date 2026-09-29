---
schema: qual/card@1
id: P-GNFIW
kind: problem
title: A $p$-group has nontrivial center
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
Show that every finite $p$-group has a nontrivial center.
:::

::: {.solution}
Let $|G|=p^n$. Under conjugation, the class equation is
\[
|G|
=
|Z(G)|+
\sum_i [G:C_G(x_i)],
\]
where the $x_i$ represent the noncentral conjugacy classes.

::: pf

::: {.pf-step #s1}

Every noncentral conjugacy-class size is divisible by $p$.

::: pf-proof

For noncentral $x_i$, the centralizer $C_G(x_i)$ is a proper subgroup of the $p$-group $G$. Thus its index
\[
[G:C_G(x_i)]
\]
is a positive power of $p$, hence divisible by $p$.

:::

:::

::: {.pf-step #s2}

Therefore $p\mid |Z(G)|$.

::: pf-proof

Reduce the class equation modulo $p$. Since $p\mid|G|$ and every term in the sum is divisible by $p$ by step [](#s1){.pf-ref},
\[
|Z(G)|\equiv0\pmod p.
\]

:::

:::

::: pf-step

Hence $Z(G)$ is nontrivial.

::: pf-proof

The center contains the identity, so $|Z(G)|\ge1$. By step [](#s2){.pf-ref} its order is divisible by $p$, hence $|Z(G)|\ge p>1$.

:::

:::

:::

:::
