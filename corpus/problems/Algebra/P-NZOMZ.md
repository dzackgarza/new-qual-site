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
Let $p$ be a prime integer, and let $G$ be a group of order $\abs{G} = p$.
Prove that:

(a) $G$ is cyclic ($G \cong \ZZ_p$).

(b) $G$ is simple (has no non-trivial proper normal subgroups).
:::

::: {.solution}

::: pf

::: pf-step

(a) $G$ is cyclic.

::: pf-proof

Choose $g\in G\setminus\{e\}$. By Lagrange's theorem,
$$
\abs{\langle g\rangle}\mid \abs{G}=p.
$$
Since $g\neq e$, the subgroup $\langle g\rangle$ is nontrivial, so its order is $p$. Hence $\langle g\rangle=G$, and $G\cong \ZZ_p$.

:::

:::

::: pf-step

(b) $G$ is simple.

::: pf-proof

By Lagrange's theorem, every subgroup $H\le G$ has order dividing $p$, so $H=1$ or $H=G$. In particular $G$ has no nontrivial proper normal subgroup, and $G\neq1$.

:::

:::

:::

:::
