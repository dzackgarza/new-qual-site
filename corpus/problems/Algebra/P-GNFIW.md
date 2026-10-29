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
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: Source asked to show that every finite p-group has nontrivial center, which fails for the trivial group; the statement now reads every nontrivial finite p-group.
---

::: {.problem}
Show that every nontrivial finite $p$-group has a nontrivial center.
:::

::: {.solution}
Let $G$ be a finite $p$-group with $\abs{G}=p^n$ and $n\ge 1$. Under conjugation, the class equation is
$$
\abs{G}
=
\abs{Z(G)}+
\sum_i [G:C_G(x_i)],
$$
where the $x_i$ represent the noncentral conjugacy classes.

::: pf

::: {.pf-step #s1}

Every noncentral conjugacy-class size is divisible by $p$.

::: pf-proof

For noncentral $x_i$, the centralizer $C_G(x_i)$ is a proper subgroup of the $p$-group $G$. Thus its index
$$
[G:C_G(x_i)]
$$
is a positive power of $p$, hence divisible by $p$.

:::

:::

::: {.pf-step #s2}

Therefore $p\mid \abs{Z(G)}$.

::: pf-proof

Reduce the class equation modulo $p$. Since $p\mid\abs{G}$ and every term in the sum is divisible by $p$ by step [](#s1){.pf-ref},
$$
\abs{Z(G)}\equiv0\pmod p.
$$

:::

:::

::: pf-step

Hence $Z(G)$ is nontrivial.

::: pf-proof

The center contains the identity, so $\abs{Z(G)}\ge1$. By step [](#s2){.pf-ref} its order is divisible by $p$, hence $\abs{Z(G)}\ge p>1$.

:::

:::

:::

:::
