---
schema: qual/card@1
id: P-APA22H
kind: problem
title: Sum of two simple bivectors is not a single exterior product
classification:
  areas:
  - applied-algebra
  topics:
  - Multilinear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Let $\{v_1, v_2, v_3, v_4\}$ be a linearly independent set in a $\CC$-vector space $V$.
Prove that the tensor $\omega = v_1 \wedge v_2 + v_3 \wedge v_4$ cannot be represented as a single-term exterior product.
:::

::: {.solution}

::: pf

::: {.pf-step #square}

$\omega\wedge\omega=2\,v_1\wedge v_2\wedge v_3\wedge v_4\ne0$.

::: pf-proof

Expanding, $(v_1\wedge v_2)\wedge(v_1\wedge v_2)=0$ and $(v_3\wedge v_4)\wedge(v_3\wedge v_4)=0$ because each has a repeated factor, and $v_3\wedge v_4\wedge v_1\wedge v_2=v_1\wedge v_2\wedge v_3\wedge v_4$ because $2$-forms commute. Since $v_1,\ldots,v_4$ are linearly independent, $v_1\wedge v_2\wedge v_3\wedge v_4\ne0$, and $2\ne0$ in $\CC$.

:::

:::

::: pf-qed

If $\omega=u\wedge w$ for some $u,w\in V$, then $\omega\wedge\omega=u\wedge w\wedge u\wedge w=0$ because $u$ is repeated, which contradicts step [](#square){.pf-ref}.

:::

:::
:::
