---
schema: qual/card@1
id: P-4STQR
kind: problem
title: A spanning set with no proper spanning subset is linearly independent
classification:
  areas:
  - prelim
  topics:
  - Vector Spaces
  - Bases
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
a) Define what it means for vectors $v_1, \ldots, v_n$ in a vector space $V$ to be linearly independent.

b) Suppose that vectors $v_1, \ldots, v_n$ in a vector space $V$ span $V$ and that no proper subset of $\{v_1, \ldots, v_n\}$ spans $V$.
Prove that $v_1, \ldots, v_n$ are linearly independent.
:::

::: {.solution}
**(a).**

::: pf

::: {.pf-step #p1-1}
The vectors $v_1, \ldots, v_n$ are linearly independent if the only scalars $c_1, \ldots, c_n$ with $c_1 v_1 + \cdots + c_n v_n = 0$ are $c_1 = \cdots = c_n = 0$.

::: pf-proof
definition of linear independence.
:::

:::

:::

**(b).**

::: pf

::: pf-step
Suppose for contradiction that $v_1, \ldots, v_n$ are linearly dependent.

::: pf-proof
assume the conclusion fails.
:::

:::

::: {.pf-step #p2-2}
Then there is a nontrivial relation $c_1 v_1 + \cdots + c_n v_n = 0$ with some $c_j \neq 0$.

::: pf-proof
Step [](#p1-1){.pf-ref} (a).
:::

:::

::: {.pf-step #p2-3}
Hence $v_j = -\sum_{i \neq j} \frac{c_i}{c_j} v_i$, so $v_j$ is a linear combination of the other vectors.

::: pf-proof
Step [](#p2-2){.pf-ref}, solving for $v_j$.
:::

:::

::: {.pf-step #p2-4}
Therefore $\{v_1, \ldots, v_n\} \setminus \{v_j\}$ still spans $V$ (any linear combination using $v_j$ can be rewritten using the other vectors).

::: pf-proof
Step [](#p2-3){.pf-ref}.
:::

:::

::: {.pf-step #p2-5}
This contradicts the hypothesis that no proper subset spans $V$.

::: pf-proof
Step [](#p2-4){.pf-ref}.
:::

:::

::: {.pf-step #p2-6}
Hence $v_1, \ldots, v_n$ are linearly independent.

::: pf-proof
Step [](#p2-5){.pf-ref}.
:::

:::

::: pf-qed
Step [](#p1-1){.pf-ref} (a) and step [](#p2-6){.pf-ref} (b).
:::

:::
:::
