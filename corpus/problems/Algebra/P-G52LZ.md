---
schema: qual/card@1
id: P-G52LZ
kind: problem
title: Every $p$-group is nilpotent
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Nilpotent Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}

Show that every $p\dash$group is nilpotent.

:::

::: {.solution}

Let $G$ be a finite $p$-group, and let
$$
1=Z_0(G)\le Z_1(G)\le Z_2(G)\le\cdots,
\qquad Z_{i+1}(G)/Z_i(G)=Z(G/Z_i(G)),
$$
be its upper central series.

::: pf

::: {.pf-step #center}

Every nontrivial finite $p$-group has nontrivial center.

::: pf-proof

By the class equation,
$$
\abs{G}=\abs{Z(G)}+\sum_i [G:C_G(x_i)],
$$
where the $x_i$ represent the conjugacy classes of size greater than $1$. Every term $[G:C_G(x_i)]$ is a power of $p$ greater than $1$, and $p\mid\abs{G}$, hence $p\mid \abs{Z(G)}$.

:::

:::

::: {.pf-step #strict}

If $Z_i(G)\ne G$, then $Z_i(G)<Z_{i+1}(G)$.

::: pf-proof

The quotient $G/Z_i(G)$ is a nontrivial finite $p$-group, so its center $Z_{i+1}(G)/Z_i(G)$ is nontrivial by step [](#center){.pf-ref}.

:::

:::

::: pf-step

The upper central series reaches $G$, so $G$ is nilpotent.

::: pf-proof

By step [](#strict){.pf-ref}, each inclusion before the series reaches $G$ is strict and so multiplies the order by at least $p$. Since $G$ is finite, $Z_n(G)=G$ for some $n$.

:::

:::

:::

:::
