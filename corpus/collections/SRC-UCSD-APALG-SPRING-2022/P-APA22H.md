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

::: problem
Let $\{v_1, v_2, v_3, v_4\}$ be a linearly independent set in a $\mathbb{C}$-vector space $V$.
Prove that the tensor $\omega = v_1 \wedge v_2 + v_3 \wedge v_4$ cannot be represented as a single-term exterior product.
:::

::: {.solution}
<1>1. Suppose $\omega = u \wedge w$ for some $u, w \in V$.
::: {.proof}
assume for contradiction.
:::

<1>2. Then $\omega \wedge \omega = (u \wedge w) \wedge (u \wedge w) = 0$.
::: {.proof}
$u \wedge w \wedge u \wedge w = 0$ (repeated factor).
:::

<1>3. But $\omega \wedge \omega = (v_1 \wedge v_2 + v_3 \wedge v_4) \wedge (v_1 \wedge v_2 + v_3 \wedge v_4) = 2 v_1 \wedge v_2 \wedge v_3 \wedge v_4 \neq 0$.
::: {.proof}
expand; the cross terms vanish ($v_1 \wedge v_2 \wedge v_1 \wedge v_2 = 0$ and $v_3 \wedge v_4 \wedge v_3 \wedge v_4 = 0$), leaving $v_1 \wedge v_2 \wedge v_3 \wedge v_4 + v_3 \wedge v_4 \wedge v_1 \wedge v_2 = 2 v_1 \wedge v_2 \wedge v_3 \wedge v_4$, which is nonzero since $\{v_1, v_2, v_3, v_4\}$ is linearly independent.
:::

<1>4. Contradiction, so $\omega$ is not a single exterior product.
::: {.proof}
<1>2 and <1>3.
:::

<1>5. Q.E.D.
::: {.proof}
<1>4.
:::
:::
