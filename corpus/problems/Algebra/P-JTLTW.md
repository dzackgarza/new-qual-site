---
schema: qual/card@1
id: P-JTLTW
kind: problem
title: Nontrivial centre of a group of order $p^3$
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Centralizers and Normalizers
  - Normal Subgroups
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
Let $G$ be a group of order $p^3$, where $p$ is prime. Show that $Z(G)$ is nontrivial, and hence that $G$ has a nontrivial normal subgroup.
:::

::: {.solution}

::: pf

::: {.pf-step #center}

$Z(G)\ne1$.

::: pf-proof

The class equation for the conjugation action reads
$$
\abs{G}=\abs{Z(G)}+\sum_i[G:C_G(x_i)],
$$
where the $x_i$ represent the noncentral conjugacy classes. For noncentral $x_i$, $C_G(x_i)$ is a proper subgroup of $G$, so $[G:C_G(x_i)]$ is a positive power of $p$. Since $p\mid\abs{G}$, it follows that $p\mid\abs{Z(G)}$, and $\abs{Z(G)}\ge1$ gives $\abs{Z(G)}\ge p$.

:::

:::

::: pf-step

$G$ has a nontrivial normal subgroup.

::: pf-proof

The center is normal, and it is nontrivial by step [](#center){.pf-ref}.

:::

:::

:::

:::
